# Speech to Text Converter - Flowchart

## Main Program Flow

```
                        START
                          |
                          v
        Import Libraries
        ├─ pyttsx3 (text-to-speech)
        ├─ speech_recognition (speech-to-text)
        ├─ webbrowser (browser control)
        └─ datetime (date/time)
                          |
                          v
        Define sptext() function
                          |
                          v
        Call sptext()
                          |
                          v
        ┌─────────────────────────────┐
        │  SPEECH RECOGNITION PROCESS │
        └─────────────────────────────┘
                          |
                          v
                        END
```

## sptext() Function Flow

```
              sptext() Called
                    |
                    v
        Create Recognizer object
        recognizer = sr.Recognizer()
                    |
                    v
        Open Microphone as context
        with sr.Microphone() as source:
                    |
                    v
        Print status message
        "Listening to your Voice....."
                    |
                    v
    ┌──────────────────────────────┐
    │  AUDIO CAPTURE PHASE         │
    └──────────────────────────────┘
                    |
                    v
        Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)
        (analyzes noise level)
                    |
                    v
        Listen for audio input
        audio = recognizer.listen(source)
        (records until silence detected)
                    |
                    v
    ┌──────────────────────────────┐
    │  RECOGNITION PHASE           │
    └──────────────────────────────┘
                    |
                    v
        Print processing message
        "Recognizing your voice...."
                    |
                    v
        Try to recognize speech
        data = recognizer.recognize_google(audio)
                    |
        __________|__________
       |                    |
       v                    v
    SUCCESS              ERROR
    (Recognized)      (Not recognized)
       |                    |
       v                    v
    Print result       Catch exception
    print(data)        (sr.UnknownValueError)
       |                    |
       v                    v
    Display         Print error message
    recognized      "I Don't Understand..."
    text                   |
       |                    |
       |____________________|
                    |
                    v
        Microphone context ends
        (connection closed)
                    |
                    v
        Return from function
                    |
                    v
                  END
```

## Audio Processing Pipeline

```
┌────────────────────────────┐
│   AUDIO INPUT (Microphone) │
└────────────────────────────┘
            |
            v
┌────────────────────────────┐
│  NOISE ANALYSIS            │
│  (adjust_for_ambient_noise)│
└────────────────────────────┘
            |
            v
    Detect background noise level
    Establish baseline threshold
            |
            v
┌────────────────────────────┐
│   AUDIO RECORDING          │
│   (listen)                 │
└────────────────────────────┘
            |
            v
    Record audio until:
    - Silence detected
    - Timeout reached
    - User stops speaking
            |
            v
┌────────────────────────────┐
│   AUDIO BUFFER CREATED     │
│   (audio object)           │
└────────────────────────────┘
            |
            v
┌────────────────────────────┐
│   SEND TO GOOGLE API       │
│   (recognize_google)       │
└────────────────────────────┘
            |
            v
    Convert audio to:
    - WAV format
    - Compress if needed
    - Send over internet
            |
            v
┌────────────────────────────┐
│   GOOGLE SERVERS           │
│   (speech recognition)     │
└────────────────────────────┘
            |
            v
    Process audio
    Match against language models
    Generate text output
            |
            v
┌────────────────────────────┐
│   RESPONSE RECEIVED        │
│   (text string)            │
└────────────────────────────┘
            |
            v
┌────────────────────────────┐
│   DISPLAY RESULT           │
│   (print to console)       │
└────────────────────────────┘
```

## Noise Adjustment Process

```
    Microphone connected
            |
            v
    adjust_for_ambient_noise()
            |
            v
    Listen for 1 second
    (default duration)
            |
            v
    Measure noise level
    (energy threshold)
            |
            v
    Store as baseline
            |
            v
    Ready for speech capture
    (will ignore noise below baseline)
            |
            v
    Listen for voice
    (only records above threshold)
```

## Error Handling Flow

