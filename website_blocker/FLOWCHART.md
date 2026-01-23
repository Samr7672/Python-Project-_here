# Website Blocker - Flowchart and Process Documentation

## 1. Application Startup Flow

```
┌──────────────────────────────────────┐
│   Program Start                      │
│   python website_blocker.py          │
└──────────────┬───────────────────────┘
               │
               ▼
┌──────────────────────────────────────┐
│   Import Libraries                   │
│   - time                             │
│   - datetime                         │
│   - os                               │
│   - sys                              │
└──────────────┬───────────────────────┘
               │
               ▼
┌──────────────────────────────────────┐
│   Define Configuration               │
│   - website_to_block list            │
│   - Linux_host path                  │
│   - Window_host path                 │
│   - redirect IP (127.0.0.1)         │
└──────────────┬───────────────────────┘
               │
               ▼
        ┌──────────────┐
        │ Detect OS    │
        └──────┬───────┘
               │
        ┌──────┴──────┐
        │             │
        ▼             ▼
    ┌────────┐   ┌──────────┐
    │ posix? │   │   nt?    │
    │(Linux/ │   │(Windows) │
    │ macOS) │   │          │
    └───┬────┘   └────┬─────┘
        │             │
        ▼             ▼
    Use          Use
    /etc/hosts   C:\Windows\
                 System32\...
        │             │
        └──────┬──────┘
               │
               ▼
    ┌──────────────────────┐
    │ Set default_hoster   │
    │ to appropriate path  │
    └──────────┬───────────┘
               │
        ┌──────┴──────┐
        │             │
      YES           NO
        │             │
        ▼             ▼
   Continue    Print Error
   Running     "OS Unknown"
        │      Exit Program
        └──────┬──────┘
               │
               ▼
    ┌──────────────────────┐
    │ if __name__ == "__main__" │
    └──────────┬───────────────┘
               │
               ▼
    ┌──────────────────────┐
    │ Call block_website()  │
    │ with time parameters │
    │ block_website(9, 21) │
    │ (9 AM to 9 PM)      │
    └──────────┬───────────┘
               │
               ▼
    ┌──────────────────────┐
    │ Display Message:     │
    │ "Website Blocker... │
    │ (Target file: ...)" │
    │ "Press Ctrl+C..."   │
    └──────────┬───────────┘
               │
               ▼
        Enter Blocking Loop
```

## 2. OS Detection Detailed Flow

```
┌─────────────────────────────────────┐
│   Detect Operating System           │
│   Using: os.name                    │
└──────────────┬──────────────────────┘
               │
               ▼
        ┌──────────────┐
        │ Check os.name │
        └──────┬───────┘
               │
    ┌──────────┼──────────┐
    │          │          │
    ▼          ▼          ▼
┌─────────┐ ┌─────────┐ ┌──────────┐
│'posix'  │ │'nt'     │ │other     │
└────┬────┘ └────┬────┘ └────┬─────┘
     │           │           │
     ▼           ▼           ▼
┌──────────┐ ┌──────────┐ ┌─────────────┐
│Linux or  │ │Windows   │ │ Unknown OS  │
│macOS     │ │          │ │             │
└─────┬────┘ └────┬─────┘ └──────┬──────┘
      │           │              │
      ▼           ▼              ▼
 Set to      Set to         Print Error
 /etc/hosts  C:\Windows\    "OS Unknown."
             System32\      Input pause
             drivers\etc\   sys.exit()
             hosts
      │           │              │
      └──────┬────┴──────────────┘
             │
             ▼
    ┌──────────────────┐
    │ default_hoster   │
    │ is configured    │
    │ for this system  │
    └──────────────────┘
```

## 3. Main Loop Flow - block_website() Function

