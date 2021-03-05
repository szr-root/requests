from api.address import Address


class Test_address:
    def setup(self):
        self.address = Address()

    def test_addmember(self):
       # 数据清理
       self.address.delete_member("xiaohong")

       # 创建成员
       r = self.address.add_member("xiaohong", "小红", "18111111111", [1])
       assert r.get("errmsg", "未创建成功") == "created"

