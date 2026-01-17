#import pywhatkit as pw

#text="Python is a high-level, interpreted programming language known for its clear syntax and readability, making it an excellent choice for both beginners and experienced developers. Created by Guido van Rossum and released in 1991, Python follows a philosophy centered on simplicity and the efficient use of whitespace to enhance code clarity.One of Python's greatest strengths is its extensive standard library and a vast ecosystem of third-party packages. This allows it to excel in diverse fields such as Data Science, Artificial Intelligence (AI), Web Development, and Automation. For example, a screen recorder can be built in Python by capturing screenshots using pyautogui, processing them into arrays with numpy, and merging them into a video file using the cv2 (OpenCV) library.The language supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Because it is interpreted, developers can run code line-by-line, which speeds up the debugging process. Whether you are building complex machine learning models or writing simple scripts to automate daily tasks, Python's versatility and strong community support make it one of the most popular and influential languages in the modern tech landscape.Would you like me to explain how to set up a Python environment on your computer to start coding?"

## pw.text_to_handwriting(text, "demo.png",[0,255,255]) # this will not always work beacause it uses a web server ApI which can have traffic
## so use this 
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def text_to_handwriting_local(text, output_file, font_path, font_size=30):
    # Check if font exists before trying to open it
    if not os.path.exists(font_path):
        print(f"CRITICAL ERROR: Font not found at {font_path}")
        return

    # Create a larger canvas for a long paragraph
    img = Image.new('RGB', (1200, 1500), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)

    # Wrap the text so it stays within the image margins
    lines = textwrap.wrap(text, width=70) 
    
    # Draw each line one by one
    y_text = 50
    for line in lines:
        d.text((50, y_text), line, fill=(0, 0, 138), font=font)
        y_text += font_size + 10 # Move down for the next line

    img.save(output_file)
    print(f"SUCCESS: {output_file} has been created!")

text = "Python is a high-level, interpreted programming language known for its clear syntax and readability, making it an excellent choice for both beginners and experienced developers. Created by Guido van Rossum and released in 1991, Python follows a philosophy centered on simplicity and the efficient use of whitespace to enhance code clarity. One of Python's greatest strengths is its extensive standard library and a vast ecosystem of third-party packages. This allows it to excel in diverse fields such as Data Science, Artificial Intelligence (AI), Web Development, and Automation."



path_to_my_font = r"C:\Users\rebik\Downloads\python project\my_nerve.ttf"

text_to_handwriting_local(text, "demo.png", path_to_my_font)