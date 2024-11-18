# Immo-Eliza-project

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [Timeline](#timeline)
- [Project status](#project-status)
  
## Description
This is the first stage of a larger project to create a Machine Learning (ML) model to predict sell prices of real estate properties in Belgium. The current task is to gather actual data (at least 10,000 entries) from the Belgian real estate market. This data will be used to train and test ML prediction model.

The Python-based tool uses [ImmoWeb](https://www.immoweb.be/en) website, the leading real estate website in Belgium, to scrape the required information and stores it in a dictionary format and later is written as a `csv` file.


**The dataset delivered as a csv file and covers the following subjects:**
- Locality
- Type of property (House/apartment)
- Subtype of property (Bungalow, Chalet, Mansion, ...)
- Price
- Type of sale (Exclusion of life sales)
- Number of rooms
- Living Area
- Fully equipped kitchen (Yes/No)
- Furnished (Yes/No)
- Open fire (Yes/No)
- Terrace (Yes/No)
- If yes: Area
- Garden (Yes/No)
- If yes: Area
- Surface of the land
- Surface area of the plot of land
- Number of facades
- Swimming pool (Yes/No)
- State of the building (New, to be renovated, ...)

## Installation
1. Clone the repository: ``` git clone https://github.com/BeatrizJover/Immo-Eliza-project.git```
2. Install dependencies: 
  - ```Python 3.12.4```
  - ```pip install request beautifulSoup selenium pandas tqdm ```
3. Set Up a WebDriver
- Selenium requires a WebDriver to control the browser. Examples include ChromeDriver for Chrome, GeckoDriver for Firefox, etc. To set up:
- Download WebDriver:
- For Chrome: [Download ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads)
- For Firefox: [Download GeckoDriver](https://geckodriver.com/download/)
- Ensure the driver version matches your browser version.

## Usage
- Execute the script by running the command `python main_url_scrapper.py` in the terminal. This will scrape properties urls listing from [ImmoWeb](https://www.immoweb.be/en) and store them in the `url_store` directory in both `json` and `csv` formats.

- Execute the script by running the command `python main_scrapper.py` in the terminal. This will scrape each property listing from provided list of [ImmoWeb](https://www.immoweb.be/en) urls and store them in the `csv_files` directory in csv format. The script will have to be run more then one time to scrap both apartments and houses and to check additional links acquired during the process. The `tqdm` library provides user with progress bar to check the % of scraping script execution.


## Contributors
The project was made by a group of Junior AI & Data Scientists (in alphabetical order):

- [Alkszo](https://github.com/Alkszo)
- [BeatrizJover](https://github.com/BeatrizJover)
- [elsagk](https://github.com/elsagk)

## Timeline
- This stage of the project lasted 4 days in the week of 15/11/2024 16:30.

## Project status
- [Build status](https://trello.com/b/Kumf4YKs/agile-board)

                 
