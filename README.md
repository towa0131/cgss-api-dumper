# cgss-api-dumper
cgss-api-dumper はデレステの通信内容を解析する mitmproxy 用 Python スクリプトです

## 必要なもの
- Python 3
- DMM版アイドルマスターシンデレラガールズスターライトステージ

## 使用方法
- 必要なパッケージをインストール

```console
$ pip install -r requirements.txt
```

- mitmproxy を `cgss_script.py` を読み込み指定して起動

```console
$ mitmdump -s cgss_script.py
```

- Windows の プロキシ設定から「プロキシサーバーを使う」のセットアップを開く

![プロキシ設定 1](docs/proxy_settings_1.png)

- 「プロキシサーバーを使う」をオンにし、「プロキシIPアドレス」に `127.0.0.1` を、「ポート」に `8080` を入力し保存

![プロキシ設定 2](docs/proxy_settings_2.png)

- http://mitm.it にアクセスし、Windows 用の証明書をダウンロード

![mitm.it](docs/mitm_proxy_website.png)

- 手順に従い、証明書をコンピュータにインストールする

![証明書のインストール](docs/cert_install.png)

- DMM版アイドルマスターシンデレラガールズスターライトステージを起動

![デレステタイトル](docs/imascg_title.png)

- APIサーバとの通信が行われたらリクエストとレスポンスがコンソールに表示される

![コンソール](docs/api_body.png)