import base64
import os
import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


desired_cap={
                "platformName": "Android Automation",
                "platformVersion": "10.0",
                "appPackage": "com.coppi.bestbuy",
                "appActivity": "com.bestbuy.android.activity.HomeScreenActivity",
                "newCommandTimeout": 600,
}

driver=webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
# Start Recording
driver.start_recording_screen()
time.sleep(8)




#Search an element by customized xpath
driver.find_element_by_xpath("//android.widget.TextView[@text='Products']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Computers, Tablets & Accessories']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Laptops and Desktops']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='MacBooks']").click()
driver.implicitly_wait(5)
# price=driver.find_element_by_xpath("//android.widget.ImageView[@bounds='[32,384][332,684]']").get_attribute("text")

# print("The price of first Macbook is "+price)
# assert price=="$1,299.99","The price does not match"
"""
Touch Actions for scolling best buy=
TouchAction(driver)   .press(x=327, y=1073)   .move_to(x=314, y=458)   .release()   .perform()
TouchAction(driver)   .press(x=322, y=1109)   .move_to(x=327, y=410)   .release()   .perform()

"""
driver.implicitly_wait(600)
TouchAction(driver).long_press(x=322, y=1109).move_to(x=327, y=410).release().perform()

for i in range(1):
    touch = TouchAction(driver)
    touch.long_press(x=322, y=1109).move_to(x=327, y=410).release().perform()
    time.sleep(2)
#
#
#Testing Gestures

#Bestbuy logo click coordinates ==TouchAction(driver)   .press(x=357, y=108)   .move_to(x=357, y=108)   .release()   .perform()
gestures=TouchAction(driver)
gestures.tap(x=357, y=108).perform()
#Going top to bottom coordinates= TouchAction(driver)   .press(x=333, y=1050)   .move_to(x=357, y=239)   .release()   .perform()
gestures.long_press(x=333, y=1050).move_to(x=357, y=239).release().perform()
#Going bottom to top coordinates==    TouchAction(driver)   .press(x=326, y=242)   .move_to(x=343, y=1050)   .release()   .perform()
gestures.long_press(x=326, y=242).move_to(x=343, y=1050).release().perform()
driver.find_element_by_id("com.coppi.bestbuy:id/toolbarSearchHint").click()
driver.find_element_by_id("com.coppi.bestbuy:id/search_edit_text").send_keys("SONY 1000XM4")
gestures.tap(x=656, y=1305).perform()



#Looking for Gaming laptop:
driver.implicitly_wait(5)
gestures.tap(x=350, y=98).perform()
driver.find_element_by_xpath("//android.widget.TextView[@text='Products']").click()
# driver.find_element_by_xpath("//android.widget.TextView[@text='Computers, Tablets & Accessories']").click()
# driver.find_element_by_xpath("//android.widget.TextView[@text='Laptops and Desktops']").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("//android.widget.TextView[@text='Laptops']").click()
driver.implicitly_wait(5)
driver.find_element_by_id("com.coppi.bestbuy:id/sortAndFilter").click()
driver.implicitly_wait(5)
driver.find_element_by_xpath("(//android.widget.TextView[@content-desc='bestBuySortFilterExpandFacet'])[1]").click()
driver.find_element_by_xpath("//android.widget.CheckedTextView[@text='Gaming Laptops (1637)']").click()
time.sleep(4)
driver.find_element_by_id("com.coppi.bestbuy:id/apply").click()
time.sleep(4)

#For loop for gestures after applying the filter.
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5)
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5)

gestures.long_press(x=333, y=444).move_to(x=324, y=1118).release().perform()
driver.implicitly_wait(15)
time.sleep(4)

gestures.tap(x=118, y=458).perform()

gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5)
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5)
time.sleep(4)

gestures.long_press(x=333, y=444).move_to(x=324, y=1118).release().perform()
driver.find_element_by_xpath("//android.widget.TextView[@text='Add To Cart']").click()
driver.find_element_by_xpath("//android.widget.TextView[@text='View Cart']").click()
time.sleep(7)
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5)
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
driver.implicitly_wait(5)
gestures.long_press(x=316, y=1203).move_to(x=343, y=398).release().perform()
time.sleep(4)


# Video processing code:
vide_rawdata=driver.stop_recording_screen()
video_name=driver.current_activity+time.strftime("%Y_%m_%d_%H%M%S")
filepath=os.path.join("S:/Appium/ "+video_name+".mp4")
with open(filepath,"wb") as vd:
    vd.write(base64.b64decode(vide_rawdata))
time.sleep(4)
driver.save_screenshot("S:/Appium/ "+video_name+".png")