```
┌────────────────────────────────────┐
│ block_website(start_time, end_time) │
│ Example: block_website(9, 21)       │
└─────────────┬──────────────────────┘
              │
              ▼
┌────────────────────────────────────┐
│ Print Status Messages:              │
│ - "Website Blocker Running..."     │
│ - Display target hosts file        │
│ - "Press Ctrl+C to stop"           │
└─────────────┬──────────────────────┘
              │
              ▼
    ┌─────────────────────┐
    │  while True:        │
    │  Enter Infinite Loop│
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │   try:              │
    │ Try-except block    │
    │ for error handling  │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────────────────┐
    │ Get Current DateTime            │
    │ current_time = dt.now()         │
    │ Extract: year, month, day, hour │
    └──────────┬──────────────────────┘
               │
               ▼
    ┌────────────────────────────────┐
    │ Build Two DateTime Objects:    │
    │                                │
    │ start_datetime =               │
    │ dt(year, month, day,start_time)│
    │                                │
    │ end_datetime =                 │
    │ dt(year, month, day, end_time) │
    │                                │
    │ current = dt.now()             │
    └──────────┬─────────────────────┘
               │
               ▼
    ┌────────────────────────────────┐
    │ Compare Times:                 │
    │ start_datetime < current <     │
    │ end_datetime?                  │
    └──────────┬──────────┬──────────┘
               │          │
           TRUE │          │ FALSE
               │          │
               ▼          ▼
      ┌──────────────┐ ┌──────────────────┐
      │ WORKING HOURS│ │  FREE TIME       │
      │ Within range │ │ Outside range    │
      └──────┬───────┘ └─────────┬────────┘
             │                  │
             ▼                  ▼
      ┌──────────────┐  ┌────────────────┐
      │Print:        │  │Print:          │
      │"Working      │  │"Free time...   │
      │ hours...     │  │Unblocking..." │
      │ Blocking"    │  │                │
      └──────┬───────┘  └────────┬───────┘
             │                  │
             ▼                  ▼
      ┌──────────────────────────────┐
      │ Open hosts file (read+write) │
      │ with open(default_hoster, "r+")│
      └──────────┬───────────────────┘
                 │
          ┌──────┴──────┐
          │             │
    BLOCKING      UNBLOCKING
          │             │
          ▼             ▼
    ┌──────────┐  ┌────────────────┐
    │Add Sites │  │Read all lines  │
    │to hosts  │  │from file       │
    └─────┬────┘  └────────┬───────┘
          │                │
          ▼                ▼
    ┌──────────┐  ┌───────────────────┐
    │For each  │  │Seek to beginning  │
    │site in   │  │of file (seek(0))  │
    │blocked   │  └────────┬──────────┘
    │list:     │           │
    └─────┬────┘           ▼
          │       ┌────────────────────┐
          ▼       │For each line in    │
    ┌──────────┐  │file:               │
    │If site   │  │Check if any blocked│
    │NOT in    │  │site in this line   │
    │hosts file│  │                    │
    │yet:      │  │If NO: write line   │
    └─────┬────┘  │back to file        │
          │       └────────┬───────────┘
          ▼                │
    ┌──────────────┐       ▼
    │Write to file:│  ┌──────────────┐
    │127.0.0.1 {site}   │Truncate file │
    │                   │(remove rest) │
    └──────────┬────────┘              │
               │       └────────┬──────┘
               │                │
               └────────┬───────┘
                        │
                        ▼
              ┌──────────────────┐
              │ Close hosts file │
              │ (auto with: exit)│
              └──────────┬───────┘
                        │
                        ▼
              ┌──────────────────┐
              │ Sleep for 5 sec  │
              │ time.sleep(5)    │
              └──────────┬───────┘
                        │
                        ▼
              ┌──────────────────┐
              │ Next iteration   │
              │ Loop continues   │
              └─────────────────┘
```

## 4. Time Comparison Logic

```
┌─────────────────────────────────────┐
│ Time Comparison Step-by-Step        │
├─────────────────────────────────────┤
│ Example: block_website(9, 21)       │
│ Current Time: 14:30 (2:30 PM)       │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ 1. Get Current DateTime             │
│    now = dt.now()                   │
│    Result: 2025-01-23 14:30:45      │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ 2. Extract Date Components          │
│    year = 2025                      │
│    month = 1                        │
│    day = 23                         │
│    hour = 14 (2 PM)                 │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ 3. Create Start Time Datetime       │
│    start = dt(2025, 1, 23, 9, 0, 0)│
│    (9:00 AM today)                  │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ 4. Create End Time Datetime         │
│    end = dt(2025, 1, 23, 21, 0, 0) │
│    (9:00 PM today)                  │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ 5. Compare: start < current < end?  │
│                                     │
│    2025-01-23 09:00 <               │
│    2025-01-23 14:30 <               │
│    2025-01-23 21:00 ?               │
│                                     │
│    9 AM < 2:30 PM < 9 PM?           │
│    TRUE!                            │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│ Result: WORKING HOURS               │
│ Action: Block websites              │
└─────────────────────────────────────┘
```

## 5. Website Blocking Operation

