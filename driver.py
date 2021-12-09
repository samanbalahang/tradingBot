from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
import webbrowser
import time
class driver:    
    def getAnalyse(self,address, sleeptime,os):
        print("opening site please wait!...")
        if(os == 1):
         browser = webdriver.Chrome("chromedriver.exe")
        else:
         browser = webdriver.Chrome("chromedriver")    
        browser.maximize_window()
        address = "https://www.tradingview.com/symbols/"+address+"USD/technicals/"
        print(address)
        browser.get(address)
        time.sleep(10)
        while True:
            print("tick")
            print("opening site please wait!...")
            try:
              find_serial = browser.find_element_by_css_selector(".tv-card-container__ideas.tv-card-container__ideas--with-padding")
            except:
                print("S")
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
            time.sleep(sleeptime)
    def getdata(self,cripto,os,sleep):
        sleep = int(sleep)
        if(cripto == '1'):
            cripto = "BTC"
            # print(cripto)
        elif(cripto == "2"): 
             cripto = "DOT" 
            #  print(cripto)
        elif(cripto == "3"):  
            cripto = "LTC" 
            # print(cripto)
        elif(cripto == "4"):  
            cripto = "ETH"  
            # print(cripto)  
        else:
            print(cripto) 
            # print("not validate")               
        self.getAnalyse(driver,cripto,sleep,os)
