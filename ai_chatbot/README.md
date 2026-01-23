# AI Chatbot (Peter)

A voice-activated AI assistant that responds to voice commands using speech recognition and text-to-speech technology.

## Features

- 🎤 **Speech Recognition**: Converts spoken words to text using Google's speech recognition API
- 🔊 **Text-to-Speech**: Responds with synthesized audio output
- 🌐 **Web Browser Integration**: Opens YouTube and GitHub
- ⏰ **Time Information**: Provides current system time
- 😂 **Joke Telling**: Generates and speaks random jokes
- 🎵 **Music Player**: Plays songs from your local music folder
- ⚙️ **Customizable**: Easy to modify voice, speed, and commands

## Requirements

- Python 3.x
- `pyttsx3` - Text-to-speech conversion
- `SpeechRecognition` - Speech recognition using Google API
- `pyjokes` - Joke generator
- Microphone for audio input
- Internet connection (for Google speech recognition)

## Installation

1. Install required packages:
```bash
pip install pyttsx3 SpeechRecognition pyjokes
```

2. Ensure you have a microphone connected to your system.

## Usage

1. Run the chatbot:
```bash
python chatbot1.py
```

2. Activate the assistant by saying: **"Hey Peter"**

3. Give voice commands:
   - **"What's your name?"** → Responds with name
   - **"How old are you?"** → Responds with age
   - **"What's the time now?"** → Tells current time
   - **"Open YouTube"** → Opens YouTube in browser
   - **"Open webpage"** → Opens GitHub in browser
   - **"Tell me a joke"** → Tells a random joke
   - **"Play song"** → Plays first song from Music folder
   - **"Exit"** → Closes the assistant

## Configuration

### Change Voice Gender
Modify the voice in `speechtx()` function:
- `voices[0].id` = Male voice
- `voices[1].id` = Female voice (default)

### Change Speaking Speed
Adjust the rate parameter (default: 150):
```python
engine.setProperty('rate', 150)  # Increase for faster, decrease for slower
```

### Change Music Path
Update the path in the "play song" command:
```python
path = r"C:\Users\YOUR_USERNAME\Music"
```

## How It Works

1. **Initialization**: Listens for activation phrase "Hey Peter"
2. **Command Recognition**: Continuously listens for voice commands
3. **Processing**: Matches spoken input against predefined commands
4. **Response**: Executes corresponding action and provides audio feedback
5. **Loop**: Waits 5 seconds before listening for the next command
6. **Exit**: Closes when user says "Exit"

## Troubleshooting

- **"Not Understanding" message**: Speak clearly and closer to the microphone
- **No sound output**: Check your system volume and speaker settings
- **Google API errors**: Ensure internet connection is active
- **Microphone not detected**: Check microphone is properly connected and selected as default input device

## Future Enhancements

- Add weather information
- Integrate with online APIs for news, stocks, etc.
- Improve NLP for better command recognition
- Add user name customization
- Support for multiple languages
- Calendar integration

## License

This project is open source and available for personal use.
