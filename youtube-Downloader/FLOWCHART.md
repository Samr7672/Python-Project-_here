# YouTube Video Downloader - Flowchart and Process Documentation

## 1. Application Initialization Flow

```
┌────────────────────────────────────┐
│   Program Start                    │
│   python tube.py                   │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│   Import Libraries                 │
│   - tkinter                        │
│   - StringVar from tkinter         │
│   - YouTube from pytubefix         │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│   Create Tkinter Root Window       │
│   root = tk.Tk()                   │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│   Configure Window Properties      │
│   - Geometry: 500x300              │
│   - Resizable: False               │
│   - Title: "Youtube-video-..."     │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│   Create StringVar Variable        │
│   link = StringVar()               │
│   (Stores URL input dynamically)   │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│   Create GUI Components            │
│   ├─ Label: "Paste Link Here:"     │
│   ├─ Entry: Text input field       │
│   ├─ Button: "DOWNLOAD"            │
│   └─ (Status Label - created later)│
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│   Place Components in Window       │
│   Using .place() geometry manager  │
│   Position all widgets at (x, y)   │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│   Connect Button to Function       │
│   Button command = downloader()    │
│   (Link button click to function)  │
└────────────────┬───────────────────┘
                 │
                 ▼
┌────────────────────────────────────┐
│   Start Event Loop                 │
│   root.mainloop()                  │
│   (Window becomes interactive)     │
└────────────────┬───────────────────┘
                 │
                 ▼
   Window Ready for User Input
   (Waiting for Download Click)
```

## 2. Window Configuration Process

```
┌──────────────────────────────────────┐
│   Tkinter Window Setup               │
└──────────────┬───────────────────────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
┌──────────┐ ┌─────────┐ ┌──────────┐
│Geometry  │ │Resizable│ │  Title   │
│500x300   │ │False    │ │"Youtube- │
│pixels    │ │(Fixed)  │ │downloader│
└─────┬────┘ └────┬────┘ └────┬─────┘
      │           │           │
      └───────────┼───────────┘
                  │
                  ▼
        ┌──────────────────┐
        │ Window Created & │
        │ Configured       │
        └──────────────────┘
```

## 3. GUI Layout and Component Placement

```
┌─────────────────────────────────────────────┐
│   YouTube Video Downloader Window           │
│   500 × 300 pixels                          │
├─────────────────────────────────────────────┤
│                                             │
│                                             │
│          Paste Link Here:   (y=60)         │
│          [Label - Arial 12 Bold]           │
│                                             │
│     ┌─────────────────────────────────┐    │
│     │ https://youtube.com/watch?v=..  │ (y=100)
│     │ [Entry Field - 50 chars wide]   │    │
│     └─────────────────────────────────┘    │
│                                             │
│                                             │
│     ┌──────────────────────────┐   (y=150)│
│     │     DOWNLOAD             │           │
│     │ [Button - Pale Violet]   │           │
│     └──────────────────────────┘           │
│                                             │
│                                             │
│      DOWNLOADED! ✅  or  ERROR!  (y=210)   │
│      [Status Label - Green or Red]         │
│                                             │
│                                             │
└─────────────────────────────────────────────┘

COORDINATE SYSTEM (x, y):
- Origin (0,0) at top-left
- x: horizontal position (left=0, right=500)
- y: vertical position (top=0, bottom=300)
```

## 4. User Interaction Flow - Download Button Click

```
┌──────────────────────────────────────┐
│   User Clicks "DOWNLOAD" Button      │
└──────────────┬───────────────────────┘
               │
               ▼
    ┌──────────────────────────┐
    │ Tkinter Event Triggered  │
    │ Button.clicked signal    │
    └──────────────┬───────────┘
                   │
                   ▼
    ┌──────────────────────────┐
    │ Call downloader()        │
    │ Function Executed        │
    └──────────────┬───────────┘
                   │
                   ▼
              Enter try block
                   │
                   ▼
    (See Detailed Download Flow)
```

