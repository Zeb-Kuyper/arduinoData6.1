from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime

app = Flask(__name__)
board = 0

class Reading:

    def __init__(self, timestamp, temperature, humidity, light) -> None:
        self.timestamp = datetime.fromtimestamp(int(timestamp)).strftime("%m/%d/%Y, %H:%M:%S")
        self.temperature = float(temperature)
        self.humidity = float(humidity)
        self.light = float(light)

    def __str__(self):
        return f'timestamp: {self.timestamp}; temperature: {self.temperature:.2f}; humidity: {self.humidity:.2f}; light: {self.light:.2f}'


readings: list[Reading] = []


@app.route('/')
def index():
    return render_template('index.html', readings=readings, _humidity_func=_humidity, max_humidity_func = _max_humidity, min_humidity_func = _min_humidity, _temperature_func=_temperature, _max_temperature_func = _max_temperature, _min_temperature_func = _min_temperature, _max_light_func = _max_light, _min_light_func = _min_light, _light_func = _light)


#CSV file application needs to be made and done like the arduino data
# @app.route('/data', methods=["POST"])
# def get_csv_data():
#     data = request.get_json(silent=True)
#     print(*data.items())
#     readings.append(Reading(*data.values()))
#     return Reading(*data.values()).__dict__


@app.route('/data', methods=["POST"])
def get_arduino_data():
    data = request.get_json(silent=True)
    print(*data.items())
    readings.append(Reading(*data.values()))
    return Reading(*data.values()).__dict__

def _max_humidity(readings):
    return max([j.humidity if len(readings) > 0 else 0 for j in readings])


def _min_humidity(readings):
    return min([j.humidity if len(readings) > 0 else 0 for j in readings])

def _humidity(readings):
    return sum([int(j.humidity) if len(readings) > 0 else 0 for j in readings]) / len(readings) if len(readings) > 0 else 0

def _max_temperature(readings):
    return max([j.temperature if len(readings) > 0 else 0 for j in readings])

def _min_temperature(readings):
    return min([j.temperature if len(readings) > 0 else 0 for j in readings])

def _temperature(readings):
    return sum([int(j.temperature) if len(readings) > 0 else 1 for j in readings]) / len(readings) if len(readings) > 0 else 1

def _max_light(readings):
    return max([j.light if len(readings) > 0 else 0 for j in readings])

def _min_light(readings):
    return min([j.light if len(readings) > 0 else 0 for j in readings])

def _light(readings):
    return sum([int(j.light) if len(readings) > 0 else 0 for j in readings]) / len(readings) if len(readings) > 0 else 0