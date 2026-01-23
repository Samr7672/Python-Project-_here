# Website Blocker

## Overview
Website Blocker is a Python utility that automatically blocks and unblocks specified websites during working and non-working hours respectively. It works by modifying the system's hosts file to redirect blocked websites to localhost (127.0.0.1), making them inaccessible during configured time periods.

## Features
- **Time-Based Website Blocking**: Automatically blocks websites during configured working hours
- **Automatic Unblocking**: Removes website blocks during free time (outside working hours)
- **Cross-Platform Support**: Compatible with Windows, Linux, and macOS
- **OS Auto-Detection**: Automatically detects the operating system and uses appropriate hosts file location
- **Multiple Website Support**: Block multiple websites simultaneously
- **Localhost Redirection**: Redirects blocked sites to 127.0.0.1 (localhost)
- **Configurable Time Windows**: Set custom start and end times for blocking
- **Error Handling**: Comprehensive error handling for permission issues and file access
- **Persistent Blocking**: Maintains blocking even if browser is restarted (uses system-level hosts file)
- **Status Messages**: Regular console feedback showing current application state

## Requirements
- Python 3.x
- Administrator/Sudo privileges (required to modify hosts file)
- Write access to system hosts file

## Installation

1. **Clone or download the project**:
   ```
   cd website_blocker
   ```

2. **No additional dependencies needed** (uses only built-in Python libraries)

3. **Run with elevated privileges**:
   
   **Windows**:
   - Right-click Command Prompt or PowerShell
   - Select "Run as Administrator"
   - Run: `python website_blocker.py`
   
   **Linux/macOS**:
   ```bash
   sudo python3 website_blocker.py
   ```

## Usage

### Basic Usage
Run the script with administrator/sudo privileges:

**Windows**:
```
python website_blocker.py
```

**Linux/macOS**:
```bash
sudo python3 website_blocker.py
```

### Configuration

#### Setting Blocked Websites
Edit the `website_to_block` list in the script:
```python
website_to_block = [
    "www.facebook.com",
    "www.instagram.com",
    "www.google.com",
    "www.gmail.com",
    "www.chrome.com"
]
```

#### Setting Work Hours
Modify the call to `block_website()` at the bottom of the script:
```python
block_website(start_hour, end_hour)
```

Example - Block from 9 AM to 9 PM:
```python
block_website(9, 21)
```

Example - Block from 8 AM to 6 PM:
```python
block_website(8, 18)
```

#### Hosts File Locations
The script automatically detects and uses the correct hosts file:
- **Windows**: `C:\Windows\System32\drivers\etc\hosts`
- **Linux**: `/etc/hosts`
- **macOS**: `/etc/hosts`

### Runtime Behavior

1. **Application Starts**: Displays target hosts file location
2. **Enters Loop**: Checks current time every 5 seconds
3. **During Working Hours**:
   - Displays: "Working hours... Blocking sites."
   - Adds all configured websites to hosts file
   - Each blocked site redirects to 127.0.0.1
4. **During Free Time**:
   - Displays: "Free time... Unblocking sites."
   - Removes blocked site entries from hosts file
5. **Manual Stop**: Press Ctrl+C to stop the blocker
6. **Exit**: Press Enter to close the program window

## Examples

### Example 1: Productivity Hours
```python
# Configuration
website_to_block = [
    "www.facebook.com",
    "www.instagram.com",
    "www.twitter.com"
]

# Run from 9 AM to 6 PM
block_website(9, 18)
```

**Result**:
- 8:00 AM - Free time, websites unblocked
- 9:00 AM - Working hours begin, Facebook/Instagram/Twitter blocked
- 6:00 PM - Free time begins, websites unblocked

### Example 2: Gaming Block
```python
website_to_block = [
    "www.twitch.tv",
    "www.youtube.com",
    "www.reddit.com"
]

block_website(8, 22)  # 8 AM to 10 PM
```

### Example 3: Social Media Block
```python
website_to_block = [
    "www.facebook.com",
    "www.instagram.com",
    "www.tiktok.com",
    "www.snapchat.com",
    "www.twitter.com"
]

block_website(7, 20)  # 7 AM to 8 PM
```

## How It Works

### System-Level Blocking (Hosts File)
The application modifies the system's hosts file, which is consulted before DNS resolution:

```
Hosts File Entry:
127.0.0.1 www.facebook.com
```

When a user tries to access www.facebook.com:
1. System checks hosts file first
2. Finds entry pointing to 127.0.0.1 (localhost)
3. Browser cannot connect (localhost is not a web server)
4. Website is effectively blocked

### Time-Based Logic
- **Working Hours**: start_time < current_time < end_time
- **Free Time**: current_time < start_time OR current_time >= end_time
- **Check Interval**: Every 5 seconds

## Hosts File Entries

### Blocked Website Entry Format
```
127.0.0.1 www.facebook.com
127.0.0.1 www.instagram.com
127.0.0.1 www.google.com
```

