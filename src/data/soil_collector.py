import flet as ft
from src.sensors.read_soil_moisture import read_soil_moisture
from src.sensors.read_soil_temperature import read_soil_temperature
import time

def main(page: ft.Page):
    page.title = "GreenCity SoilGuard - Dashboard"
    page.window_width = 400
    page.window_height = 300
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title = ft.Text("Monitoreo del Suelo", size=22, weight="bold")
    moisture_text = ft.Text()
    temperature_text = ft.Text()

    def update_loop():
        while True:
            moisture = read_soil_moisture()
            temperature = read_soil_temperature()

            moisture_text.value = f"Humedad del suelo: {moisture} %"
            temperature_text.value = f"Temperatura del suelo: {temperature} °C"

            page.update()
            time.sleep(30)

    page.add(title, moisture_text, temperature_text)

    import threading
    threading.Thread(target=update_loop, daemon=True).start()

ft.app(target=main, view=ft.AppView.FLET_APP_HIDDEN)
