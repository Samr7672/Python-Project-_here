# Alarm Clock Application

A simple, user-friendly alarm clock application built with Python and Tkinter that allows you to set alarms for specific times.

## Features

- 🕐 **Easy Time Selection**: Dropdown menus for hours, minutes, and seconds
- ⏰ **Real-time Alarm Checking**: Continuously monitors current time against alarm time
- 🧵 **Multi-threading**: Uses threading to prevent UI freezing while alarm is active
- 🖥️ **GUI Interface**: Simple graphical user interface built with Tkinter
- 🔔 **Simple Activation**: One-click "Set Alarm" button to start the alarm

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- Standard libraries: `datetime`, `time`, `threading`

## Installation

No external packages needed! Tkinter comes with Python by default.

## Usage

1. Run the application:
```bash
python alarm_clock.py
```

2. A window will open with:
   - **Hour Dropdown**: Select hour (00-24)
   - **Minute Dropdown**: Select minute (00-60)
   - **Second Dropdown**: Select second (00-60)

3. Click the **"Set Alarm"** button to activate the alarm

4. The application will continuously check the current time

5. When the current time matches your set alarm time, the console will print:
   ```
   Time to Wake up
   ```

## How It Works

- The application creates a GUI window with time selection dropdowns
- When you click "Set Alarm", a new thread is started
- The alarm function runs in the background, checking every second if the current time matches the set time
- Once the alarm triggers, a message is printed to the console
- The application continues running and listening for the next alarm

## Window Details

- **Window Size**: 500x300 pixels
- **Title**: Alarm Clock
- **Font**: Helvetica (20pt for title, 15pt for labels)

## Notes

- The alarm only prints a message to the console; audio alert is not implemented
- Hours range from 00-24 (24-hour format)
- The application uses threading to keep the GUI responsive
- Time is checked in 1-second intervals

## Future Enhancements

- Add sound/audio alert when alarm triggers
- Add visual notification window
- Multiple alarms support
- Snooze functionality
- Ability to cancel/stop alarm
- Display current time in the window
- Save and load alarm settings

## Troubleshooting

- **Window doesn't appear**: Ensure Tkinter is installed and your display/environment supports GUI
- **Console not showing alarm message**: Check console output or redirect stderr/stdout
- **GUI freezing**: This shouldn't happen as threading is used, but try updating Tkinter

## License

Open source - Free to use and modify.
