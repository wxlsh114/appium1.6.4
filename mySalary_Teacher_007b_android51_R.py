#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
#from appium.webdriver.common.touch_action import TouchAction
from pub_Teacher import login,logout

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestTeacher(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['automationName'] = 'UIAutomator2'
        desired_caps['deviceName'] = 'N1'
        #desired_caps['udid'] = 'L25093FSN1K2'
        desired_caps['app'] = PATH('../VIPTeacher_2.0.2.apk')
        desired_caps['appPackage'] = 'com.pnlyy.pnlclass_teacher.test'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['fullReset'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(3)

    def tearDown(self):
        # end the session
        self.driver.quit()
        

    def mySalary(self):
        driver=self.driver       
        login(self)
        driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("我的薪资")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_007b_mySalaryBase_R.png'
        driver.save_screenshot(sf1)
        sleep(1)
        driver.find_element_by_android_uiautomator('new UiSelector().text("提成")').click()
        sleep(2)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf1='./'+now+'_007b_mySalaryExtra_R.png'
        driver.save_screenshot(sf1)
        sleep(1)

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher('mySalary'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_007b_result_R.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='Test environment android5.1.1(NOKIA N1)[查看我的薪资] test case report by Appium1.6.5',
                          description='Test case executed status:')
    runner.run(testunit)
    fp.close()
