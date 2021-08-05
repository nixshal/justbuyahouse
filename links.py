
import requests
from bs4 import BeautifulSoup
from time import sleep
from itertools import chain
import pandas as pd
import numpy as np
import re

lrt_kelana_jaya_line_1 = ['gombak-543', 'ampang-park-89', 'pasar-seni-414', 'bangsar-625', 'asia-jaya-187', 'ara-damansara-415', 'usj-7-608',
                          'putra-heights-678', 'taman-melati-624', 'jelatek-51', 'masjid-jamek-600', 'abdullah-hukum-325', 'taman-paramount-466',
                          'glenmarie-250', 'taipan-719', 'subang-alam-584', 'wangsa-maju-276', 'dato-keramat-607', 'kampung-baru-121', 'kerinchi-431',
                          'taman-bahagia-529', 'subang-jaya-1', 'wawasan-432', 'sri-rampai-513', 'damai-683', 'dang-wangi-291', 'universiti-168', 'kelana-jaya-260',
                          'ss-15-316', 'usj-21-531', 'setiawangsa-20', 'klcc-666', 'kl-sentral-438', 'taman-jaya-560', 'lembah-subang-170', 'ss-18-189', 'alam-megah-23']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}


class LRTlinks():

    "This is a LRTlinks class"

    def __init__(self, station_id):
        self.station_id = station_id
        print('Obtaining property links near station_id : ' + self.station_id)

    def get_links(self):


l = LRTlinks('kl-sentral-438')


##################################################################################################
# BeautifulSoup stuff
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

page_num = 0

links = []
for page in range(0, 1):
    page_num += 1
    iproperty_url = 'https://www.iproperty.com.my/rent/all-residential/transport/kl-sentral-438/?page=' + \
        str(page_num)
    r = requests.get(iproperty_url, headers=headers)
    print(r)
    sleep(5)
    print('Now scraping page ' + str(page_num))
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.findAll('a'):
        # print(link.get('href'))
        links.append(link.get('href'))

links = [i for i in links if i]  # removes None
print(len(links))


print('**********ALL LINKS FOR TRAIN STATION ID: ' + 'COMPLETE**********')

to_remove = ['http', 'tel', 'photo', 'video', 'floorplan']

filtered_list = [
    i for i in links if "http" not in i and "tel" not in i and "photo" not in i and "video" not in i and "floorplan" not in i and len(i) > 10]

# for loop implementation
# for i in links:
#     if "http" not in i and "tel" not in i and "photo" not in i and "video" not in i and "floorplan" not in i and len(i) > 10:
#         nlist.append(i)


df = pd.DataFrame(filtered_list, columns=["links"])

df.drop_duplicates(inplace=True)

filename = iproperty_url.split('/')
filename = filename[3] + '-' + filename[6] + '-' + 'property-links' + '.csv'

df.to_csv(filename, index=False)  # to print to a csv
