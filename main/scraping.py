import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from common.selenium_manager import *


def main():
    manager = SeleniumManager(use_headless=False)
    chrome = manager.chrome
    chrome.get("https://google.co.jp")
    time.sleep(1)
    chrome.execute_script("""
                          let elm = document.createElement("div")
                          elm.innerHTML = "<input type='submit' value='テストボタン'>"
                          document.querySelector("form").appendChild(elm)
                          """)
    time.sleep(1000)
    

main()