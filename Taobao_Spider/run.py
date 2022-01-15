from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
import random


chrome = webdriver.Chrome()

def login():
    chrome.get('https://www.taobao.com/')
    try:
        chrome.find_element(By.LINK_TEXT, value='亲，请登录').click()
        # the original login type is account/password, but we need to login with QRcode
        # the switch button is in another frame
        iframe = chrome.find_element(By.CSS_SELECTOR, value='#J_Member')
        # switch to the iframe
        chrome.switch_to.frame(iframe)
        # click the switch-to-QRcode-button
        icon = chrome.find_element(By.CSS_SELECTOR, value='#login > div.corner-icon-view.view-type-qrcode > i')
        icon.click()
        # switch back to chrome driver
        chrome.switch_to.default_content()
        time.sleep(30)
        print('login completed!')
    except Exception as e:
        print(str(e))

def go_cart_and_wait():
    chrome.get(url='https://cart.taobao.com/cart.htm')
    while True:
        current = datetime.now()
        # compute the time diff
        # if time.diff(now, specific time).second > 180
        if True:
            time.sleep(random.randint(52, 78))
            chrome.refresh()
            pass
        else:
            break
    
# following https://www.cnblogs.com/sljsz/p/14887102.html 
if __name__ == "__main__":
    login()
    go_cart_and_wait()
    