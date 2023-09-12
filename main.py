from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://toloka.yandex.com/tasks"

chrome_default_path = "/home/hp/.config/google-chrome/Default"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir={chrome_default_path}")


driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

wait = WebDriverWait(driver, 10)
ul_element = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.snippets"))
)

page_source = driver.page_source
print(page_source)