```
┌──────────────────────────────────────┐
│ Blocking Operation - During Work Hours│
└─────────────┬────────────────────────┘
              │
              ▼
  ┌─────────────────────────┐
  │ Open hosts file:        │
  │ with open(file, "r+")   │
  │ (read + write mode)     │
  └────────────┬────────────┘
               │
               ▼
  ┌─────────────────────────┐
  │ Read entire file:       │
  │ hosts = hostfile.read() │
  │ (String of all content) │
  └────────────┬────────────┘
               │
               ▼
  ┌─────────────────────────────────┐
  │ For Each Website in Blocked List│
  │ for site in website_to_block:   │
  │                                 │
  │ Example list:                   │
  │ ["facebook.com",                │
  │  "instagram.com",               │
  │  "google.com"]                  │
  └────────────┬────────────────────┘
               │
          ┌────┴──────────────────┐
          │                       │
          ▼ First Iteration       ▼ Next
        site = "facebook.com"
          │
          ▼
  ┌──────────────────────────┐
  │ Check if site already    │
  │ in hosts file:           │
  │ if site not in hosts:    │
  │                          │
  │ Is "facebook.com" in     │
  │ the current hosts file?  │
  └────────────┬─────────────┘
               │
         ┌─────┴──────┐
         │            │
      NOT IN        IN FILE
      (Write)     (Skip)
         │            │
         ▼            │
  ┌──────────────┐    │
  │hostfile.write()    │
  │Add to file:  │    │
  │127.0.0.1    │    │
  │facebook.com  │    │
  │              │    │
  │Result:       │    │
  │127.0.0.1 facebook.com
  │              │    │
  └──────┬───────┘    │
         │            │
         └─────┬──────┘
               │
               ▼ (Next iteration)
         Check "instagram.com"
               │
         Similar process
               │
               ▼
         Check "google.com"
               │
         Similar process
               │
               ▼
  ┌──────────────────────────┐
  │ All blocking entries     │
  │ have been added to hosts │
  └──────────────────────────┘
```

## 6. Website Unblocking Operation

```
┌──────────────────────────────────────┐
│ Unblocking Operation - During Free Time│
└─────────────┬────────────────────────┘
              │
              ▼
  ┌─────────────────────────┐
  │ Open hosts file:        │
  │ with open(file, "r+")   │
  │ (read + write mode)     │
  └────────────┬────────────┘
               │
               ▼
  ┌──────────────────────────┐
  │ Read all lines:          │
  │ hosts = hostfile.readlines()
  │ Returns list of lines    │
  │ with newline chars (\n)  │
  │                          │
  │ Example:                 │
  │ ['127.0.0.1 facebook\n',│
  │  '127.0.0.1 insta\n',   │
  │  '# Comment line\n']     │
  └────────────┬─────────────┘
               │
               ▼
  ┌──────────────────────────┐
  │ Seek to start of file:   │
  │ hostfile.seek(0)         │
  │                          │
  │ Position pointer at byte │
  │ 0 (beginning)            │
  └────────────┬─────────────┘
               │
               ▼
  ┌──────────────────────────────────┐
  │ For Each Line in File:           │
  │ for host in hosts:               │
  │                                  │
  │ Check if any blocked site is     │
  │ in this line                     │
  │ if not any(site in host for      │
  │        site in website_to_block):│
  └────────────┬─────────────────────┘
               │
         ┌─────┴──────┐
         │            │
    No Blocked    Has Blocked
    Site Found    Site
         │            │
         ▼            │
  ┌──────────────┐    │
  │ Write Line   │    │
  │ Back to File │    │
  │ hostfile.write()   │
  │ (host)             │
  │                    │
  │ Line is safe,      │
  │ not a blocked site │
  │ entry              │
  │                    │
  │ Example:           │
  │ Write: "127.0.0.1 example.com\n"
  │ Write: "# Comment\n"
  │                    │
  └──────────┬─────────┘
             │
             ▼ (Line skipped)
    If line contains blocked site:
    ["facebook.com", "instagram.com"]
    
    Line: "127.0.0.1 facebook.com\n"
    → any(site in host) = TRUE
    → Line NOT written (deleted)
             │
             ▼
  ┌──────────────────────────┐
  │ Truncate File:           │
  │ hostfile.truncate()      │
  │                          │
  │ Remove anything after    │
  │ current file position    │
  │ Ensures old data removed │
  └──────────────┬───────────┘
                 │
                 ▼
  ┌──────────────────────────┐
  │ File now contains:       │
  │ - Original non-blocked   │
  │ - All comments           │
  │ - NO blocked site entries│
  │                          │
  │ Websites now accessible  │
  └──────────────────────────┘
```

## 7. Error Handling Flow

