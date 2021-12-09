from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
import webbrowser
import time

browser = webdriver.Chrome("chromedriver")
browser.maximize_window()
print("opening site please wait!...")
browser.get("https://www.tradingview.com/symbols/LTCUSD/technicals/")
time.sleep(10)
while True:
    print("tick")
    print("opening site please wait!...")
    find_serial = browser.find_element_by_css_selector("span.speedometerSignal-DPgs-R4s")
    print("eleman is find you can have signal now")
    print(find_serial.text)
    time.sleep(10)
    print("AFTERSLEEP: ")
    if find_serial.text == 'SELL': 
        print("Sell")
    elif find_serial.text == 'STRONG SELL': 
        print("Sell") 
    elif find_serial.text == 'BUY': 
        print("Buy")
    elif find_serial.text == 'STRONG BUY': 
        print("Buy") 
    else:
        print("nutral") 
    time.sleep(300)