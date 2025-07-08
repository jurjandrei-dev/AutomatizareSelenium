from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from config import CHROME_PATH, DRIVER_PATH

def get_driver():
    options = Options()
    options.binary_location = CHROME_PATH
    #options.add_argument("--headless")  # activeaza daca vrei rulare fara interfata grafica
    options.add_argument("user-agent=Mozilla/5.0 ...")

    service = Service(DRIVER_PATH)
    return webdriver.Chrome(service=service, options=options)
