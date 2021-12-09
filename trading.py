import time
from driver import driver
print("what is you'r operating system:")
print("please just put number")
print("1 : Windows")
print("2 : linux")
os = input("what is your os:\n")
print("what is you'r criptocurency:")
print("please just put number")
print("1 : BTC Bitcoin ")
print("2 : DOT BitcoinCash")
print("3 : LTC Cardano")
print("4 : ETH ETHEREUM")
cripto =  input("what is your criptocurency:\n")
print("i want report every ... secound")
print("please just put number")
print("for wxample input 10 for every 10 secound report")
sleep = input("i whant my report every :\n")
try:
    driver.getdata(driver,cripto,os,sleep)
except:
    print("please just put number")  
    print("1 : Windows")
    print("2 : linux")
    os = input("what is your os:\n") 