```
┌──────────────────────────────┐
│ Exception Occurs During Loop │
└──────────────┬───────────────┘
               │
        ┌──────┴──────────┐
        │                │
        ▼                ▼
    except        except
  PermissionError FileNotFoundError
        │                │
        ▼                ▼
   ┌────────┐    ┌──────────────┐
   │ User/OS│    │ Hosts file    │
   │ denies │    │ path invalid  │
   │ access │    │ or not found  │
   └───┬────┘    └────────┬──────┘
       │                  │
       ▼                  ▼
  Print Error         Print Error
  "[ERROR]            "[ERROR]
   Permission         Could not find
   Denied!"           hosts file at:"
                      (show path)
       │                  │
       ├──────────┬───────┤
       │          │       │
       ▼          ▼       ▼
    Print        Print    Print
    Instructions Solution Message
    "You must           │
     run as        ┌────┴──────┐
     Admin"        │           │
                   ▼           ▼
           except Exception:
           (Catch-all for 
            any other errors)
                   │
                   ▼
           ┌──────────────┐
           │ Print:       │
           │ "[ERROR]     │
           │ Unexpected   │
           │ error: {e}"  │
           └──────┬───────┘
                  │
                  ▼
        ┌──────────────────┐
        │ break            │
        │ (Exit while True)│
        └──────────┬───────┘
                   │
                   ▼
        ┌──────────────────┐
        │ Exit block_website()
        │ Function         │
        └──────────┬───────┘
                   │
                   ▼
        ┌──────────────────┐
        │ Print Message:   │
        │ "Program         │
        │ finished."       │
        │                  │
        │ input("Press...") │
        │ Pause window     │
        └──────────────────┘
```

## 8. Complete User Journey Timeline

```
TIME  EVENT                              ACTION
─────────────────────────────────────────────────────────────

T0    User Launches App                  
      Run: python website_blocker.py    
      (as Administrator/Sudo)           

T1    OS Detection                       Detect OS (Windows/Linux/Mac)
      
T2    Display Messages                   Show "Website Blocker Running..."
      
T3    Enter Main Loop                    Start while True loop
      
T4-8  Loop Execution (5-second intervals):

T4    Check Current Time                 Get dt.now()
      Compare with work hours            Check 9 AM - 9 PM?
      
T5    Scenario A: During Work Hours      
      (9 AM - 9 PM)                      
      - Print "Working hours..."         
      - Open hosts file                  
      - Add all blocked sites            
      - Sleep 5 seconds                  
      
T6    Scenario B: Outside Work Hours     
      (Before 9 AM, After 9 PM)          
      - Print "Free time..."             
      - Open hosts file                  
      - Remove blocked site entries      
      - Sleep 5 seconds                  
      
T7    User Presses Ctrl+C                Signal caught
      
T8    Program Catches KeyboardInterrupt  (Implicitly exits loop)
      
T9    Display "Program finished."        Print exit message
      
T10   input("Press Enter to exit...")    Pause for user
      
T11   User Presses Enter                 Window closes
      Program terminates
```

## 9. Hosts File State Transitions

```
INITIAL STATE:
──────────────
127.0.0.1 localhost
::1 localhost
# Other system entries


BEFORE BLOCKING (T: 8:00 AM - Free Time)
─────────────────────────────────────────
127.0.0.1 localhost
::1 localhost
# No blocked site entries


ENTER WORKING HOURS (T: 9:00 AM)
────────────────────────────────
Application adds entries:

127.0.0.1 localhost
::1 localhost
127.0.0.1 www.facebook.com
127.0.0.1 www.instagram.com
127.0.0.1 www.google.com
127.0.0.1 www.gmail.com
127.0.0.1 www.chrome.com


DURING WORKING HOURS (T: 9:00 AM - 9:00 PM)
─────────────────────────────────────────────
Hosts file remains with blocked entries
Every 5 seconds: Check and maintain blocked entries


EXIT WORKING HOURS (T: 9:00 PM)
───────────────────────────────
Application removes blocked entries:

127.0.0.1 localhost
::1 localhost
# Blocked entries removed


FINAL STATE (Free Time)
──────────────────────
127.0.0.1 localhost
::1 localhost
# System returned to normal


NEXT DAY AT 9:00 AM
───────────────────
Cycle repeats:
- Blocked entries added again
- Websites inaccessible
```

## 10. Website Blocking Mechanism Diagram

