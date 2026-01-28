# Live Weather HeatMapper - Flowchart

## Application Flow

```
START
  |
  v
Initialize Tkinter Window
  |
  +-- Set Window Title: "Live Weather HeatMapper"
  +-- Set Window Size: 300x200
  +-- Create UI Elements (Label, Button, Status Label)
  |
  v
Display GUI Window
  |
  v
User Clicks "Start Auto-Refresh" Button?
  |
  +-- YES --> Set is_running = True
  |            |
  |            v
  |            Change Button to "Stop Monitoring" (Red)
  |            |
  |            v
  |            Enter Update Loop
  |            |
  |            +---> Update Status: "Updating Map..."
  |            |     |
  |            |     v
  |            |     Fetch Heat Data:
  |            |     |
  |            |     +-- For each location in LOCATIONS:
  |            |     |   - Build OpenWeatherMap API URL
  |            |     |   - Make HTTP request
  |            |     |   - Extract temperature value
  |            |     |   - Append [latitude, longitude, temp] to heat_data
  |            |     |   - On error: skip location
  |            |     |
  |            |     v
  |            |     Data Retrieved?
  |            |     |
  |            |     +-- YES --> Create Folium Map
  |            |     |            |
  |            |     |            v
  |            |     |            Add HeatMap Layer
  |            |     |            |
  |            |     |            v
  |            |     |            Save as "live_heatmap.html"
  |            |     |            |
  |            |     |            v
  |            |     |            Open in Web Browser
  |            |     |            (First time only)
  |            |     |            |
  |            |     |            v
  |            |     |            Update Status: "Map Updated!"
  |            |     |
  |            |     +-- NO --> Continue (no map update)
  |            |
  |            |     v
  |            |     Schedule Next Update
  |            |     (30 seconds = 30000 ms)
  |            |     |
  |            |     v
  |            |     Wait for User Input or Timer
  |            |     |
  |            |     +-- User Clicks Button --> Toggle Off
  |            |     +-- Timer Expires --> Loop Back to Fetch Data
  |
  +-- NO --> Stay in Idle State
             Status: "Idle"
             Wait for Button Click
```

## Detailed Process Flow

### 1. **Initialization Phase**
   - Create Tkinter root window
   - Configure window properties
   - Create UI components
   - Set initial state to not running

### 2. **Toggle Monitor Phase**
   - User clicks button
   - Toggle `is_running` flag
   - Update button appearance and status label

### 3. **Update Loop Phase** (when running)
   - Fetch real-time weather data from API
   - Process temperature data for each location
   - Create interactive map with heatmap layer
   - Save and display map in browser
   - Schedule next update after 30 seconds
   - Loop back to step 3 until stopped

### 4. **Stop Phase**
   - User clicks "Stop Monitoring" button
   - Set `is_running = False`
   - Exit update loop
   - Return button to "Start Auto-Refresh"

## Data Flow

```
OpenWeatherMap API
       |
       v
fetch_heat_data() function
       |
       +-- Extract: latitude, longitude, temperature
       |
       v
Heat Data Array [[lat1, lon1, temp1], [lat2, lon2, temp2], ...]
       |
       v
Folium HeatMap Layer
       |
       v
Interactive Map (HTML)
       |
       v
Web Browser Display
```
