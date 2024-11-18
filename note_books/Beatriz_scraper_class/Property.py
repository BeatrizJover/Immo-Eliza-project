
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re

 
class Property:
    def __init__(self,url, driver_path ):
        self.url = url
        self.driver_path = driver_path
        self.driver= webdriver.Chrome(service=Service(driver_path))
        self.each_property_data = {
        'Locality': None,
        'Type of property': None,       #(House/apartment)
        'Subtype of property': None,    #(Bungalow, Chalet, Mansion, ...)
        'Price': None,
        'Number of rooms': None,
        'Living Area': None,
        'Fully equipped kitchen': None,    #(Yes/No)
        'Furnished':None,                 #(Yes/No)
        'Open fire': None,                 #(Yes/No)
        'Terrace': None,                   #(Yes/No)
        'Terrace Area': None,
        'Garden': None,                    #(Yes/No)
        'Garden Area': None,
        'Surface of the land': None,
        'Surface area of the plot of land': None,
        'Number of facades': None,
        'Swimming pool': None,                      #(Yes/No)
        'State of the building': None,            #(New, to be renovated, ...)
        }
        properties_data = self.property_scrapping()
        self.driver.quit()
        
        self.each_property_data['Locality'] = properties_data.get("Locality") if "Locality" in properties_data else None
        self.each_property_data['Type of property'] = properties_data.get('Property Type') if 'Property Type' in properties_data else None
        self.each_property_data['Subtype of property'] = properties_data.get('Property Type')if 'Property Type' in properties_data else None
        self.each_property_data['Price'] = properties_data.get('Price') if 'Price' in properties_data else None
        self.each_property_data['Number of rooms'] = properties_data.get('Bedrooms') if 'Bedrooms' in properties_data else None
        self.each_property_data['Living Area'] = properties_data.get('Living Area') if 'Living Area' in properties_data else None
        self.each_property_data['Fully equipped kitchen'] = properties_data.get('Kitchen type') if 'Kitchen type' in properties_data else None
        self.each_property_data['Furnished'] = properties_data.get('Furnished') if 'Furnished' in properties_data else None
        self.each_property_data['Open fire'] = properties_data.get("Open fire") if "Open fire" in properties_data else None
        self.each_property_data['Terrace'] = properties_data.get('Terrace') if 'Terrace' in properties_data else None
        self.each_property_data['Terrace Area'] = properties_data.get('Terrace surface') if 'Terrace surface' in properties_data else None
        self.each_property_data['Garden'] = properties_data.get('Garden') if 'Garden' in properties_data else None
        self.each_property_data['Garden Area'] = properties_data.get('Garden surface') if 'Garden surface' in properties_data else None
        self.each_property_data['Surface of the land'] = properties_data.get('Surface of the land') if 'Surface of the land' in properties_data else None
        self.each_property_data['Surface area of the plot of land'] = properties_data.get('Surface of the land') if 'Surface of the land' in properties_data else None
        self.each_property_data['Number of facades'] = properties_data.get('Number of frontages') if 'Number of frontages' in properties_data else None       
        # self.each_property_data['Swimming pool'] = properties_data['Swimming pool']
        self.each_property_data['State of the building'] = properties_data.get('Building condition') if 'Building condition' in properties_data else None   


    def property_scrapping(self):
        # List to store the data dictionaries for each property
        properties_data = {}
       
        self.driver.get(self.url)
        time.sleep(2)  # Allow the page to load

        # Parse the page content and storage in data-dict
        data_dict = {}

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        
        # Property type
        title_tag = soup.find('h1', class_='classified__title')
        if title_tag:
            property_type = title_tag.get_text(separator=" ", strip=True)  # Get text and clean whitespace
            property_type = property_type.replace("for sale", "").strip()  # Remove "for sale" and extra whitespace
            data_dict['Property Type'] = property_type

        # Price
        price_tag = soup.find('p', class_='classified__price')
        if price_tag:
            price_span = price_tag.find('span', class_="sr-only")
            if price_span:
                price = price_span.get_text(strip=True)
                price = re.sub(r"[€,\s]", "", price)
                data_dict['Price'] = price
                
        
        # Locality
        locality = soup.find_all('span', class_='classified__information--address-row')
        if len(locality) > 1:        
            second_address = locality[1].get_text(strip=True).split("—") 
            address = " ".join(second_address).strip()  
            data_dict['Locality'] = address

        # #Swimming pool
        # swimming_pool = soup.find_all('tbody', class_="classified-table__body")
        # for sp in swimming_pool:
        #     label_s = sp.find("th",  class_="classified-table__header")
        #     value_s = sp.find("td", class_="classified-table__data")
        #     if label_s and value_s:
        #         label_s = label_s.get_text(strip=True)
        #         value_s = value_s.get_text(strip=True)
        #         data_dict[label_s] = value_s


        # The rest of labels and values
        rows = soup.find_all('tr', class_='classified-table__row')    
        for row in rows:
            label = row.find('th', class_='classified-table__header')
            value = row.find('td', class_='classified-table__data')

            if label and value:
                label = label.get_text(strip=True)
                value = value.get_text(strip=True)                            
                    # Remove "m²" if it's in the value and convert to a clean number
                if "m²" in value:
                    value = re.sub(r"\s*(m²|square meters)", "", value).strip()
                data_dict[label] = value  # Store label-value pair

                 
                
        
        # Optional: add a delay between requests to avoid server overload
        time.sleep(1)
        
        return data_dict

    def get_property(self):

        return self.each_property_data
    
    def get_property_url(self):

        return self.url
    
    def print_property(self):
        print(self.each_property_data)
        


