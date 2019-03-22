# -*- coding: utf-8 -*-
'''示例测试用例
'''
#2019/03/22 QTAF自动生成

from demo4wlib.testcase import Demo4wTestCase

class HelloTest(Demo4wTestCase):
    '''示例测试用例
    '''
    owner = "root"
    timeout = 5
    priority = Demo4wTestCase.EnumPriority.High
    status = Demo4wTestCase.EnumStatus.Design
    
    def run_test(self):
        self.log_info("hello testcase")
        self.assert_equal(True, True)
    
if __name__ == '__main__':
    HelloTest().debug_run()