```
USER TRIES TO ACCESS: www.facebook.com
│
├─ Browser initiates connection
├─ System checks Hosts file FIRST
│  (before DNS resolution)
│
├─ Found in hosts file:
│  127.0.0.1 www.facebook.com
│
├─ Redirects to 127.0.0.1 (localhost)
│
├─ Browser tries to connect to localhost
│
├─ Connection fails:
│  - No web server on localhost
│  - OR server doesn't respond on port 80/443
│
└─ Browser shows error:
   "Cannot reach website"
   "Connection refused"


IF WEBSITE NOT BLOCKED:
──────────────────────
USER TRIES TO ACCESS: www.facebook.com
│
├─ Hosts file checked
├─ NOT found in hosts file
│
├─ System uses normal DNS resolution
├─ Queries DNS server
│
├─ Receives real IP address
├─ Browser connects to actual server
│
└─ Website loads normally


REDIRECT MECHANISM:
──────────────────
Hosts File Entry:    127.0.0.1 www.facebook.com
                     │         │
                     Localhost │
                     (this machine)
                                 └─ Domain being blocked

When accessed:
User → Browser → Localhost (127.0.0.1) → Connection Fails
```

## 11. Time Range Edge Cases

```
STANDARD CASE:
Start: 9 (9 AM)   End: 21 (9 PM)
───────────────────────────────────

00:00 ├─ FREE TIME
      │
06:00 ├─
      │
09:00 ├─────────── WORKING HOURS START
      │           Blocking activated
12:00 ├─
      │
18:00 ├─
      │
21:00 ├─────────── WORKING HOURS END
      │           Blocking deactivated
23:59 ├─ FREE TIME
      │


EARLY MORNING START:
Start: 5 (5 AM)    End: 17 (5 PM)
───────────────────────────────────

00:00 ├─ FREE TIME
      │
05:00 ├─────────── WORKING HOURS START
      │           Blocking activated
12:00 ├─
      │
17:00 ├─────────── WORKING HOURS END
      │           Blocking deactivated
23:59 ├─ FREE TIME
      │


LATE NIGHT WORK:
Start: 17 (5 PM)   End: 23 (11 PM)
──────────────────────────────────

00:00 ├─ FREE TIME
      │
17:00 ├─────────── WORKING HOURS START
      │           Blocking activated
20:00 ├─
      │
23:00 ├─────────── WORKING HOURS END
      │           Blocking deactivated
23:59 ├─ FREE TIME
      │


⚠️  UNSUPPORTED CASE (Midnight Crossing):
Start: 22 (10 PM)  End: 6 (6 AM NEXT DAY)
──────────────────────────────────────────

PROBLEM:
- Would need to block: 22:00-23:59 and 00:00-06:00
- Current logic: 22 < current_time < 6
- At 23:00: 22 < 23 < 6? FALSE
- At 01:00: 22 < 1 < 6? FALSE
- Does NOT work as intended!

LIMITATION: Script cannot handle time ranges
that cross midnight. Would require:
- Additional logic for 24-hour boundary
- OR separate two time ranges
- OR use 24-hour shift configuration
```

## 12. Configuration Examples Flow

```
CONFIGURATION 1: MORNING BLOCKER
Start Time: 6  (6 AM)
End Time: 12   (12 PM)
Effect: Block until noon for morning focus
───────────────────────────────────────────

00:00-05:59  │ FREE TIME (websites accessible)
06:00-11:59  │ BLOCKED (websites inaccessible)
12:00-23:59  │ FREE TIME (websites accessible)


CONFIGURATION 2: ALL-DAY BLOCKER
Start Time: 0   (12 AM - midnight)
End Time: 24    (⚠️ INVALID - max hour is 23)
Effect: Block all day long (Modified to 0-23)
──────────────────────────────────────────────

CORRECTED:
Start Time: 0   (12 AM)
End Time: 23    (11 PM)
NOTE: Websites unblock for 1 hour (23:00-00:00)

Better approach: Multiple shift configurations


CONFIGURATION 3: NIGHT BLOCKER
Start Time: 20  (8 PM)
End Time: 23    (11 PM)
Effect: Block only evening (like after work relaxation)
────────────────────────────────────────────

00:00-19:59  │ FREE TIME
20:00-22:59  │ BLOCKED
23:00-23:59  │ FREE TIME


CONFIGURATION 4: MAXIMUM COVERAGE (Partial)
Start Time: 7   (7 AM)
End Time: 23    (11 PM)
Effect: Block entire working day + evening
────────────────────────────────────────────

00:00-06:59  │ FREE TIME
07:00-22:59  │ BLOCKED
23:00-23:59  │ FREE TIME (1 hour unblocked)
```

## 13. File I/O Operations Detailed View

