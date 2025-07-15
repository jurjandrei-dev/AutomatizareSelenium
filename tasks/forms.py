from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.browser import get_driver
import time


def create_quiz():
    driver = get_driver()
    driver.get("https://forms.office.com/Pages/DesignPageV2.aspx")

    wait = WebDriverWait(driver, 20)

    feedback_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and @aria-label="Feedback"]'))
    )
    feedback_btn.click()

    title_button = wait.until(EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[3]/div[2]/div[2]/div[1]/div[3]/div/div/div"
    )))
    title_button.click()

    # #title_input.click()
    # driver.execute_script("arguments[0].click()", title_input )
    # print("Title clicked!")

    # try:
    #     message_box = wait.until(EC.presence_of_element_located((
    #         By.XPATH, '//div[@id="form-title-container"]//div[@contenteditable="true"]'
    #     )))
    # except Exception as e:
    #     print("Textbox-ul pentru titlu nu a apărut.")
    

    # wait = WebDriverWait(driver, 10)
    # message_box = wait.until(EC.element_to_be_clickable((
    #     By.XPATH,
    #     '//div[@contenteditable="true" and @aria-label="Titlu formular"]'
    # )))
    # print("Displayed:", message_box.is_displayed())     # True dacă se vede
    # print("Enabled:", message_box.is_enabled())  # True dacă poate fi interacționat  

    # actions = ActionChains(driver)
    # actions.move_to_element(message_box).click().key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
    # actions.send_keys(Keys.BACKSPACE)
    # actions.send_keys("Fotbal")
    # actions.perform()



    # Așteaptă până când butonul de creare întrebare apare
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Întrebare nouă") or contains(text(), "Add new")]')))

    # questions = [
    #     {
    #         "text": "Cine a câștigat Campionatul Mondial din 2022?",
    #         "options": ["Argentina", "Franța", "Brazilia", "Germania"]
    #     },
    #     {
    #         "text": "Câte minute are o repriză într-un meci de fotbal?",
    #         "options": ["45", "30", "60", "90"]
    #     },
    #     {
    #         "text": "Care este clubul cu cele mai multe trofee UEFA Champions League?",
    #         "options": ["Real Madrid", "Barcelona", "AC Milan", "Liverpool"]
    #     },
    #     {
    #         "text": "Ce jucător este cunoscut drept 'La Pulga'?",
    #         "options": ["Cristiano Ronaldo", "Lionel Messi", "Neymar", "Mbappé"]
    #     }
    # ]

    # for i, q in enumerate(questions):
    #     if i > 0:
    #         # Apasă pe "Întrebare nouă" (Add new)
    #         add_new_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Întrebare nouă") or contains(text(), "Add new")]')))
    #         add_new_btn.click()
    #         time.sleep(1)

    #         # Selectează "Opțiune" (Choice)
    #         choice_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Opțiune") or contains(text(), "Choice")]')))
    #         choice_btn.click()
    #         time.sleep(1)

    #     # Introduce textul întrebării
    #     question_input = wait.until(EC.presence_of_element_located((
    #         By.XPATH, '//textarea[contains(@placeholder, "Întrebare") or contains(@aria-label, "Question")]'
    #     )))
    #     question_input.clear()
    #     question_input.send_keys(q["text"])
    #     time.sleep(0.5)

    #     # Introduce opțiunile
    #     option_inputs = driver.find_elements(By.XPATH, '//input[contains(@placeholder, "Opțiune") or contains(@aria-label, "Option")]')

    #     for j, option_text in enumerate(q["options"]):
    #         if j < len(option_inputs):
    #             option_inputs[j].clear()
    #             option_inputs[j].send_keys(option_text)
    #         else:
    #             # Adaugă o nouă opțiune
    #             plus_btn = driver.find_element(By.XPATH, '//button[@aria-label="Adăugați opțiune" or @aria-label="Add option"]')
    #             plus_btn.click()
    #             time.sleep(0.5)
    #             new_input = driver.find_elements(By.XPATH, '//input[contains(@placeholder, "Opțiune") or contains(@aria-label, "Option")]')[-1]
    #             new_input.send_keys(option_text)

    #     time.sleep(1)

    print("Formular creat cu succes!")
