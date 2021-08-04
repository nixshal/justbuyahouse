import requests
from bs4 import BeautifulSoup
from time import sleep
from itertools import chain
import pandas as pd
import re

# BeautifulSoup stuff
# url = 'https://www.iproperty.com.my/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }
# r = requests.get(url, headers=headers)

page_num = 0

links = []
cleanlinks = []
for page in range(0, 5):
    page_num += 1
    
    iproperty_url = 'https://www.iproperty.com.my/rent/all-residential/transport/kl-sentral-438/?page=' + \
        str(page_num)
    r = requests.get(iproperty_url, headers=headers)
    print(r)
    sleep(4)
    print('Now scraping page ' +str(page_num))
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.findAll('a'):
        # print(link.get('href'))
        links.append(link.get('href'))

print(links)
print('================================')

df = pd.DataFrame(links, columns=["Links"])
df.to_csv('list.csv', index=False)