## 5. Detailed Download Process - downloader() Function

```
┌────────────────────────────────────────┐
│   downloader() Function Called         │
└────────────────┬──────────────────────┘
                 │
                 ▼
    ┌──────────────────────────────┐
    │   try:                       │
    │   (Begin error handling)     │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────────┐
    │ 1. GET URL FROM INPUT FIELD      │
    │                                  │
    │ url_text = link.get()            │
    │                                  │
    │ Retrieves StringVar value        │
    │ from Entry widget                │
    │                                  │
    │ Example Result:                  │
    │ "https://www.youtube.com/..."    │
    └──────────────┬───────────────────┘
                   │
                   ▼
    ┌──────────────────────────────────┐
    │ 2. CREATE YOUTUBE OBJECT         │
    │                                  │
    │ yt = YouTube(url_text)           │
    │                                  │
    │ pytubefix creates YouTube object │
    │ Connects to YouTube              │
    │ Fetches video metadata:          │
    │ - Video title                    │
    │ - Available streams              │
    │ - Duration                       │
    │ - Channel name                   │
    │ - Thumbnail                      │
    │ - Other info                     │
    │                                  │
    │ Time: 1-5 seconds (network I/O)  │
    └──────────────┬───────────────────┘
                   │
                   ▼
    ┌──────────────────────────────────┐
    │ 3. SELECT HIGHEST RESOLUTION     │
    │                                  │
    │ video = yt.streams.             │
    │   get_highest_resolution()      │
    │                                  │
    │ Selects best quality stream:     │
    │ Examines all available streams   │
    │ Chooses highest resolution       │
    │                                  │
    │ Possible Values:                 │
    │ - 1080p                          │
    │ - 720p                           │
    │ - 480p                           │
    │ - 360p                           │
    │ - 240p                           │
    │ (depends on video availability)  │
    │                                  │
    │ Time: <1 second (local)          │
    └──────────────┬───────────────────┘
                   │
                   ▼
    ┌──────────────────────────────────┐
    │ 4. DOWNLOAD VIDEO FILE           │
    │                                  │
    │ video.download()                 │
    │                                  │
    │ Initiates download:              │
    │ - Connects to YouTube server     │
    │ - Streams video data             │
    │ - Writes to disk                 │
    │ - Saves in current directory     │
    │                                  │
    │ Filename Format:                 │
    │ "[Video Title].mp4"              │
    │                                  │
    │ Time: Depends on:                │
    │ - Video length                   │
    │ - Internet speed                 │
    │ - Server speed                   │
    │ - File size                      │
    │ Typical: 30 sec - 30 min         │
    └──────────────┬───────────────────┘
                   │
                   ▼
    ┌──────────────────────────────────┐
    │ 5. DISPLAY SUCCESS MESSAGE       │
    │                                  │
    │ tk.Label(                        │
    │   root,                          │
    │   text="DOWNLOADED! ✅",         │
    │   font='arial 15',               │
    │   fg="green"                     │
    │ ).place(x=160, y=210)            │
    │                                  │
    │ Creates new label on window      │
    │ Shows green success message      │
    │ Placed in lower section          │
    └──────────────┬───────────────────┘
                   │
                   ▼
    ┌──────────────────────────────────┐
    │ Download Complete!               │
    │ User sees: DOWNLOADED! ✅        │
    └──────────────────────────────────┘
```

## 6. Error Handling Flow

