#coding=utf-8
import unittest,time,os
from time import sleep
from appium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from HTMLTestRunner import HTMLTestRunner
#from appium.webdriver.common.touch_action import TouchAction


def login(self):
    driver=self.driver
    #driver.touch('drag',{'fromX':1350,'fromY':1600,'toX':50,'toY':1600,'duration':1})
    driver.swipe(1350,1600,50,1600,1000)
    sleep(1)
    driver.swipe(1350,1600,50,1600,1000)
    sleep(1)
    driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/btnStart').click()
    sleep(2)
    #driver.find_find_element_by_android_uiautomator('马上体验').click()
    #sleep(4)
    user=driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/etUserName')
    user.click()
    user.set_value('18311111111')
    sleep(1)
    pwd=driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/etPassword')
    pwd.click()
    pwd.set_value('123456')
    sleep(1)
    #登录
    driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/btnLogin').click()
    sleep(4)
    #test now
    driver.find_element_by_android_uiautomator('new UiSelector().text("开始测试")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("点击开始录音")').click()
    sleep(4)
    driver.find_element_by_android_uiautomator('new UiSelector().text("停止录音")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("有听到声音")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("完成测试")').click()
    sleep(3)
    """
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    sf1='./'+now+'_login_R.png'
    driver.save_screenshot(sf1)
    sleep(1)
    """

def logout(self):
    driver=self.driver 
    driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
    sleep(2)
    """
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    sf2='./'+now+'_personcenter_R.png'
    driver.save_screenshot(sf2)
    sleep(2)
    """
    driver.find_element_by_android_uiautomator('new UiSelector().text("退出登录")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("确定")').click()
    sleep(2)
    """
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    sf3='./'+now+'_logout_R.png'
    driver.save_screenshot(sf3)
    sleep(2)
    """

def testdevice(self):
    driver=self.driver 
    driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
    sleep(2)
    t=driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/testingHintTv').text
    print(t)
    assert '测试已通过' in t
    sleep(2)
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    sf='./'+now+'_personCenter_R.png'
    driver.save_screenshot(sf)
    sleep(2)
    driver.find_element_by_id('com.pnlyy.pnlclass_teacher.test:id/testingHintTv').click()
    sleep(2)
    #test now
    driver.find_element_by_android_uiautomator('new UiSelector().text("开始测试")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("点击开始录音")').click()
    sleep(3)
    driver.find_element_by_android_uiautomator('new UiSelector().text("停止录音")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("有听到声音")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("下一步")').click()
    sleep(2)
    driver.find_element_by_android_uiautomator('new UiSelector().text("完成测试")').click()
    sleep(3)

