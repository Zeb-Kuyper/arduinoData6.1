from fhict_cb_01.CustomPymata4 import CustomPymata4
import time,sys
import requests

DHTPIN = 12
LDRPIN = 2

headers = {"Content-Type": "application/json; charset=utf-8"}
sensorID = 50054315
humidity = 0
brightness = 0
temperature = 0
currentTime = ''

def get_time(): 
    global currentTime
    currentTime = time.strftime("%H:%M:%S", time.localtime())
     

def store_LDR(data):
    global brightness
    brightness = data[2]
    
def store_temp_hum(data): 
    global humidity, temperature
    humidity = data[4]
    temperature = data[5]
    
def setup(): # Initialize readings
    global board
    board = CustomPymata4(com_port="COM3")
    board.set_pin_mode_dht(DHTPIN, sensor_type = 11, differential = .05, callback = store_temp_hum)
    board.set_pin_mode_analog_input(LDRPIN, callback = store_LDR, differential = 10)


def loop():
    global humidity, brightness, temperature
    store_LDR()
    store_temp_hum()
    data = { 'id': sensorID, 'time': currentTime, 'humidity':humidity, 'temp':temperature, 'brightness':brightness}
    requests.post("http:localhost:5000/data", json=data, headers=headers)
    time.sleep(0.01)

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