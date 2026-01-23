# Screen Recorder

A Python application that captures your screen and records it as a video file. Records continuous screen activity at 30 FPS and saves it as an MP4 video file.

## Features

- 📹 **Full Screen Recording**: Captures entire screen in real-time
- 🎬 **Video Output**: Saves recording as MP4 video file
- ⏱️ **Fixed Duration**: Records for a specified duration (default: 10 seconds)
- 🖥️ **System Resolution**: Automatically detects and uses your screen resolution
- 🎥 **30 FPS Playback**: Records at 30 frames per second for smooth video
- 🎞️ **Frame Processing**: Converts frames from RGB to BGR format for OpenCV compatibility
- 💾 **File Management**: Automatically saves as MP4 with XVID codec

## Requirements

- Python 3.x
- `opencv-python` (cv2) - Video processing and writing
- `pyautogui` - Screenshot capture
- `pywin32` - Windows API access for screen dimensions
- `numpy` - Array operations

## Installation

1. Install required packages:
```bash
pip install opencv-python pyautogui pywin32 numpy
```

Or install them individually:
```bash
pip install opencv-python
pip install pyautogui
pip install pywin32
pip install numpy
```

2. (Optional) Post-installation for pywin32:
```bash
python -m pip install --upgrade pywin32
```

## Usage

1. Run the recorder:
```bash
python screenrecorder.py
```

2. Upon execution:
   - Screen dimensions are detected automatically
   - Video writer is initialized
   - "Recording started..." message appears
   - Recording begins immediately for 10 seconds

3. Wait for recording to complete:
```
Recording started...
(10 seconds pass)
Recording finished and saved as test.mp4
```

4. Find your video:
   - Default output: `test.mp4` in the same directory

## How It Works

### Step-by-step Process

1. **Get Screen Dimensions**: Uses Windows API to get monitor resolution
2. **Initialize Video Writer**: Sets up MP4 codec (XVID) with detected resolution
3. **Set Duration**: Records for 10 seconds (adjustable in code)
4. **Capture Loop**: 
   - Takes screenshot
   - Converts color format (RGB → BGR)
   - Writes frame to video file
5. **Time Check**: Stops when duration is reached
6. **Finalize**: Releases video file and closes

## Configuration

### Change Recording Duration

Modify the `duration` variable:
```python
duration = 10  # Change to desired seconds (e.g., 30, 60)
```

### Change Output Filename

Modify the output parameter:
```python
output = cv2.VideoWriter("test.mp4", fourcc, 30.0, dimension)
                                    # Change "test.mp4" to desired name
```

### Change Frame Rate

Modify the FPS parameter:
```python
output = cv2.VideoWriter("test.mp4", fourcc, 30.0, dimension)
                                              # 30.0 = FPS (try 24, 25, 60)
```

### Change Codec

Use different video codec:
```python
# XVID (default)
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Alternative codecs:
fourcc = cv2.VideoWriter_fourcc(*"MP4V")  # MP4 codec
fourcc = cv2.VideoWriter_fourcc(*"MJPG")  # Motion JPEG
fourcc = cv2.VideoWriter_fourcc(*"WMV1")  # Windows Media
```

## Video Specifications

| Parameter | Value |
|-----------|-------|
| **Codec** | XVID (mpeg-4 part 2) |
| **Frame Rate** | 30 FPS |
| **Resolution** | Your screen resolution |
| **Format** | MP4 |
| **Duration** | 10 seconds (default) |
| **Color Space** | BGR (OpenCV standard) |

## Screen Dimensions

The program automatically detects:
- **Width**: Your monitor's horizontal resolution (pixels)
- **Height**: Your monitor's vertical resolution (pixels)
- **Dimension Tuple**: (width, height)

Example for 1920×1080 monitor:
```
width = 1920
height = 1080
dimension = (1920, 1080)
```

## Frame Processing Pipeline

1. **Screenshot**: `pyautogui.screenshot()` - Captures as RGB
2. **NumPy Array**: Converts to numpy array for processing
3. **Color Conversion**: `cv2.cvtColor(RGB → BGR)` - OpenCV expects BGR
4. **Frame Write**: Writes processed frame to video file
5. **Repeat**: 30 times per second until duration ends

## Recording Process

