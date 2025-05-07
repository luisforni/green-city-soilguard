# src/sensors/read_soil_temperature.py

import os
import glob
import time

# Cargar módulos del kernel necesarios para 1-Wire
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Buscar el archivo del sensor
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines

def read_soil_temperature():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return round(temp_c, 2)

if __name__ == "__main__":
    while True:
        temp = read_soil_temperature()
        print(f"Temperatura del suelo: {temp} °C")
        time.sleep(2)
