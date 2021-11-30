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
    chrome.get("https://google.com")
    chrome.find_element(by=By.NAME, value="q").send_keys("test")
    