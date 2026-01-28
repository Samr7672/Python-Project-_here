import tkinter as tk
from tkinter import messagebox
import requests
import folium
from folium.plugins import HeatMap
import webbrowser
import os


API_KEY = "YOUR_OPENWEATHER_API_KEY"

LOCATIONS = [
    ("London", 51.5, -0.12), ("Paris", 48.8, 2.35), ("Berlin", 52.5, 13.4),
    ("Madrid", 40.4, -3.7), ("Rome", 41.9, 12.4), ("Oslo", 59.9, 10.7)
]

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Weather HeatMapper")
        self.root.geometry("300x200")
        
        self.is_running = False
        
        # UI Elements
        self.label = tk.Label(root, text="Weather Monitor", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.btn_toggle = tk.Button(root, text="Start Auto-Refresh", command=self.toggle_monitor, bg="green", fg="white")
        self.btn_toggle.pack(pady=10)
        
        self.status_label = tk.Label(root, text="Status: Idle", fg="gray")
        self.status_label.pack(pady=5)

    def toggle_monitor(self):
        self.is_running = not self.is_running
        if self.is_running:
            self.btn_toggle.config(text="Stop Monitoring", bg="red")
            self.update_loop()
        else:
            self.btn_toggle.config(text="Start Auto-Refresh", bg="green")
            self.status_label.config(text="Status: Stopped")

    def fetch_heat_data(self):
        heat_data = []
        for name, lat, lon in LOCATIONS:
            url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
            try:
                res = requests.get(url).json()
                temp = res['main']['temp']
                # HeatMap expects [lat, lon, intensity]
                heat_data.append([lat, lon, temp])
            except:
                continue
        return heat_data

    def update_loop(self):
        if not self.is_running:
            return
            
        self.status_label.config(text="Status: Updating Map...")
        data = self.fetch_heat_data()
        
        if data:
            # Create Map
            m = folium.Map(location=[50, 10], zoom_start=4, tiles="stamentoner")
            
            # Add HeatMap Layer
            HeatMap(data, radius=25, blur=15, max_zoom=1).add_to(m)
            
            # Save and Open
            file_path = os.path.abspath("live_heatmap.html")
            m.save(file_path)
            
            # Open in browser only the first time, then just refresh manually or via JS
            if self.status_label.cget("text") == "Status: Updating Map...":
                webbrowser.open(f"file://{file_path}")
            
            self.status_label.config(text="Status: Map Updated!")
        
        # Schedule next update in 30 seconds (30000 ms)
        self.root.after(30000, self.update_loop)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()