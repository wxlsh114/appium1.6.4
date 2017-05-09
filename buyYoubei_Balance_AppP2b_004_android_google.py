#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import *
#from appium.webdriver.common.touch_action import TouchAction
from HTMLTestRunner import HTMLTestRunner

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AppP2b(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['automationName'] = 'UIAutomator2'
        desired_caps['app'] = PATH('/users/samwang/desktop/app/51p2b_debug_2.4.5.apk')
        desired_caps['appPackage'] = 'com.richfinancial.pujiaosuo'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        #desired_caps['udid'] = '192.168.56.101:5555'
        desired_caps['fullReset'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        sleep(5)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def buy_Youbei(self):
        driver=self.driver       

        driver.swipe(950,1600,50,1600,1000)
        sleep(3)
        driver.swipe(950,1600,50,1600,1000)
        sleep(3)
        driver.swipe(950,1600,50,1600,1000)
        sleep(3)
        driver.find_element_by_id('com.richfinancial.pujiaosuo:id/welcome_button').click()
        sleep(5)
        driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()
        #driver.find_element_by_id('com.richfinancial.pujiaosuo:id/tv_title_view_left').click()
        sleep(5)
        driver.find_element_by_id('com.richfinancial.pujiaosuo:id/phone').click()
        driver.find_element_by_id('com.richfinancial.pujiaosuo:id/phone').set_value('13816032863')
        sleep(2)
        driver.find_element_by_id('com.richfinancial.pujiaosuo:id/password').click()
        driver.find_element_by_id('com.richfinancial.pujiaosuo:id/password').set_value('0422wxl')
        sleep(2)
        driver.find_element_by_id('com.richfinancial.pujiaosuo:id/login').click()
        sleep(3)
        #cancel
        driver.find_elements_by_class_name('android.widget.Button')[0].click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("投资")').click()
        sleep(4)
        #Youbei
        #driver.find_element_by_id('com.richfinancial.pujiaosuo:id/tab_all_investing_product_list_right').click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("优贝")').click()
        sleep(3)
        #scroll to page2
        driver.swipe(520,1600,520,100,1000)
        sleep(2)
        driver.swipe(520,1600,520,200,1000)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("优贝90 14期")').click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("立即投资")').click()
        sleep(3)
        driver.find_element_by_id('com.richfinancial.pujiaosuo:id/invest_pay_value').click()
        driver.find_element_by_id('com.richfinancial.pujiaosuo:id/invest_pay_value').set_value('1500')
        sleep(2)
        #e-Bai
        #driver.find_element_by_id('com.richfinancial.pujiaosuo:id/cb_ebei').click()
        #sleep(2)
        driver.find_element_by_id('com.richfinancial.pujiaosuo:id/invest_mothed').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("账户余额（元）")').click()
        sleep(2)
        #driver.find_element_by_id('com.richfinancial.pujiaosuo:id/xieyi_check').click()
        driver.find_element_by_android_uiautomator('new UiSelector().text("我同意")').click()
        sleep(2)
        driver.find_element_by_id('com.richfinancial.pujiaosuo:id/pay_now').click()
        sleep(5)
        driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        sleep(3)
        driver.find_element_by_android_uiautomator('new UiSelector().text("优贝赚呗投资记录")').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf2='./'+now+'_004_inv_records_google.png'
        driver.save_screenshot(sf2)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("投资优贝90 14期")').click()
        #driver.find_element_by_id('com.richfinancial.pujiaosuo:id/item_title').click()
        sleep(3)
        now=time.strftime('%Y-%m-%d %H_%M_%S')
        sf3='./'+now+'_004_inv_detail_google.png'
        driver.save_screenshot(sf3)
        sleep(3)
        driver.find_element_by_id("com.richfinancial.pujiaosuo:id/layout_title_view_return").click()
        sleep(3)
        driver.find_element_by_id("com.richfinancial.pujiaosuo:id/layout_title_view_return").click()
        sleep(3)
        driver.swipe(540,1000,540,300,1000)
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("账户余额（元）")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("查看余额明细")').click()
        sleep(2)
        driver.find_element_by_android_uiautomator('new UiSelector().text("本金")').click()
        sleep(3)
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf0="./"+now+"_004_capital_records_google.png"
        driver.save_screenshot(sf0)
        sleep(2)
        driver.find_element_by_id("com.richfinancial.pujiaosuo:id/channel").click()
        sleep(2)
        now=time.strftime("%Y-%m-%d %H_%M_%S")
        sf1="./"+now+"_004_capital_detail_google.png"
        driver.save_screenshot(sf1)
        sleep(2)
                    
if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(AppP2b('buy_Youbei'))
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename='./'+now+'_004_result_google.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='51p2b of App environment android6.0[投资优贝(用账户余额支付)] test case report by Appium1.6.4',
                          description='Test case executed status:')
    runner.run(testunit)
    fp.close()