### Multiple Domains
Some websites may have multiple domain variations:
```python
website_to_block = [
    "www.facebook.com",
    "facebook.com",  # Include both www and non-www versions
    "m.facebook.com"  # Mobile version
]
```

## Error Handling

### Permission Denied Error
```
[ERROR] Permission Denied!
You must run this script as Administrator (Windows) or Sudo (Linux/Mac).
```

**Solution**:
- **Windows**: Run Command Prompt as Administrator before running script
- **Linux/macOS**: Prefix command with `sudo`

### Hosts File Not Found
```
[ERROR] Could not find the hosts file at: C:\Windows\System32\drivers\etc\hosts
```

**Solution**:
- Verify hosts file exists at the displayed location
- Check file path is correct for your OS
- Ensure read/write permissions on the hosts file

### Unexpected Errors
```
[ERROR] An unexpected error occurred: [error details]
```

**Solutions**:
- Check file permissions
- Ensure sufficient disk space
- Verify hosts file is not corrupted
- Run with administrator privileges
- Check command syntax in configuration

## OS Detection and Compatibility

### OS Detection Process
```
if os.name == 'posix':
    # Linux or macOS
    default_hoster = "/etc/hosts"
elif os.name == 'nt':
    # Windows
    default_hoster = r"C:\Windows\System32\drivers\etc\hosts"
else:
    # Unknown OS
    print("OS Unknown. Exiting.")
```

### Supported Operating Systems
| OS | Status | Hosts File Location |
|---|---|---|
| Windows 7/8/10/11 | ✓ Supported | C:\Windows\System32\drivers\etc\hosts |
| Linux (Ubuntu, Debian, etc.) | ✓ Supported | /etc/hosts |
| macOS | ✓ Supported | /etc/hosts |

## Performance Considerations

### Resource Usage
- **CPU**: Minimal (checks time every 5 seconds)
- **Memory**: < 10 MB
- **Disk I/O**: Light (reads/writes hosts file every 5 seconds)

### Check Frequency
The script checks the current time every 5 seconds:
```python
time.sleep(5)
```

**Adjustment**:
To change check frequency, modify the sleep duration:
```python
time.sleep(10)  # Check every 10 seconds
time.sleep(1)   # Check every 1 second
```

## Advanced Configuration

### Custom Redirect IP
By default, blocked sites redirect to 127.0.0.1:
```python
redirect = "127.0.0.1"
```

To redirect to a different IP (not recommended):
```python
redirect = "192.168.1.1"  # Custom IP
```

### Dynamic Website List
Add websites from user input:
```python
website_to_block = []
while True:
    site = input("Enter website to block (or 'done'): ")
    if site.lower() == 'done':
        break
    website_to_block.append(site)

block_website(9, 21)
```

### Logging Blocked Attempts
Create a log file to track when websites are accessed:
```python
with open("block_log.txt", "a") as log:
    log.write(f"{dt.now()} - Website access attempted\n")
```

## Troubleshooting

### Websites Still Accessible
**Problem**: Website still loads despite blocking
**Solutions**:
1. Verify script is running with administrator/sudo privileges
2. Check website is in the `website_to_block` list
3. Restart browser or clear DNS cache:
   - **Windows**: `ipconfig /flushdns`
   - **Linux**: `sudo resolvectl flush-caches`
   - **macOS**: `sudo dscacheutil -flushcache`
4. Verify hosts file contains the entries:
   - **Windows**: Open `C:\Windows\System32\drivers\etc\hosts`
   - **Linux/macOS**: Run `cat /etc/hosts`

### Script Not Running
**Problem**: "OS Unknown. Exiting."
**Solution**: 
- Check OS compatibility
- Verify Python 3.x is installed
- Ensure script is in correct location

### Websites Won't Unblock
**Problem**: Websites remain blocked outside working hours
**Solutions**:
1. Manually check and remove entries from hosts file
2. Restart the blocker application
3. Clear browser cache and restart browser
4. Check system time is correct

### Permission Issues
**Problem**: "Permission Denied" error
**Solutions**:
- **Windows**: Right-click Command Prompt → "Run as Administrator"
- **Linux/macOS**: Use `sudo python3 website_blocker.py`
- Check hosts file permissions: `ls -l /etc/hosts` (Linux/macOS)

## Security Considerations

### Hosts File Security
- The hosts file is a critical system file
- Modifications require administrator privileges
- Always verify entries before making changes
- Keep backups of the original hosts file

### Backup Hosts File
**Before running the script, backup your hosts file**:

**Windows**:
```
copy C:\Windows\System32\drivers\etc\hosts C:\Windows\System32\drivers\etc\hosts.backup
```

**Linux/macOS**:
```bash
sudo cp /etc/hosts /etc/hosts.backup
```

### Restore Hosts File
If something goes wrong:

**Windows**:
```
copy C:\Windows\System32\drivers\etc\hosts.backup C:\Windows\System32\drivers\etc\hosts
```

**Linux/macOS**:
```bash
sudo cp /etc/hosts.backup /etc/hosts
```

## Code Structure

### Main Components

