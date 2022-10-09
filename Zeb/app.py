from flask import Flask, render_template, json, request
from fhict_cb_01.CustomPymata4 import CustomPymata4
import time,sys
from numpy import average

app =  Flask(__name__)

averagesList = {
    'humidity' : [],
    'brightness' : [],
    'temp' : []
}

statsDict = {}
currentTime = time.strftime("%H:%M:%S", time.localtime())

@app.route("/")
def index():
    return render_template('index2.html', stats = statsDict, calculate_average = calculate_average)

@app.route("/data", methods = ['POST'])
def receive_data():
    stats = request.json
    
    # Extract data without id
    temp = stats.copy()
    del temp["id"]
    
    id = stats["id"]
    if id in statsDict:
        statsDict[id].append(temp)
        print(statsDict)
    else:
        statsDict[id] = [temp]
        print(statsDict)
    
    index()
    
    return "OK",200

def calculate_average(id, measurement):
    average = round(sum([reading[measurement] for reading in statsDict[id]]) / len(statsDict[id]),2)
    return average


if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=5000)