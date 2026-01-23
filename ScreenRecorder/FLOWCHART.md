# Screen Recorder - Flowchart

## Main Application Flow

```
                        START
                          |
                          v
        Import Required Libraries
        ├─ cv2 (OpenCV)
        ├─ pyautogui (screenshot)
        ├─ win32api (Windows API)
        ├─ numpy (array operations)
        └─ time (duration tracking)
                          |
                          v
        Get Screen Dimensions
        width = win32api.GetSystemMetrics(0)
        height = win32api.GetSystemMetrics(1)
        dimension = (width, height)
                          |
                          v
        Initialize Video Codec
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
                          |
                          v
        Create VideoWriter Object
        output = cv2.VideoWriter(
            "test.mp4",
            fourcc,
            30.0,          # 30 FPS
            dimension      # Screen resolution
        )
                          |
                          v
        Set Recording Duration
        start_time = time.time()
        duration = 10 seconds
        end_time = start_time + duration
                          |
                          v
        Print Status Message
        "Recording started..."
                          |
                          v
        ┌─────────────────────────────┐
        │    RECORDING LOOP           │
        │    while True:              │
        └─────────────────────────────┘
                          |
                          v
        Capture Screenshot
        image = pyautogui.screenshot()
                          |
                          v
        Convert to NumPy Array
        frame_1 = np.array(image)
                          |
                          v
        Convert Color Space
        RGB to BGR
        frame = cv2.cvtColor(frame_1,
                COLOR_RGB2BGR)
                          |
                          v
        Write Frame to Video
        output.write(frame)
                          |
                          v
        Check Duration
        current_time = time.time()
        if current_time > end_time:
                  /            \
                Yes            No
                 |              |
                 v              v
            BREAK           Continue Loop
            Loop         (capture next frame)
                 |              |
                 |______________|
                          |
                          v
        Release Video File
        output.release()
                          |
                          v
        Print Completion Message
        "Recording finished and
         saved as test.mp4"
                          |
                          v
                        END
         (test.mp4 file created)
```

## Screen Dimension Detection

```
START: Get Screen Size
     |
     v
USE Windows API
  win32api.GetSystemMetrics()
     |
     |___________getSystemMetrics(0)
     |           └─→ Returns screen width
     |
     |___________getSystemMetrics(1)
               └─→ Returns screen height
     |
     v
EXAMPLE (1920×1080):
width = 1920
height = 1080
dimension = (1920, 1080)
     |
     v
Ready for video initialization
```

## Video Writer Initialization

```
Step 1: Define Codec
  fourcc = cv2.VideoWriter_fourcc(*"XVID")
                |
                v
           Codec value created
           for MPEG-4 Part 2
                |
Step 2: Create VideoWriter
  cv2.VideoWriter(
    filename = "test.mp4",
    fourcc = codec,
    fps = 30.0,
    frameSize = (width, height)
  )
                |
                v
           VideoWriter initialized
           and ready to receive frames
                |
Step 3: Object Created
  stored in variable "output"
```

## Frame Capture & Processing Pipeline

```
┌──────────────────────────────────────┐
│    EACH FRAME (30 times per second)   │
└──────────────────────────────────────┘
            |
Step 1: Screenshot
            |
      pyautogui.screenshot()
            |
            v
      Returns PIL Image
      (RGB color space)
            |
Step 2: Convert to NumPy Array
            |
      np.array(image)
            |
            v
      3D array: (height, width, 3)
      RGB values
            |
Step 3: Color Space Conversion
            |
      cv2.cvtColor(RGB → BGR)
            |
            v
      OpenCV-compatible format
      (BGR is standard for cv2)
            |
Step 4: Write to Video
            |
      output.write(frame)
            |
            v
      Frame encoded and
      written to MP4 file
            |
Step 5: Return to Loop
      (repeat 30 times/second)
```

## Time Tracking & Duration Control

