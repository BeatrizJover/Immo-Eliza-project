# Immo-Eliza-project

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [Timeline](#timeline)
- [Project status](#project-status)
  
## Description
This is the first stage of a larger project to create a Machine Learning (ML) model to predict sell prices of real estate properties in Belgium.
The current task is to gather actual data (at least 10,000 entries) from the Belgian real estate market. This data will be used to train and test ML prediction model.
finding all the urls
#Clean data set catagories
- equipped_kitchen: {0: 'installed', 1: '0', 2: 'hyper equipped', 3: 'semi equipped', 4: 'not installed', 5: 'usa semi 
  equipped', 6: 'usa hyper equipped', 7: 'usa installed', 8: 'usa uninstalled'}
- Subtype of property column: 0: 'apartment', 1: 'penthouse', 2: 'flat studio', 3: 'ground floor', 4: 'duplex', 5: 'loft', 6: 'service flat', 7: 'kot', 8: 'triplex', 9: 'apartment unit', 10: 'duplex unit', 11: 'ground floor unit', 12: 'kot unit', 13: 'flat studio unit', 14: 'penthouse unit', 15: 'loft unit', 16: 'triplex unit', 17: 'service flat unit'

**#The dataset delivered as a csv file and covers the following subjects:**
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

## Instalation
1. Clone the repository: ``` git clone https://github.com/BeatrizJover/Immo-Eliza-project.git```
2. Install dependencies: 
  - ```Python 3.12.4```
  - ```pip install request beautifulSoup selenium chardet pandas  ```
3. Set Up a WebDriver
- Selenium requires a WebDriver to control the browser. Examples include ChromeDriver for Chrome, GeckoDriver for Firefox, etc. To set up:
- Download WebDriver:
- For Chrome: Download ChromeDriver
- For Firefox: Download GeckoDriver
- Ensure the driver version matches your browser version.

## Usage
The Python-based tool uses ImmoWeb website, the leading real estate website in Belgium, to scrape the required information and stores it in a dictionary format and later is written as a csv file 

## Contributors
- [BeatrizJover](https://github.com/BeatrizJover)
- [Alkszo](https://github.com/Alkszo)
- [elsagk](https://github.com/elsagk)

**##Timeline**
- This stage of the project lasted 4 days in the week of 15/11/2024 16:30.

## Project status
- [Build status](https://trello.com/b/Kumf4YKs/agile-board)

                 
