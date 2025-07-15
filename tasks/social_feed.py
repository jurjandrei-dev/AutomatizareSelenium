from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utils.browser import get_driver
import webbrowser, os
import time

def extract_x_posts(max_posts: int = 5):

    driver = get_driver()
    driver.get("https://twitter.com/Twitter")

    driver.refresh()
    time.sleep(3)

    wait = WebDriverWait(driver, 10)
    home_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//a[@role="link" and @aria-label="Home"]'
    )))
    home_btn.click()
    
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//article[@data-testid="tweet"]')))

    tweets = driver.find_elements(By.XPATH, '//article[@data-testid="tweet"]')
    posts_data = []

    for tweet in tweets[:max_posts]:
         
        try:
            username =tweet.find_element(
                                By.XPATH,
                                './/a[.//span[contains(@class,"r-poiln3")] and contains(@href, "/")]'
                            ).text
        except:
            username = ""

        try:
            content = tweet.find_element(By.XPATH, './/div[@data-testid="tweetText"]').text
        except:
            content = ""

        try:
            image = tweet.find_element(By.XPATH, './/img[contains(@src, "twimg.com/media")]').get_attribute("src")
        except:
            image = None

        posts_data.append({
            "username": username,
            "text": content,
            "image": image
        })

        print("username: ", username)
        print("\ntext: ", content)
        print("\nimage: ", image)
        print("\n")
    return posts_data


def create_html_feed(posts: list, template_path='tasks/feed.html', output_path='tasks/feed_output.html'):
    with open(template_path, 'r', encoding='utf-8') as f:
        html_template = f.read()

    posts_html = ""
    for post in posts:
        post_block = f"""
        <div class="post">
            <div class="username">@{post['username']}</div>
            <div class="text">{post['text']}</div>
            {'<img src="' + post['image'] + '" class="image">' if post['image'] else ''}
        </div>
        """
        posts_html += post_block

    final_html = html_template.replace("{{POSTS_HERE}}", posts_html)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

    webbrowser.open("file://" + os.path.abspath(output_path))