```
┌──────────────────────────────────────┐
│   Exception Occurs During Download   │
│   (Invalid URL, Network Error, etc)  │
└──────────────┬───────────────────────┘
               │
               ▼
    ┌──────────────────────────────┐
    │ except Exception as e:       │
    │ (Catch any exception)        │
    └──────────────┬───────────────┘
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
    ┌────────────┐    ┌─────────────────┐
    │ Display    │    │ Print Exception │
    │ Error GUI  │    │ to Console      │
    │ Message    │    │ print(e)        │
    └────┬───────┘    └────────┬────────┘
         │                     │
         ▼                     │
    tk.Label(              Debug Output
      root,                │
      text="ERROR!",       │
      font='arial 15',     │
      fg="red"             │
    ).place(x=200, y=210)  │
         │                 │
         ▼                 ▼
    ┌──────────────────────────────┐
    │ User sees: ERROR!            │
    │ Exception details in console │
    └──────────────────────────────┘
```

## 7. Complete User Journey Timeline

```
TIME  EVENT                              ACTION
────────────────────────────────────────────────────────────

T0    User Launches Application         
      python tube.py                    
      
T1    Window Appears                    
      "Youtube-video-downloader" window 
      with input field and button        
      
T2    User Copies YouTube Link          
      Navigates to YouTube              
      Finds video to download           
      Copies URL from address bar       
      
T3    User Pastes Link                  
      Clicks in text field              
      Pastes link (Ctrl+V)              
      Example: https://youtube.com/...  
      
T4    User Clicks Download Button       
      Button click registered           
      downloader() function called      
      
T5    Fetch YouTube Metadata            
      YouTube(url) created              
      Connection to YouTube             
      Video information retrieved       
      Wait: 1-5 seconds                 
      
T6    Select Resolution                 
      All streams examined              
      Highest resolution selected       
      (e.g., 720p, 1080p)               
      
T7    Download Video                    
      Download begins                   
      File written to disk              
      Wait: 30 sec - 30+ minutes        
      (depends on video length)         
      
T8    Success/Error Status              
      Display appropriate message       
      Green "DOWNLOADED! ✅"            
      OR Red "ERROR!"                   
      
T9    User Can Download Again           
      Application ready for next URL    
      OR User closes window             
```

## 8. Data Flow - From Input to Download

```
┌─────────────────────────────┐
│   User Input                │
│   Pastes YouTube Link       │
│   "https://youtube.com/..." │
└──────────────┬──────────────┘
               │
               ▼
    ┌──────────────────────────┐
    │ StringVar: link          │
    │ Stores URL in memory     │
    └──────────────┬───────────┘
                   │
                   ▼
    ┌──────────────────────────┐
    │ link.get()               │
    │ Retrieve from StringVar  │
    │ → url_text               │
    └──────────────┬───────────┘
                   │
                   ▼
    ┌──────────────────────────┐
    │ YouTube(url_text)        │
    │ Create YouTube object    │
    │ → yt                     │
    │ Fetches metadata         │
    └──────────────┬───────────┘
                   │
                   ▼
    ┌──────────────────────────┐
    │ yt.streams               │
    │ All available streams    │
    │ Properties:              │
    │ - resolution             │
    │ - fps                    │
    │ - filesize               │
    │ - mime_type              │
    └──────────────┬───────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ get_highest_resolution()     │
    │ Filter and select best       │
    │ → video                      │
    │ Selected stream object       │
    └──────────────┬───────────────┘
                   │
                   ▼
    ┌──────────────────────────────┐
    │ video.download()             │
    │ Initiate download            │
    │ Stream to disk               │
    │ → File saved                 │
    │ Location: Current directory  │
    │ Filename: "[Video Title].mp4"│
    └──────────────────────────────┘
```

## 9. GUI Component Lifecycle

