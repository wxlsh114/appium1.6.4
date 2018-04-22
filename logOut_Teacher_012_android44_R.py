#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
#from selenium.webdriver.common.action_chains import *
#from appium.webdriver.common.touch_action import TouchAction
from HTMLTestRunner import HTMLTestRunner

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class TestTeacher(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4'
        desired_caps['deviceName'] = 'N958St'
        desired_caps['udid'] = '0123456789'
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

    def logOut(self):
        driver=self.driver       
        #720*1280
        driver.swipe(650,1000,50,1000,1000)
        sleep(1)
        driver.swipe(650,1000,50,1000,1000)
        sleep(1)
        driver.find_element_by_id("com.pnlyy.pnlclass_teacher.test:id/btnStart").click()
        sleep(3)
        user=driver.find_element_by_id("com.pnlyy.pnlclass_teacher.test:id/etUserName")
        user.click()
        user.set_value("18311111111")
        sleep(2)
        pwd=driver.find_element_by_id("com.pnlyy.pnlclass_teacher.test:id/etPassword")
        pwd.click()
        pwd.set_value("123456")
        sleep(1)
        driver.find_element_by_id("com.pnlyy.pnlclass_teacher.test:id/btnLogin").click()
        sleep(3)
        #test now
        driver.find_element_by_android_uiautomator('text("开始测试")').click()
        sleep(2)

        driver.find_element_by_android_uiautomator('text("点击开始录音")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('text("停止录音")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('text("有听到声音")').click()
        sleep(2)
        
        driver.find_element_by_android_uiautomator('text("下一步")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('text("下一步")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('text("完成测试")').click()
        sleep(2)
        """
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf2="./"+now+"_012_logout_R.png"
        driver.save_screenshot(sf2)
        sleep(1)
        """
        driver.find_element_by_android_uiautomator('text("个人中心")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('text("退出登录")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('text("确定")').click()
        sleep(2)
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf3="./"+now+"_012_logout_R.png"
        driver.save_screenshot(sf3)
        sleep(3)
                    
if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(TestTeacher("logOut"))
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename="./"+now+"_012_result_R.html"
    fp=open(filename,"wb")
    runner=HTMLTestRunner(stream=fp,title='Test environment of Teacher android4.4(ZTE V5Max)(退出登录) test case report by Appium1.6.5',
                          description='Test case executed status:')
    runner.run(testunit)
    fp.close()
