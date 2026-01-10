import time
from datetime import datetime as dt
import os
import sys

# --- CONFIGURATION ---
website_to_block = [
    "www.facebook.com",  # Fixed the comma to a dot
    "www.instagram.com",
    "www.google.com",
    "www.gmail.com",
    "www.chrome.com"
]

Linux_host = "/etc/hosts"
Window_host = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

# --- 1. FIXED OS DETECTION ---
if os.name == 'posix':
    default_hoster = Linux_host
elif os.name == 'nt':
    default_hoster = Window_host
else:
    print("OS Unknown. Exiting.")
    input("Press Enter to exit...") # Pause so you can read the message
    sys.exit()

def block_website(start_time, end_time):
    print(f"Website Blocker Running... (Target file: {default_hoster})")
    print("Press Ctrl+C to stop manually.\n")
    
    while True:
        try:
            # Check if current time is within working hours
            if (dt(dt.now().year, dt.now().month, dt.now().day, start_time) 
                < dt.now() 
                < dt(dt.now().year, dt.now().month, dt.now().day, end_time)):
                
                print("Working hours... Blocking sites.")
                with open(default_hoster, "r+") as hostfile:
                    hosts = hostfile.read()
                    for site in website_to_block:
                        if site not in hosts:
                            hostfile.write(redirect + " " + site + "\n")
            
            else:
                print("Free time... Unblocking sites.")
                with open(default_hoster, "r+") as hostfile:
                    hosts = hostfile.readlines()
                    hostfile.seek(0)
                    for host in hosts:
                        if not any(site in host for site in website_to_block):
                            hostfile.write(host)
                    hostfile.truncate()
            
            time.sleep(5)

        # --- 2. IMPROVED ERROR HANDLING ---
        except PermissionError:
            print("\n[ERROR] Permission Denied!")
            print("You must run this script as Administrator (Windows) or Sudo (Linux/Mac).")
            break # Break loop to reach the input() at the end
        
        except FileNotFoundError:
            print(f"\n[ERROR] Could not find the hosts file at: {default_hoster}")
            break

        except Exception as e:
            print(f"\n[ERROR] An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    # Example: Block from 9 AM to 9 PM (21:00)
    block_website(9, 21)

# --- 3. THIS KEEPS THE WINDOW OPEN ---
print("\nProgram finished.")
input("Press Enter to exit...")