```
COMPONENT 1: ROOT WINDOW
────────────────────────
Created: At program start
Modified: Never
Destroyed: When user closes window
Lifecycle: Program start → Program end

COMPONENT 2: LABEL (Instructions)
──────────────────────────────────
Text: "Paste Link Here:"
Created: At startup
Modified: Never
Destroyed: When window closes
Status: Static (read-only)

COMPONENT 3: ENTRY FIELD
────────────────────────
Created: At startup
Modified: Every time user types
Contents: StringVar(link)
Destroyed: When window closes
Purpose: Receives YouTube URL input

COMPONENT 4: BUTTON
──────────────────
Text: "DOWNLOAD"
Created: At startup
Modified: Never
Command: downloader() function
Destroyed: When window closes
Interaction: Click to trigger download

COMPONENT 5: STATUS LABEL
─────────────────────────
Text: "DOWNLOADED! ✅" or "ERROR!"
Created: Dynamically during download (after button click)
Color: Green for success, Red for error
Destroyed: On next button click (new label created)
Note: Each download attempt creates NEW label
      (Previous labels not removed, but covered by new one)
```

## 10. Stream Selection Logic

```
AVAILABLE STREAMS FOR A TYPICAL VIDEO:
──────────────────────────────────────

Stream List from yt.streams:
│
├─ Stream 1: 1080p, 30fps, MP4, 500MB
├─ Stream 2: 720p, 30fps, MP4, 250MB
├─ Stream 3: 480p, 30fps, MP4, 100MB
├─ Stream 4: 360p, 30fps, MP4, 50MB
├─ Stream 5: 240p, 30fps, MP4, 25MB
├─ Stream 6: Audio only, 128kbps, MP3
└─ (More combinations possible)

RESOLUTION PRIORITY:
────────────────────
The get_highest_resolution() method:

Step 1: Examine all streams
        │
Step 2: Filter to video-only streams
        (Remove audio-only)
        │
Step 3: Find highest resolution
        (Compare pixel dimensions)
        │
Step 4: Select and return stream
        Example: 1080p stream selected
        │
        ▼
   SELECTED: 1080p 30fps MP4 (500MB)
```

## 11. Exception Handling Decision Tree

```
                    Exception Occurs
                           │
                ┌──────────┴──────────┐
                │                     │
                ▼                     ▼
        ┌──────────────┐    ┌─────────────────┐
        │ InvalidURL?  │    │ NetworkError?   │
        │              │    │                 │
        │ - Malformed  │    │ - No internet   │
        │ - Not YouTube│    │ - Timeout       │
        └───┬──────────┘    │ - Server down   │
            │               └────────┬────────┘
            │                        │
            ├─────────┬──────────────┤
            │         │              │
            ▼         ▼              ▼
        ┌─────────────────────────────────┐
        │ except Exception as e:          │
        │ (Catch-all for any exception)   │
        └─────────────┬───────────────────┘
                      │
            ┌─────────┴──────────┐
            │                    │
            ▼                    ▼
        GUI: ERROR!          Console: print(e)
        (Red text)           (Exception details)
            │                    │
            └──────────┬─────────┘
                       │
                       ▼
            User sees error feedback
            Can try different URL
```

## 12. File System Operations

```
DOWNLOAD LOCATION:
──────────────────
Default: Current Working Directory
         (where Python script is run from)

Example Paths:
├─ Windows: C:\Users\username\Downloads\
├─ macOS:   /Users/username/Downloads/
└─ Linux:   /home/username/Downloads/

ACTUAL SAVED FILE:
───────────────────
Filename: [Video Title].mp4
Example:  "How to Learn Python - Full Course.mp4"

File Properties:
├─ Format: MP4 (video/audio combined)
├─ Resolution: As selected (highest available)
├─ Size: Varies (10MB - 1000MB+)
├─ Duration: Same as YouTube video
└─ Playable by: Most media players

DIRECTORY CONTENT AFTER DOWNLOAD:
──────────────────────────────────
Before:
├─ tube.py
├─ README.md
└─ FLOWCHART.md

After (single download):
├─ tube.py
├─ README.md
├─ FLOWCHART.md
└─ How to Learn Python - Full Course.mp4

After (multiple downloads):
├─ tube.py
├─ README.md
├─ FLOWCHART.md
├─ How to Learn Python - Full Course.mp4
├─ Python Tutorial for Beginners.mp4
├─ Advanced Python Programming.mp4
└─ ... (more video files)
```

