# Asaxiy_Parser 

Asaxiy_Parser is a Django-based web scraping tool that extracts data from the phone category of the Asaxiy.uz website, including both product names and prices. The scraped information is stored in a PostgreSQL database and exported to Excel and CSV files. Additionally, the data is presented on a webpage.

## Features

✅ Scrapes the phone category (56 pages) from the Asaxiy.uz website, capturing both price and name.

✅ Database: Utilizes PostgreSQL for data storage.

✅ Scheduled Updates: Automatically updates data every day at 5:00 to ensure the latest information.

✅ Web Framework: Developed with Django for a robust and scalable web application.

✅ Historical Data: Retains daily Excel and CSV files, enabling users to compare data with previous records.

Feel free to incorporate these changes into your project documentation.


## Installation

Clone the repository:

```bash
git clone https://github.com/ufs8889/Asaxiy_Parser-.git
```
Create a virtual environment:
```bash
python -m venv env
```
Activate the virtual environment:
```bash
.\env\Scripts\Activate.ps1
```
Install all required libraries:
```bash
pip install -r requirements.txt
```


## Usage

Navigate to the scraping_projects directory:
```bash
cd scraping_projects
```
Run the postgress_db.py script to create a table in the PostgreSQL database:
```bash
python -i postgress_db.py
```
Create a table using the create_table() function within the interactive Python shell:
``` 
>>> create_table()
"Table 'asaxiy_uz' successfully created."
>>>exit()
```
Navigate back to the root directory:
```bash
cd..
```
Move to the master directory:
```bash
cd master 
```
Apply migrations to set up the database:
```bash
python manage.py makemigrations;python manage.py migrate
```
Start the Django development server:
```bash
python manage.py runserver
```
Open another terminal to run scheduler script:
```
python scheduler_for_script.py 
```

Open your browser and visit http://127.0.0.1:8000/ to interact with the application.
