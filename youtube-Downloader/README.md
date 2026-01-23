# YouTube Video Downloader

## Overview
YouTube Video Downloader is a simple, user-friendly Python desktop application built with Tkinter that allows users to download YouTube videos in the highest available resolution. The application provides a clean GUI interface where users can paste a YouTube video link and download the video to their local machine.

## Features
- **User-Friendly GUI**: Simple Tkinter-based graphical interface
- **Highest Resolution Download**: Automatically selects and downloads videos in the highest available resolution
- **URL Input**: Easy link entry field for YouTube video URLs
- **Download Button**: Single-click download functionality
- **Status Feedback**: Visual feedback indicating successful download or errors
- **Error Handling**: Catches and displays download errors with exception messages
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Lightweight**: Minimal dependencies and fast execution
- **Window Customization**: Fixed window size and title for consistent experience

## Requirements
- Python 3.x
- tkinter (usually comes with Python)
- pytubefix (or pytube)

## Installation

1. **Clone or download the project**:
   ```
   cd youtube-Downloader
   ```

2. **Install required packages**:
   ```
   pip install pytubefix
   ```
   
   Alternative (if pytubefix unavailable):
   ```
   pip install pytube
   ```

3. **Run the application**:
   ```
   python tube.py
   ```

## Usage

### Step-by-Step Guide

1. **Launch the Application**:
   ```bash
   python tube.py
   ```

2. **Copy YouTube Video Link**:
   - Go to YouTube.com
   - Find the video you want to download
   - Copy the video URL (the full link from the address bar)
   - Example: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

3. **Paste Link in Application**:
   - Click in the text input field
   - Paste the YouTube link (Ctrl+V or Cmd+V)

4. **Click Download Button**:
   - Click the "DOWNLOAD" button
   - The application will:
     - Fetch video information
     - Select the highest resolution stream
     - Download the video to your current directory

5. **Check Download Status**:
   - **Success**: Green "DOWNLOADED! ✅" message appears
   - **Error**: Red "ERROR!" message appears (check console for details)

### Examples

#### Example 1: Standard YouTube Video
```
Input URL: https://www.youtube.com/watch?v=jNQXAC9IVRw
Output: Downloaded to current directory as MP4 file
Status: DOWNLOADED! ✅
```

#### Example 2: Long YouTube Video
```
Input URL: https://www.youtube.com/watch?v=long_video_id
Note: May take several minutes depending on video length and internet speed
Status: DOWNLOADED! ✅ (when complete)
```

#### Example 3: Invalid URL
```
Input URL: https://example.com (not a YouTube link)
Output: ERROR! (console shows exception details)
```

## User Interface

### Window Properties
- **Title**: "Youtube-video-downloader"
- **Size**: 500x300 pixels
- **Resizable**: No (fixed size)
- **Theme**: Light default

### GUI Components

#### 1. Label: Title
- **Text**: "Paste Link Here:"
- **Font**: Arial, 12pt, Bold
- **Position**: Upper section of window

#### 2. Entry Field: Link Input
- **Type**: Text input field (Entry widget)
- **Width**: 50 characters
- **Placeholder**: Accepts YouTube URLs
- **Binding**: Connected to StringVar variable `link`

#### 3. Button: Download
- **Text**: "DOWNLOAD"
- **Font**: Arial, 15pt, Bold
- **Color**: Pale violet red background
- **Function**: Triggers downloader() function
- **Position**: Center of window

#### 4. Status Label: Download Feedback
- **Success Message**: "DOWNLOADED! ✅" (green text, 15pt)
- **Error Message**: "ERROR!" (red text, 15pt)
- **Position**: Lower section of window
- **Behavior**: Displays after download attempt

## How It Works

### Video Download Process

1. **User Input**: User pastes YouTube video URL into text field

2. **URL Retrieval**: 
   ```python
   url_text = link.get()
   ```
   Extracts the URL from the input field

3. **YouTube Object Creation**:
   ```python
   yt = YouTube(url_text)
   ```
   Creates a YouTube object that fetches video metadata

4. **Stream Selection**:
   ```python
   video = yt.streams.get_highest_resolution()
   ```
   Selects the stream with highest available resolution
   - Typical: 1080p, 720p, 480p, 360p, etc.
   - Resolution depends on what's available for that video

5. **Download Execution**:
   ```python
   video.download()
   ```
   Downloads the video file to current working directory

6. **Status Display**: Shows success/error message

### File Download Location
Videos are downloaded to the **current working directory** (where the script is run from).

**To change download location**, modify the download() call:
```python
video.download('path/to/your/folder')
```