## 13. Widget Positioning (Place Geometry Manager)

```
WINDOW COORDINATE SPACE:
─────────────────────────

   0                  250                 500 (x-axis)
0  ┌──────────────────────────────────────┐
   │                                      │
   │                                      │
60 │    "Paste Link Here:"                │
   │                                      │
   │  ┌────────────────────────────────┐  │
100│  │ https://youtube.com/...        │  │
   │  └────────────────────────────────┘  │
   │                                      │
150│        ┌──────────────────┐          │
   │        │   DOWNLOAD       │          │
   │        └──────────────────┘          │
   │                                      │
210│    DOWNLOADED! ✅ or ERROR!          │
   │                                      │
   │                                      │
300└──────────────────────────────────────┘

COMPONENT POSITIONS:
────────────────────
Label "Paste Link Here":
  x=160 (center-ish), y=60

Entry Field:
  x=90 (left of center), y=100
  width=50 characters

Button "DOWNLOAD":
  x=180 (near center), y=150

Status Label:
  x=160 or x=200 (depends on message), y=210
```

## 14. Time and Performance Analysis

```
TYPICAL DOWNLOAD TIMELINE:
──────────────────────────

Action                      Time        Notes
─────────────────────────────────────────────────────
User clicks button          0 ms        Instant

YouTube() object creation   1-5 sec     Network I/O
Metadata fetching           │           Connecting to YouTube
                           │           Fetching video info

Stream selection            <1 sec      Local processing
get_highest_resolution()    │           Examining available streams

Download initiation         <1 sec      Start streaming
Connection to YouTube       │           Begin download

Video Download              Varies      Depends on:
video.download()            30s-30m     - Video length
                           │           - File size
                           │           - Internet speed
                           │           - YouTube server speed

Display success message     <1 sec      Update GUI
Status label creation       │           Show DOWNLOADED! ✅

TOTAL TIME:                 ~32s-31m    Dominated by download time


TYPICAL FILE SIZES:
────────────────────────
Video Length    Quality    File Size
10 minutes      480p       30-50 MB
10 minutes      720p       60-100 MB
10 minutes      1080p      100-200 MB
60 minutes      480p       150-250 MB
60 minutes      720p       300-600 MB
60 minutes      1080p      500-1000 MB+


NETWORK SPEED vs DOWNLOAD TIME:
────────────────────────────────
Internet Speed    100 MB file    500 MB file
5 Mbps           160 seconds     800 seconds
10 Mbps          80 seconds      400 seconds
25 Mbps          32 seconds      160 seconds
50 Mbps          16 seconds      80 seconds
100 Mbps         8 seconds       40 seconds
```

## 15. Library Dependency Flow

```
APPLICATION DEPENDS ON:
───────────────────────

┌─ tkinter (Built-in)
│  ├─ tk.Tk()
│  ├─ tk.Label()
│  ├─ tk.Entry()
│  ├─ tk.Button()
│  ├─ StringVar()
│  └─ mainloop()
│
└─ pytubefix (Third-party)
   └─ YouTube()
      ├─ YouTube.__init__()
      ├─ .streams (Stream object)
      │  └─ .get_highest_resolution()
      └─ .download()

IMPORT RESOLUTION:
──────────────────

import tkinter as tk
   │
   ├─ tkinter module location
   ├─ (Usually: Python\Lib\tkinter\)
   │
   ├─ If successful: Continue
   └─ If fails: GUI cannot start


from pytubefix import YouTube
   │
   ├─ pytubefix package location
   ├─ (Usually: Python\Lib\site-packages\pytubefix\)
   │
   ├─ If successful: Can download videos
   └─ If fails: ERROR - "ModuleNotFoundError"
      Solution: pip install pytubefix


FALLBACK (Commented Code):
──────────────────────────
#from pytube import YouTube
   │
   └─ If pytubefix unavailable:
      1. Uncomment this line
      2. Comment out pytubefix import
      3. Install pytube: pip install pytube
      4. Works similarly to pytubefix
```

