import cv2
import pyautogui
import win32api
import numpy as np
import time

# 1. Get the screen resolution (width and height)
width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
dimension = (width, height) #

# 2. Define the video format and output file
# XVID is a common codec used for MP4/AVI files
fourcc = cv2.VideoWriter_fourcc(*"XVID") 
output = cv2.VideoWriter("test.mp4", fourcc, 30.0, dimension) #

# 3. Set the recording duration
start_time = time.time()
duration = 10 # Seconds to record
end_time = start_time + duration #

print("Recording started...")

# 4. Main recording loop
while True:
    # Capture the screenshot
    image = pyautogui.screenshot()
    
    # Convert the screenshot into a numpy array for OpenCV
    frame_1 = np.array(image)
    
    # Convert colors from RGB (PyAutoGUI) to BGR (OpenCV)
    # Note: The video mentions COLOR_BGR2RGB to keep colors original
    frame = cv2.cvtColor(frame_1, cv2.COLOR_RGB2BGR)
    
    # Write the frame to the video file
    output.write(frame)
    
    # Check if the current time has exceeded the end time
    current_time = time.time()
    if current_time > end_time:
        break

# 5. Release the video file and finish
output.release()
print("Recording finished and saved as test.mp4")