import csv,time,sys
import random
from flask import json
import requests

generatedList = []
dataInfo = ["Time","SensorID","Humidity","Temperature","Brightness"]
headers = {"Content-Type": "application/json; charset=utf-8"}

def getTime():
    t = time.localtime()
    currentTime = time.strftime("%d/%m/%Y, %H:%M:%S",t)
    
    return currentTime

def getRandomSensorID():
    newSensorIDs = [112335,2234446,3345557,4456668]
    sensorID = random.choice(newSensorIDs)
    
    return sensorID

def genMeasurements():
    humidity = random.randint(30,80)
    temperature = random.randint(18,28)
    brightness = random.randint(256,754)
    
    return humidity, temperature, brightness


def loop():

    sensorID, currentTime , humidity, temperature, brightness = getRandomSensorID(), getTime() , genMeasurements()[0], genMeasurements()[1], genMeasurements()[2]
    data = { 'id': sensorID, 'time': currentTime, 'humidity':humidity, 'temp':temperature, 'brightness':brightness}
    time.sleep(0.5)
    response = requests.post("http://127.0.0.1:5000/data", json=data, headers=headers)


def data_generator_main():
    while True:
        try:
            loop()
        except KeyboardInterrupt:
            print('shutdown')
            sys.exit(0)
            

if __name__ == "__main__":
    data_generator_main()


    # with open('./static/generatedData.csv','w') as genData:
    #     writer = csv.writer(genData)
    #     writer.writerow(dataInfo)
    #     writer.writerows(generatedList)

        

# Parse into json data 
# Call request post 
# Flask endpoint to handle json data