```
        Call recognize_google()
                |
                v
        Try to recognize
        audio data
                |
        _______|_______
       |               |
       v               v
    SUCCESS         ERROR
    (Speech          (Cannot
    recognized)       recognize)
       |               |
       v               v
    Return        Check exception
    recognized     type
    text              |
       |              v
       |          UnknownValueError?
       |          (speech too unclear)
       |              |
       |          YES → Print error
       |              "I Don't
       |               Understand..."
       |              |
       |          RequestError?
       |          (API error)
       |              |
       |          YES → Print API error
       |              "Could not
       |               request..."
       |              |
       |______________|
                |
                v
        Continue execution
```

## Microphone Access Flow

```
        ┌──────────────────────────┐
        │  with sr.Microphone() as │
        │  source:                 │
        └──────────────────────────┘
                    |
                    v
        Open microphone device
        (access system default)
                    |
                    v
    Microphone is available
    and ready for use
                    |
                    v
    Execute indented code block
    (sptext() operations)
                    |
                    v
        All operations complete
                    |
                    v
    Automatically close microphone
    (context manager closes)
                    |
                    v
        Microphone released
        (ready for other apps)
```

## Complete Execution Trace

```
START PROGRAM
    |
    v
Import all libraries
    |
    v
Define sptext() function
    |
    v
Call: sptext()
    |
    v
├─ Create recognizer object
    |
    v
├─ Open microphone
    | Print: "Listening to your Voice....."
    |
    v
├─ Analyze noise
    | (silent moment to measure ambient noise)
    |
    v
├─ Listen for speech
    | (user speaks here)
    | (records until silence)
    |
    v
├─ Print: "Recognizing your voice...."
    |
    v
├─ Send audio to Google API
    | (internet request)
    | (server processes)
    | (receives response)
    |
    v
├─ Check if speech recognized
    |
 ___|___ 
|       |
v       v
YES    NO (UnknownValueError)
|      |
v      v
Print Print
text  "I Don't
      Understand..."
|      |
|______|
    |
    v
Close microphone
    |
    v
Return from function
    |
    v
PROGRAM END
```

## Network Communication

```
            Local Machine
    ┌──────────────────────────┐
    │                          │
    │  Audio File              │
    │  (recorded from mic)     │
    │                          │
    │  recognizer.recognize_   │
    │  google(audio)           │
    └──────────┬───────────────┘
               |
               | HTTP Request
               | (over internet)
               v
    ┌──────────────────────────┐
    │    GOOGLE SERVERS        │
    │                          │
    │ ┌────────────────────┐   │
    │ │ Speech Recognition │   │
    │ │ Engine             │   │
    │ └────────────────────┘   │
    │         |                │
    │         v                │
    │ Process audio            │
    │ Generate text            │
    └──────────┬───────────────┘
               |
               | HTTP Response
               | (JSON with text)
               v
    ┌──────────────────────────┐
    │    Local Machine         │
    │                          │
    │  data = recognized text  │
    │  print(data)             │
    │                          │
    └──────────────────────────┘
```

## Status Messages Timeline

```
TIME: 0s
    ├─ Program starts
    └─ sptext() called

TIME: 0-1s
    ├─ "Listening to your Voice....."
    └─ Adjusting for noise

TIME: 1-3s
    ├─ Waiting for user to speak
    └─ Recording audio

TIME: 3s
    ├─ User stops speaking
    └─ Silence detected

TIME: 3-1s
    ├─ "Recognizing your voice...."
    └─ Sending to Google API

TIME: 4-6s
    ├─ API processing
    └─ Waiting for response

TIME: 6s
    ├─ Response received
    └─ Parse result

TIME: 6s+
    ├─ EITHER:
    ├─ Print: [Recognized text]
    └─ OR:
       Print: "I Don't Understand..."
```

## Recognition Result Flow

```
        Audio sent to Google
                |
                v
        Server processes
        Uses language models
        Generates confidence scores
                |
                v
        Did recognition succeed?
            /              \
          YES              NO
           |                |
           v                v
    Return text       Raise exception:
    (high confidence) UnknownValueError
           |                |
           v                v
    Python receives     Python receives
    recognized text     exception
           |                |
           v                v
    Assign to 'data'   Catch exception
           |                |
           v                v
    Print text         Print error
    "Hello world"      "I Don't
                        Understand..."
           |                |
           |________________|
                |
                v
        Function returns
```

## Language Support Configuration

