# QR Code Scanner & Generator

A Python application that generates QR codes from URLs and text. Includes two versions: a simple generator and an advanced customizable version with color and size options.

## Features

- 📱 **QR Code Generation**: Create QR codes from URLs and text strings
- 🎨 **Customizable Colors**: Choose custom fill and background colors
- 📏 **Adjustable Size**: Control box size and border width
- 🛡️ **Error Correction**: High error correction capability (ERROR_CORRECT_H)
- 💾 **Save to File**: Export generated QR codes as PNG images
- 🔗 **URL Support**: Embed URLs in QR codes for easy sharing
- ⚡ **Two Versions**: Simple version (v1) and advanced version (v2)

## Requirements

- Python 3.x
- `qrcode` - QR code generation library
- `Pillow (PIL)` - Image processing library

## Installation

1. Install required packages:
```bash
pip install qrcode[pil] pillow
```

Or install them separately:
```bash
pip install qrcode
pip install pillow
```

## Usage

### Version 1 - Simple QR Code Generator

**File**: `qr_code_v1.py`

This is the basic version that generates a simple QR code.

```python
import qrcode as qr

img = qr.make("https://github.com/Samr7672")
img.save("my github account.png")
```

**Run it:**
```bash
python qr_code_v1.py
```

**What it does:**
- Creates a QR code for the GitHub URL
- Saves it as `my github account.png`

### Version 2 - Advanced QR Code Generator

**File**: `qr_code-v2.py`

This advanced version offers customization options for appearance and error correction.

```python
import qrcode as qr
from PIL import Image

qrcode = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=20,
    border=8
)
qrcode.add_data("https://github.com/Samr7672")
qrcode.make(fit=True)
img = qrcode.make_image(fill_color="Blue", back_color="Black")
img.save("my github account -v2.png")
```

**Run it:**
```bash
python qr_code-v2.py
```

**What it does:**
- Creates a customized QR code
- Sets fill color to Blue and background to Black
- Saves as `my github account -v2.png`

## How It Works

### Version 1 Flow
1. Import qrcode library
2. Create QR code from URL/text
3. Save as PNG file

### Version 2 Flow
1. Import qrcode and Pillow libraries
2. Initialize QRCode object with parameters
3. Add data (URL or text)
4. Generate the QR code
5. Create image with custom colors
6. Save as PNG file

## QRCode Parameters Explained

### Version Parameter
- **version=1**: Controls the size of the QR code (1-40)
- Higher versions = larger QR codes = more data capacity
- version=1 can hold ~41 bytes of data

### Error Correction Levels

| Level | Constant | Recovery Capacity |
|-------|----------|------------------|
| Low (7%) | ERROR_CORRECT_L | ~7% data loss |
| Medium (15%) | ERROR_CORRECT_M | ~15% data loss |
| **High (30%)** | **ERROR_CORRECT_H** | **~30% data loss** |
| Quartile (25%) | ERROR_CORRECT_Q | ~25% data loss |

### Box Size
- **box_size=20**: Size of each "box" in the QR code (in pixels)
- Larger values = bigger QR code image
- Default is typically 10

### Border
- **border=8**: Quiet zone around QR code (in boxes, not pixels)
- Minimum recommended is 4
- Default is 4

### Colors
- **fill_color**: Color of the QR code pattern (default: black)
- **back_color**: Color of the background (default: white)
- Accepts color names: "Blue", "Red", "Green", etc.
- Accepts hex colors: "#FF0000" (red), "#00FF00" (green)

## Example Customizations

### Large Blue QR Code
```python
qrcode = qr.QRCode(version=2, box_size=30, border=4)
qrcode.add_data("Your URL here")
qrcode.make(fit=True)
img = qrcode.make_image(fill_color="Blue", back_color="White")
img.save("blue_qr.png")
```

### Red on Yellow
```python
qrcode = qr.QRCode(version=1, box_size=15, border=5)
qrcode.add_data("https://example.com")
qrcode.make(fit=True)
img = qrcode.make_image(fill_color="Red", back_color="Yellow")
img.save("red_yellow_qr.png")
```

### High Resolution
```python
qrcode = qr.QRCode(version=3, box_size=25, border=8)
qrcode.add_data("High res QR code")
qrcode.make(fit=True)
img = qrcode.make_image(fill_color="Black", back_color="White")
img.save("high_res_qr.png")
```

## Output Files

Both versions generate PNG image files:
- **v1 output**: `my github account.png` (simple black and white)
- **v2 output**: `my github account -v2.png` (blue on black)

The generated files can be:
- Printed on materials
- Displayed on screens
- Shared digitally
- Scanned with any QR code reader

## Color Names Supported

Common color names that work:
- Black, White
- Red, Green, Blue
- Yellow, Cyan, Magenta
- Orange, Purple, Pink
- Gray, Brown
- Lime, Navy, Teal

Or use hex color codes: `#FF5733`, `#33FF57`, etc.

## QR Code Data Capacity

| Data Type | Version 1 |
|-----------|-----------|
| Numeric | ~41 digits |
| Alphanumeric | ~25 characters |
| Byte | ~17 bytes |
| Kanji | ~10 characters |

For longer data, increase the version number.

## Troubleshooting

- **ModuleNotFoundError: No module named 'qrcode'**: Run `pip install qrcode[pil]`
- **ModuleNotFoundError: No module named 'PIL'**: Run `pip install pillow`
- **File not saving**: Check write permissions in the directory
- **Invalid color name**: Use standard color names or hex codes
- **QR code too small**: Increase box_size or version parameter

## Tips & Best Practices

✅ **Do this:**
- Use high error correction for print applications
- Test the QR code with your phone before printing
- Use high contrast colors (black on white, blue on yellow)
- Increase box_size for better readability

❌ **Don't do this:**
- Use similar colors for fill and background
- Make QR codes too small
- Use too many special characters
- Ignore the quiet zone (border)

## Advanced Features

### Dynamic QR Codes
Modify the data before making:
```python
qrcode = qr.QRCode(version=1)
qrcode.add_data("Your data here")
qrcode.make(fit=True)
qrcode.add_data("More data")  # Add more if needed
```

### Automatic Sizing
Use `fit=True` to automatically adjust version:
```python
qrcode.make(fit=True)  # Automatically picks best version
```

## Future Enhancements

- Add QR code reading/decoding functionality
- Create GUI interface for code generation
- Batch QR code generation from CSV
- Add pattern/style variations
- Create QR code with logo in center
- Add animation to QR codes
- Support for embedded images
- Add analytics tracking
- Create video QR codes

## Learning Concepts

This project teaches:
- **Library usage**: Working with qrcode and Pillow libraries
- **Error correction**: Understanding data redundancy
- **Image generation**: Creating images programmatically
- **Parameter tuning**: Adjusting code behavior
- **File I/O**: Saving files to disk
- **Data encoding**: How information is encoded in visual format

## License

Open source - Free to use and modify for personal and commercial projects.
