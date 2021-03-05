from api.base import Base


class Address(Base):
    def add_member(self, userid, name, phonenum, department, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        body = {
            "userid": userid,
            "name": name,
            "mobile": phonenum,
            "department": department
        }
        body.update(**kwargs)
        return self.send('post', url=url, json=body)

    def get_member(self, userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send('get', url)

    def update_member(self,userid, name, **kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        body = {
            "userid": userid,
            "name": name,
        }
        body.update(**kwargs)
        return self.send('post', url=url, json=body)

    def delete_member(self, userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send('get', url=url)
