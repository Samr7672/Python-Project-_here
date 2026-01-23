# Weather App

## Overview
Weather App is a PyQt5-based graphical user interface application that fetches real-time weather data from the OpenWeatherMap API. Users can enter any city name and receive current temperature, weather conditions, and weather emoji indicators.

## Features
- **Real-time Weather Data**: Fetches current weather information from OpenWeatherMap API
- **Graphical User Interface**: Professional GUI built with PyQt5 for user-friendly experience
- **Temperature Display**: Shows temperature in Celsius with large, readable font
- **Weather Emoji**: Displays emoji indicators for different weather conditions (thunderstorm, rain, snow, etc.)
- **Weather Description**: Shows detailed text description of weather conditions (Capitalized format)
- **Comprehensive Error Handling**: 
  - HTTP error handling for 400, 401, 403, 404, 500 status codes
  - Connection error handling for internet connectivity issues
  - Timeout error handling for slow network requests
  - Generic request exception handling for other errors
- **Centered Layout**: All UI elements centered for clean appearance
- **Custom Styling**: CSS stylesheet for professional appearance with calibri font
- **API Integration**: Secure API key integration with OpenWeatherMap

## Requirements
- Python 3.7+
- PyQt5
- requests

## Installation

1. **Clone or download the project**:
   ```
   cd Weather_App
   ```

2. **Install required packages**:
   ```
   pip install PyQt5 requests
   ```

3. **Run the application**:
   ```
   python weather_app.py
   ```

## Usage

1. **Launch the Application**:
   - Run `python weather_app.py` from command line
   - A window titled "Weather App" will appear

2. **Enter City Name**:
   - Type any city name in the text input field
   - Example: "London", "New York", "Tokyo"

3. **Get Weather Data**:
   - Click the "Get Weather" button
   - The app will fetch weather data from OpenWeatherMap API

4. **View Results**:
   - Temperature displays in large text (75px font) in Celsius (°C format)
   - Weather emoji displays (100px font using Segoe UI emoji)
   - Description displays weather condition (50px font)

5. **Error Messages**:
   - If city not found: "Not Found: City not found"
   - If no internet: "Connection Error: Check your internet connection"
   - If timeout: "Timeout Error: The request timed out"

## Examples

### Example 1: London Weather
```
Input: London
Output:
  Temperature: 10°C
  Emoji: ☀️ (or appropriate weather emoji)
  Description: Partly cloudy
```

### Example 2: Tokyo Weather
```
Input: Tokyo
Output:
  Temperature: 15°C
  Emoji: 🌧️ (or appropriate weather emoji)
  Description: Light rain
```

### Example 3: Invalid City
```
Input: XyzNotACity
Output:
  Error Message: Not Found: City not found
```

## UI Components

### Main Window (QWidget)
- **Window Title**: "Weather App "
- **Layout**: Vertical Box Layout (QVBoxLayout)
- **Size**: Auto-adjusting based on content

### Input Elements
1. **City Label** (QLabel)
   - Text: "Enter city name: "
   - Font: Calibri, 40px, italic
   - Alignment: Center

2. **City Input** (QLineEdit)
   - Placeholder for city name
   - Font: Calibri, 40px
   - Alignment: Center

3. **Get Weather Button** (QPushButton)
   - Text: "Get Weather"
   - Font: Calibri, 30px, bold
   - Connected to: get_weather() method

### Output Elements
1. **Temperature Label** (QLabel)
   - Displays: Temperature in Celsius
   - Font: 75px
   - Alignment: Center

2. **Emoji Label** (QLabel)
   - Displays: Weather condition emoji
   - Font: 100px, Segoe UI emoji family
   - Alignment: Center

3. **Description Label** (QLabel)
   - Displays: Weather description text
   - Font: Calibri, 50px
   - Alignment: Center

## Weather Code to Emoji Mapping

| Weather Code Range | Condition | Emoji |
|---|---|---|
| 200-232 | Thunderstorm | ⛈️ |
| 300-321 | Drizzle | 🌦️ |
| 500-531 | Rain | 🌧️ |
| 600-622 | Snow | ❄️ |
| 701-741 | Mist/Fog/Smoke | 🌫️ |
| 762 | Volcanic Ash | 🌋 |
| 771 | Squall | 💨 |
| 781 | Tornado | 🌪️ |
| 800 | Clear Sky | ☀️ |
| 801-804 | Clouds | ☁️ |

## API Integration Details

### OpenWeatherMap API
- **Endpoint**: `https://api.openweathermap.org/data/2.5/weather`
- **API Key**: `134e993b633291ffe2c4ea1c9ffb65ad`
- **Units**: Metric (Celsius)
- **Required Parameter**: `q` (city name)
- **Response Format**: JSON

### Response Structure
```json
{
  "cod": "200",
  "main": {
    "temp": 15.5
  },
  "weather": [
    {
      "id": 800,
      "description": "clear sky"
    }
  ]
}
```

