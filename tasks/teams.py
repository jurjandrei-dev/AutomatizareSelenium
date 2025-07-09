from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.browser import get_driver
import time

def send_teams_message(user_name: str, message: str):
    driver = get_driver()

    try:
        driver.get("https://teams.microsoft.com")
        print("Se deschide Microsoft Teams...")

        # Găsește și folosește bara de căutare

        wait = WebDriverWait(driver, 20)  # așteaptă până la 20 de secunde
        search_bar = wait.until(EC.presence_of_element_located((By.ID, 'ms-searchux-input')))
        search_bar.clear()
        search_bar.send_keys(user_name)
        time.sleep(2)
        search_bar.send_keys(Keys.ENTER)

        persoana = wait.until(EC.element_to_be_clickable((
            By.XPATH,
            '//div[@data-tid="search-layout"]'
        )))
        persoana.click()

        # Trimite mesajul
        wait = WebDriverWait(driver, 10)
        message_box = wait.until(EC.presence_of_element_located((
            By.XPATH,
            '//div[@data-tid="ckeditor" and @contenteditable="true"]'
        )))

        actions = ActionChains(driver)
        actions.move_to_element(message_box)
        actions.click()
        actions.send_keys(message)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        
        print("Mesaj trimis către:", user_name)

    except Exception as e:
        print("Eroare:", e)
    finally:
        time.sleep(3)
        driver.quit()
