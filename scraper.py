import requests
from bs4 import BeautifulSoup
from time import sleep
import itertools
import pandas as pd
import numpy as np
import re


class Task():
    def property_type(self):
        if 'Property Type' in details_dict:
            temp = details_dict['Property Type']
            property_type.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Property Type                    : ' + 'Success')
        else:
            print('Property Type                    : '+'NaN')
            property_type.append('NaN')

    def land_title(self):
        if 'Land Title' in details_dict:
            temp = details_dict['Land Title']
            land_title.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Land Title                       : ' + 'Success')
        else:
            print('Land Title                       : '+'NaN')
            land_title.append('NaN')

    def property_title_type(self):
        if 'Property Title Type' in details_dict:
            temp = details_dict['Property Title Type']
            property_title_type.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Property Title Type              : '+'Success')
        else:
            print('Property Title Type              : '+'NaN')
            property_title_type.append('NaN')

    def tenure(self):
        if 'Tenure' in details_dict:
            temp = details_dict['Tenure']
            tenure.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Tenure                           : ' + 'Success')
        else:
            print('Tenure                           : ' + 'NaN')
            tenure.append('NaN')

    def built_up_size_sq_ft(self):
        if 'Built-up Size' in details_dict:
            temp = details_dict['Built-up Size']
            built_up_size_sq_ft.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Built-up Size                    : ' + 'Success')
        else:
            print('Built-up Size                    : ' + 'NaN')
            built_up_size_sq_ft.append('NaN')

    def built_up_price_per_sq_ft(self):
        if 'Built-up Price' in details_dict:
            temp = details_dict['Built-up Price']
            built_up_price_per_sq_ft.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Built-up Price                   : ' + 'Success')
        else:
            print('Built-up Price                   : ' + 'NaN')
            built_up_price_per_sq_ft.append('NaN')

    def furnishing(self):
        if 'Furnishing' in details_dict:
            temp = details_dict['Furnishing']
            furnishing.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Furnishing                       : ' + 'Success')
        else:
            print('Furnishing                       : ' + 'NaN')
            furnishing.append('NaN')

    def occupancy(self):
        if 'Occupancy' in details_dict:
            temp = details_dict['Occupancy']
            occupancy.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Occupancy                        : ' + 'Success')
        else:
            print('Occupancy                        : ' + 'NaN')
            occupancy.append('NaN')

    def unit_type(self):
        if 'Unit Type' in details_dict:
            temp = details_dict['Unit Type']
            unit_type.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Unit Type                        : ' + 'Success')
        else:
            print('Unit Type                        : ' + 'NaN')
            unit_type.append('NaN')

    def facing_direction(self):
        if 'Facing Direction' in details_dict:
            temp = details_dict['Facing Direction']
            facing_direction.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Facing Direction                 : '+'Success')
        else:
            print('Facing Direction                 : '+'NaN')
            facing_direction.append('NaN')

    def reference(self):
        if 'Reference No.' in details_dict:
            temp = details_dict['Reference No.']
            reference.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Reference                        : ' + 'Success')
        else:
            print('Reference                        : ' + 'NaN')
            reference.append('NaN')

    def available_date(self):
        if 'Available Date' in details_dict:
            temp = details_dict['Available Date']
            available_date.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Available Date                   : ' + 'Success')
        else:
            print('Available Date                   : ' + 'NaN')
            available_date.append('NaN')

    def posted_date(self):
        if 'Posted Date' in details_dict:
            temp = details_dict['Posted Date']
            posted_date.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Posted Date                      : ' + 'Success')
        else:
            print('Posted Date                      : ' + 'NaN')
            posted_date.append('NaN')

    def get_method(self, method_name):
        method = getattr(self, method_name)
        return method()

# t = Task()
# t.property_type()
# method1 = callbyname.get_method(method_name)


print('\nWill begin in 1 seconds')
sleep(1)

d = pd.read_csv(
    'hardcopy-rent-kl-sentral-438-property-links.csv').values.tolist()
links = list(itertools.chain(*d))
test_list = links[5:8]

print('\n')
print(test_list)
print('\n')

# BeautifulSoup stuff
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

rent_id = []
title = []
property_price = []
property_summary = []
property_address = []
built_up = []
land_area = []
details = []
# Property details
property_type = []
land_title = []
property_title_type = []
tenure = []
built_up_size_sq_ft = []
built_up_price_per_sq_ft = []
furnishing = []
occupancy = []
unit_type = []
facing_direction = []
reference = []
available_date = []
posted_date = []
property_features = []