## 16. Event Handling and Signal Flow

```
USER INTERACTION → EVENT → HANDLER → ACTION
──────────────────────────────────────────

SCENARIO 1: Button Click
────────────────────────
User clicks Download button
         │
         ▼
tkinter detects click event
         │
         ▼
Button emits "clicked" signal
         │
         ▼
Calls connected command: downloader()
         │
         ▼
downloader() function executes
         │
         ▼
Download process begins


SCENARIO 2: User Types in Entry Field
──────────────────────────────────────
User types character
         │
         ▼
tkinter detects key event
         │
         ▼
Character added to Entry widget
         │
         ▼
StringVar(link) automatically updates
         │
         ▼
Text appears in input field


SCENARIO 3: Window Close
────────────────────────
User clicks X button
         │
         ▼
tkinter detects close event
         │
         ▼
root.mainloop() terminates
         │
         ▼
Program execution ends
         │
         ▼
All widgets destroyed
Window closes
```

## 17. StringVar and Data Binding

```
STRINGVAR PURPOSE:
──────────────────

StringVar acts as bridge between GUI and Python code:

┌──────────────────────────────────┐
│ StringVar: link                  │
│ (Holds string value in memory)   │
└──────────────┬───────────────────┘
               │
        ┌──────┴──────┐
        │             │
        ▼             ▼
    Entry Widget   downloader()
    Input field    Function
        │             │
        ├─ Write ─ Read ──┤
        │             │
    User types      link.get()
    "https://..."   returns value

BINDING MECHANISM:
──────────────────
When Entry created:
tk.Entry(root, textvariable=link)
     │
     └─ Entry widget BOUND to StringVar(link)

Result:
- User types in Entry
- Value automatically stored in link
- downloader() accesses via link.get()
- No manual data transfer needed


DATA FLOW:
──────────
User Types:    "https://youtube.com/watch?v=abc123"
         │
         ▼
   Entry Widget
         │
         ▼
   StringVar: link
   (Internal storage)
         │
         ▼
   link.get()
   Returns: "https://youtube.com/watch?v=abc123"
         │
         ▼
   url_text variable
         │
         ▼
   Passed to YouTube()
```

## 18. Error Messages and Debugging

```
ERROR SCENARIOS AND MESSAGES:
──────────────────────────────

SCENARIO 1: Invalid YouTube URL
──────────────────────────────
User Input: "https://example.com"
            │
            ▼
YouTube(url) constructor fails
            │
            ▼
Raises Exception: 
  "pytube.exceptions.RegexMatchError"
            │
            ▼
except Exception as e: catches it
            │
            ├─ GUI shows: "ERROR!"
            └─ Console prints: Exception details

USER SEES: Red "ERROR!" label
DEVELOPER SEES: Exception trace in console


SCENARIO 2: Video Not Available
────────────────────────────────
User Input: Private/Deleted video URL
            │
            ▼
YouTube() successfully created
            │
            ▼
yt.streams accesses video
            │
            ▼
Raises Exception:
  "pytube.exceptions.VideoUnavailable"
            │
            ▼
except catches it
            │
            ├─ GUI shows: "ERROR!"
            └─ Console prints: Exception details

USER SEES: Red "ERROR!" label
DEVELOPER SEES: "VideoUnavailable" message


SCENARIO 3: Network/Connection Error
──────────────────────────────────────
Internet disconnected
            │
            ▼
YouTube() tries to connect
            │
            ▼
Raises Exception:
  "ConnectionError" or "TimeoutError"
            │
            ▼
except catches it
            │
            ├─ GUI shows: "ERROR!"
            └─ Console prints: Exception details

USER SEES: Red "ERROR!" label
DEVELOPER SEES: Connection error trace


DEBUGGING WITH CONSOLE OUTPUT:
───────────────────────────────
When ERROR! displayed:
1. Check Python console/terminal
2. Look for exception message: print(e)
3. Message tells what went wrong
4. Examples:
   - "Invalid URL format"
   - "No internet connection"
   - "Video is private"
   - "HTTP Error 403"
5. Use message to troubleshoot
```