Example:
```python
video.download('C:\\Downloads\\')  # Windows
video.download('/Users/username/Downloads/')  # macOS
video.download('/home/username/Downloads/')  # Linux
```

## Supported YouTube Link Formats

### Valid Formats
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://m.youtube.com/watch?v=VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID`

### Invalid Formats
- Playlist URLs (will download only first video)
- Channel URLs
- Non-YouTube URLs
- Malformed or broken links

## Error Handling

### Common Errors and Solutions

#### 1. Invalid URL Error
```
ERROR!
Exception: [exception details in console]
```
**Cause**: URL is not a valid YouTube link
**Solution**:
- Verify the URL is correct
- Copy full URL from address bar
- Check for typos

#### 2. Video Not Available
```
ERROR!
```
**Cause**: Video is private, deleted, or restricted
**Solution**:
- Check if video is publicly available
- Verify you have access to the video
- Try a different video

#### 3. pytubefix Import Error
```
ModuleNotFoundError: No module named 'pytubefix'
```
**Solution**:
```bash
pip install pytubefix
```

#### 4. No Streams Available
```
ERROR!
```
**Cause**: Video has no downloadable streams
**Solution**:
- Try a different video
- Update pytubefix: `pip install --upgrade pytubefix`

#### 5. Permission Denied
```
ERROR!
```
**Cause**: No write permission to current directory
**Solution**:
- Run application from a directory you have write access to
- Change download directory in code

#### 6. Network Timeout
```
ERROR!
```
**Cause**: Slow internet connection or YouTube server issues
**Solution**:
- Check internet connection
- Try again later
- Try a shorter video first

## Code Structure

### Main Components

#### 1. Window Setup
```python
root = tk.Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("Youtube-video-downloader")
```
Creates and configures the main Tkinter window

#### 2. Variable Definition
```python
link = StringVar()
```
StringVar to store the URL input dynamically

#### 3. GUI Elements
- **Label**: Instructions for user
- **Entry**: Text input field for URL
- **Button**: Download trigger
- **Label**: Status feedback

#### 4. Main Function: downloader()
```python
def downloader():
    try:
        url_text = link.get()
        yt = YouTube(url_text)
        video = yt.streams.get_highest_resolution()
        video.download()
        tk.Label(root, text="DOWNLOADED! ✅", ...).place(x=160, y=210)
    except Exception as e:
        tk.Label(root, text="ERROR!", ...).place(x=200, y=210)
        print(e)
```

Handles the complete download workflow

#### 5. Event Loop
```python
root.mainloop()
```
Keeps the window open and responsive

## Pytubefix vs Pytube

### Pytubefix (Recommended)
- **Pros**: 
  - More actively maintained
  - Better compatibility with current YouTube
  - Fixes bugs in original pytube
  - More reliable stream extraction
- **Cons**: None significant
- **Installation**: `pip install pytubefix`

### Pytube (Original)
- **Pros**: 
  - Original library
  - Large community
- **Cons**:
  - Less frequently updated
  - May have compatibility issues with current YouTube
  - Stream extraction may fail
- **Installation**: `pip install pytube`

## Advanced Configuration

### Custom Download Path
Edit the download line in the downloader() function:

```python
# Instead of:
video.download()

# Use:
video.download('/path/to/downloads/')
```

### Filter by Resolution
Instead of highest resolution, select specific resolution:

```python
# Get 720p video
video = yt.streams.filter(resolution='720p').first()

# Get 1080p video
video = yt.streams.filter(resolution='1080p').first()

# Get 480p video
video = yt.streams.filter(resolution='480p').first()
```

### Download Audio Only
```python
audio = yt.streams.filter(only_audio=True).first()
audio.download()
```

### Custom Filename
```python
stream = yt.streams.get_highest_resolution()
stream.download(filename='my_custom_name.mp4')
```

### Get Video Information
```python
yt = YouTube(url_text)
print(yt.title)          # Video title
print(yt.length)         # Duration in seconds
print(yt.author)         # Channel name
print(yt.streams)        # All available streams
```

## Performance Characteristics

### Resource Usage
- **Memory**: ~50-200 MB (depends on video size)
- **CPU**: Low during download (I/O bound)
- **Disk Space**: Required = Video file size

### Download Speed
Depends on:
- Internet connection speed
- Video file size
- YouTube server response time
- Video quality/resolution

### Typical Times
- Fetching metadata: 1-5 seconds
- Downloading 10-minute video: 30 seconds - 5 minutes
- Downloading 1-hour video: 5-30 minutes

## Limitations

