import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re
from Property import Property

properties = []
csv_file_path = 'properties_urls.csv'
driv_path = '/home/betty/Desktop/Immo-Eliza project/web-scrapping/chromedriver'
houses_url = []

try:
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        houses_url = [row[0] for row in reader]  # Read each URL into houses_url list
    print(f"Loaded {len(houses_url)} URLs from {csv_file_path}")
except Exception as e:
    print(f"Error reading from CSV: {e}")
    
# Limit to the first n URLs
# houses_url = houses_url[:3]

for url in houses_url:
    properties.append(Property(url,driv_path))


# Define the path for your output CSV file
output_csv_path = 'properties.csv'

# Collect headers from the first entry in properties_data
print(properties[1].get_property())
headers = set()
for property_obj in properties:
    headers.update(property_obj.each_property_data.keys())
headers = ["URL"] + list(headers)  # "URL" será el primer encabezado

with open("properties.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()  # Escribir los encabezados en el archivo

    # Escribir cada objeto en una fila del archivo CSV
    for property_obj in properties:
        # Crear una fila con todos los encabezados, llenando los valores faltantes con None
        row = {header: property_obj.each_property_data.get(header, None) for header in headers if header != "URL"}
        row["URL"] = property_obj.url  # Agregar la URL al inicio de la fila
        writer.writerow(row)