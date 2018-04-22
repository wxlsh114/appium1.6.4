#coding=utf-8
from macaca import WebDriver
import unittest,time,os
from time import sleep
from HTMLTestRunner import HTMLTestRunner
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from appium.webdriver.common.touch_action import TouchAction
#from selenium.webdriver.common.action_chains import ActionChains


desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0',
        'deviceName': 'emulator-5554',
        'automationName': 'UIAutomator2',
        #'udid':'7c72478d',
        'app': os.path.abspath('/Users/shoubyoukatsu/Desktop/macaca_android/VIPTeacher_2.0.2.apk'),
        'appPackage': 'com.pnlyy.pnlclass_teacher.test',
        'unicodeKeyboard': 'true',
        'resetKeyboard': 'true',
        'fullReset': 'true',
}

server_url = {
    'hostname': 'localhost',
    'port': 3456
}

class TestTeacher(unittest.TestCase):
    def setUp(self):
        # set up macaca
        self.driver = WebDriver(desired_caps, server_url)
        self.driver.init()
        sleep(2)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def mySalary(self):
        driver=self.driver       

        driver.touch('drag',{'fromX':950,'fromY':1600,'toX':50,'toY':1600,'duration':1})
        sleep(1)
        driver.touch('drag',{'fromX':950,'fromY':1600,'toX':50,'toY':1600,'duration':1})
        sleep(1)
        driver.element_by_id('com.pnlyy.pnlclass_teacher.test:id/btnStart').click()
        sleep(2)
        #driver.element_by_name('马上体验').click()
        #sleep(4)
        user=driver.element_by_id('com.pnlyy.pnlclass_teacher.test:id/etUserName')
        user.click()
        user.send_keys('18311111111')
        sleep(1)
        pwd=driver.element_by_id('com.pnlyy.pnlclass_teacher.test:id/etPassword')
        pwd.click()
        pwd.send_keys('123456')
        sleep(1)
        #登录
        driver.element_by_id('com.pnlyy.pnlclass_teacher.test:id/btnLogin').click()
        sleep(4)
        #allow
        driver.touch('tap',{'x':828,'y':928,'duration':1})
        sleep(3)
        driver.touch('tap',{'x':828,'y':928,'duration':1})
        sleep(3)
        driver.touch('tap',{'x':540,'y':1385,'duration':1})
        sleep(3)
        driver.touch('tap',{'x':540,'y':1385,'duration':1})
        sleep(3)
        driver.touch('tap',{'x':540,'y':1385,'duration':1})
        sleep(3)
        #can hear
        driver.touch('tap',{'x':320,'y':1385,'duration':1})
        sleep(3)
        driver.touch('tap',{'x':540,'y':1385,'duration':1})
        sleep(3)
        driver.touch('tap',{'x':540,'y':1385,'duration':1})
        sleep(3)
        driver.touch('tap',{'x':540,'y':1385,'duration':1})
        sleep(4)
        """
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_007_login_macaca.png'
        driver.save_screenshot(sf1)
        sleep(2)
        """
        driver.element_by_name('个人中心').click()
        sleep(2)
        driver.touch('drag',{'fromX':950,'fromY':800,'toX':950,'toY':550,'duration':1})
        sleep(1)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_007_mycenter_macaca.png'
        driver.save_screenshot(sf2)
        sleep(2)
        driver.element_by_name('我的薪资').click()
        sleep(4)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_007_mySalaryBase_macaca.png'
        driver.save_screenshot(sf3)
        sleep(2)
        #driver.elements_by_class_name('android.view.View')[1].click()
        driver.touch('tap',{'x':800,'y':630,'duration':1})
        sleep(2)
        sf4='./'+now+'_007_mySalaryExtra_macaca.png'
        driver.save_screenshot(sf4)
        sleep(2)
        driver.element_by_id('com.pnlyy.pnlclass_teacher.test:id/leftTv').click()
        sleep(2)


if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('mySalary'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_007_result_macaca.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='Test environment android6.0(google)[查看我的薪资] test case report by Macaca',
                          description='Test case executed status:')
    runner.run(testunit)
    fp.close()
