from selenium.webdriver import Chrome
from common.selenium_manager import SeleniumManager, By
import time

def run(chrome: Chrome):    
    chrome.get("https://google.com")
    
    while True:
        print("loop...")
        time.sleep(10)
       
    


def execute_function(chrome: Chrome):
    '''
    実行したい処理を記述
    '''
    #chrome.get("https://google.com")
    if "https://auctions.yahoo.co.jp/search/search" in chrome.current_url:
        elms = chrome.find_elements(by=By.CSS_SELECTOR, value=".Product__titleLink.js-rapid-override.js-browseHistory-add")
        for elm in elms:
            print(elm.text)
    else:
        print("開いているURLが不正です")