### Current Limitations
1. **Single Video Only**: Downloads one video at a time
2. **No Playlist Support**: Cannot batch download playlists
3. **Fixed Download Location**: Default is current directory
4. **No Quality Selection**: Always uses highest available
5. **No Progress Bar**: No visual download progress indicator
6. **Basic Error Display**: Limited error information in GUI
7. **No Resume**: Interrupted downloads cannot be resumed
8. **Single Threading**: Application freezes during download

### YouTube Restrictions
1. **Copyright**: Cannot download copyrighted content in some regions
2. **Geo-blocking**: Some videos restricted by region
3. **Age-restricted**: May not work with age-restricted videos
4. **Private Videos**: Cannot download private or unlisted videos
5. **Terms of Service**: Downloading may violate YouTube ToS in some jurisdictions

## Learning Concepts

### 1. GUI Programming with Tkinter
- Widget creation and layout
- Event handling with buttons
- Label updates and dynamic content
- StringVar for variable binding

### 2. External Library Integration
- Importing third-party libraries
- Using library functions and methods
- Handling library-specific exceptions

### 3. Error Handling
- Try-except blocks
- Exception catching
- User feedback on errors

### 4. URL and Web Interaction
- Working with URLs
- HTTP-based library operations
- Video stream selection

### 5. File Operations
- File downloads
- Directory management
- File naming

## Security Considerations

### Safe Usage
1. **Only download videos you have permission to download**
2. **Respect copyright and intellectual property rights**
3. **Check local laws** regarding video downloads
4. **Use from trusted sources** - don't modify code from untrusted sources

### Risks
1. **Copyright Infringement**: Downloading copyrighted content may be illegal
2. **YouTube ToS Violation**: May violate YouTube's terms of service
3. **Malware Risk**: Modified versions could contain malware

## Future Enhancements

- Add progress bar for download status
- Implement playlist download capability
- Add quality selection dropdown
- Implement custom download path selection
- Add pause/resume functionality
- Implement background download threading
- Add download queue management
- Implement video conversion (MP4, MP3)
- Add metadata tagging for downloaded files
- Create download history log
- Add subtitle download capability
- Implement better error messages in GUI

## Use Cases

### 1. Educational Content
Download educational videos for offline study and reference

### 2. Content Creation
Download videos for analysis, remix, or reference in content creation

### 3. Offline Viewing
Download videos to watch later without internet connection

### 4. Personal Archive
Keep personal favorite videos as backup

### 5. Accessibility
Download videos for accessibility purposes (with subtitles, etc.)

## Dependencies Summary
| Package | Version | Purpose |
|---|---|---|
| tkinter | Built-in | GUI framework |
| pytubefix | Latest | YouTube video downloading |

## Running on Different Platforms

### Windows
```
python tube.py
```
Download location: Current directory (usually where tube.py is located)

### macOS
```
python3 tube.py
```
Download location: Current directory

### Linux
```
python3 tube.py
```
Download location: Current directory

## Tips and Best Practices

### 1. File Organization
- Create a dedicated downloads folder
- Modify code to download to specific folder
- Organize downloaded videos by date or category

### 2. Connection Optimization
- Use stable internet connection
- Download during off-peak hours for faster speeds
- Avoid other bandwidth-intensive activities during download

### 3. Error Prevention
- Always use complete YouTube URLs
- Test with short videos first
- Keep pytubefix updated: `pip install --upgrade pytubefix`

### 4. Efficient Workflow
- Copy YouTube URLs directly from address bar
- Use keyboard shortcuts (Ctrl+C to copy, Ctrl+V to paste)
- Keep application window visible to monitor progress

## Troubleshooting

### Application Won't Start
**Problem**: Window doesn't appear
**Solutions**:
- Check Python installation: `python --version`
- Verify tkinter available: `python -m tkinter`
- Check for syntax errors in code

### Downloads Keep Failing
**Problem**: Always shows ERROR! message
**Solutions**:
- Update pytubefix: `pip install --upgrade pytubefix`
- Check internet connection
- Try a different YouTube video
- Check YouTube URL format

### Files Downloaded to Wrong Location
**Problem**: Can't find downloaded videos
**Solutions**:
- Check current working directory
- Search system for video file
- Modify code to specify download path explicitly

## License
This project is provided for educational purposes.

## Disclaimer
This tool is provided as-is for educational and personal use. Users are responsible for ensuring their usage complies with YouTube's Terms of Service and applicable laws. The author is not responsible for misuse or legal issues arising from the use of this tool.

## Author Notes
YouTube Video Downloader demonstrates practical GUI programming with Python, external library integration, and error handling. It's a useful tool for downloading videos while showcasing beginner-to-intermediate Python concepts including Tkinter, file I/O, and exception handling.
