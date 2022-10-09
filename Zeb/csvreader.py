import csv,time,sys
import random
from flask import json
import requests

def readData():
    with open('csvfile.csv', 'r') as f:
    