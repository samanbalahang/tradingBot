# ALTER TABLE tablename AUTO_INCREMENT = 1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from msqlConnection import connecting
import chromedriver_autoinstaller
chromedriver_autoinstaller.install() 
conn = connecting.conn()
mycursor = conn.cursor()
excutable = conn.cursor(dictionary=True)
import webbrowser
import datetime
import time
class newdriver:    
    def getAnalyse(self,address, sleeptime,os,child):
        cripto = address      
        child=child
        reportInSecond  = sleeptime
        if(sleeptime > 60):
            sleeptime = 60
        if(os == 1):
         
        #  browser = webdriver.Chrome("chromedriver.exe")
         browser = webdriver.Chrome()
            
        else:
         browser = webdriver.Chrome("chromedriver")    
        browser.maximize_window()
        address = "https://www.tradingview.com/symbols/"+address+"USD/technicals/"
        print("opening "+ address+" site please wait!...")
        print("browser should be complitly loaded be patient till then...")
        browser.get(address)
        self.fillIndicators(newdriver,browser)
    
        time.sleep(10)
        try:
           find_serial = browser.find_element_by_css_selector(".button-qM2OSl9-.size-xsmall-1UtgdwJA.color-brand-eDTq6RMz.variant-primary-3m2-v4cq")            
           find_serial.click()   
           #path = "#technicals-root .technicalsTab-DPgs-R4s .tabs-3-f9q69b"  
           path = "#technicals-root .technicalsTab-DPgs-R4s .tabs-3-f9q69b button:"+child  
           find_serial = browser.find_element_by_css_selector(path)
           print(find_serial.tag_name)
           #print(path)         
           find_serial.click()
        except:
           time.sleep(10)
           print("reset bot something wrong")
           find_serial = browser.find_element_by_css_selector("span.speedometerSignal-DPgs-R4s")
        counter = 1
        while True:            
            print("OK!")
            print("horray")
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
                sleeptime = reportInSecond   
                curentprice =  browser.find_element_by_css_selector(".tv-symbol-price-quote__value.js-symbol-last")  
                curentprice = curentprice.text 
                print(curentprice)   
                text = str(sleeptime) +" "
                text= text+str(datetime.datetime.now())+" "
                text= text+"UTC: "+str(datetime.datetime.utcnow())+" "
                text= text+"price: "+str(curentprice)+" "
                text = text+ str(signal)
                # print(text)
                self.fillAnalises(newdriver,browser,cripto,sleeptime)
                self.fillBaseChart(newdriver,browser,cripto,sleeptime)
                print("")
                print("start again for next signal, don't need any action everey thing are automated!")
                print("")
               except:
                print("notext") 
               try:
                   self.printTotxt(newdriver,text,cripto,sleeptime)  
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

   # تنظیم چالد و صدا زدن فانکشن بعدی
    def getdata(self,cripto,os,sleep):
        cripto= str(cripto)
        os = str(os)
        sleep = str(sleep)
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
        print("we will check: "+str(cripto)+" every "+ str(sleep)+" seconds:")          
        self.getAnalyse(newdriver,cripto,sleep,os,child)


        # فانکشن خواسته های نرم افزار که با اجرای این فایل اجرا میشه
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
        self.getdata(newdriver,str(cripto),str(os),str(sleep))
     
    def fillIndicators(self,browser):
        # print("fillIndicators")
        activitysql = "SELECT EXISTS (SELECT 1 FROM indicators)"
        excutable.execute(activitysql)
        optionsExcute = excutable.fetchall()
        tableHasData = optionsExcute[0]["EXISTS (SELECT 1 FROM indicators)"]
        if(tableHasData == 0):
            print("if")
            try:
                Oscillators = browser.find_element_by_css_selector(".container-2-juHm8n.tableWithAction-DPgs-R4s .tableWrapper-2-juHm8n .table-2-juHm8n tbody")
                print(Oscillators.tag_name)
                all_children_by_xpath = Oscillators.find_elements_by_xpath(".//*")
                index = 0
                for article in all_children_by_xpath:
                    if(index >3):
                      if(article.tag_name == "tr"):
                        rows = article.find_elements_by_xpath(".//*")  
                        i=1
                        j=1
                        for column in rows:
                         if(column.tag_name == "td"):                         
                            if(i == j): 
                                print(column.tag_name+"-"+column.text)
                                activitysql = "INSERT INTO indicators (indecator_name,indecator_shortname,type) VALUES (%s, %s,%s)"
                                val = (column.text, column.text,"oscillator")
                                mycursor.execute(activitysql, val)
                                conn.commit()
                                print(mycursor.rowcount, "record inserted.")
                            i = i+3 
                        j= j+1 
                    index = index+1  
                print("before")    
                MovingAverages =  browser.find_element_by_css_selector(".container-2-juHm8n.maTable-DPgs-R4s.tableWithAction-DPgs-R4s .tableWrapper-2-juHm8n .table-2-juHm8n tbody")   
                print("imhere")
                print(MovingAverages.tag_name)
                MovingAverages_children = MovingAverages.find_elements_by_xpath(".//*")
                index = 0
                for indicator in MovingAverages_children:
                    if(index >3):
                      if(indicator.tag_name == "tr"):
                        rows = indicator.find_elements_by_xpath(".//*")  
                        i=1
                        j=1
                        for column in rows:
                         if(column.tag_name == "td"):                         
                            if(i == j): 
                                print(column.tag_name+"-"+column.text)
                                activitysql = "INSERT INTO indicators (indecator_name,indecator_shortname,type) VALUES (%s, %s,%s)"
                                val = (column.text, column.text,"Moving Averages")
                                mycursor.execute(activitysql, val)
                                conn.commit()
                                print(mycursor.rowcount, "record inserted.")
                            i = i+3 
                        j= j+1 
                    index = index+1  
            except:
                print("herer !!!!")    
        # print("After if")        
    def fillAnalises(self,browser,address,sleeptime): 
        thisindecator = None 
        print("address: "+ str(address))    
        print("address: "+ str(sleeptime))
        time_id = self.convertSleeptimeToTimeId(newdriver,sleeptime)
        cripto_id = self.convertAssressToCriptoId(newdriver,address,browser)
        print("time_id"+ str(time_id))
        print("cripto_id: " + str(cripto_id))
        priceDiv =  browser.find_element_by_css_selector(".tv-symbol-price-quote__value.js-symbol-last")     
        price = priceDiv.text
        print("price: "+price)
        FirstAfPriseDIv =  browser.find_element_by_css_selector(".js-symbol-change.tv-symbol-price-quote__change-value")
        FirstAfPrise = FirstAfPriseDIv.text
        print("FirstAfPrise: "+FirstAfPrise)
        signFirstAfprise = FirstAfPrise[0]
        print("signFirstAfprise: "+signFirstAfprise)
        secAfPriseDIv = browser.find_element_by_css_selector(".js-symbol-change-pt.tv-symbol-price-quote__change-value")     
        secAfPrise = secAfPriseDIv.text
        print("secAfPrise: "+secAfPrise)
        signSecAfprise = secAfPrise[1]
        print("signSecAfprise: "+signSecAfprise)
        marketopenDiv =  browser.find_element_by_css_selector(".js-symbol-lp-time")     
        marketopen = marketopenDiv.text
        print("marketopen: "+marketopen)
        tehran_time= str(datetime.datetime.now())
        utc_time= str(datetime.datetime.utcnow())
        Oscillators = browser.find_element_by_css_selector(".container-2-juHm8n.tableWithAction-DPgs-R4s .tableWrapper-2-juHm8n .table-2-juHm8n tbody")
        all_children_by_xpath = Oscillators.find_elements_by_xpath(".//*")
        index = 0
        datacounter = 1
        rowcounter = 1
        rownumber=5
        samecol = 1
        for article in all_children_by_xpath:
            if(index > 3): 
                if datacounter == 2 or  datacounter == 5 or datacounter == 6:
                    print(str(rowcounter)+":"+article.text) 
                    print("samecol:"+str(samecol))
                    try:
                        print("samecol:"+str(samecol))
                        if(samecol == 3):
                            print(samecol)
                            if(thisindecator != None):
                                action = article.text
                                activitysql = "UPDATE analises SET action = %s  WHERE id = %s"
                                val =(action , thisindecator)
                                mycursor.execute(activitysql, val)
                                conn.commit()  
                                print(mycursor.rowcount, "record inserted.")
                                samecol = 0 
                        if(samecol == 2):
                            print(samecol)
                            if(thisindecator != None):
                                value = article.text
                                activitysql = "UPDATE analises SET value = %s  WHERE id = %s"
                                val =(value , thisindecator)
                                mycursor.execute(activitysql, val)
                                conn.commit()
                                print(mycursor.rowcount, "record inserted.") 
                                samecol = samecol +1    
                        if(samecol == 1):
                            print(samecol)
                            activitysql = "INSERT INTO analises (time_id,cripto_id,indecator_id,price,FirstAfPrise,signFirstAfprise,secAfPrise,signSecAfprise,marketOpen,tehran_time,utcT_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            val =(time_id,cripto_id,rowcounter,price,FirstAfPrise,signFirstAfprise,secAfPrise,signSecAfprise,marketopen,tehran_time,utc_time)
                            print(activitysql)
                            print(val)
                            mycursor.execute(activitysql, val)
                            thisindecator = mycursor.lastrowid
                            conn.commit()
                            print(mycursor.rowcount, "record inserted.")
                            samecol = samecol +1
                    except:
                        print('lo')
       
                               
                if(rownumber == 0):
                    rownumber = 6
                    rowcounter = rowcounter+1     
                    samecol = samecol +1              
                rownumber = rownumber -1 
                datacounter= datacounter+1 
               
                if datacounter == 7:
                    datacounter = 1   
            index = index+1
           
           
        MovingAverages = browser.find_element_by_css_selector(".container-2-juHm8n.maTable-DPgs-R4s.tableWithAction-DPgs-R4s .tableWrapper-2-juHm8n .table-2-juHm8n tbody")   
        MovingAverages_children = MovingAverages.find_elements_by_xpath(".//*")    
        index=0
        datacounter = 1
        rowcounter = 12
        rownumber=5
        for indexes in MovingAverages_children:
            if(index > 3): 
                if datacounter == 2 or  datacounter == 5 or datacounter == 6:
                    print(str(rowcounter)+":"+indexes.text)
                    print("samecol:"+str(samecol))
                    try:
                        print("samecol:"+str(samecol))
                        if(samecol == 3):
                            print(samecol)
                            if(thisindecator != None):
                                action = article.text
                                activitysql = "UPDATE analises SET action = %s  WHERE id = %s"
                                val =(action , thisindecator)
                                mycursor.execute(activitysql, val)
                                conn.commit()  
                                print(mycursor.rowcount, "record inserted.")
                                samecol = 0 
                        if(samecol == 2):
                            print(samecol)
                            if(thisindecator != None):
                                value = article.text
                                activitysql = "UPDATE analises SET value = %s  WHERE id = %s"
                                val =(value , thisindecator)
                                mycursor.execute(activitysql, val)
                                conn.commit()
                                print(mycursor.rowcount, "record inserted.") 
                                samecol = samecol +1    
                        if(samecol == 1):
                            print(samecol)
                            activitysql = "INSERT INTO analises (time_id,cripto_id,indecator_id,price,FirstAfPrise,signFirstAfprise,secAfPrise,signSecAfprise,marketOpen,tehran_time,utcT_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            val =(time_id,cripto_id,rowcounter,price,FirstAfPrise,signFirstAfprise,secAfPrise,signSecAfprise,marketopen,tehran_time,utc_time)
                            print(activitysql)
                            print(val)
                            mycursor.execute(activitysql, val)
                            thisindecator = mycursor.lastrowid
                            conn.commit()
                            print(mycursor.rowcount, "record inserted.")
                            samecol = samecol +1
                    except:
                        print('lo')
                       
                if(rownumber == 0):
                    rownumber = 6
                    rowcounter = rowcounter+1     
                    samecol = samecol +1              
                rownumber = rownumber -1 
                datacounter= datacounter+1 
               
                if datacounter == 7:
                    datacounter = 1   
            index = index+1 
    def fillBaseChart(self,browser,cripto,sleeptime):

        BasechartSumeryname = "Summary"
        BaseChartOscillators = "Oscillators"
        BaseChartMovingAverages = "Moving Averages"
        SumeryAction = self.SumeryAction(newdriver,browser)
        print("SumeryAction: " + str(SumeryAction))
        SumerySell = self.SumerySell(newdriver,browser)
        print("SumerySell: "+str(SumerySell))
        SumeryNeutral = self.SumeryNeutral(newdriver,browser)
        print("SumeryNeutral: "+SumeryNeutral)
        SumeryBuy = self.SumeryBuy(newdriver,browser)
        print("SumeryBuy: "+str(SumeryBuy))



        OscillatorsAction = self.OscillatorsAction(newdriver,browser)
        print("OscillatorsAction: "+str(OscillatorsAction))
        OscillatorsSell = self.OscillatorsSell(newdriver,browser)
        print("OscillatorsSell: "+ str(OscillatorsSell))
        OscillatorsNeutral = self.OscillatorsNeutral(newdriver,browser)
        print("OscillatorsNeutral: " + str(OscillatorsNeutral))
        OscillatorsBuy = self.OscillatorsBuy(newdriver,browser)
        print("OscillatorsBuy: " + str(OscillatorsBuy))


        MovingAveragesAction = self.MovingAveragesAction(newdriver,browser)
        print("MovingAveragesAction: "+ str(MovingAveragesAction))
        MovingAveragesSell = self.MovingAveragesSell(newdriver,browser)
        print("MovingAveragesSell: " + str(MovingAveragesSell))
        MovingAveragesNeutral = self.MovingAveragesNeutral(newdriver,browser)
        print("MovingAveragesNeutral: " + str(MovingAveragesNeutral))
        MovingAveragessBuy = self.MovingAveragessBuy(newdriver,browser)
        print("MovingAveragessBuy" + str(MovingAveragessBuy))


    def SumeryAction(self,browser):
        SumeryActionDiv = browser.find_element_by_css_selector(".speedometerSignal-DPgs-R4s.neutralColor-DPgs-R4s")   
        return SumeryActionDiv.text
    def SumerySell(self,browser):
        try:
            SumerySell = browser.find_element_by_css_selector(".speedometerWrapper-DPgs-R4s.summary-DPgs-R4s .counterNumber-DPgs-R4s.sellColor-DPgs-R4s")   
            return SumerySell.text
        except:
            return None
    def SumeryNeutral(self,browser):
        try:
            SumeryNeutral = browser.find_element_by_css_selector(".speedometerWrapper-DPgs-R4s.summary-DPgs-R4s .counterNumber-DPgs-R4s.neutralColor-DPgs-R4s")   
            return SumeryNeutral.text
        except:
            return None 
    def SumeryBuy(self,browser):
        try:
            SumeryBuy = browser.find_element_by_css_selector(".speedometerWrapper-DPgs-R4s.summary-DPgs-R4s .counterNumber-DPgs-R4s.buyColor-DPgs-R4s")   
            return SumeryBuy.text
        except:
            return None



    def OscillatorsAction(self,browser):
        try:
            OscillatorsActionDiv = browser.find_element_by_css_selector(".speedometerSignal-DPgs-R4s.sellColor-DPgs-R4s")   
            return OscillatorsActionDiv.text
        except:
            return None        
    def OscillatorsSell(self,browser):
        try:
            OscillatorsSellDiv = browser.find_element_by_css_selector(".speedometersContainer-DPgs-R4s .speedometerWrapper-DPgs-R4s:first-child .counterNumber-DPgs-R4s.sellColor-DPgs-R4s")   
            return OscillatorsSellDiv.text
        except:
            return None
    def OscillatorsNeutral(self,browser):
        try:
            OscillatorsNeutralDiv = browser.find_element_by_css_selector(".speedometersContainer-DPgs-R4s .speedometerWrapper-DPgs-R4s:first-child .counterNumber-DPgs-R4s.neutralColor-DPgs-R4s")   
            return OscillatorsNeutralDiv.text
        except:
            return None  
    def OscillatorsBuy(self,browser):
        try:
            OscillatorsBuylDiv = browser.find_element_by_css_selector(".speedometersContainer-DPgs-R4s .speedometerWrapper-DPgs-R4s:first-child .counterNumber-DPgs-R4s.buyColor-DPgs-R4s")   
            return OscillatorsBuylDiv.text
        except:
            return None  




    def MovingAveragesAction(self,browser):
        try:
            MovingAveragesActionDIV = browser.find_element_by_css_selector(".speedometerSignal-DPgs-R4s.sellColor-DPgs-R4s")   
            return MovingAveragesActionDIV.text
        except:
            return None        
    def MovingAveragesSell(self,browser):
        try:
            MovingAveragesSell = browser.find_element_by_css_selector(".speedometersContainer-DPgs-R4s .speedometerWrapper-DPgs-R4s:first-child .counterNumber-DPgs-R4s.sellColor-DPgs-R4s")   
            return MovingAveragesSell.text
        except:
            return None
    def MovingAveragesNeutralNeutral(self,browser):
        try:
            MovingAveragesNeutralNeutralDiv = browser.find_element_by_css_selector(".speedometersContainer-DPgs-R4s .speedometerWrapper-DPgs-R4s:first-child .counterNumber-DPgs-R4s.neutralColor-DPgs-R4s")   
            return MovingAveragesNeutralNeutralDiv.text
        except:
            return None  
    def MovingAveragessBuy(self,browser):
        try:
            MovingAveragessBuyDiv = browser.find_element_by_css_selector(".speedometersContainer-DPgs-R4s .speedometerWrapper-DPgs-R4s:first-child .counterNumber-DPgs-R4s.buyColor-DPgs-R4s")   
            return MovingAveragessBuyDiv.text
        except:
            return None 



    def convertSleeptimeToTimeId(self,sleeptime):
        findsleeptime = "select id from timeFrames where timeFrameSeconds = '{}' LIMIT 1".format(sleeptime)
        excutable.execute(findsleeptime)
        myresult = excutable.fetchall() 
        return (myresult[0]['id'])
    def convertAssressToCriptoId(self,address,browser):
        try:
            findCriptoId = "select id from criptoCurences where cripto_short_name = '{}' LIMIT 1".format(address)
            excutable.execute(findCriptoId)
            myresult = excutable.fetchall() 
            return (myresult[0]['id'])
        except:
            priceDiv =  browser.find_element_by_css_selector("h2.tv-symbol-header__first-line")
            my_string = priceDiv.text
            criptoName = my_string.split("/",1)[0]
            activitysql = "INSERT INTO criptoCurences (cripto_name,cripto_short_name,cripto_trade_name) VALUES (%s, %s,%s)"
            val = (criptoName, address,address)
            mycursor.execute(activitysql, val)
            return  mycursor.lastrowid        




# newdriver.printWhatIneed(newdriver)


driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
# driver.quit()

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