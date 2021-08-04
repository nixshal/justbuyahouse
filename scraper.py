import requests
from bs4 import BeautifulSoup
import pandas as pd
import re 

#BeautifulSoup stuff
# url = 'https://www.iproperty.com.my/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
# r = requests.get(url, headers=headers)

page_num = 0 

links = []
cleanlinks =[]
for page in range(0,2):
    page_num += 1
    iproperty_url = 'https://www.iproperty.com.my/rent/all-residential/transport/kl-sentral-438/?page=' + str(page_num)
    r = requests.get(iproperty_url, headers=headers)
    soup = BeautifulSoup(r.content,'html.parser')
    for link in soup.findAll('a'):
        #print(link.get('href'))
        links.append(link.get('href'))

    print(len(links))

    links = [i for i in links if i] #removes None
    print(len(links))

    links = [i for i in links if 'http' not in i]
    print(len(links))

    links = [i for i in links if 'tel' not in i]
    print(len(links))

    links = [i for i in links if 'photo' not in i]
    print(len(links))

    links = [i for i in links if 'video' not in i]
    print(len(links))

    links = [i for i in links if 'floorplan' not in i]
    print(len(links))

    links = [i for i in links if len(i) > 10]
    print(len(links))

    cleanlinks.append(links)
