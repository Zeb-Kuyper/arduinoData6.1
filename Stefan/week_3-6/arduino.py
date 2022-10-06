import time
import sys
from fhict_cb_01.CustomPymata4 import CustomPymata4
import requests

MULTI_SENSOR = 12
headers = {"Content-Type": "application/json; charset=utf-8"}

class Reading:

    def __init__(self, humidity, temperature, timestamp, light) -> None:
        self.timestamp = timestamp
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

    def __str__(self):
        return f'timestamp: {self.timestamp}; temperature: {self.temperature:.2f}; humidity: {self.humidity:.2f}; light: {self.light:.2f}'

def setup():
    global board
    board = CustomPymata4(com_port = "COM3")
    board.set_pin_mode_dht(MULTI_SENSOR, sensor_type = 11, differential = .05)
    board.set_pin_mode_analog_input(2, differential=50)

def loop():
    global temperature_storage
    global humidity_storage
    time.sleep(5)
    light = board.analog_read(2)
    resistance_sensor = (1023 - light[0]) * 10 / light[0]
    requests.post("http://localhost:5000/data", json=Reading(*board.dht_read(MULTI_SENSOR), 325 * pow(resistance_sensor, -1.4) / 1000).__dict__, headers=headers)

def arduino_main():
    setup()
    while True:
        try:
            loop()
        except KeyboardInterrupt:
            print('shutdown')
            board.shutdown()
            sys.exit(0)


if __name__ == "__main__":
    arduino_main()
