import requests
from bs4 import BeautifulSoup

#BeautifulSoup stuff
url = 'https://www.iproperty.com.my/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
r = requests.get(url, headers=headers)

print('placeholder')