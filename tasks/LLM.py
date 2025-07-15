from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from utils.browser import get_driver
import time

def wait_until_chatgpt_finishes(driver):
    while True:
        time.sleep(1)
        # ChatGPT are un span animat la finalul generării
        loading = driver.find_elements(By.XPATH, '//div[contains(@class, "text-token-streaming")]')
        if not loading:
            break

def extract_response(driver):
    previous = driver.find_elements(By.CSS_SELECTOR, "div.markdown.prose.dark\\:prose-invert")
    last_text = previous[-1].text if previous else ""

    max_wait = 60
    start_time = time.time()

    while time.time() - start_time < max_wait:
        time.sleep(1.5)
        current = driver.find_elements(By.CSS_SELECTOR, "div.markdown.prose.dark\\:prose-invert")
        if not current:
            continue

        current_text = current[-1].text.strip()
        if current_text and current_text != last_text:
            break

    else:
        raise TimeoutError("ChatGPT nu a răspuns în timp util.")

    # ✅ Așteaptă completarea generării
    wait_until_chatgpt_finishes(driver)

    # ✅ Așteaptă ca textul final să rămână neschimbat 3 secunde
    stable_text = ""
    stable_count = 0

    while stable_count < 3:
        time.sleep(1)
        current = driver.find_elements(By.CSS_SELECTOR, "div.markdown.prose.dark\\:prose-invert")
        if not current:
            continue
        current_text = current[-1].text.strip()
        if current_text != stable_text:
            stable_text = current_text
            stable_count = 0
        else:
            stable_count += 1

    # ✅ Citește doar când textul e stabil și gata
    final_element = current[-1]
    parts = final_element.find_elements(By.XPATH, ".//*")
    lines = []
    seen = set()

    for el in parts:
        txt = el.text.strip()
        if txt and txt not in seen:
            lines.append(txt)
            seen.add(txt)  # evită duplicarea cuvintelor

    return "\n".join(lines)
        
def send_prompt(driver, prompt):
    wait = WebDriverWait(driver, 30)

    message_box = wait.until(EC.presence_of_element_located((
        By.XPATH,
        '//div[@id="prompt-textarea" and @contenteditable="true"]'
    )))

    actions = ActionChains(driver)
    actions.move_to_element(message_box)
    actions.click()
    actions.send_keys(prompt)
    actions.send_keys(Keys.ENTER)
    actions.perform()


def conversation():
    driver = get_driver()
    driver.get("https://chat.openai.com/")

    print(" ChatGPT automat pornit. Scrie EXIT pentru a ieși.\n")

    while True:
        user_input = input("TU: ")
        if user_input.strip().upper() == "EXIT":
            print(" Închidere...")
            break

        try:
            send_prompt(driver, user_input)
            reply = extract_response(driver)
            print(f"\n ChatGPT: {reply}\n")
        except Exception as e:
            print(f"[Eroare]: {e}\n")
            continue

