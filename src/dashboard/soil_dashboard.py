import csv
import os
import time
from datetime import datetime
from src.sensors.read_soil_moisture import read_soil_moisture
from src.sensors.read_soil_temperature import read_soil_temperature

OUTPUT_FILE = "data/soil_dataset.csv"
INTERVAL_SECONDS = 60  # recolectar cada 1 minuto

# Cabecera del CSV
HEADERS = ["timestamp", "soil_moisture", "soil_temperature"]

def init_csv():
    if not os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS)
            writer.writeheader()

def append_data():
    row = {
        "timestamp": datetime.now().isoformat(),
        "soil_moisture": read_soil_moisture(),
        "soil_temperature": read_soil_temperature()
    }
    with open(OUTPUT_FILE, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=HEADERS)
        writer.writerow(row)

def main():
    init_csv()
    print("Recolectando datos del suelo cada", INTERVAL_SECONDS, "segundos. Presiona Ctrl+C para detener.")
    try:
        while True:
            append_data()
            time.sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nFinalizado.")

if __name__ == "__main__":
    main()
