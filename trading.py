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
browser.get("https://www.tradingview.com/symbols/18CBTC/technicals/")
find_serial = browser.find_element_by_css_selector(".speedometerSignal-DPgs-R4s.sellColor-DPgs-R4sfirst-child")
if find_serial.text == 'Sell': 
    print("Sell")
elseif find_serial.text == 'Sell':     