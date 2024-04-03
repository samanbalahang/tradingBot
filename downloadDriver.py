    # import requests
    # import wget
    # import zipfile
    # import os

    # # get the latest chrome driver version number
    # url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
    # response = requests.get(url)
    # version_number = response.text

    # # build the donwload url
    # download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

    # # download the zip file using the url built above
    # latest_driver_zip = wget.download(download_url,'chromedriver.zip')

    # # extract the zip file
    # with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
    #     zip_ref.extractall() # you can specify the destination folder path here
    # # delete the zip file downloaded above
    # os.remove(latest_driver_zip)
# ########################################################
# ########################################################
# ########################################################
# ########################################################
    # import chromedriver_autoinstaller
    # from selenium import webdriver

    # opt = webdriver.ChromeOptions()
    # opt.add_argument("--start-maximized")

    # chromedriver_autoinstaller.install()
    # driver = webdriver.Chrome(options=opt)
    # driver.get('https://stackoverflow.com/')

# ########################################################
# ########################################################
# ########################################################
# ########################################################

    # from chromedriver import get_driver
    # d = get_driver()
    # d.get('https://www.google.com')
# ########################################################
# ########################################################
# ########################################################
# ########################################################

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == "__main__":
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get("https://www.reddit.com/")
    browser.quit()