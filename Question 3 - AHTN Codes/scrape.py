#THIS IS FOR TESTING ONLY, IGNORE THIS CODE

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to extract AHTN data from a given URL
def extract_ahtn_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Assuming the data is in a table format
    table = soup.find('table')
    df = pd.read_html(str(table))[0]  # Read the first table found
    df.columns = ['Code', 'Description']  # Adjust according to the actual table structure
    return df

# URLs for 2017 and 2022 AHTN data
url_2017 = 'https://tariffcommission.gov.ph/tariff-book'
url_2022 = 'https://tariffcommission.gov.ph/tariff-book-2022'

# Extracting data
ahtn_2017_df = extract_ahtn_data(url_2017)
ahtn_2022_df = extract_ahtn_data(url_2022)

# Focus on Chapter 85
ahtn_2017_chapter85 = ahtn_2017_df[ahtn_2017_df['Code'].str.startswith('85')]
ahtn_2022_chapter85 = ahtn_2022_df[ahtn_2022_df['Code'].str.startswith('85')]