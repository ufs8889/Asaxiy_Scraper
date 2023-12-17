import psycopg2
from  dotenv import *
from dateutil import parser

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=USERNAME,
    password=PASSWORD,
    host=HOST,
    port=PORT
)

def create_table():
    with conn.cursor() as curs:
        # Check if the table already exists
        curs.execute('''
            SELECT to_regclass('public.asaxiy_uz')
        ''')
        table_exists = curs.fetchone()[0]

        if not table_exists:
            # If the table does not exist, create it
            curs.execute('''
                CREATE TABLE asaxiy_uz (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255),
                    price VARCHAR(255),
                    scraped_time VARCHAR(255)
                )
            ''')
            conn.commit()
            return "Table 'asaxiy_uz' successfully created."
        else:
            return "Table 'asaxiy_uz' already exists."

def insert_to_database(name, price, scraped_time):
    with conn.cursor() as curs:
        curs.execute("INSERT INTO asaxiy_uz (name, price, scraped_time) VALUES (%s, %s, %s);", (name, price, scraped_time))
    conn.commit()
    return "Successfully added!"

def all_data():
    with conn.cursor() as curs:
        curs.execute("SELECT * FROM asaxiy_uz;")
        rows = curs.fetchall()
        keys = ("id", "name", "price", "scraped_time")
        list_of_dict = [dict(zip(keys, values)) for values in rows]
        scraped_times = [parser.parse(item['scraped_time'].replace('(UTC+5)', '')) for item in list_of_dict]
        oldest_time = min(scraped_times)
        oldest_time_with_timezone = f"{oldest_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')}UTC+5"
        return [oldest_time_with_timezone,list_of_dict]

def delete_all_data():
    try:
        with conn.cursor() as curs:
            curs.execute(f"DELETE FROM asaxiy_uz;")
        conn.commit()
        print(f"All data deleted from asaxiy_uz table.")
    except psycopg2.Error as e:
        print("Error deleting data:", e)

def check_connection(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        return "Connection to the database established."
    except psycopg2.Error as e:
        return "Error connecting to the database:", e


def close_connection():
    #print("works")
    conn.close()

#check_connection(conn)
#create_table()
#all_data()    