for i in range(len(test_list)):
    property_url = 'https://www.iproperty.com.my' + test_list[i]
    r = requests.get(property_url, headers=headers)  # print(r)
    sleep(5)
    soup = BeautifulSoup(r.content, 'html.parser')

    prop_name = soup.find_all(
        'h1', class_='PropertySummarystyle__ProjectTitleWrapper-kAhflS PNQmp')[0].text

    print('********** ' + str(i) + ' Scraping data for: ' +
          prop_name + ' **********')

    # getting all the data from the website
    rent_id.append(property_url.split('/')[6])
    title.append(soup.find_all('title')[0].text)
    str_price = soup.find_all('div', class_='ListingPrice__Price-cYBbuG cspQqH property-price')[
        0].text.split(' ')[2].replace(',', '')
    property_price.append(
        int(''.join(itertools.takewhile(str.isdigit, str_price))))
    property_summary.append(soup.find_all(
        'h1', class_='PropertySummarystyle__ProjectTitleWrapper-kAhflS PNQmp')[0].text)
    property_address.append(soup.find_all(
        'span', class_='property-address rent-default')[0].text)
    built_up.append(soup.find_all(
        'li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[0].text.split(': ')[1])
    land_area.append(soup.find_all(
        'li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[1].text.split(': ')[1])
    details.append(str(soup.find('pre')).split('>')[1].splitlines())

    # >>> Property details <<< (tricky)
    # problem here is that proeprty details are different for each property. So need to have conditionals to match the correct list to be updated
    propdetails = soup.find_all(
        'div', class_='PropertyDetailsListstyle__AttributeItemTitle-gtQJBp YzpOn')
    details = [i.text for i in propdetails]
    details = [i.split(':') for i in details]
    details = [i[0] for i in details]
    # print(details)
    val = list(range(0, len(propdetails)))
    # print(val)
    details_dict = dict(zip(details, val))
    # print(details_dict)
    #['Property Type', 'Land Title', 'Property Title Type', 'Tenure', 'Built-up Size', 'Built-up Price', 'Furnishing', 'Occupancy', 'Facing Direction', 'Reference No.', 'Posted Date']
    # for example '/property/seputeh/sri-tiara-residences/rent-102350152/'

    # use classes??? https://stackoverflow.com/a/65408311

    t = Task()

    t.property_type()
    t.land_title()
    t.property_title_type()
    t.tenure()
    t.built_up_size_sq_ft()
    t.built_up_price_per_sq_ft()
    t.furnishing()
    t.occupancy()
    t.unit_type()
    t.facing_direction()
    t.reference()
    t.available_date()
    t.posted_date()

    # property_type.append(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[0].text)

    # land_title.append(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[1].text)

    # property_title_type.append(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[2].text)

    # tenure.append(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[3].text)

    # built_up_size_sq_ft.append(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[4].text.split(' ')[0])

    # built_up_price_per_sq_ft.append(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[5].text.split(' ')[1])

    # furnishing.append(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[6].text)

    # occupancy.append(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[7].text)

    # unit_type.append(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[8].text)

    # facing_direction.append(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[6].text)

    # reference.append(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[9].text)

    # posted_date.append(pd.to_datetime(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[10].text))

    # available.append(pd.to_datetime(soup.find_all(
    #     'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[10].text))

    # >>> End of property details <<<
    if [i.text for i in soup.find_all('div', class_='attribute-title-container')] != []:
        property_features.append([i.text for i in soup.find_all(
            'div', class_='attribute-title-container')])
    else:
        property_features.append('NaN')

    # print('\n PRINTING VALUES')
    # print(rent_id)
    # print(title)
    # print(property_price)
    # print(property_summary)
    # print(property_address)
    # print(built_up)
    # print(land_area)
    # print(details)
    # print(property_type)
    # print(land_title)
    # print(property_title_type)
    # print(tenure)
    # print(built_up_size_sq_ft)
    # print(built_up_price_per_sq_ft)
    # print(furnishing)
    # print(occupancy)
    # print(unit_type)
    # print(reference)
    # print(posted_date)
    # print(property_features)


print('\n********** SCRAPE COMPLETED **********')


# Adding to a DataFrame
columns = ['rent_id', 'title', 'property_price', 'property_summary', 'property_address', 'built_up', 'land_area', 'details', 'property_type', 'land_title',
           'property_title_type', 'tenure', 'built_up_size_sq_ft', 'built_up_price_per_sq_ft', 'furnishing', 'occupancy', 'unit_type', 'reference',
           'posted_date', 'property_features', 'facing_direction', 'available_date']


#value error from details column
kl_sentral = pd.DataFrame({'rent_id': rent_id,
                           'title': title,
                           'property_price': property_price,
                           'property_summary': property_summary,
                           'property_address': property_address,
                           'built_up': built_up,
                           'land_area': land_area,
                           'details': details,
                           'property_type': property_type,
                           'land_title': land_title,
                           'property_title_type': property_title_type,
                           'tenure': tenure,
                           'built_up_size_sq_ft': built_up_size_sq_ft,
                           'built_up_price_per_sq_ft': built_up_price_per_sq_ft,
                           'furnishing': furnishing,
                           'occupancy': occupancy,
                           'unit_type': unit_type,
                           'reference': reference,
                           'posted_date': posted_date,
                           'property_features': property_features,
                           'facing_direction': facing_direction,
                           'available_date': available_date})[columns]

kl_sentral.to_excel('kl_sentral.xlsx')
