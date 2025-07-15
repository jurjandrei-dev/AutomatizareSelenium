from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from utils.browser import get_driver
import time

from config import CHROME_PATH, DRIVER_PATH


def get_emag_price(url: str) -> float | None:
    driver = get_driver(True, False)

    try:
        driver.get(url)
        print("Pagina s-a deschis!")
        elements = driver.find_elements(By.CLASS_NAME, "product-new-price")

        if elements:
            text = elements[0].get_attribute("innerText").strip()
            if "Lei" in text and "," in text:
                pret_curat = (
                    text.replace("Lei", "")
                    .replace(".", "")    
                    .replace(",", ".")    
                    .replace(" ", "")
                    .strip()
                )
                return float(pret_curat)
            else:
                print("Elementul există, dar nu pare un preț valid:", text)
                return None
        else:
            print("Nu s-a găsit niciun element cu clasa 'product-new-price'")
            return None

    except Exception as e:
        print("Eroare completă:", repr(e))
        return None

    finally:
        driver.quit()
