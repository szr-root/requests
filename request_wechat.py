import requests


def test_wechat():
    # 获取token
    corpid = "wwd3a75fafe47798a0"
    corpsecret = "gLmfpg_jp53hToyCQuvZlRg3a5ae9LmVMK9KBAPBvBs"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    r = requests.get(url=url)
    token = r.json()["access_token"]

    # 创建成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
    body={
        "userid": "xiaoming",
        "name": "小明",
        "mobile": "+86 13800000000",
        "department": [1]
    }
    r = requests.post(url=url, json=body)
    # print(r.json())
    # 更新成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}"
    body={
        "userid": "xiaoming",
        "name": "小红",
    }
    r = requests.post(url=url, json=body)
    # print(r.json())
    # 删除成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=xiaoming"
    r = requests.get(url=url)
    print(r.json())