```
Start
  ↓
Detect screen size
  ↓
Initialize video codec (XVID)
  ↓
Set 30 FPS and resolution
  ↓
Calculate end time (now + 10 seconds)
  ↓
Begin recording loop
  ├─ Capture screenshot
  ├─ Convert RGB to BGR
  ├─ Write frame to video
  ├─ Check if time exceeded
  └─ Repeat until time ends
  ↓
Release video file
  ↓
Save as test.mp4
```

## Example Output

### Console Output
```
Recording started...
Recording finished and saved as test.mp4
```

### Generated File
- **Filename**: `test.mp4`
- **Duration**: 10 seconds
- **Size**: ~5-10 MB (depends on screen activity)
- **Location**: Same directory as the script
- **Playable**: All major media players (VLC, Windows Media Player, etc.)

## Performance Considerations

### CPU Usage
- Recording uses significant CPU (screen capture + encoding)
- At 30 FPS, expect 15-30% CPU usage on modern systems

### File Size
- Screen recording generates large files
- ~10 seconds at 1920×1080 = 5-15 MB
- Larger at higher resolutions

### Memory
- Uses minimal RAM (frame-by-frame processing)
- Most heavy lifting done by OpenCV/codec

## Troubleshooting

- **Black screen recording**: Ensure no other applications are blocking access
- **No audio**: This recorder only captures video, not audio
- **File not created**: Check write permissions in the directory
- **ModuleNotFoundError**: Ensure all packages are installed (`pip install` command)
- **Video won't play**: Try different codec or use VLC player
- **Poor video quality**: Increase duration or adjust codec settings
- **Very large file**: Normal for screen recording; compression helps

## Tips & Best Practices

✅ **Do this:**
- Close unnecessary background processes for better performance
- Clear clutter from desktop before recording
- Use shorter durations for testing
- Test playback before relying on recording

❌ **Don't do this:**
- Run resource-intensive applications during recording
- Record for very long durations (causes very large files)
- Expect audio capture (use separate audio recorder)
- Move windows rapidly (causes video codec strain)

## Advanced Customization

### Record for 60 Seconds
```python
duration = 60
```

### Record at 60 FPS
```python
output = cv2.VideoWriter("test.mp4", fourcc, 60.0, dimension)
```

### Custom Filename with Timestamp
```python
from datetime import datetime
filename = f"recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
output = cv2.VideoWriter(filename, fourcc, 30.0, dimension)
```

### Add Before/After Time Tracking
```python
print(f"Recording for {duration} seconds...")
start_time = time.time()
duration = 30
end_time = start_time + duration
# ... recording loop ...
elapsed = time.time() - start_time
print(f"Recording complete. Duration: {elapsed:.2f} seconds")
```

## Video Codec Comparison

| Codec | Size | Quality | Compatibility |
|-------|------|---------|---|
| XVID | Medium | High | Very Good |
| MP4V | Small | High | Excellent |
| MJPG | Large | Medium | Good |
| WMV1 | Medium | Medium | Windows Only |

## Supported Color Spaces

The program converts:
- **Input**: RGB (from pyautogui)
- **Output**: BGR (OpenCV standard)
- **Why**: OpenCV expects BGR format for video encoding

## File Size Estimation

```
File Size ≈ (Width × Height × FPS × Duration × Bits_Per_Pixel) / 8 / 1,000,000

Example for 1920×1080, 30 FPS, 10 seconds:
≈ (1920 × 1080 × 30 × 10 × 24) / 8 / 1,000,000
≈ 18.6 MB (uncompressed)
≈ 5-10 MB (compressed with XVID)
```

## Future Enhancements

- Add audio recording capability
- Implement pause/resume functionality
- Create GUI for easy control
- Add region-specific recording (crop area)
- Implement real-time FPS display
- Add watermark/timestamp overlay
- Create batch recording for multiple videos
- Add mouse cursor highlighting
- Implement quality/bitrate selection
- Add automatic video compression

## Learning Concepts

This project teaches:
- **Video Processing**: Using OpenCV for video creation
- **Screen Capture**: Using pyautogui for screenshot
- **System API**: Using Windows API for screen dimensions
- **Image Processing**: Color space conversion (RGB to BGR)
- **File I/O**: Writing video files
- **Time Management**: Duration-based loops
- **NumPy Arrays**: Working with image data
- **Codec Selection**: Understanding video compression

## License

Open source - Free to use and modify for personal use.
