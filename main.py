from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

url = "https://www.reddit.com/r/Kenya/"

chrome_default_path = "/home/hp/.config/google-chrome"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir={chrome_default_path}")

chrome_driver_path = "/usr/local/bin/chromedriver"
chrome_options.add_argument(f"executable_path={chrome_driver_path}")

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
driver.get(url)

# wait = WebDriverWait(driver, 10)
# ul_element = wait.until(
#     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.snippets"))
# )

wait = WebDriverWait(driver, 10)
ul_element = wait.until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, "[data-testid='post-container']")
    )
)

page_source = driver.page_source
print(page_source)
