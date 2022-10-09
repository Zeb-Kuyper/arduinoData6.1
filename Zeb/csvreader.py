import csv,time,sys
import random
from flask import json
import requests

def readData():
    with open('.\static\sensor_log_with_id.csv', 'r') as file:
        stats = csv.DictReader(file)
        for lines in stats:
            print(lines)
        
readData()