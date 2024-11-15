import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import re
from Property import Property
import concurrent.futures

# Initialize variables
csv_file_path =  '/home/betty/Desktop/Immo-Eliza project/web-scrapping/house_and_apart/apartments_links.csv'
output_csv_path = 'properties.csv'
driv_path = '/home/betty/Desktop/Immo-Eliza project/web-scrapping/chromedriver'
houses_url = []
properties = []

# Load URLs from CSV file
try:
    with open(csv_file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        houses_url = [row[0] for row in reader]  # Read each URL into houses_url list
    print(f"Loaded {len(houses_url)} URLs from {csv_file_path}")
except Exception as e:
    print(f"Error reading from CSV: {e}")

# This will separate the urls list in chunks
houses_url = houses_url[:100]

# Function to scrape a single property
def scrape_property(url):
    try:
        property_obj = Property(url, driv_path)
        return property_obj
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return None

# Start the timer
start_time = time.time()

# Use ThreadPoolExecutor for concurrent scraping
print("Starting concurrent scraping...")
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(scrape_property, houses_url))
# Stop the timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print(f"Scraping completed in {elapsed_time:.2f} seconds.")

# Filter out None results
properties = [prop for prop in results if prop is not None]

# Extract headers for the CSV
headers = set()
for property_obj in properties:
    headers.update(property_obj.each_property_data.keys())
headers = ["URL"] + list(headers)  # "URL" will be the first header

# Write the results to a CSV file
print("Writing results to CSV...")
with open(output_csv_path, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()  # Write headers to the CSV

    # Write each property object to a row in the CSV
    for property_obj in properties:
        # Create a row with all headers, filling missing values with None
        row = {header: property_obj.each_property_data.get(header, None) for header in headers if header != "URL"}
        row["URL"] = property_obj.url  # Add the URL at the beginning of the row
        writer.writerow(row)

print(f"Scraping completed. Results saved to {output_csv_path}")