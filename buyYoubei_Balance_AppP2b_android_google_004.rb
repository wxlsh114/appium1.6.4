require 'rubygems'
require 'appium_lib'
require 'selenium-webdriver'
require 'date'

def desired_caps
{ 
	caps:       { 
      #appiumVersion:       ‘1.6.4’,
      platformName:        'Android',
	  platformVersion:     '6.0',
      automationName:      'UIAutomator2',
      #udid:				   '192.168.56.101:5555',
	  deviceName:          'emulator-5554',
	  app:                 'c://rb//51p2b_debug_2.4.5.apk',
	  appPackage:          'com.richfinancial.pujiaosuo',
	  unicodeKeyboard:     'true',
	  resetKeyboard:       'true',
      fullReset:           'true'
	},
    
	appium_lib: 
	{ sauce_username: nil, 
	  sauce_access_key: nil, 
	  server_url: 'http://127.0.0.1:4723/wd/hub'
	  #debug: true
	} 
}
end
dr = Appium::Driver.new(desired_caps).start_driver
sleep 5

Appium::TouchAction.new.press(x: 950, y: 1600).wait(1000).move_to(x: 50, y: 1600).release().perform
#action=Appium::TouchAction.new.swipe(start_x: 950, start_y: 1600, end_x: 50, end_y: 1600, duration: 200)
#action.perform
sleep 3
Appium::TouchAction.new.press(x: 950, y: 1600).wait(1000).move_to(x: 50, y: 1600).release().perform
sleep 3
Appium::TouchAction.new.press(x: 950, y: 1600).wait(1000).move_to(x: 50, y: 1600).release().perform
sleep 3
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/welcome_button').click
sleep 5
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/tv_title_view_left').click
#dr.find_element(:name, "登录").click
sleep 3
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/phone').click
dr.hide_keyboard
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/phone').send_keys "13816032863"
sleep 1
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/password').click
dr.hide_keyboard
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/password').send_keys "0422wxl"
sleep 1
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/login').click
sleep 2
dr.find_elements(:class_name, 'android.widget.Button')[0].click
sleep 3
#invest
dr.find_elements(:id, 'com.richfinancial.pujiaosuo:id/tabname')[2].click
sleep 3
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/tab_all_investing_product_list_right').click
sleep 3
Appium::TouchAction.new.press(x: 520, y: 1600).wait(1000).move_to(x: 520, y: 50).release().perform
sleep 2
Appium::TouchAction.new.press(x: 520, y: 1600).wait(1000).move_to(x: 520, y: 50).release().perform
sleep 2
dr.find_element(:uiautomator, 'new UiSelector().text("优贝90 14期")').click
#dr.find_elements(:id, 'com.richfinancial.pujiaosuo:id/product_title')[0].click
sleep 3
#dr.find_element(:uiautomator, 'new UiSelector().text("立即投资")').click
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/confirmed_invest').click
sleep 3
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/invest_pay_value').click
dr.hide_keyboard
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/invest_pay_value').send_keys "2000"
dr.hide_keyboard
sleep 1
#without eBei
#dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/cb_ebei').click
#sleep 1
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/invest_mothed').click
sleep 2
#text("账户余额（元）")').click
dr.find_elements(:id, 'com.richfinancial.pujiaosuo:id/item_title')[0].click
sleep 2
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/xieyi_check').click
sleep 1
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/pay_now').click
sleep 3
#got it.
#dr.find_elements(:class_name, 'android.widget.Button')[0].click
#sleep 1
dr.find_element(:uiautomator, 'new UiSelector().text("我的")').click
#dr.find_elements(:id, 'com.richfinancial.pujiaosuo:id/tabname')[4].click
sleep 3
dr.find_element(:uiautomator, 'new UiSelector().text("优贝赚呗投资记录")').click
#dr.find_elements(:id, 'com.richfinancial.pujiaosuo:id/name')[0].click
sleep 3
t=Time.new
now=t.strftime("%Y%m%d_%H%M%S")
sf1="./"+now+"_004_inv_records_google.png"
dr.save_screenshot sf1
sleep 2
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/invest_balance').click
sleep 3
t=Time.new
now=t.strftime("%Y%m%d_%H%M%S")
sf2="./"+now+"_004_inv_detail_google.png"
dr.save_screenshot sf2
sleep 2
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/layout_title_view_return').click
sleep 2
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/layout_title_view_return').click
sleep 2
#balance
dr.find_element(:uiautomator, 'new UiSelector().text("账户余额（元）")').click
sleep 3
#detail
#'new UiSelector().text("查看余额明细")'
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/touch_balance').click
sleep 2
#capital
#'new UiSelector().text("本金")'
dr.find_element(:id, 'com.richfinancial.pujiaosuo:id/tab_capital').click
sleep 2
t=Time.new
now=t.strftime("%Y%m%d_%H%M%S")
sf4="./"+now+"_004_capital_records_google.png"
dr.save_screenshot sf4
sleep 2
dr.find_element(:uiautomator, 'new UiSelector().text("投资优贝90 14期")').click
sleep 3
t=Time.new
now=t.strftime("%Y%m%d_%H%M%S")
sf5="./"+now+"_004_capital_detail_google.png"
dr.save_screenshot sf5
sleep 2
puts 'So far so good.'
dr.quit
