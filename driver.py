from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
import webbrowser
import datetime
import time
class driver:    
    def getAnalyse(self,address, sleeptime,os,child):
        cripto = address
      
        child=child
        if(os == 1):
         browser = webdriver.Chrome("chromedriver.exe")
        else:
         browser = webdriver.Chrome("chromedriver")    
        browser.maximize_window()
        address = "https://www.tradingview.com/symbols/"+address+"USD/technicals/"
        print("opening "+ address+" site please wait!...")
        print("browser should be complitly loaded be patient till then...")
        browser.get(address)
        time.sleep(10)
        counter = 1
        while True:            
            print("OK!")
            try:
             #path = "#technicals-root .technicalsTab-DPgs-R4s .tabs-3-f9q69b"  
              path = "#technicals-root .technicalsTab-DPgs-R4s .tabs-3-f9q69b button:"+child  
              find_serial = browser.find_element_by_css_selector(path)
              print("horray")
             #print(path)
              find_serial.click()
            except:
                print("")
            find_serial = browser.find_element_by_css_selector("span.speedometerSignal-DPgs-R4s")
            
            print("you can have signal after 10 secound")
            time.sleep(10)
            signal = find_serial.text
            if find_serial.text == 'SELL': 
                print("SELL")
            elif find_serial.text == 'STRONG SELL': 
                print("STRONG SELL") 
            elif find_serial.text == 'BUY': 
                print("BUY")
            elif find_serial.text == 'STRONG BUY': 
                print("STRONG BUY") 
            else:
                print("nutral") 
            if(counter == 1):
               time.sleep(sleeptime)
            else: 
               try:
                curentprice =  browser.find_element_by_css_selector(".tv-symbol-price-quote__value.js-symbol-last")  
                curentprice = curentprice.text 
                print(curentprice)   
                text = str(sleeptime) +" "
                text= text+str(datetime.datetime.now())+" "
                text= text+"UTC: "+str(datetime.datetime.utcnow())+" "
                text= text+"price: "+str(curentprice)+" "
                text = text+ str(signal)
                # print(text)
                print("")
                print("start again for next signal, don't need any action everey thing are automated!")
                print("")
               except:
                print("notext") 
               try:
                   self.printTotxt(driver,text,cripto,sleeptime)  
               except:
                   print("")
               sleeptime = int(sleeptime)         
               time.sleep(sleeptime)
            counter = counter + 1   
    def printTotxt(self,text,address,sleeptime):
        # text_file = open("./data.txt", "a+")
        try:
            sleeptime=str(sleeptime)
            print(address)
            text_file = open("./"+address+"-"+sleeptime+".txt", "a+")
            text_file.write("\n")
            text_file.write(text)
        except:
            print("we coudent create file to save report on it:")    
                    
    def getdata(self,cripto,os,sleep):
        if(sleep == '1'):
            child = "first-child"
            sleep = int(60)
        elif(sleep == "2"): 
            child = "nth-child(2)"
            sleep = int(60*5)
        elif(sleep == "3"): 
            child = "nth-child(3)"
            sleep = int(60*15)  
        elif(sleep == "4"): 
            child = "nth-child(4)"
            sleep = int(60*30) 
        elif(sleep == "5"): 
            child = "nth-child(5)"
            sleep = int(60*60*1)  
        elif(sleep == "6"): 
            child = "nth-child(6)"
            sleep = int(60*60*2)  
        elif(sleep == "7"): 
            child = "nth-child(7)"
            sleep = int(60*60*4)  
        elif(sleep == "8"): 
            child = "nth-child(8)"
            sleep = int(60*60*12*1)  
        elif(sleep == "9"): 
            child = "nth-child(9)"
            sleep = int(60*60*12*7)        
        elif(sleep == "10"): 
            child = "nth-child(10)"
            sleep = int(60*60*12*30)     
        sleep = int(sleep)
        print("we will check: "+cripto+" every "+ sleep+" seconds:")          
        self.getAnalyse(driver,cripto,sleep,os,child)
    def printWhatIneed(self):
        print("what is you'r operating system:")
        print("please just put number")
        print("1 : Windows")
        print("2 : linux")
        os = input("what is your os:\n")
        print("what is you'r criptocurency:")
        print("what is you'r criptocurency:")
        print("type curency by its short code")
        print("EXAMPLE: FOR GET SIGNAL FROM BITCOIN type:")
        print("BTC")
        cripto =  input("what is your criptocurency:\n")
        print("i want report every ... secound")
        print("1:   1  minute")
        print("2:   5  minute")
        print("3:   15 minute")
        print("4:   30 minute")
        print("5:   1 hour")
        print("6:   2 hour")
        print("7:   4 hour")
        print("8:   1 day")
        print("9:   1 week")
        print("10:  1 month")
        sleep = input("i whant my report every :\n")  
        try:
            self.getdata(driver,cripto,os,sleep)
        except:
            print("please just put number")  
            print("1 : Windows")
            print("2 : linux")
            os = input("what is your os:\n")   
