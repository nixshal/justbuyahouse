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
from classes import LRTlinks

startTime = time.time()

# To do
# rename the Task class
# create a class for the scraping of links
# how to get the phone number and agent etc? use JSON? https://stackoverflow.com/questions/67515161/beautiful-soup-returns-an-empty-string-when-website-has-text
# error handling, add some try, except clauses
# when running for full list, script hung after 1800++ files
# how to add Task class to classes.py? problem with detail_dict
# make sure works for other train stations too etc gombak. alter the code for general use cases


class Task():
    """ This is a Task class to carry out all the scraping functions """

    def rent_id(self):                      # START: Standard data on each property page
        if property_url != '':
            rent_id.append(property_url.split('/')[-2])
            print('Rent ID                          : ' + 'Success')
        else:
            print('Rent ID                          : '+'NaN')
            rent_id.append('NaN')

    def prop_url(self):
        if property_url != '':
            prop_url.append(property_url)
            print('Property URL                     : ' + 'Success')
        else:
            print('Property URL                     : '+'NaN')
            prop_url.append('NaN')

    def title(self):
        if soup.find_all('title')[0].text != '':
            title.append(soup.find_all('title')[0].text)
            print('Title                            : ' + 'Success')
        else:
            print('Title                            : '+'NaN')
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
            print('Property Price                   : '+'NaN')
            title.append('NaN')

    def property_summary(self):
        if soup.find_all('h1', class_='PropertySummarystyle__ProjectTitleWrapper-kAhflS PNQmp')[0].text != '':
            property_summary.append(soup.find_all(
                'h1', class_='PropertySummarystyle__ProjectTitleWrapper-kAhflS PNQmp')[0].text)
            print('Property Summary                 : ' + 'Success')
        else:
            print('Property Summary                 : '+'NaN')
            property_summary.append('NaN')

    def property_address(self):
        if soup.find_all(
                'span', class_='property-address rent-default')[0].text != '':
            property_address.append(soup.find_all(
                'span', class_='property-address rent-default')[0].text)
            print('Property Address                 : ' + 'Success')
        else:
            print('Property Address                 : '+'NaN')
            property_address.append('NaN')

    def built_up(self):
        if soup.find_all(
                'li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[0].text != '':
            built_up.append(soup.find_all(
                'li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[0].text.split(': ')[1])
            print('Built Up                         : ' + 'Success')
        else:
            print('Built Up                         : '+'NaN')
            built_up.append('NaN')

    def land_area_sq_ft(self):
        if soup.find_all(
                'li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[1].text != '':
            land_area_sq_ft.append(soup.find_all(
                'li', class_='PropertySummarystyle__AreaInfoItem-NjZCY dUovgc')[1].text.split(': ')[1])
            print('Land Area_sq_ft                  : ' + 'Success')
        else:
            print('Land Area_sq_ft                  : '+'NaN')
            land_area_sq_ft.append('NaN')

    def property_details(self):
        if str(soup.find_all('pre')) != '':
            property_details.append(str(soup.find_all('pre')))
            print('Property Details                 : ' + 'Success')
        else:
            print('Property Details                 : '+'NaN')
            property_details.append('NaN')

    def property_features(self):    # END: Standard data on each property page
        if [i.text for i in soup.find_all('div', class_='attribute-title-container')] != []:
            property_features.append([i.text for i in soup.find_all(
                'div', class_='attribute-title-container')])
            print('Property Features                : ' + 'Success')
        else:
            print('Property Features                : '+'NaN')
            property_features.append('NaN')

    def property_type(self):          # START: Data in property details container (can vary)
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

    def posted_date(self):              # END: Data in property details container (can vary)
        if 'Posted Date' in details_dict:
            temp = details_dict['Posted Date']
            posted_date.append(soup.find_all(
                'div', class_='PropertyDetailsListstyle__AttributeItemData-jpQfWB HUTFZ')[temp].text)
            print('Posted Date                      : ' + 'Success')
        else:
            print('Posted Date                      : ' + 'NaN')
            posted_date.append('NaN')

    # def get_method(self, method_name):  # method1 = callbyname.get_method(method_name)
    #     method = getattr(self, method_name)
    #     return method()


# ampang-park-89
# kl-sentral-438
# USER INPUT REQUIRED
location_of_interest = 'ss-15-316'  # 'usj-21-531'
num_pages_to_scrape = 50  # 20 results per page

print('\n| iProperty.com.my Scraper |')

# Use the LRTlinks method
# choose which Train Station ID here
l = LRTlinks(location_of_interest)
# choose how many pages to scrape (limit = 100)
l.get_links(num_pages_to_scrape)

file_to_be_read = 'rent-' + location_of_interest + '-property-links.csv'
data_links = pd.read_csv(file_to_be_read).values.tolist()
links = list(itertools.chain(*data_links))

# try with generators
# how many properties to scrape (for test purposes)
test_list = (i for i in links)

print('\nList of properties to be scraped...')
text = "{}".format("\n".join(links))
print(text + '\n')

# headers specific to this website -- required for BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

# Initialize empty lists
rent_id, prop_url, title, property_price, property_summary, property_address, built_up, land_area_sq_ft, property_details, property_features, property_type, land_title, property_title_type, tenure, built_up_size_sq_ft, built_up_price_per_sq_ft, furnishing, occupancy, unit_type, facing_direction, reference, available_date, posted_date = ([
] for i in range(23))

count = 0

try:
    # Loop through the different properties from the .csv file (links)
    for i in test_list:  # range(len(test_list)) IF USING LISTS
        count += 1
        property_url = 'https://www.iproperty.com.my' + i
        # print(r) #to get website's response
        r = requests.get(property_url, headers=headers)
        sleep(2)
        soup = BeautifulSoup(r.content, 'html.parser')

        prop_name = soup.find_all(
            'h1', class_='PropertySummarystyle__ProjectTitleWrapper-kAhflS PNQmp')[0].text

        print('********** ' + str(count) + ' Scraping data for: ' +
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

        t = Task()  # Initialize Task object as t
        # Identify all methods in class and execute, rather than list methods 1 by 1
        # https://stackoverflow.com/a/37075789

        attrs = (getattr(t, name) for name in dir(t))
        methods = filter(inspect.ismethod, attrs)
        for method in methods:
            try:
                method()
            except Exception as e:
                print(e)

    print('\n********** SCRAPE COMPLETED **********')

    # Adding to a DataFrame
    columns = ['rent_id', 'prop_url', 'title', 'property_price', 'property_summary', 'property_address', 'built_up', 'land_area_sq_ft', 'property_details', 'property_type', 'land_title',
               'property_title_type', 'tenure', 'built_up_size_sq_ft', 'built_up_price_per_sq_ft', 'furnishing', 'occupancy', 'unit_type', 'reference', 'posted_date', 'available_date',
               'property_features', 'facing_direction']

    properties = pd.DataFrame({'rent_id': rent_id,
                               'prop_url': prop_url,
                               'title': title,
                               'property_price': property_price,
                               'property_summary': property_summary,
                               'property_address': property_address,
                               'built_up': built_up,
                               'land_area_sq_ft': land_area_sq_ft,
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

    date = datetime.now().strftime("%Y_%m_%d-%I-%M-%S_%p")
    filename = location_of_interest + '-' + date + '.xlsx'
    properties.to_excel(filename)

    # Timing info
    print('\nThe script took {0} seconds !'.format(time.time() - startTime))

    # File save location info
    print('\nFile saved to: ' + filename)

except Exception as e:
    print(e)