```
Initialize Time
     |
start_time = time.time()
     |
     v
Current time stored
     |
Set Duration
     |
duration = 10
     |
     v
Calculate End Time
     |
end_time = start_time + duration
end_time = current + 10 seconds
     |
     v
Enter Recording Loop
     |
     |───────────────────────────┐
     |                           |
     v                           v
Frame Captured            Check Time
     |                           |
     |                    current_time =
     |                    time.time()
     |                           |
     |                    Is time > end?
     |                      /        \
     |                    YES        NO
     |                     |          |
     |    ________________|          |
     |   |                 v         |
     |   |              BREAK       v
     |   |              LOOP    Continue
     |   |               |       Loop
     |   |______________|_________|
     |                    |
     v                    v
Release Video      Loop back to
  &                Frame Capture
 Save             (repeat)
```

## Color Space Conversion

```
Input Frame (RGB):
    R G B
    R G B
    R G B
    
Each pixel has 3 values:
- Red channel
- Green channel
- Blue channel

    |
    v

cv2.cvtColor(frame, COLOR_RGB2BGR)
    
    |
    v

Output Frame (BGR):
    B G R
    B G R
    B G R
    
Each pixel rearranged:
- Blue channel (first)
- Green channel (second)
- Red channel (third)

Why? OpenCV expects BGR format
for video encoding and processing
```

## Complete Recording Session

```
TIME: 0s
    ↓
START recording
    ├─ Screen: 1920×1080
    ├─ Codec: XVID
    ├─ FPS: 30
    └─ Duration: 10 seconds

TIME: 0-3.33s (100 frames)
    ├─ Capture frame 1
    ├─ Capture frame 2
    ├─ ...
    └─ Capture frame 100

TIME: 3.33-6.66s (100 frames)
    ├─ Capture frame 101
    ├─ ...
    └─ Capture frame 200

TIME: 6.66-10s (100+ frames)
    ├─ Capture frame 201
    ├─ ...
    └─ Capture frame ~300

TIME: 10s
    ↓
TIME EXCEEDED (current_time > end_time)
    ↓
BREAK loop
    ↓
Release video file
    ↓
Save test.mp4 (~5-10 MB)
    ↓
END
```

## Loop Execution Detail

```
LOOP ITERATION (happens every ~33ms for 30 FPS)

┌────────────────────────────────┐
│  Start of iteration            │
└────────────────────────────────┘
            |
            v
┌────────────────────────────────┐
│  Take screenshot               │
│  (captures current screen)     │
└────────────────────────────────┘
            |
            v
┌────────────────────────────────┐
│  Convert to array              │
│  (image → numpy array)         │
└────────────────────────────────┘
            |
            v
┌────────────────────────────────┐
│  Convert color (RGB to BGR)    │
│  (rearrange color channels)    │
└────────────────────────────────┘
            |
            v
┌────────────────────────────────┐
│  Write to video file           │
│  (encode and save frame)       │
└────────────────────────────────┘
            |
            v
┌────────────────────────────────┐
│  Get current time              │
│  Compare with end time         │
└────────────────────────────────┘
            |
     _______|_______
    |               |
    v               v
Time Not Yet      Time Exceeded
Reached           (10+ seconds)
    |               |
    v               v
Continue          Break Loop
Loop              
    |               |
    v               v
Next Frame      End Recording
(~33ms later)       |
                    v
                Release/Save
```

## Data Flow Diagram

```
┌─────────────────────────────────────┐
│    Windows Screen (pixels)          │
│    (1920×1080 pixels)               │
└─────────────────────────────────────┘
            |
            v (pyautogui.screenshot)
┌─────────────────────────────────────┐
│    PIL Image (RGB format)           │
│    Red-Green-Blue channels          │
└─────────────────────────────────────┘
            |
            v (np.array)
┌─────────────────────────────────────┐
│    NumPy Array (height×width×3)     │
│    RGB values in memory             │
└─────────────────────────────────────┘
            |
            v (cv2.cvtColor)
┌─────────────────────────────────────┐
│    NumPy Array (BGR format)         │
│    Blue-Green-Red channels          │
└─────────────────────────────────────┘
            |
            v (output.write)
┌─────────────────────────────────────┐
│    MP4 Video File (on disk)         │
│    Encoded with XVID codec          │
└─────────────────────────────────────┘
```