```
READING OPERATION (Blocking):
──────────────────────────────
hostfile.read()
    │
    ├─ Returns entire file as single string
    ├─ Includes all newlines (\n) characters
    ├─ Memory: All content in RAM at once
    │
    ▼
String Content:
"127.0.0.1 localhost\n
 ::1 localhost\n
 # Comment line\n
 127.0.0.1 blocked.com\n"
    │
    ├─ Check with: if site not in hosts
    ├─ Very fast for small files
    │
    ▼
Output: String for membership checking


READING OPERATION (Unblocking):
───────────────────────────────
hostfile.readlines()
    │
    ├─ Returns list of lines (each with \n)
    ├─ Each line is separate string element
    ├─ More memory efficient than read()
    │
    ▼
List Content:
["127.0.0.1 localhost\n",
 "::1 localhost\n",
 "# Comment line\n",
 "127.0.0.1 blocked.com\n"]
    │
    ├─ Iterate through: for host in hosts
    ├─ Check each line individually
    │
    ▼
Output: List of strings for iteration


WRITING OPERATION:
──────────────────
hostfile.write(line)
    │
    ├─ Append content to file
    ├─ Position after current content
    ├─ Requires already having data
    │
    ▼
Example: 
hostfile.write("127.0.0.1 facebook.com\n")
    │
    └─ Line added to file


SEEK OPERATION:
───────────────
hostfile.seek(0)
    │
    ├─ Move file pointer to beginning
    ├─ Position = byte 0
    ├─ Essential for rewriting file
    │
    ▼
Required before re-writing
    │
    └─ Without seek: appends instead of overwrite


TRUNCATE OPERATION:
───────────────────
hostfile.truncate()
    │
    ├─ Delete all content after current position
    ├─ Removes garbage data
    ├─ Essential for clean unblocking
    │
    ▼
Example:
Before truncate:
"127.0.0.1 localhost
 127.0.0.1 facebook.com
 127.0.0.1 instagram.com"

Write 2 lines, position at byte X
Then truncate()

After truncate:
"127.0.0.1 localhost
 127.0.0.1 example.com"
    │
    └─ Old facebook/instagram entries gone
```

## 14. Loop Iteration Timing

```
TIME PROGRESSION - ONE COMPLETE CYCLE:
───────────────────────────────────────

T(0)        Start of iteration
            │
            ├─ Get current time:        ~0ms
            ├─ Create datetime objects: ~0ms
            ├─ Compare times:           ~0ms
            │
T(1)        Open hosts file:           ~10-50ms
            │
T(2)        Read hosts file:           ~20-100ms
            │                           (depends on file size)
            │
T(3)        Process websites:          ~50-200ms
            │                           (10-50ms per site)
            │
T(4)        Write to file:             ~50-500ms
            │                           (depends on write speed)
            │
T(5)        Close hosts file:          ~5-20ms (auto)
            │
T(6)        Sleep for 5 seconds:       5000ms
            │
T(5000)     Next iteration begins


EFFECTIVE CHECK INTERVAL: ~5 seconds
                          (with negligible overhead)


PERFORMANCE CHARACTERISTICS:
────────────────────────────
File I/O Time:      ~150-900ms per check
Sleep Time:         ~5000ms per check
───────────────────────────────
Total Per Cycle:    ~5.15-5.9 seconds

CPU Usage:          Minimal (idle during sleep)
Disk Usage:         Minimal (light I/O)
Memory Usage:       Low (<10MB)
Thread Count:       1 (single-threaded)
```

## 15. Configuration Variations

```
BASIC CONFIGURATION:
────────────────────
website_to_block = [
    "www.facebook.com",
    "www.instagram.com"
]
block_website(9, 21)

Result: 2 websites blocked from 9 AM to 9 PM


COMPREHENSIVE CONFIGURATION:
─────────────────────────────
website_to_block = [
    "www.facebook.com",
    "facebook.com",
    "m.facebook.com",
    "www.instagram.com",
    "instagram.com",
    "www.twitter.com",
    "twitter.com",
    "www.reddit.com",
    "reddit.com",
    "www.youtube.com",
    "youtube.com"
]
block_website(7, 22)

Result: 11 domain variations blocked from 7 AM to 10 PM


MINIMAL CONFIGURATION:
──────────────────────
website_to_block = [
    "www.youtube.com"
]
block_website(9, 17)

Result: 1 website blocked from 9 AM to 5 PM


AGGRESSIVE CONFIGURATION:
──────────────────────────
website_to_block = [
    "www.facebook.com",
    "www.instagram.com",
    "www.tiktok.com",
    "www.twitter.com",
    "www.reddit.com",
    "www.youtube.com",
    "www.twitch.tv",
    "www.netflix.com",
    "www.amazon.com"
]
block_website(6, 23)

Result: 9 entertainment/social sites blocked from 6 AM to 11 PM


PRODUCTIVITY FOCUSED:
─────────────────────
website_to_block = [
    "www.facebook.com",
    "www.instagram.com",
    "www.twitter.com",
    "www.gmail.com",
    "www.slack.com",  # Even work chat to force focus
    "www.youtube.com"
]
block_website(8, 17)

Result: Maximum focus mode - only essential tools allowed
```

