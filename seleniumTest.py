from selenium import webdriver
import requests

url_to_test = "https://toloka.yandex.com/tasks"

driver = webdriver.Chrome()

driver.get(url_to_test)

response = requests.get(url_to_test)

status_code = response.status_code
print(f"HTTP Status Code: {status_code}")

# Close the browser window
driver.quit()
