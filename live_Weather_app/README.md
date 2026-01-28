# Live Weather HeatMapper

## Description
A real-time weather monitoring application that visualizes temperature data from multiple European cities on an interactive heatmap. The application fetches live weather data from OpenWeatherMap API and displays it using folium, with automatic periodic updates.

## Features
- **Real-time Weather Data**: Fetches current temperature data from OpenWeatherMap API
- **Interactive Heatmap**: Visualizes temperature variations across European cities
- **Auto-Refresh**: Automatically updates weather data every 30 seconds
- **Web-based Visualization**: Displays the heatmap in a web browser using folium
- **GUI Control**: Simple tkinter interface to start/stop monitoring
- **Multiple Locations**: Monitors 6 major European cities: London, Paris, Berlin, Madrid, Rome, and Oslo

## Prerequisites
- Python 3.7 or higher
- Required libraries:
  - tkinter
  - requests
  - folium
  - webbrowser (built-in)

## Installation
1. Install required packages:
   ```bash
   pip install requests folium
   ```

2. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)

3. Update the `API_KEY` variable in `live.py` with your API key:
   ```python
   API_KEY = "YOUR_OPENWEATHER_API_KEY"
   ```

## Usage
Run the application:
```bash
python live.py
```

1. A GUI window titled "Live Weather HeatMapper" will appear
2. Click "Start Auto-Refresh" to begin monitoring
3. The application will fetch weather data and open a heatmap in your default browser
4. The heatmap updates automatically every 30 seconds
5. Click "Stop Monitoring" to stop the periodic updates

## Output
- Generates `live_heatmap.html` file containing the interactive heatmap
- The heatmap shows temperature intensity using color gradients (cooler = blue, warmer = red)

## Configuration
You can customize the application by modifying:
- `LOCATIONS`: Add or remove cities with their coordinates
- Update interval: Change `30000` (milliseconds) in the `update_loop()` method for faster/slower updates
- Map settings: Modify zoom level and tile style in the `folium.Map()` call

## Error Handling
The application gracefully handles:
- API connection failures
- Missing or invalid temperature data
- Browser opening issues

## Notes
- Ensure your internet connection is active for API calls
- The heatmap file is saved in the current working directory
- Temperature data is in Celsius by default
