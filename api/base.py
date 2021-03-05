import requests

class Base:
    def __init__(self):
        corpid = "wwd3a75fafe47798a0"
        corpsecret = "gLmfpg_jp53hToyCQuvZlRg3a5ae9LmVMK9KBAPBvBs"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url)
        self.token = r.json()["access_token"]
        self.s = requests.Session()
        self.s.params = {'access_token':self.token}

    def send(self, *args, **kwargs):
        r = self.s.request(*args, **kwargs)
        return r.json()
