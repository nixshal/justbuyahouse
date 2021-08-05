import requests
from bs4 import BeautifulSoup
from time import sleep
import itertools
import pandas as pd
import numpy as np
import re

# To do
# use classes??? https://stackoverflow.com/a/65408311 DONE
# ValueError from property_details column cause array not same length DONE
# fix classes and add all the functions there to scraped
# how to get the phone number and agent etc? use JSON? https://stackoverflow.com/questions/67515161/beautiful-soup-returns-an-empty-string-when-website-has-text


class Task():
    # START: Standard data on each property page
    def rent_id(self):
        if property_url != None:
            rent_id.append(property_url.split('/')[6])
            print('Rent ID                    : ' + 'Success')
        else:
            print('Rent ID                   : '+'NaN')
            rent_id.append('NaN')

    def prop_url(self):
        if property_url != None:
            prop_url.append(property_url)
            print('Property URL                   : ' + 'Success')
        else:
            print('Property URL                     : '+'NaN')
            prop_url.append('NaN')

    def title(self):
        if soup.find_all('title')[0].text != '':
            title.append(soup.find_all('title')[0].text)
            print('Title                   : ' + 'Success')
        else:
            print('Title                     : '+'NaN')
            title.append('NaN')

    def property_price(self):
        if soup.find_all('div', class_='ListingPrice__Price-cYBbuG cspQqH property-price')[
                0].text != '':
            str_price = soup.find_all('div', class_='ListingPrice__Price-cYBbuG cspQqH property-price')[
                0].text.split(' ')[2].replace(',', '')
            property_price.append(
                int(''.join(itertools.takewhile(str.isdigit, str_price))))
            print('Property Price                   : ' + 'Success')
        else:
            print('Property Price                     : '+'NaN')
            title.append('NaN')

    def property_summary(self):
        if soup.find_all('h1', class_='PropertySummarystyle__ProjectTitleWrapper-kAhflS PNQmp')[0].text != '':
            property_summary.append(soup.find_all('h1', class_='PropertySummarystyle__ProjectTitleWrapper-kAhflS PNQmp')[0].text)
            print('Property Summary                   : ' + 'Success')
        else:
            print('Property Summary                      : '+'NaN')
            property_summary.append('NaN')

    def property_address(self):
        if soup.find_all(
        'span', class_='property-address rent-default')[0].text != '':
            property_address.append(soup.find_all(
        'span', class_='property-address rent-default')[0].text)
            print('Property Address                   : ' + 'Success')
        else:
            print('Property Address                     : '+'NaN')
            property_address.append('NaN')

    def built_up(self):
        if soup.find_all(
        'li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[0].text != '':
            built_up.append(soup.find_all('li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[0].text.split(': ')[1])
            print('Built Up                   : ' + 'Success')
        else:
            print('Built Up                     : '+'NaN')
            built_up.append('NaN')

    def land_area(self):
        if soup.find_all(
        'li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[1].text != '':
            land_area.append(soup.find_all('li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[1].text.split(': ')[1])
            print('Land Area                   : ' + 'Success')
        else:
            print('Land Area                     : '+'NaN')
            land_area.append('NaN')

    def property_details(self):
        if str(soup.find_all('pre')) != []:
            property_details.append(str(soup.find_all('pre')))
            print('Title                   : ' + 'Success')
        else:
            print('Title                     : '+'NaN')
            property_details.append('NaN')





    # END: Standard data on each property page

    # START: Data in property details container (can vary)

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

    # END: Data in property details container (can vary)

    # FINALLY: Property_features (incl Features & Facilities)
    def property_features(self):
        if 'Posted Date' in details_dict:
            temp = details_dict['Posted Date']
            posted_date.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Posted Date                      : ' + 'Success')
        else:
            print('Posted Date                      : ' + 'NaN')
            posted_date.append('NaN')

    def get_method(self, method_name):  # method1 = callbyname.get_method(method_name)
        method = getattr(self, method_name)
        return method()


print('\n| iProperty.com.my Scraper |')
sleep(1)

d = pd.read_csv(
    'hardcopy-rent-kl-sentral-438-property-links.csv').values.tolist()
links = list(itertools.chain(*d))
test_list = links[5:8]

print('\n')
print('List of properties to be scraped...')
sleep(2)
text = "{}".format("\n".join(test_list))
print(text)
print('\n')

# BeautifulSoup stuff
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

# Create empty lists for scraped data to be appended to
rent_id = []  # FINISHED
prop_url = []  # FINISHED
title = []  # finished
property_price = []  # finished
property_summary = [] #finished
property_address = [] #finsihed
built_up = []
land_area = []
property_details = []

# START: Property details container
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
# END: Property details container
property_features = []

for i in range(len(test_list)):
    property_url = 'https://www.iproperty.com.my' + test_list[i]
    # print(r) #to get website's response
    r = requests.get(property_url, headers=headers)
    sleep(5)
    soup = BeautifulSoup(r.content, 'html.parser')

    prop_name = soup.find_all(
        'h1', class_='PropertySummarystyle__ProjectTitleWrapper-kAhflS PNQmp')[0].text

    print('********** ' + str(i) + ' Scraping data for: ' +
          prop_name + ' **********')

    # Creating a dictionary for property details held in container
    # Needed because problem here is that proeprty details are different for each property. So need to have conditionals to match the correct list to be updated
    propdetails = soup.find_all(
        'div', class_='PropertyDetailsListstyle__AttributeItemTitle-gtQJBp YzpOn')
    details = [i.text for i in propdetails]
    details = [i.split(':') for i in details]
    details = [i[0] for i in details]  # print(details)
    val = list(range(0, len(propdetails)))  # print(val)
    details_dict = dict(zip(details, val))  # print(details_dict)

    t = Task()  # create a new Task object that handles the scraping calls
    t.rent_id()
    t.prop_url()
    t.title()
    t.property_price()
    t.property_summary()
    t.property_address()
    t.built_up()
    t.land_area()

    # getting all the data from the website

    # rent_id.append(property_url.split('/')[6])

    # prop_url.append(property_url)

    # title.append(soup.find_all('title')[0].text)

    # str_price = soup.find_all('div', class_='ListingPrice__Price-cYBbuG cspQqH property-price')[
    #     0].text.split(' ')[2].replace(',', '')

    # property_price.append(
    #     int(''.join(itertools.takewhile(str.isdigit, str_price))))

    # property_summary.append(soup.find_all(
    #     'h1', class_='PropertySummarystyle__ProjectTitleWrapper-kAhflS PNQmp')[0].text)

    # property_address.append(soup.find_all(
    #     'span', class_='property-address rent-default')[0].text)

    # built_up.append(soup.find_all(
    #     'li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[0].text.split(': ')[1])

    # land_area.append(soup.find_all(
    #     'li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[1].text.split(': ')[1])

    # details.append(str(soup.find('pre')).split('>')[1].splitlines())
    # dumps everything into one element of a list

    property_details.append(str(soup.find_all('pre')))

    # >>> Property details <<<
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
    # >>> End of property details <<<

    if [i.text for i in soup.find_all('div', class_='attribute-title-container')] != []:
        property_features.append([i.text for i in soup.find_all(
            'div', class_='attribute-title-container')])
    else:
        property_features.append('NaN')

print('\n********** SCRAPE COMPLETED **********')

# Adding to a DataFrame
columns = ['rent_id', 'prop_url', 'title', 'property_price', 'property_summary', 'property_address', 'built_up', 'land_area', 'property_details', 'property_type', 'land_title',
           'property_title_type', 'tenure', 'built_up_size_sq_ft', 'built_up_price_per_sq_ft', 'furnishing', 'occupancy', 'unit_type', 'reference',
           'posted_date', 'property_features', 'facing_direction', 'available_date']

kl_sentral = pd.DataFrame({'rent_id': rent_id,
                           'prop_url': prop_url,
                           'title': title,
                           'property_price': property_price,
                           'property_summary': property_summary,
                           'property_address': property_address,
                           'built_up': built_up,
                           'land_area': land_area,
                           'property_details': property_details,
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
