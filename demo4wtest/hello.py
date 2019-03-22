# -*- coding: utf-8 -*-
'''示例测试用例
'''
# 2019/03/22 QTAF自动生成

import time
from qt4w.browser.browser import Browser
from demo4wlib.testcase import Demo4wTestCase
from demo4wlib.demopage import DemoPage, ProfilePage


class HelloTest(Demo4wTestCase):
    '''示例测试用例
    '''
    owner = "qta"
    timeout = 5
    priority = Demo4wTestCase.EnumPriority.High
    status = Demo4wTestCase.EnumStatus.Design

    def run_test(self):
        self.startStep('1.设置信息并提交')
        browser = Browser("IE")
        self.logInfo('打开web页面')
        page = browser.open_url('https://qtacore.github.io/qt4w/demo.html', DemoPage)
        self.logInfo('用户名设置为qta')
        page.set_name("qta")
        self.logInfo('年龄设置为20')
        page.set_age(str(20))
        self.logInfo('公司设置为tencent')
        page.set_company("tencent")
        self.logInfo('性别设置为女')
        page.set_female()
        self.logInfo('点击提交')
        page.submit()

        time.sleep(3)  # 等待页面跳转

        self.start_step('2. 检查页面跳转以及内容是否正确')
        page = browser.find_by_url('https://qtacore.github.io/qt4w/welcome.html?name=qta&sex=female&age=20&company=tencent', ProfilePage)
        page.wait_for_ready()
        self.logInfo('检查页面标题')
        self.waitForEqual('检查页面标题', page, 'title', "欢迎您：qta女士")
        self.logInfo('检查公司')
        self.waitForEqual('检查公司', page.control('公司'), 'inner_text', 'tencent')


if __name__ == '__main__':
    HelloTest().debug_run()
