import re
import requests
from bs4 import BeautifulSoup as bs
import json
import csv
from tqdm import tqdm


def requests_scrapper(html_text, property_type=0):
    real_estate = {'immo_id': None, 'zip_code': None, 'type_of_property': property_type, 'subtype_of_property': None, 'price': None, 'building_condition': None, 'facade_number': None, 'living_area': None, 
               'equipped_kitchen': 0, 'bedroom_nr': None, 'swimming_pool': 0, 'furnished': 0, 'open_fire': 0, 'terrace': 0, 'garden': 0, 'plot_surface': 0}
    url_list = []

    soup = bs(html_text, 'html.parser')    

    info_script = soup.find('script', string=re.compile("window.dataLayer.push"))
    expr = re.compile('"classified":[\S\n ]+"customer":')   
    dict_like = re.findall(expr, info_script.string)[0]
    dict_like = re.sub('"classified":', '', dict_like)
    dict_like = re.sub(',\n\s*"customer":', '', dict_like)        
    prop_dict = (json.loads(dict_like))    

    annuitant_check = soup.find_all('th', string=re.compile("annuitant"))
    title = soup.find('title').text

    if len(annuitant_check) > 0:
        return False

    elif len(re.findall("(\s\d+m)", title)) > 0:
        real_estate['living_area'] = int(re.findall("(\s\d+m)", title)[0][1:-1])

        frontages_header = soup.find("th", class_="classified-table__header", string=re.compile("Number of frontages"))
        if frontages_header is not None:
                real_estate['facade_number'] = int(frontages_header.parent.find('td').string.strip())

        terrace_header = soup.find("th", class_="classified-table__header", string=re.compile("Terrace surface"))
        if terrace_header is not None:
            data_cell = terrace_header.parent.find('td')
            real_estate['terrace'] = int(re.findall("(\d+)", str(data_cell))[0])

        furnished_header = soup.find("th", class_="classified-table__header", string=re.compile("Furnished"))
        if furnished_header is not None:
            if furnished_header.parent.find('td').string.strip() == "Yes":
                real_estate['furnished'] = 1

        descr = soup.find('p', class_="classified__description")
        if descr is not None:
            if 'open fire' in descr.text:
                real_estate['open_fire'] = 1

        real_estate['zip_code'] = int(prop_dict['zip'])
        real_estate['immo_id'] = prop_dict['id']
        real_estate['subtype_of_property'] = prop_dict['subtype']
        if prop_dict['price'] == "no price":
            real_estate['price'] = None
        else:    
            real_estate['price'] = int(prop_dict['price'])
        real_estate['building_condition'] = prop_dict['building']['condition']    
        real_estate['bedroom_nr'] = int(prop_dict['bedroom']['count'])
        if prop_dict['kitchen']['type'] != "":
            real_estate['equipped_kitchen'] = prop_dict['kitchen']['type']
        if prop_dict['wellnessEquipment']['hasSwimmingPool'] == "true":
            real_estate['swimming_pool'] = 1
        if prop_dict['outdoor']['terrace']['exists'] == "true" and real_estate['terrace'] == 0:
            real_estate['terrace'] = 1
        if 'surface' in prop_dict['outdoor']['garden'] and prop_dict['outdoor']['garden']['surface'] != "":
            real_estate['garden'] = int(prop_dict['outdoor']['garden']['surface'])
        if prop_dict['land']['surface'] != "":
            real_estate['plot_surface'] = int(prop_dict['land']['surface'])

        return real_estate
    
    elif "group" in prop_dict['type']:
        anchor = soup.find('template', string=re.compile("All properties"))
        for link in anchor.parent.find_all('a'):
            url_list.append([link['href']])
        
        return url_list
    
    else:
        return True
    

def scraping_session(property_type=0): #property_type is binary for is_house: 0=apartment, 1=house
    field_names = ['immo_id', 'zip_code', 'type_of_property', 'subtype_of_property', 'price', 'building_condition', 'facade_number', 'living_area', 'equipped_kitchen', 'bedroom_nr', 'swimming_pool', 'furnished', 'open_fire', 'terrace', 'garden', 'plot_surface']

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    session = requests.Session()
    session.headers = headers

    apartments_path = "url_store/apartments_links.csv"
    houses_path = "url_store/houses_links.csv"    

    apartments_save = "Alek_scrapper_results/apartment"
    houses_save = "Alek_scrapper_results/houses"

    def scraping_loop(load_path, save_path):

        csv_list = []
        with open(load_path, newline='') as f:
            reader = csv.reader(f)    
            for entry in reader:
                csv_list.append(entry[0])

        all_links = csv_list[1:]

        for link in tqdm(all_links):
            response = session.get(link, headers=headers)
            try:
                result = requests_scrapper(response.text, property_type)
                if isinstance(result, dict):
                    with open(f'{save_path}_data.csv', 'a', newline='') as file:
                        csv.DictWriter(file, fieldnames=field_names).writerow(result)
                elif isinstance(result, list):
                    with open(f'{save_path}_additional_urls.csv', 'a', newline='') as file:
                        for url in result:
                            csv.writer(file).writerow(url)
            except Exception as ex:
                with open(f'{save_path}_failed_urls.csv', 'a', newline='') as file:
                    csv.writer(file).writerow([link])        
                continue

    if property_type == 1:
        scraping_loop(houses_path, houses_save)
    else:
        scraping_loop(apartments_path, apartments_save)

scraping_session(1)
