import unittest
# 接口测试库
import requests
from ddt import ddt,file_data


@ddt
class TestDdtJson(unittest.TestCase):
    def setUp(self):
        self.url='https://reqres.in/api/users'
    # 传一个json 文件
    @file_data('test_data.json')
    # **表示json格式，*是表示列表
    def testInterFace01(self,**value):
        print(value)
        req =requests.post(url=self.url,json=value)
        self.assertEqual(201,req.status_code)
        self.assertEqual('morpheus',req.json()['name'])
        self.assertEqual('leader', req.json()['job'])


if __name__ == '__main__':
    unittest.main