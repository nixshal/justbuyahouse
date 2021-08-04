import requests
from bs4 import BeautifulSoup
from time import sleep
from itertools import chain
import pandas as pd
import re

# BeautifulSoup stuff
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

page_num = 0

links = []
cleanlinks = []
for page in range(0, 3):
    page_num += 1
    iproperty_url = 'https://www.iproperty.com.my/rent/all-residential/transport/kl-sentral-438/?page=' + \
        str(page_num)
    r = requests.get(iproperty_url, headers=headers)
    print(r)
    sleep(5)
    print('Now scraping page ' +str(page_num))
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.findAll('a'):
        # print(link.get('href'))
        links.append(link.get('href'))

links = [i for i in links if i] #removes None
print(len(links))
print('**********SCRAPING COMPLETE**********')

to_remove = ['http','tel','photo','video','floorplan']

filtered_list = [ i for i in links if "http" not in i and "tel" not in i and "photo" not in i and "video" not in i and "floorplan" not in i and len(i) > 10]

# for loop implementation
# for i in links:
#     if "http" not in i and "tel" not in i and "photo" not in i and "video" not in i and "floorplan" not in i and len(i) > 10:
#         nlist.append(i)

df = pd.DataFrame(filtered_list, columns=["links"])

df.drop_duplicates(inplace=True)

filename = iproperty_url.split('/')
filename = filename[3] + '-' + filename[6] + '.csv'

df.to_csv(filename, index=False) #to print to a csv