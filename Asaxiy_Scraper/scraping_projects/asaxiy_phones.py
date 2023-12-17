import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from postgress_db import *

data = []
timestamp = datetime.timestamp(datetime.now())
time = datetime.fromtimestamp(timestamp)
current_time = time.replace(microsecond=0)
for x in range(1):#56
    url = f"https://asaxiy.uz/product/telefony-i-gadzhety/telefony/smartfony/page={x}"
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")
        outer_div = soup.find('div', class_="row custom-gutter mb-40")
        if outer_div:
            product_name = outer_div.find_all('p', class_="title__link")
            product_price = outer_div.find_all('div', class_="produrct__item-prices--wrapper")
            remove_chars = {ord(i): None for i in '\n,'}
            not_ready_names = [(element.get_text()).translate(remove_chars) for element in product_name]
            ready_names = [item.strip() for item in not_ready_names if item.strip()]
            ready_price = [(element.get_text()).translate(remove_chars) for element in product_price]
            cleaned_price = [item.split('сум')[0] + 'сум' for item in ready_price]
            page_data = [{'name': name, 'price': price, "scraped_time":f"{current_time} (UTC+5)"} for name, price in zip(ready_names, cleaned_price)]
            data.extend(page_data)
json_data = json.dumps(data, ensure_ascii=False, indent=4)

delete_all_data()

for item in data:
    insert_to_database(item['name'], item['price'], item['scraped_time'])  
close_connection() 
print("Runned perfectly!")
