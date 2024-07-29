from bs4 import BeautifulSoup
from dotenv import load_dotenv
from os import getenv
from fetch import *
from save_html import *
from write_csv import *

load_dotenv("./.env")                   # load environment variables from .env file

url = getenv('URL')
path = getenv('FILE_PATH')
html = ''
response = fetch(url)
if response.status_code==200:
    save(path , response.text)
    html = read(path)
elif response.status_code==404:
    print("Network error")

path_html = getenv('HTML_PATH')
html = read(path_html)

soup = BeautifulSoup(html, "html.parser")

phone_names = []
prices = []

for tag in soup.find_all(class_="KzDlHZ"):
    phone_names.append(tag.string.replace("\n", "").strip())

for price in soup.find_all(class_="Nx9bqj _4b5DiR"):
    prices.append(price.string)

phone_names_tup = tuple(phone_names)
prices_tup = tuple(prices)
names_prices = list(zip(phone_names_tup , prices_tup))

for index,item in enumerate(names_prices):
    list_item = list(item)
    names_prices[index] = list_item

print(names_prices)

path_csv = getenv('CSV_PATH')
write_to_csv(path_csv, names_prices)