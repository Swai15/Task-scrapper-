from bs4 import BeautifulSoup
import requests

url = 'https://toloka.yandex.com/tasks'

response = requests.get(url)

print(response)

if response.status_code == '200' : 
  html_content = response.text
else:
  print('Failed to load the web page')