import os
import sys
import eel
import json
import threading

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import common.eel_util as eel_util
from common.logger import delete_backlog, set_logger
from common.utility import delete_old_files
from common.selenium_manager import SeleniumManager
import engine.crawler as crawler
delete_backlog()

manager = SeleniumManager(use_headless=False)
chrome = manager.chrome

@eel.expose
def start_crawler():
    global chrome
    thread = threading.Thread(target=crawler.run, args=(chrome,))
    thread.start()
    

@eel.expose
def execute_function():
    global chrome
    thread = threading.Thread(target=crawler.execute_function, args=(chrome,))
    thread.start()


# controller.init_agent()
eel_util.start("html", "index.html", (1280, 800))