```
        Default: English (US)
        recognizer.recognize_google(audio)
                |
                v
        To use different language:
        recognizer.recognize_google(
            audio,
            language='es-ES'  # Spanish
        )
                |
        _______|_______
       |               |
       v               v
    English        Spanish
    (en-US)        (es-ES)
       |               |
       |   French      |
       |   (fr-FR)     |
       |   German      |
       |   (de-DE)     |
       |   Japanese    |
       |   (ja-JP)     |
       |   Chinese     |
       |   (zh-CN)     |
       |   ... and more
       |               |
       |_______________|
              |
              v
    Recognized in selected language
```

## Resource Management

```
        START
        |
        v
    Allocate microphone
    Allocate audio buffer
    Allocate network connection
        |
        v
    EXECUTE SPEECH RECOGNITION
        |
        v
    Release audio buffer
    Release microphone
    Close network connection
        |
        v
        END

    (Automatic via context manager)
```

## Data Transformation

```
┌──────────────────────┐
│   SPEECH (Audio)     │
│  (WAV/PCM format)    │
└──────────────────────┘
            |
            v
┌──────────────────────┐
│   ENCODED AUDIO      │
│   (sent to Google)   │
└──────────────────────┘
            |
            v
   GOOGLE API PROCESSING
            |
            v
┌──────────────────────┐
│   RECOGNIZED TEXT    │
│   (string in Python) │
└──────────────────────┘
            |
            v
┌──────────────────────┐
│   CONSOLE OUTPUT     │
│   (printed to user)  │
└──────────────────────┘
```

## Exception Handling Details

```
        recognize_google() called
                |
        _______|_______
       |               |
       v               v
    SUCCESS         EXCEPTION
       |                |
       v                v
    Return string   What type?
       |                |
       v          _______|_______
                 |                |
                 v                v
           UnknownValue        RequestError
           ValueError           (API error)
                |                |
                v                v
           Cannot          Network issue
           understand       or API problem
           speech               |
                |               v
                v           Handle API error
            Handle and      (show error
            show error      message)
            message             |
                |               v
                |______________|
                       |
                       v
              Continue execution
```

## Timing Sequence Diagram

```
User speaks:    "Hello world"
                |
        ____|____
       |        |
       v        v
    0.5s      1.5s
    Start     End
             |
             v
    Duration: 1 second of speech
             |
             v
    Audio file created
    (1 second duration)
             |
             v
    Sent to Google API
    (upload time: 0.5-2s)
             |
             v
    Google processes
    (processing time: 1-3s)
             |
             v
    Response received
    Contains: "hello world"
             |
             v
    Display: "hello world"
    (instant)
```

## Complete System Architecture

```
┌─────────────────────────────────────────┐
│         LOCAL SYSTEM                    │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Python Program (speech_to_text) │   │
│  │  ├─ Recognizer object           │   │
│  │  ├─ Microphone access           │   │
│  │  └─ Audio buffer                │   │
│  └────────────┬────────────────────┘   │
│               │                         │
│  ┌────────────v────────────────────┐   │
│  │ Audio Input Device              │   │
│  │ (Microphone)                    │   │
│  └────────────┬────────────────────┘   │
│               │                         │
│  ┌────────────v────────────────────┐   │
│  │ Network Connection              │   │
│  │ (Internet)                      │   │
│  └────────────┬────────────────────┘   │
│               │                         │
└───────────────┼─────────────────────────┘
                │
                | Audio (HTTP)
                v
    ┌─────────────────────────────────┐
    │   CLOUD (Google Servers)        │
    │   ├─ Speech Recognition Engine  │
    │   ├─ Language Models            │
    │   └─ API Response               │
    └─────────────────────────────────┘
                |
                | Text (HTTP Response)
                v
┌─────────────────────────────────────────┐
│         LOCAL SYSTEM                    │
├─────────────────────────────────────────┤
│  ┌─────────────────────────────────┐   │
│  │ Python Program                  │   │
│  │ ├─ Receives text response       │   │
│  │ ├─ Print to console             │   │
│  │ └─ Display to user              │   │
│  └─────────────────────────────────┘   │
│               │                         │
│  ┌────────────v────────────────────┐   │
│  │ Console Output                  │   │
│  │ (recognized text)               │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```
