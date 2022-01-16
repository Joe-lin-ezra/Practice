from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
import random

specific_time = input('Specific time(24hr) (hh:mm:ss): ')
specific_time = datetime.strptime(specific_time, '%H:%M:%S')

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

def go_cart_buy_and_pay():
    chrome.get(url='https://world.taobao.com/cart/cart.htm')

    # click first store checkbutton
    chrome.find_element(By.XPATH, 
                        value='//*[@id="tp-bought-root"]/div[4]/div/table/tbody[1]/tr/td[1]/label/span[1]/input').
    click()
    
    while True:
        now = datetime.strptime(datetime.now(), '%H:%M:%S')
        inteval = now - specific_time
        if inteval.hour == 0 and inteval.minute == 0 and inteval.second == 2:
            break
        else: 
            time.sleep(1)
    
    # submit the selected goods and go payment page
    chrome.find_element(By.XPATH, 
                        value='//*[@id="J_SmallSubmit"]').click()
    # submit this order
    chrome.find_element(By.XPATH, 
                        value='//*[@id="submitOrderPC_1"]/div/a[2]').click()

# check order is valid
def check_order_details():
    chrome.get('https://i.taobao.com/my_taobao.htm')
    chrome.find_element(By.XPATH, value='//*[@id="bought"]').click()
    chrome.find_element(By.XPATH, value='//*[@id="viewDetail"]').click()
    print(chrome.find_element(By.XPATH, value='//*[@id="detail-panel"]/div/div[4]/div[2]/div/div/div/div[3]/div[1]/div[2]/span[3]/span[2]/span').text)


# following https://www.cnblogs.com/sljsz/p/14887102.html 
if __name__ == "__main__":
    login()
    go_cart_buy_and_pay()
    check_order_details()
    print("Please check your order history details.")