# 🌱 GreenCity SoilGuard – Smart Soil Monitoring with Raspberry Pi

**GreenCity SoilGuard** is an IoT solution that monitors soil conditions in real time using physical sensors connected to a Raspberry Pi 4. It's ideal for urban agriculture, green roofs, public parks, or sustainable gardening.

---

## 🚀 What does it measure?

- **Soil moisture** with a capacitive sensor (analog output)
- **Soil temperature** with a waterproof DS18B20 sensor
- (Optional) **Soil conductivity / nutrient levels** via TDS sensor

---

## 🔧 Required hardware

- Raspberry Pi 4 (2 GB RAM or more)
- Capacitive Soil Moisture Sensor v2.0 (analog)
- DS18B20 waterproof temperature sensor
- MCP3008 ADC (to read analog signals)
- Breadboard, Dupont wires, 4.7kΩ resistor for DS18B20

---

## 🛠️ Wiring overview

### Soil Moisture Sensor
- VCC → 3.3V (Pin 1)
- GND → GND (Pin 6)
- AOUT → MCP3008 CH1

### MCP3008 (connected to SPI)
- VDD, VREF → 3.3V
- AGND, DGND → GND
- CLK → GPIO 11 (Pin 23)
- DOUT → GPIO 9 (Pin 21)
- DIN → GPIO 10 (Pin 19)
- CS → GPIO 8 (Pin 24)

### DS18B20
- VCC → 3.3V
- GND → GND
- DATA → GPIO 4 (Pin 7) with 4.7kΩ resistor between DATA and VCC

---

## 📦 Installation

```bash
git clone https://github.com/luisforni/green-city-soilguard.git
cd green-city-soilguard
pip install -r requirements.txt
```

---

## 🏃 How to run

### Start data collection
```bash
python src/data/soil_collector.py
```

### Launch real-time dashboard
```bash
python src/dashboard/soil_dashboard.py
```

---

## 📁 Project structure

```
green-city-soilguard/
├── data/
│   └── soil_dataset.csv
├── src/
│   ├── sensors/
│   │   ├── read_soil_moisture.py
│   │   └── read_soil_temperature.py
│   ├── data/
│   │   └── soil_collector.py
│   └── dashboard/
│       └── soil_dashboard.py
├── requirements.txt
└── README.md
```

---

## 🧠 Author

Developed by [Luis Forni](https://www.linkedin.com/in/luis-forni-97aa49223)  
Part of the **GreenCity IoT ecosystem**.

---

## 📃 License

MIT – Free to use, modify and contribute. Credits are appreciated.