#### 1. Configuration Section
```python
website_to_block = [...]  # List of websites to block
redirect = "127.0.0.1"    # Redirect IP address
```

#### 2. OS Detection
```python
if os.name == 'posix':
    default_hoster = Linux_host
elif os.name == 'nt':
    default_hoster = Window_host
```

#### 3. Main Function: block_website(start_time, end_time)
- Starts infinite loop checking current time
- Compares current time with work hours
- Modifies hosts file based on time
- Includes error handling and status messages

#### 4. Error Handling
- **PermissionError**: Handles insufficient privileges
- **FileNotFoundError**: Handles missing hosts file
- **Exception**: Catches any unexpected errors

### Time Comparison Logic
```python
if (dt(year, month, day, start_time) < dt.now() < dt(year, month, day, end_time)):
    # Working hours: Block websites
else:
    # Free time: Unblock websites
```

## Learning Concepts

### 1. System File Manipulation
- Reading and writing system files
- Hosts file format and purpose
- File I/O operations in Python

### 2. Time and Scheduling
- datetime module for time comparisons
- Current time retrieval
- Time window calculations

### 3. Operating System Interaction
- OS detection and abstraction
- Cross-platform compatibility
- Environment-specific file paths

### 4. System Administration
- Permission requirements
- System-level configuration
- Administrative operations

### 5. Error Handling
- Exception catching and handling
- User-friendly error messages
- Error recovery strategies

### 6. Scripting Concepts
- Infinite loops with time-based logic
- Signal handling (Ctrl+C)
- Status monitoring and reporting

## Limitations and Considerations

### Limitations
1. **Root/Admin Dependency**: Requires elevated privileges to run
2. **Local Network Only**: Only blocks on the local machine
3. **Browser-Independent**: Blocks at OS level (not browser extension)
4. **No Custom Messages**: Blocked sites show browser error, not custom page
5. **Time Format**: Uses 24-hour format only (0-23)
6. **No Graphical Interface**: Console-based application only

### Edge Cases
1. **Midnight Crossing**: Work hours spanning midnight (e.g., 22:00 to 6:00) not supported
2. **System Time Changes**: If system time is changed, check interval may skip
3. **Daylight Saving Time**: May affect scheduling during DST transitions
4. **Fast Domain Switches**: Switching between HTTP/HTTPS may require double entries

## Future Enhancements
- Add GUI for easier configuration
- Support midnight-crossing time ranges (22:00 to 6:00)
- Implement logging and statistics
- Add schedule flexibility (different times per day)
- Support for domain patterns and wildcards
- Add whitelisting alongside blacklisting
- Create Windows service for background execution
- Add notifications when blocking/unblocking
- Implement configuration file support
- Add remote blocking capability

## Use Cases

### 1. Productivity Enhancement
Block social media during work hours to minimize distractions

### 2. Parental Control
Block entertainment websites during study hours for children

### 3. Internet Addiction Management
Automatically restrict access to specific websites during defined periods

### 4. Work-Life Balance
Enforce technology boundaries by blocking work sites after hours

### 5. Focus Sessions
Block all distracting websites during focused work periods

## Dependencies Summary
| Library | Type | Purpose |
|---|---|---|
| time | Built-in | Sleep function for check intervals |
| datetime | Built-in | Current time and time comparisons |
| os | Built-in | Operating system detection |
| sys | Built-in | System exit function |

## Running in Background

### Windows - Task Scheduler
1. Open Task Scheduler
2. Create Basic Task
3. Set trigger for system startup
4. Set action to run `python website_blocker.py`
5. Enable "Run with highest privileges"

### Linux - Cron Job (requires setup)
```bash
# Add to crontab with sudo
sudo crontab -e

# Add line (runs at startup)
@reboot sudo python3 /path/to/website_blocker.py &
```

### macOS - LaunchAgent
Create `~/Library/LaunchAgents/com.websiteblocker.plist`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" 
"http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.websiteblocker</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>/path/to/website_blocker.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
</dict>
</plist>
```

## Tips and Best Practices

### 1. Time Format
- Use 24-hour format (0-23)
- 0 = 12:00 AM, 9 = 9:00 AM, 21 = 9:00 PM

### 2. Website List
- Use complete domain names (www.facebook.com)
- Add both www and non-www versions if needed
- Test each website after configuration

### 3. Regular Testing
- Test blocking during work hours
- Test unblocking during free time
- Verify hosts file is being modified correctly

### 4. Keep Script Running
- Leave terminal window open while script is running
- For persistent blocking, add to Task Scheduler or Cron
- Monitor console messages for errors

### 5. Hosts File Maintenance
- Regularly review hosts file entries
- Remove old/unnecessary entries
- Keep backups of the original file

## Author Notes
Website Blocker demonstrates practical system administration concepts in Python, including OS-level file manipulation, time-based scheduling, and error handling. It's a useful productivity tool that works at the system level, making it more effective than browser-based solutions.

## Disclaimer
This tool modifies critical system files. Use responsibly and with administrative approval. Always maintain backups of important system files. The author is not responsible for misuse or system damage caused by improper use of this tool.
