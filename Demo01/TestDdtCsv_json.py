
import unittest
from ddt import ddt,data,unpack
import csv
import requests
import json

# 建立一个方法，将csv文件传入到方法中
# 数据准备建立一个csv
def get_data(file_name):
    # 创建一个列表,保存读过来的数据
    rows=[]
    # 打开一个csv文件，文件名通过参数传进来
    data_file =open(file_name,'r')
    # 建立一个csv的读的工具，将文件读进来
    reader = csv.reader(data_file)
    # 跳过第一行的头，头有格式信息，这个头可以是参数名
    next(reader,None)
    # 将reader中的东西读到row中，循环多次
    for row in reader:
    # 将每个row的东西追加到此前定义
        rows.append(row)
    # rows列表中
    return rows
    # 将读到所有信息以列表形式返回待用

@ddt
class TestForCsv(unittest.TestCase):
    def setUp(self):
        self.url='https://reqres.in/api/users'

    @data(*get_data('test_data_json.csv'))
    @unpack
    def test_get_csv(self,value):
        # print(value)
        # print(type(value))
        # str 转dict使用，dict是python，json是中间传递数据类型
        data = json.loads(value)
        # 从测试用例中读出名字
        print(data['name'])
        req =requests.post(url=self.url,data=data)
        # 是从输出响应中读到名称
        print(req.json()['name'])
        self.assertEqual(201,req.status_code)
        # 比对这两值是否一致，测试功能
        self.assertEqual(data['name'],req.json()['name'])
        self.assertEqual(data['job'], req.json()['job'])


if __name__ == '__main__':
    unittest.main



