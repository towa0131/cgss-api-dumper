import re
import base64
import binascii
import msgpack
import json
from mitmproxy import flowfilter
from mitmproxy import ctx, http
from rijndael import Rijndael
from cryptographer import Cryptographer
from file_writer import FileWriter

class CGSSAnalyzer:
    def __init__(self):
        self.writer = FileWriter("cgss_dump.log")

    def response(self, flow: http.HTTPFlow) -> None:
        if re.match(".*starlight-stage.jp", flow.request.host):
            endpoint = "/" + flow.request.pretty_url.split("/", 3)[-1]
            res = flow.response.content
            rv = base64.b64decode(flow.request.content)
            req_context = rv[0:len(rv) - 32]
            msg_iv = binascii.unhexlify(Cryptographer.decode(flow.request.headers["UDID"]).replace("-", "").encode("ascii"))
            src = base64.b64decode(res)
            res_context = src[0:len(src) - 32]
            key = src[-32::]
            req_plain = Rijndael.decrypt_cbc(req_context, msg_iv, rv[-32::])
            req_plainBytes = base64.b64decode(req_plain)
            req_json = msgpack.unpackb(req_plainBytes, strict_map_key=False)
            res_plain = Rijndael.decrypt_cbc(res_context, msg_iv, key)
            res_plainBytes = base64.b64decode(res_plain)
            res_json = msgpack.unpackb(res_plainBytes, strict_map_key=False)
            self.writer.write(endpoint, json.dumps(req_json, indent=2), json.dumps(res_json, indent=2))
            print("Endpoint : " + endpoint)
            print("Request :")
            print(json.dumps(req_json, indent=2))
            print("Response : ")
            print(json.dumps(res_json, indent=2))

addons = [CGSSAnalyzer()]