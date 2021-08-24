import requests
from bs4 import BeautifulSoup
from time import sleep
import time
from datetime import datetime
import itertools
import inspect
import pandas as pd
import numpy as np
import re

lrt_kelana_jaya_line_1 = ['gombak-543',
                          'ampang-park-89',
                          'pasar-seni-414',
                          'bangsar-625',
                          'asia-jaya-187',
                          'ara-damansara-415',
                          'usj-7-608',
                          'putra-heights-678',
                          'taman-melati-624',
                          'jelatek',
                          'masjid-jamek-600',
                          'abdullah-hukum-325',
                          'taman-paramount-466',
                          'glenmarie-250',
                          'taipan-719',
                          'subang-alam-584',
                          'wangsa-maju-276',
                          'dato-keramat-607',
                          'kampung-baru-121',
                          'kerinchi-431',
                          'taman-bahagia-529',
                          'subang-jaya-1',
                          'wawasan-432',
                          'sri-rampai-513',
                          'damai-683',
                          'dang-wangi-291',
                          'universiti-168',
                          'kelana-jaya-260',
                          'ss-15-316',
                          'usj-21-531',
                          'setiawangsa-20',
                          'klcc-666',
                          'kl-sentral-438',
                          'taman-jaya-560',
                          'lembah-subang-170',
                          'ss-18-189',
                          'alam-megah-23']


class LRTlinks():
    "This is a LRTlinks class"

    def __init__(self, station_id):
        self.station_id = station_id
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
        self.to_remove = ['http', 'tel', 'photo', 'video', 'floorplan']
        self.links = []
        self.page_num = 0
        print('Initializing scraper to gather property links...')

    def get_links(self, last_page_number):
        try:
            self.last_page_number = last_page_number
            print('Scraping for links near: ' + self.station_id + ' ...')
            print('Scraping until page: ' + str(self.last_page_number))
            for i in range(0, last_page_number):
                self.page_num += 1
                self.iproperty_url = 'https://www.iproperty.com.my/rent/all-residential/transport/' + \
                    self.station_id + '/?page=' + str(self.page_num)
                self.r = requests.get(self.iproperty_url, headers=self.headers)
                sleep(2)
                print('Now scraping page ' + str(self.page_num))
                self.soup = BeautifulSoup(self.r.content, 'html.parser')
                for link in self.soup.findAll('a'):
                    # print(link.get('href'))
                    self.links.append(link.get('href'))

            self.links = [i for i in self.links if i]  # removes None

            self.filtered_list = [
                i for i in self.links if "http" not in i and "tel" not in i and "photo" not in i and "video" not in i and "floorplan" not in i and len(i) > 10]

            # for loop implementation
            # for i in links:
            #     if "http" not in i and "tel" not in i and "photo" not in i and "video" not in i and "floorplan" not in i and len(i) > 10:
            #         nlist.append(i)

            self.df = pd.DataFrame(self.filtered_list, columns=["links"])
            self.df.drop_duplicates(inplace=True)

            self.filename = self.iproperty_url.split('/')
            self.filename = self.filename[3] + '-' + self.filename[6] + \
                '-' + 'property-links' + '.csv'

            self.df.to_csv(self.filename, index=False)  # to print to a csv

            print('\nTotal links: ' + str(len(self.df.links)) +
                  ' (from ' + str(self.last_page_number) + ' pages)')
            print('\n.csv with property links for station_id >' +
                  self.station_id + '< saved to : ' + self.filename)
            print('\n>>> LINK SCRAPING FOR TRAIN STATION ID: ' +
                  self.station_id + ' COMPLETE')

        except:
            print('website response: ' + self.r)