## 16. Dependency and Import Analysis

```
REQUIRED IMPORTS:
────────────────

import time
├─ Purpose: Sleep functionality
├─ Function: time.sleep(5)
├─ Provides: Delay between iterations
└─ Built-in: Yes ✓


from datetime import datetime as dt
├─ Purpose: Time and date operations
├─ Functions:
│  ├─ dt.now() - Get current time
│  ├─ dt(year, month, day, hour) - Create datetime
│  └─ Comparison: < > operators
├─ Built-in: Yes ✓
└─ Import Style: Aliased as 'dt'


import os
├─ Purpose: OS detection and file paths
├─ Functions:
│  ├─ os.name - Detect OS ('posix', 'nt')
│  └─ File path constants: /etc/hosts, C:\Windows\...
├─ Built-in: Yes ✓
└─ Usage: Conditional OS detection


import sys
├─ Purpose: System operations
├─ Functions: sys.exit()
├─ Built-in: Yes ✓
└─ Usage: Exit program when OS unknown


NO EXTERNAL DEPENDENCIES:
────────────────────────
All imports are built-in Python libraries.
No pip install required!
Works with base Python 3.x installation.
```

## 17. State Machine Diagram

```
APPLICATION STATES:
───────────────────

                    ┌─────────────┐
                    │  START      │
                    │  Program    │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ DETECT OS   │
                    │ Set Host    │
                    │ File Path   │
                    └──────┬──────┘
                           │
                    ┌──────┴──────┐
                    │             │
                 OS OK        OS INVALID
                    │             │
                    │             ▼
                    │       ┌────────────┐
                    │       │ ERROR:     │
                    │       │ Unknown OS │
                    │       │ EXIT       │
                    │       └────────────┘
                    │
                    ▼
            ┌─────────────────┐
            │ DISPLAY MESSAGES│
            │ Ready for Loop  │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────────────┐
            │ CHECK CURRENT TIME      │
            │ Every 5 seconds         │
            └────────┬────────────────┘
                     │
            ┌────────┴─────────┐
            │                  │
       WORK HOURS         FREE TIME
            │                  │
            ▼                  ▼
      ┌──────────┐        ┌──────────┐
      │ BLOCKING │        │UNBLOCKING│
      │ STATE    │        │ STATE    │
      │          │        │          │
      │ Add      │        │ Remove   │
      │ Entries  │        │ Entries  │
      │ to       │        │ from     │
      │ Hosts    │        │ Hosts    │
      │ File     │        │ File     │
      └────┬─────┘        └────┬─────┘
           │                   │
           └─────────┬─────────┘
                     │
            ┌────────▼────────┐
            │ SLEEP 5 SECONDS │
            └────────┬────────┘
                     │
                     └─ LOOP BACK TO CHECK TIME
                        (unless Ctrl+C pressed)
                     │
                     ▼
            ┌──────────────────┐
            │ Ctrl+C Pressed   │
            │ User interrupts  │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │ DISPLAY EXIT MSG │
            │ "Program done"   │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │ WAIT FOR INPUT   │
            │ Press Enter      │
            └────────┬─────────┘
                     │
                     ▼
            ┌──────────────────┐
            │ EXIT PROGRAM     │
            │ Hosts file left  │
            │ in current state │
            └──────────────────┘


TRANSITION CONDITIONS:
──────────────────────
START → DETECT OS:      Automatic
DETECT OS → ERROR:      os.name not recognized
DETECT OS → DISPLAY:    OS detected successfully
DISPLAY → CHECK TIME:   Start of main loop
CHECK TIME → BLOCKING:  Working hours detected
CHECK TIME → UNBLOCKING:Free time detected
BLOCKING → SLEEP:       Entries added/maintained
UNBLOCKING → SLEEP:     Entries removed
SLEEP → CHECK TIME:     After 5 seconds
ANYWHERE → EXIT:        KeyboardInterrupt (Ctrl+C)
```

