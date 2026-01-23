# Text to Handwriting Converter

A Python application that converts text into handwriting-style images. Uses custom fonts and the Pillow library to generate images of text rendered in handwriting fonts, perfect for creating personalized documents, signatures, or artistic text displays.

## Features

- ✍️ **Handwriting Style**: Renders text in handwriting/cursive fonts
- 📄 **Long Text Support**: Handles paragraphs with automatic text wrapping
- 🎨 **Customizable Fonts**: Use any TrueType font (.ttf) file
- 🖼️ **Image Output**: Generates high-quality PNG images
- 🎯 **Adjustable Font Size**: Control text size and spacing
- 📐 **Auto Text Wrapping**: Automatically wraps text to fit canvas width
- 🌈 **Color Customization**: Set text color and background color
- 💾 **File Management**: Saves output with success confirmation

## Requirements

- Python 3.x
- `Pillow (PIL)` - Image processing library
- `textwrap` - Built-in text wrapping module
- `os` - Built-in file system module
- TrueType font file (.ttf) - Any handwriting/cursive font

## Installation

1. Install required package:
```bash
pip install Pillow
```

2. Obtain a TrueType font file:
   - Download from [DaFont.com](https://www.dafont.com/)
   - Download from [Google Fonts](https://fonts.google.com/)
   - Use system fonts (usually in C:\Windows\Fonts on Windows)

3. Note the path to your font file

## Usage

1. Prepare your font file (e.g., `my_nerve.ttf`)

2. Modify the script with your settings:

```python
from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def text_to_handwriting_local(text, output_file, font_path, font_size=30):
    # Function implementation
    pass

# Your text
text = "Your text here..."

# Path to your font file
path_to_my_font = r"C:\path\to\your\font.ttf"

# Generate image
text_to_handwriting_local(text, "output.png", path_to_my_font)
```

3. Run the script:
```bash
python handwriting.py
```

4. Check the output directory for the generated PNG file:
```
demo.png created successfully!
```

## How It Works

### Step-by-step Process

1. **Verify Font**: Checks if the TrueType font file exists
2. **Create Canvas**: Creates a white image (1200×1500 pixels)
3. **Load Font**: Loads the font with specified size
4. **Wrap Text**: Automatically wraps text to 70 characters per line
5. **Draw Text**: Draws each line on the canvas
6. **Add Spacing**: Adds vertical spacing between lines
7. **Save Image**: Saves the result as PNG file
8. **Confirm**: Prints success message with filename

## Function Details

### `text_to_handwriting_local(text, output_file, font_path, font_size=30)`

Main function that converts text to handwriting image.

**Parameters:**
- `text` (str): The text to convert
- `output_file` (str): Output filename (e.g., "demo.png")
- `font_path` (str): Full path to TrueType font file
- `font_size` (int): Font size in pixels (default: 30)

**Returns:** None (saves image to file)

**Exceptions:**
- Prints error if font file not found
- No exception raised (graceful failure)

## Image Specifications

| Property | Value |
|----------|-------|
| **Width** | 1200 pixels |
| **Height** | 1500 pixels |
| **Background** | White (255, 255, 255) |
| **Text Color** | Dark Blue (0, 0, 138) |
| **Text Wrapping** | 70 characters per line |
| **Top Margin** | 50 pixels |
| **Left Margin** | 50 pixels |
| **Line Spacing** | font_size + 10 pixels |

## Configuration Options

### Change Canvas Size
```python
img = Image.new('RGB', (1200, 1500), color=(255, 255, 255))
# Change (1200, 1500) to desired (width, height)
```

### Change Text Color
```python
d.text((50, y_text), line, fill=(0, 0, 138), font=font)
# Change (0, 0, 138) to RGB color
# Example: (255, 0, 0) for red, (0, 255, 0) for green
```

### Change Background Color
```python
img = Image.new('RGB', (1200, 1500), color=(255, 255, 255))
# Change (255, 255, 255) to desired RGB color
# Example: (240, 240, 240) for light gray
```

### Change Text Wrapping Width
```python
lines = textwrap.wrap(text, width=70)
# Change 70 to desired character count per line
```

### Change Line Spacing
```python
y_text += font_size + 10
# Change 10 to desired gap (in pixels) between lines
```

### Change Font Size
```python
text_to_handwriting_local(text, "output.png", font_path, font_size=50)
# Increase for larger text, decrease for smaller
```

## Example Usage

### Example 1: Simple Text
```python
text = "Hello, World!"
path_to_my_font = r"C:\path\to\font.ttf"
text_to_handwriting_local(text, "hello.png", path_to_my_font)
# Creates: hello.png with "Hello, World!" in handwriting style
```

### Example 2: Long Paragraph
```python
text = "Python is a high-level, interpreted programming language..."
path_to_my_font = r"C:\path\to\handwriting_font.ttf"
text_to_handwriting_local(text, "paragraph.png", path_to_my_font, font_size=25)
# Creates: paragraph.png with wrapped paragraph
```

### Example 3: Custom Colors
```python
def text_to_handwriting_colored(text, output_file, font_path, 
                                text_color=(255, 0, 0),
                                bg_color=(200, 200, 255)):
    img = Image.new('RGB', (1200, 1500), color=bg_color)
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 30)
    lines = textwrap.wrap(text, width=70)
    
    y_text = 50
    for line in lines:
        d.text((50, y_text), line, fill=text_color, font=font)
        y_text += 40
    
    img.save(output_file)
    print(f"SUCCESS: {output_file} has been created!")

# Use it:
text_to_handwriting_colored(text, "colored.png", font_path, 
                            text_color=(0, 100, 200),
                            bg_color=(255, 255, 200))
```

## Recommended Handwriting Fonts

Free fonts to download:
- **Caveat** (Google Fonts) - Casual handwriting
- **Indie Flower** (Google Fonts) - Fun, hand-drawn style
- **Dancing Script** (Google Fonts) - Elegant cursive
- **Pacifico** (Google Fonts) - Playful cursive
- **Great Vibes** (Google Fonts) - Formal script
- **Quicksand** (Google Fonts) - Modern handwriting
- **Fredoka** (Google Fonts) - Geometric handwriting

## Color Reference

### Common RGB Colors
| Color | RGB Value |
|-------|-----------|
| Black | (0, 0, 0) |
| White | (255, 255, 255) |
| Red | (255, 0, 0) |
| Green | (0, 255, 0) |
| Blue | (0, 0, 255) |
| Dark Blue | (0, 0, 138) |
| Gray | (128, 128, 128) |
| Light Gray | (200, 200, 200) |
| Yellow | (255, 255, 0) |
| Cyan | (0, 255, 255) |
| Magenta | (255, 0, 255) |
| Orange | (255, 165, 0) |

## File Structure

```
handwriting.py
├─ Imports (PIL, textwrap, os)
├─ text_to_handwriting_local() function
├─ text variable (content to convert)
├─ path_to_my_font (font file path)
└─ Function call
```

## Output Files

- **Filename**: Specified in function call (e.g., "demo.png")
- **Format**: PNG image
- **Location**: Current working directory
- **Size**: ~100-500 KB depending on content
- **Playable**: Any image viewer (Windows Photos, Preview, etc.)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Font not found** | Check font path exists, use raw string (r"...") |
| **Blank image** | Check text color and background color aren't identical |
| **Text cut off** | Increase canvas height or decrease font size |
| **Text too small** | Increase font_size parameter |
| **Text too crowded** | Decrease font_size or increase line_spacing |
| **Module not found** | Run `pip install Pillow` |

## Performance Notes

- Fast execution (< 1 second for typical text)
- Memory efficient
- CPU: Minimal usage
- Suitable for batch processing

## Tips & Best Practices

✅ **Do this:**
- Use actual handwriting fonts for best results
- Test with small text first
- Keep text wrapping width between 60-80 characters
- Use contrasting colors for readability
- Save fonts locally for reliability

❌ **Don't do this:**
- Use serif fonts for "handwriting" (use cursive instead)
- Make canvas too small for long text
- Use very similar colors for text and background
- Include system paths without testing
- Assume online APIs will always work

## Advanced Features

### Batch Processing
```python
texts = ["Text 1", "Text 2", "Text 3"]
for i, text in enumerate(texts):
    text_to_handwriting_local(text, f"output_{i}.png", font_path)
```

### Custom Positioning
```python
def custom_text_to_handwriting(text, output_file, font_path, 
                               x_start=50, y_start=50, 
                               line_height=40):
    img = Image.new('RGB', (1200, 1500), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 30)
    lines = textwrap.wrap(text, width=70)
    
    y_text = y_start
    for line in lines:
        d.text((x_start, y_text), line, fill=(0, 0, 138), font=font)
        y_text += line_height
    
    img.save(output_file)
```

### Text Alignment
```python
# Center text
def text_to_handwriting_centered(text, output_file, font_path):
    img = Image.new('RGB', (1200, 1500), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, 30)
    lines = textwrap.wrap(text, width=70)
    
    img_width = 1200
    y_text = 50
    for line in lines:
        bbox = d.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (img_width - text_width) // 2
        d.text((x, y_text), line, fill=(0, 0, 138), font=font)
        y_text += 40
    
    img.save(output_file)
```

## Learning Concepts

This project teaches:
- **Image Processing**: Using Pillow library
- **Font Handling**: Loading and using TrueType fonts
- **Text Rendering**: Drawing text on images
- **Text Wrapping**: Automatic line breaking
- **File I/O**: Reading fonts and writing images
- **Color Representation**: RGB color values
- **Canvas Management**: Creating and manipulating images
- **Error Handling**: Checking file existence

## Future Enhancements

- Add GUI interface for font/color selection
- Support multiple paragraphs with custom spacing
- Add rotation/skew effects for authentic look
- Implement text alignment (left, center, right)
- Add border/frame options
- Create PDF output option
- Add signature generation
- Support for multiple fonts in same image
- Batch processing mode
- Real-time preview

## License

Open source - Free to use and modify for personal and educational purposes.
