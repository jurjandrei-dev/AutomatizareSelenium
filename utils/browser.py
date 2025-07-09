import subprocess
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from config import CHROME_PATH, DRIVER_PATH, DEBUG_PORT, USER_DATA_DIR

def start_chrome_debug():
    if not os.path.exists(USER_DATA_DIR):
        os.makedirs(USER_DATA_DIR)

    subprocess.Popen([
        CHROME_PATH,
        f"--remote-debugging-port={DEBUG_PORT}",
        f"--user-data-dir={USER_DATA_DIR}"
    ])
    time.sleep(3)

def get_driver():
    
    start_chrome_debug()
    
    options = Options()
    #options.add_argument("--headless")  # activeaza daca vrei rulare fara interfata grafica
    options.debugger_address = f"127.0.0.1:{DEBUG_PORT}"
    options.add_argument("user-agent=Mozilla/5.0 ...")

    return webdriver.Chrome(options=options)
