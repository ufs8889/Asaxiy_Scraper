import pandas as pd
from postgress_db import *
from datetime import datetime
import os

timestamp = datetime.timestamp(datetime.now())
time = datetime.fromtimestamp(timestamp)
current_time = time.replace(microsecond=0)

# Example data_list with dictionaries
data_list = all_data()

# Convert list of dictionaries to pandas DataFrame
df = pd.DataFrame(data_list)

# Save DataFrame to an Excel file
directory = 'scraped_data_by_time'
if not os.path.exists(directory):
    os.makedirs(directory)

# Replace special characters from the timestamp to create a valid filename
formatted_time = str(current_time).replace(':', '-').replace(' ', '_')  # Replace special characters

# Form the filenames
excel_file_name = f'asaxiy_uz_phones_{formatted_time}.xlsx'
csv_file_name = f'asaxiy_uz_phones_{formatted_time}.csv'

excel_file_path = os.path.join(directory, excel_file_name)
csv_file_path = os.path.join(directory, csv_file_name)

# Save DataFrame to an Excel file
df.to_excel(excel_file_path, index=False)

# Save DataFrame to a CSV file
if not os.path.exists(csv_file_path):
    df.to_csv(csv_file_path, index=False)
else:
    df.to_csv(csv_file_path, index=False, mode='a', header=False)
