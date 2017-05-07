require 'rubygems'
require 'appium_lib'
require 'selenium-webdriver'
require 'date'

def desired_caps
{ 
	caps:       { 
      appiumVersion:       '1.6.4',
      platformName:        'iOS',
      automationName:      'XCUITest',
	    versionNumber:       '10.3',
	    deviceName:          'iPhone 6',
	    app:                 '/Users/samwang/Desktop/PJS.app',
      udid:                '43B328A0-EB1D-4FF5-9B75-33F3E1596BC7',
      fullReset:           true,
      newCommandTimeout:   '90'
	},
    
	appium_lib: 
	{ sauce_username: nil, 
	  sauce_access_key: nil, 
	  debug: true
	}
    
}
end

server_url="http://0.0.0.0:4723/wd/hub"
dr = Appium::Driver.new(desired_caps).start_driver
sleep 3

#action=Appium::TouchAction.new.press(x: 325, y: 500).wait(1000).move_to(x: -275, y: 0).release()
#action.perform
#dr.execute_script('mobile: swipe',direction: 'left', start_x:325,start_y:500,end_x:-275,end_y:0)
dr.execute_script('mobile: dragFromToForDuration',direction: 'left', fromX:325,fromY:500,toX:-275,toY:0, duration:1.0)
sleep 2
dr.execute_script('mobile: dragFromToForDuration',direction: 'left', fromX:325,fromY:500,toX:-275,toY:0, duration:1.0)
sleep 2
dr.execute_script('mobile: dragFromToForDuration',direction: 'left', fromX:325,fromY:500,toX:-275,toY:0, duration:1.0)
sleep 2
dr.find_element(:class_name, 'Button').click
sleep 4
dr.find_element(:name, '登录').click
sleep 3
mo=dr.find_element(:xpath, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
mo.click
mo.send_keys "13816032863"
dr.find_element(:name, 'Done').click
sleep 1
pwd=dr.find_element(:xpath, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[2]/XCUIElementTypeSecureTextField[1]')
pwd.click
pwd.send_keys "0422wxl"
dr.find_element(:name, 'Done').click
sleep 1
dr.find_element(:xpath, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeButton[2]').click
sleep 3
dr.find_element(:name, '取消').click
sleep 3
dr.find_element(:name, '投资').click
sleep 3
dr.find_element(:name, '优贝').click
sleep 3
#action2=Appium::TouchAction.new.press(x: 160, y: 600).wait(1000).move_to(x: 0, y: -550).release()
#action2.perform
dr.execute_script('mobile: dragFromToForDuration',direction: 'up', fromX:160,fromY:600,toX:0,toY:-550, duration:1.0)
sleep 2
dr.execute_script('mobile: dragFromToForDuration',direction: 'up', fromX:160,fromY:600,toX:0,toY:-550, duration:1.0)
sleep 2
#action3=Appium::TouchAction.new.press(x: 160, y: 600).wait(1000).move_to(x: 0, y: -300).release()
#dr.execute_script('mobile: dragFromToForDuration',direction: 'up', fromX:160,fromY:600,toX:0,toY:-300, duration:1.0)
#sleep 2
dr.find_element(:name, '优贝90 14期').click
sleep 3
dr.find_element(:name, '立即投资').click
sleep 3
amount=dr.find_element(:xpath, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeTextField[1]')
amount.click
amount.send_keys "1400"
dr.find_element(:name, 'Done').click
sleep 1
#no eBei
dr.find_element(:name, 'Button').click
sleep 1
#coupon
#dr.find_element(:xpath, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]/XCUIElementTypeButton[1]').click
#sleep 1
#100 Yuan coupon
#'100元投资券'
#sleep 1
#payment method
dr.find_element(:xpath, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeScrollView[1]/XCUIElementTypeOther[3]/XCUIElementTypeOther[3]').click
sleep 2
#balance
#'本金账户（元）'
dr.find_elements(:class_name, 'Cell')[0].click
sleep 2
#xinzhibao
#'薪智宝（元）'
#sleep 1
#bankcard
#'建设银行 (尾号1425)'
#sleep 1
#I agree
dr.find_element(:name, 'd9').click
dr.find_element(:name, '立即支付').click
sleep 3
#dr.find_element(:name, '知道了').click
#sleep 2
dr.find_element(:name, '我的').click
sleep 3
#action4=Appium::TouchAction.new.press(x: 160, y: 600).wait(1000).move_to(x: 0, y: -200).release()
#action4.perform
dr.execute_script('mobile: dragFromToForDuration',direction: 'up', fromX:160,fromY:600,toX:0,toY:-300, duration:1.0)
sleep 1
dr.find_element(:name, '优贝赚呗投资记录').click
sleep 3
t=Time.new
now=t.strftime("%Y%m%d_%H%M%S")
sf1="./"+now+"_004_inv_records.png"
dr.save_screenshot sf1
sleep 2
dr.find_element(:name, '投资优贝90 14期').click
sleep 3
t=Time.new
now=t.strftime("%Y%m%d_%H%M%S")
sf2="./"+now+"_004_inv_detail.png"
dr.save_screenshot sf2
sleep 2
dr.find_element(:name, 'leftback').click
sleep 2
dr.find_element(:name, 'leftback white').click
sleep 2
#ebei
dr.find_element(:xpath, '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[4]').click
sleep 3
t=Time.new
now=t.strftime("%Y%m%d_%H%M%S")
sf3="./"+now+"_004_eBei.png"
dr.save_screenshot sf3
sleep 2
puts 'So far so good.'
dr.quit
