
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium_firefox import Firefox
from msqlConnection import connecting
conn = connecting.conn()
mycursor = conn.cursor()
excutable = conn.cursor(dictionary=True)
import webbrowser
import datetime
import time
class newdriver:    
    # برای تعیین نوع رمز ارز و نوع کندل ها
    def printWhatIneed(self):
        print("what is you'r criptocurency:")
        print("type curency by its short code")
        print("EXAMPLE: FOR GET SIGNAL FROM BITCOIN type:")
        print("BTC")
        cripto =  input("what is your criptocurency:\n")
        # print("i want report every ... secound")
        # print("1:   1  minute")
        # print("2:   5  minute")
        # print("3:   15 minute")
        # print("4:   30 minute")
        # print("5:   1 hour")
        # print("6:   2 hour")
        # print("7:   4 hour")
        # print("8:   1 day")
        # print("9:   1 week")
        # print("10:  1 month")
        # sleep = input("i whant my report every :\n")
        # self.getdata(newdriver,str(cripto))
        if(cripto == ""):
            cripto = "btc"
        self.getAnalyse(newdriver,cripto)
    #    تعیین الگوهای تردینگ ویو برای خواندن قیمت 
    def getAnalyse(self,address):
        startsaving = 0
        cripto = address      
        try:
            # browser = webdriver.Chrome("chromedriver.exe")
            browser = webdriver.Firefox()
       
        except:
            browser = webdriver.Chrome()
      
        browser.maximize_window()
        address = "https://www.tradingview.com/symbols/"+address+"USDT/technicals/"
        print("opening "+ address+" site please wait!...")
        print("browser should be complitly loaded be patient till then...")
        browser.get(address)  
        time.sleep(10)
        print("please Log in to your Trading view Acount: ")
        userStatus = input("logined:1 :\n")
        minute = datetime.datetime.utcnow().minute
        startmin = 0
        uppertime= 0
        downertime=0

        try:
            find_serial = browser.find_element(By.ID,"1m")     
            find_serial.click()               
        except:
            time.sleep(10)
            print("reset bot something wrong")
        while True:            
            find_serial = browser.find_element(By.CSS_SELECTOR, '.lastContainer-JWoJqCpY span:first-child')
            curentprice = find_serial.text
            print(datetime.datetime.utcnow().minute)
            time.sleep(10)
            ltame = datetime.datetime.now()
            utc = datetime.datetime.utcnow()
            if(datetime.datetime.utcnow().minute != minute and startsaving == 0):
                print("start")
                startsaving = 1
                startone = 1
                self.saveToDataBase(newdriver,cripto,ltame,utc,curentprice,startone)
                startmin = datetime.datetime.utcnow().minute
                stratprice = curentprice
                minute = datetime.datetime.utcnow().minute
            if(float(curentprice) > float(uppertime)):    
                uppertime   =   curentprice
                upcripto    =   cripto
                upltame     =   ltame
                uputc       =   utc
                upupperone  =   1
                upstartone  =   0
                upendone    =   0
            elif(downertime == 0):    
                downertime =  curentprice
                dowcripto    =   cripto
                dowltame     =   ltame
                dowutc       =   utc
                dowupperone  =   1
            elif(curentprice < downertime):
                downertime =  curentprice
                dowcripto    =   cripto
                dowltame     =   ltame
                dowutc       =   utc
                dowupperone  =   1    

  
            if(datetime.datetime.utcnow().minute != minute and startsaving == 1):   
                print("end")
                self.saveUpperOne(newdriver,cripto,upltame,uputc,uppertime,upupperone)
                self.savedownerOne(newdriver,cripto,dowltame,dowutc,downertime,dowupperone)
                endone= 1 
                startone= 0
                self.saveToDataBase(newdriver,cripto,ltame,utc,curentprice,startone,endone)
                startmin = datetime.datetime.utcnow().minute
                stratprice = curentprice
                minute = datetime.datetime.utcnow().minute

            
           
    def saveToDataBase(self,curency_name,ltame,utc,price,startone = 0,endone = 0):
        activitysql = "INSERT INTO final (curency_name,ltame,utc,price,startone,endone) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (curency_name,ltame,utc,price,startone,endone)
        excutable.execute(activitysql,val)
        conn.commit()
        print(mycursor.rowcount, "record inserted.")

    def saveUpperOne(self,curency_name,ltame,utc,price,upupperone):
        activitysql = "INSERT INTO final (curency_name,ltame,utc,price,upperone) VALUES (%s,%s,%s,%s,%s)"
        val = (curency_name,ltame,utc,price,upupperone)
        excutable.execute(activitysql,val)
        conn.commit()
        print(mycursor.rowcount, "record inserted.")

    def savedownerOne(self,curency_name,ltame,utc,price,upupperone):
        activitysql = "INSERT INTO final (curency_name,ltame,utc,price,downnerone) VALUES (%s,%s,%s,%s,%s)"
        val = (curency_name,ltame,utc,price,upupperone)
        excutable.execute(activitysql,val)
        conn.commit()
        print(mycursor.rowcount, "record inserted.")


               

    def cleartable():
        activitysql = "DELETE FROM final"
        excutable.execute(activitysql)
        conn.commit()
        time.sleep(10)
        activitysql = "ALTER TABLE final AUTO_INCREMENT = 1"
        excutable.execute(activitysql)
        conn.commit()



newdriver.printWhatIneed(newdriver)

"""
    CLEAR TABLE

"""
# UNCOMMENT bellow LINE TO CLEAR FINAL TABLE        
# newdriver.cleartable()
        


# browser = webdriver.Chrome("chromedriver")    
# browser.maximize_window()
# address = "https://www.tradingview.com/symbols/BTCUSD/technicals/"
# browser.get(address)
# find_serial = browser.find_element_by_css_selector(".button-qM2OSl9-.size-xsmall-1UtgdwJA.color-brand-eDTq6RMz.variant-primary-3m2-v4cq")            
# find_serial.click()  
# priceDiv =  browser.find_element_by_css_selector("h2.tv-symbol-header__first-line")
# my_string = priceDiv.text
# print(my_string.split("/",1)[0])

# activitysql = "INSERT INTO test (name,maname) VALUES (%s,%s)"
# vasl = ("test","test")
# excutable.execute(activitysql,vasl)

# print(excutable.lastrowid)
# conn.commit()
# ALTER TABLE tablename AUTO_INCREMENT = 1