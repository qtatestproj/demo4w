# -*- coding: utf-8 -*-
'''示例测试用例
'''
# 2019/03/22 QTAF自动生成

from testbase import testcase
from qt4w.browser.browser import Browser


class Demo4wTestCase(testcase.TestCase):
    '''demo4w测试用例基类
    '''

    def pre_test(self):
        super(Demo4wTestCase, self).pre_test()
        self._clean_env()
        Browser.register_browser('IE', 'browser.ie.IEBrowser')
        Browser.register_browser('Chrome', 'browser.chrome.ChromeBrowser')

    def _clean_env(self):
        from browser.chrome import ChromeBrowser
        from browser.ie import IEApp
        ChromeBrowser.killall()
        IEApp.killAll()

    def post_test(self):
        super(Demo4wTestCase, self).post_test()