## 19. Resolution and Stream Hierarchy

```
VIDEO STREAMS AVAILABLE ON YOUTUBE:
────────────────────────────────────

All Possible Streams:
│
├─ Video + Audio Combined (Progressive)
│  ├─ 1080p 60fps 
│  ├─ 1080p 30fps ← Highest Resolution
│  ├─ 720p 60fps
│  ├─ 720p 30fps
│  ├─ 480p 30fps
│  ├─ 360p 30fps
│  └─ 240p 30fps
│
├─ Video Only (no audio)
│  ├─ 1080p 60fps
│  ├─ 1080p 30fps
│  ├─ 720p 60fps
│  └─ (more)
│
└─ Audio Only (no video)
   ├─ 128kbps MP3
   ├─ 192kbps MP4
   └─ (more)

get_highest_resolution() SELECTION:
───────────────────────────────────

Step 1: Filter to progressive streams (video+audio)
        Removes video-only and audio-only
        Result: Combined streams only

Step 2: Compare resolutions
        1080p > 720p > 480p > 360p > 240p

Step 3: Select highest
        Returns: 1080p 30fps (most typical)

Step 4: Return stream object
        Ready for download()

EXAMPLE FOR TYPICAL VIDEO:
───────────────────────────
If 1080p available:  Select 1080p
If 1080p unavailable but 720p available: Select 720p
If only 480p available: Select 480p
(Uses best available quality)
```

## 20. Complete Program State Diagram

```
STATE 1: INITIALIZATION
─────────────────────────
Program starts
Libraries imported
Window created
Components initialized
Status: READY

STATE 2: WAITING
────────────────
Window displayed
Waiting for user input
Application idle
Status: WAITING_FOR_USER

STATE 3: RECEIVING INPUT
──────────────────────────
User types URL
Text appears in entry field
StringVar updates
Status: URL_RECEIVED

STATE 4: DOWNLOAD_PROCESSING
──────────────────────────────
User clicks DOWNLOAD button
downloader() executes
YouTube object created
Streams selected
Download in progress
Status: DOWNLOADING

STATE 5: SUCCESS
────────────────
Download complete
Status label created: "DOWNLOADED! ✅"
Color: Green
Status: SUCCESS_DISPLAYED

STATE 6: ERROR
───────────────
Exception occurred
Status label created: "ERROR!"
Color: Red
Status: ERROR_DISPLAYED

STATE 7: READY_FOR_NEXT
────────────────────────
User can click DOWNLOAD again
OR enter new URL
OR close application
Status: READY

STATE 8: TERMINATED
─────────────────────
User closes window
mainloop() stops
Program ends
Status: CLOSED
```

## Summary

The YouTube Video Downloader Flowchart documentation provides comprehensive coverage of:

1. **Application Initialization**: Window setup and component creation
2. **GUI Layout**: Component positioning and widget hierarchy
3. **User Interaction**: Click events and input handling
4. **Download Process**: URL retrieval, stream selection, file download
5. **Error Handling**: Exception catching and user feedback
6. **Data Flow**: From URL input to downloaded file
7. **Stream Selection Logic**: How highest resolution is chosen
8. **File Operations**: Where and how videos are saved
9. **Event Handling**: Signal flow from user actions
10. **Performance Metrics**: Timing and file size information
11. **Library Integration**: Dependency management for tkinter and pytubefix
12. **State Management**: Application states throughout lifecycle

The implementation demonstrates GUI programming with Tkinter, external library integration, event handling, and error management in Python.
