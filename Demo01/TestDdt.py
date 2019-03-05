import unittest
from ddt import ddt,data,unpack

# 在类前面加ddt
@ddt
class TestDdt1(unittest.TestCase):
    def setUp(self):
        print('开始了')

    def tearDown(self):
        pass

    @unittest.skip
    @data('你好','你')
    def testInFDdt01(self,value):
        print(value)
        self.assertEqual('你',value)

    @unittest.skip
    @data([1],[2])
    @unpack
    def testInFDdt02(self,value):
        print(value)
        self.assertEqual(2,value)

#     同时传入二个值执行多次
    @unittest.skip
    @data((1,2),(2,3))
    @unpack
    def testInFDdt03(self, value1,value2):
        print(value1,value2)
        self.assertEqual(value1, value2-1)

# 传字典类型可以吗？
    @unittest.skip
    @data(({'no':1,'name': 'liz'}))
    # @unpack
    def testInFDdt04(self, value1):
        print(value1)

# 传二个字典怎么办？({},{})

if __name__ == '__main__':
    unittest.main