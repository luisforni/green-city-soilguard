# src/sensors/read_soil_moisture.py

from gpiozero import MCP3008

# Canal 1 del MCP3008 (CH1) para el sensor capacitivo de humedad del suelo
soil_channel = MCP3008(channel=1)

def read_soil_moisture():
    value = soil_channel.value  # valor entre 0 y 1
    percentage = round((1.0 - value) * 100, 2)  # más seco → mayor valor, lo invertimos
    return percentage

if __name__ == "__main__":
    import time
    while True:
        humedad = read_soil_moisture()
        print(f"Humedad del suelo: {humedad} %")
        time.sleep(2)
