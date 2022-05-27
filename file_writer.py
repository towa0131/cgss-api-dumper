import datetime

class FileWriter:
    def __init__(self, path):
        self.path = path

    def write(self, endpoint, request, response):
        with open(self.path, "a") as file:
            s = f"Endpoint [{endpoint}] ({datetime.datetime.now()})\n"
            s += "Request : \n"
            s += request + "\n"
            s += "Response : \n"
            s += response + "\n\n"
            file.writelines(s)