## Resource Usage During Recording

```
CPU Usage
    ├─ Screenshot capture: 5-10%
    ├─ Color conversion: 2-5%
    ├─ Video encoding: 8-15%
    └─ Total: 15-30%

Memory Usage
    ├─ Frame buffer: ~25 MB
    ├─ Video writer: ~10 MB
    └─ Total: ~50 MB

Disk Write Speed
    ├─ 1920×1080, 30 FPS
    ├─ ~1.5-2 MB/second
    └─ Requires fast storage

File Growth Over Time
    ├─ 10 seconds: 5-10 MB
    ├─ 60 seconds: 30-60 MB
    ├─ 5 minutes: 150-300 MB
    └─ 1 hour: 1.8-3.6 GB
```

## Frame Rate Processing

```
At 30 FPS target:

Time    Frame #    Action
─────────────────────────
0 ms      1      Screenshot & write
33 ms     2      Screenshot & write
66 ms     3      Screenshot & write
99 ms     4      Screenshot & write
132 ms    5      Screenshot & write
...
10000 ms  ~300   Last frame
10000 ms  END    Stop recording

Each iteration takes ~33 milliseconds
(1000 ms ÷ 30 FPS = 33.33 ms)
```

## Video Output Creation

```
┌──────────────────────────────────┐
│  Collected Video Frames          │
│  (300 frames for 10 sec @ 30fps) │
└──────────────────────────────────┘
            |
            v
┌──────────────────────────────────┐
│  Video Codec Encoding            │
│  (XVID compression)              │
└──────────────────────────────────┘
            |
            v
┌──────────────────────────────────┐
│  Container Format Wrapping       │
│  (MP4 container)                 │
└──────────────────────────────────┘
            |
            v
┌──────────────────────────────────┐
│  File Writing to Disk            │
│  Location: Current directory     │
│  Filename: test.mp4              │
└──────────────────────────────────┘
            |
            v
┌──────────────────────────────────┐
│  FINAL OUTPUT: test.mp4          │
│  (5-10 MB video file)            │
│  Playable in any media player    │
└──────────────────────────────────┘
```

## Configuration Modification Flow

```
Want to change duration?
    |
    v
Modify: duration = 10
        duration = 60 (for 60 seconds)
    |
    v
Want to change FPS?
    |
    v
Modify: output = cv2.VideoWriter(
            "test.mp4", fourcc, 30.0, dimension)
                                      ↑
                              Change 30.0 to 60.0 for 60 FPS
    |
    v
Want to change filename?
    |
    v
Modify: "test.mp4"
        "my_recording.mp4"
    |
    v
Want to change codec?
    |
    v
Modify: fourcc = cv2.VideoWriter_fourcc(*"XVID")
        fourcc = cv2.VideoWriter_fourcc(*"MP4V")
```

## Error & Success Path

```
                    START
                      |
                      v
            Initialize Recording
                 /        \
               OK         ERROR
               |           |
               v           v
        Begin Loop     ModuleNotFoundError
               |        (missing library)
               |           |
               v           v
        Record Video    Installation Error
               |           |
               v           v
        Check Time     Fix with:
               |        pip install cv2...
               |           |
               v           v
        Time OK?      Retry
        /       \           |
      NO       YES          |
       |        |    _______|
       |        v   |
       |      BREAK  v
       |      LOOP  Success
       |        |    |
       v        v    v
    Continue  Release/Save
     Loop     Video
       |        |
       |______|
              |
              v
            END
```