## Error Handling

The application handles multiple error scenarios:

1. **HTTP 400 - Bad Request**: User input error
2. **HTTP 401 - Unauthorized**: Invalid API key
3. **HTTP 403 - Forbidden**: Access denied
4. **HTTP 404 - Not Found**: City name not found
5. **HTTP 500 - Server Error**: OpenWeatherMap server issue
6. **Connection Error**: No internet connectivity
7. **Timeout Error**: Network request timeout
8. **General Request Exception**: Other request-related errors

All errors display user-friendly messages in the temperature label with reduced font size (30px).

## Code Structure

### Class: WeatherApp(QWidget)
Main application class inheriting from PyQt5 QWidget

#### Methods:
1. **`__init__()`**
   - Initializes all UI components
   - Creates labels, input field, and button
   - Calls initUI()

2. **`initUI()`**
   - Sets window title
   - Creates vertical box layout
   - Adds all widgets to layout
   - Sets alignment for all widgets
   - Applies CSS styling
   - Connects button click event to get_weather()

3. **`get_weather()`**
   - Retrieves city name from input field
   - Constructs API URL with city and API key
   - Sends HTTP GET request
   - Handles HTTP responses and errors
   - Calls display_weather() on success
   - Calls display_error() on failure

4. **`display_weather(data)`**
   - Extracts temperature, weather_id, and description from API response
   - Formats temperature with 0 decimal places
   - Calls get_weather_emoji() for emoji mapping
   - Updates all output labels

5. **`display_error(message)`**
   - Displays error message in temperature label
   - Clears emoji and description labels
   - Reduces temperature label font size to 30px

6. **`get_weather_emoji(weather_id)` (static method)**
   - Maps OpenWeatherMap weather ID codes to emoji
   - Uses conditional logic to determine emoji
   - Returns appropriate emoji or empty string

## Learning Concepts

### 1. PyQt5 GUI Programming
- Widget hierarchy and inheritance
- Layout management (QVBoxLayout)
- Signal-slot mechanism (button clicks)
- CSS styling in PyQt5

### 2. API Integration
- Making HTTP requests with requests library
- Handling JSON responses
- URL parameter construction
- Secure API key management

### 3. Error Handling
- Try-except blocks for multiple exception types
- Match-case statements for HTTP status codes
- Specific error catching hierarchy
- User-friendly error messages

### 4. Python Patterns
- Static methods
- Conditional logic and range checking
- String formatting with f-strings
- Object-oriented design principles

## Configuration

### API Key
The API key is hardcoded in the `get_weather()` method:
```python
api_key = "134e993b633291ffe2c4ea1c9ffb65ad"
```

**Note**: For production use, consider storing API keys in environment variables or configuration files.

### Temperature Units
The API uses metric units by default (Celsius). To change to Fahrenheit, modify the URL:
```python
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
```

### Font Customization
Modify the setStyleSheet() call in initUI() to customize fonts, sizes, or colors:
- Font sizes are in px
- Font families: calibri, "Segoe UI emoji"
- Colors can be added with color property

## Troubleshooting

### City Not Found Error
- **Problem**: Entering invalid city name
- **Solution**: Check spelling and use official city names

### Connection Error
- **Problem**: No internet connection
- **Solution**: Check internet connectivity and firewall settings

### Timeout Error
- **Problem**: Network is slow or API is unresponsive
- **Solution**: Check internet speed and try again later

### Application Won't Start
- **Problem**: PyQt5 or requests not installed
- **Solution**: Run `pip install PyQt5 requests`

### Blank Temperature Display
- **Problem**: API returned unexpected response format
- **Solution**: Check API key validity and city name

## Performance Notes
- API response time: 1-3 seconds typically
- No caching implemented - each request hits the API
- UI remains responsive during API calls (synchronous implementation)

## Future Enhancements
- Add threading to prevent UI freezing during API calls
- Implement weather forecast (5-day, hourly)
- Add location detection using IP geolocation
- Cache weather data to reduce API calls
- Support for multiple temperature units toggle
- Add weather alerts and notifications
- Store search history
- Dark mode support

## Security Considerations
- API key is exposed in source code (not recommended for production)
- Use environment variables for sensitive data
- Consider using API proxy for production applications
- Validate user input to prevent injection attacks

## Dependencies Summary
| Package | Version | Purpose |
|---|---|---|
| PyQt5 | Latest | GUI framework |
| requests | Latest | HTTP requests |
| sys | Built-in | System operations |

## Running on Different Platforms

### Windows
```
python weather_app.py
```

### macOS
```
python3 weather_app.py
```

### Linux
```
python3 weather_app.py
```

## License
This project is provided as-is for educational purposes.

## Author Notes
The Weather App demonstrates practical PyQt5 GUI development with real API integration and comprehensive error handling. It's suitable for beginners learning GUI development and API integration in Python.
