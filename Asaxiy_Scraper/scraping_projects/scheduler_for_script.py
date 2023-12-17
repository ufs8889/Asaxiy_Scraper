import schedule
import time
import subprocess
from postgress_db import * 

def run_script():
    subprocess.run(["python", "asaxiy_phones.py"])  # Замените путь на путь к вашему скрипту
    subprocess.run(["python", "Upload to files.py"]) 
    
# Запуск скрипта каждый день в 8:00
schedule.every().day.at("05:00").do(run_script)

while True:
    schedule.run_pending()
    time.sleep(60)  # Проверка каждую минуту
