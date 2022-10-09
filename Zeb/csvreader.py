import csv,sys,time
from flask import json
import requests

headers = {"Content-Type": "application/json; charset=utf-8"}

def loop():
    with open('static\sensor_log_with_id.csv') as file:
        data = csv.DictReader(file)
        for reading in data:
            for key, value in reading.items():
                try:
                    reading[key] = int(value)
                except:
                    try:
                        reading[key] = float(value)
                    except:
                        reading[key] = str(value)
                
        requests.post("http://127.0.0.1:5000/data", json=reading, headers=headers)
    

def csv_reader_main():
    while True:
        try:
            loop()
            time.sleep(1)
        except KeyboardInterrupt:
            print('shutdown')
            sys.exit(0)

        
if __name__ == "__main__":
    csv_reader_main()
