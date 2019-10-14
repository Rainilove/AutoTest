# 导包
import json
import unittest
import requests
import app
from api.UserApi import UserLogin
from parameterized import parameterized


# 创建解析data包中的json文件的函数
def read_from_json():
    # 1.设置一个空列表
    data = []
    # 2. 开启文件流,读取数据并将其导入列表
    with open(app.PRO_PATH + "/data/login_data.json", "r", encoding="utf-8") as f:
        for value in json.load(f).values():
            # print("每一条用例:",value)
            # 将每条用例的 5 个字段组织成元组
            username = value.get("username")
            password = value.get("password")
            verify_code = value.get("verify_code")
            status = value.get("status")
            msg = value.get("msg")
            # 将所有字段组织成元组
            ele = (username, password, verify_code, status, msg)
            # 再把元组添加进列表
            data.append(ele)
    # 3.最后返回列表
    # return [
    #     ('13800138006', '123456', '8888', 1, '登陆成功'),
    #     ('1380013800A', '123456', '8888', -1, '账号不存在'),
    #     ('13800138006', '123456789', '8888', -2, '密码错误')
    #         ]
    return data


# 创建测试类
class TestUser(unittest.TestCase):
    # 初始化函数
    def setUp(self):
        self.session = requests.session()
        self.user_obj = UserLogin()

    # 资源销毁函数
    def tearDown(self):
        self.session.close()

    # 测试函数1
    def test_get_verify_code(self):
        # 1.请求业务
        # 创建UserLogin对象
        # user_obj = UserLogin()
        # 调用get_verify_code函数
        response = self.user_obj.get_verify_code(self.session)
        # 2.断言业务
        self.assertEqual(200, response.status_code)
        self.assertIn('image', response.headers.get('Content-Type'))

    # 测试函数2
    @parameterized.expand(read_from_json())
    def test_get_login(self, username, password, verify_code, status, msg):
        # 1.请求业务
        print(username, password, verify_code, status, msg)
        # 调用 api对象.函数()

        # 调用get_verify_code函数
        response1 = self.user_obj.get_verify_code(self.session)
        response2 = self.user_obj.get_login(self.session, username, password, verify_code)
        print(response2.json())
        # 2.断言业务
        self.assertEqual(200, response1.status_code)
        self.assertIn('image', response1.headers.get('Content-Type'))
        self.assertEqual(status, response2.json().get('status'))
        self.assertIn(msg, response2.json().get('msg'))