## 18. Decision Tree for Time Logic

```
INPUT: Current Time = dt.now()
       Start Hour = 9
       End Hour = 21

                        Current Time
                            │
                            ▼
                    Get year, month, day
                            │
                            ▼
                    Create date_only = date part
                            │
                    ┌───────┴───────┐
                    │               │
                    ▼               ▼
            Create START      Create END
            dt(y,m,d,9,0,0)  dt(y,m,d,21,0,0)
            9:00 AM today    9:00 PM today
                    │               │
                    └───────┬───────┘
                            │
                            ▼
                    START < NOW < END ?
                    │
            ┌───────┴───────┐
            │               │
          TRUE            FALSE
            │               │
            ▼               ▼
    WORKING HOURS      FREE TIME
    BLOCK WEBSITES     UNBLOCK WEBSITES
```

## 19. Error Recovery Possibilities

```
CURRENT IMPLEMENTATION:
───────────────────────
Exception Occurs
    │
    ├─ Catch Exception
    ├─ Print error message
    ├─ break (exit loop)
    │
    ▼
Program stops
    │
    └─ User presses Enter to close

PROBLEM: 
- Websites may remain blocked after program crash
- User must manually recover hosts file


IMPROVED IMPLEMENTATION (Future):
──────────────────────────────────
Exception Occurs
    │
    ├─ Log error to file
    ├─ Attempt to unblock all websites
    ├─ Restore hosts file from backup
    │
    ├─ Notify user
    │
    ▼
Graceful shutdown
    │
    └─ Hosts file in safe state


RECOVERY OPTIONS:
─────────────────
1. Manual Edit: Open hosts file, delete blocked entries
2. Restore Backup: Copy from *.backup file
3. System Restore: Use Windows/Linux system restore
4. Reinstall: Requires admin, fixes hosts file
```

## 20. Summary Diagram - Complete Application Flow

```
START
  │
  ├─→ Import Libraries
  │
  ├─→ Define Config (websites, paths, redirect)
  │
  ├─→ Detect Operating System
  │    ├─ Linux/macOS → /etc/hosts
  │    ├─ Windows → C:\Windows\System32\drivers\etc\hosts
  │    └─ Unknown → Exit
  │
  ├─→ Main Function: block_website(9, 21)
  │    │
  │    ├─→ Display Status Messages
  │    │
  │    └─→ Enter While Loop (Check every 5 seconds)
  │        │
  │        ├─→ Get Current Time
  │        │
  │        ├─→ Is it 9 AM - 9 PM?
  │        │    │
  │        │    ├─ YES → BLOCKING STATE
  │        │    │  ├─ Open hosts file
  │        │    │  ├─ Add blocked sites (127.0.0.1 + domain)
  │        │    │  └─ Print "Working hours... Blocking"
  │        │    │
  │        │    └─ NO → UNBLOCKING STATE
  │        │       ├─ Open hosts file
  │        │       ├─ Remove blocked entries
  │        │       └─ Print "Free time... Unblocking"
  │        │
  │        ├─→ Handle Errors
  │        │    ├─ PermissionError → "Run as Admin/Sudo"
  │        │    ├─ FileNotFoundError → "Hosts file not found"
  │        │    └─ Other Exception → "Unexpected error"
  │        │
  │        ├─→ Sleep for 5 Seconds
  │        │
  │        └─→ Loop continues unless Ctrl+C
  │
  ├─→ User Presses Ctrl+C
  │
  ├─→ Print "Program finished."
  │
  ├─→ input("Press Enter to exit...")
  │
  └─→ EXIT PROGRAM
     (Hosts file remains in current state)
```

---

## Summary

The Website Blocker Flowchart documentation covers:

1. **Application Startup**: OS detection and initialization
2. **Main Loop Logic**: Time-based checking every 5 seconds
3. **Blocking Operation**: Adding sites to hosts file during work hours
4. **Unblocking Operation**: Removing sites from hosts file during free time
5. **Time Comparison**: Detailed time range checking logic
6. **Error Handling**: PermissionError, FileNotFoundError, generic exceptions
7. **System Integration**: How hosts file redirection works
8. **File I/O Operations**: Reading, writing, seeking, truncating
9. **State Management**: Hosts file state transitions
10. **Edge Cases**: Midnight crossing limitations, time range variations
11. **Performance**: Loop timing and resource utilization

The application demonstrates system-level programming with file manipulation, time-based scheduling, and cross-platform compatibility in Python.
