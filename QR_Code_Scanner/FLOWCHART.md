# QR Code Scanner & Generator - Flowchart

## Version 1 - Simple QR Code Generator Flow

```
                        START
                          |
                          v
                 Import qrcode module
                          |
                          v
            Create QR code from URL/text
              qr.make("https://...")
                          |
                          v
          Store image object in variable
                    img = result
                          |
                          v
           Save image to PNG file
             img.save("filename.png")
                          |
                          v
                        END
         (PNG file created in directory)
```

## Version 2 - Advanced QR Code Generator Flow

```
                        START
                          |
                          v
                 Import qrcode module
                          |
                          v
                 Import PIL (Pillow)
                          |
                          v
         Create QRCode object with
            custom parameters:
          ├─ version = 1
          ├─ error_correction = H (30%)
          ├─ box_size = 20 (pixels)
          └─ border = 8 (boxes)
                          |
                          v
         Add data to QR code
         qrcode.add_data("URL/text")
                          |
                          v
         Generate QR code
         qrcode.make(fit=True)
                          |
                          v
        Create image with custom colors
         ├─ fill_color = "Blue"
         └─ back_color = "Black"
                          |
                          v
        Save image to PNG file
         img.save("filename.png")
                          |
                          v
                        END
         (Custom colored PNG file created)
```

## QRCode Initialization Process

```
┌──────────────────────────────────────┐
│    Create QRCode Object              │
├──────────────────────────────────────┤
│  qr.QRCode(                          │
│    version=1,                        │
│    error_correction=                 │
│      qr.constants.ERROR_CORRECT_H,   │
│    box_size=20,                      │
│    border=8                          │
│  )                                   │
└──────────────────────────────────────┘
            |
            v
┌──────────────────────────────────────┐
│   Parameter Application              │
├──────────────────────────────────────┤
│ ✓ Version set to 1                   │
│ ✓ Error correction at 30%            │
│ ✓ Each box = 20 pixels               │
│ ✓ Border = 8 boxes                   │
└──────────────────────────────────────┘
            |
            v
┌──────────────────────────────────────┐
│  QRCode Object Ready                 │
│  (waiting for data)                  │
└──────────────────────────────────────┘
```

## Data Addition & Generation Process

```
            add_data() Called
            with URL/text
                    |
                    v
         ┌──────────────────┐
         │  Data Validation │
         └──────────────────┘
                    |
                    v
         ┌──────────────────┐
         │  Encode Data     │
         │  to Binary       │
         └──────────────────┘
                    |
                    v
         ┌──────────────────┐
         │  Apply Error     │
         │  Correction      │
         │  (30% recovery)  │
         └──────────────────┘
                    |
                    v
         ┌──────────────────┐
         │  Generate QR     │
         │  Pattern         │
         └──────────────────┘
                    |
                    v
         ┌──────────────────┐
         │  Ready to        │
         │  Render Image    │
         └──────────────────┘
```

## Image Creation & Saving Flow

```
         make_image() Called
         with color options
                    |
                    v
      ┌────────────────────────┐
      │  Create Image Buffer   │
      │  (pixel canvas)        │
      └────────────────────────┘
                    |
                    v
      ┌────────────────────────┐
      │  Apply Background Color│
      │  fill entire canvas    │
      │  (back_color = Black)  │
      └────────────────────────┘
                    |
                    v
      ┌────────────────────────┐
      │  Draw QR Pattern       │
      │  using fill_color      │
      │  (fill_color = Blue)   │
      └────────────────────────┘
                    |
                    v
      ┌────────────────────────┐
      │  Image Object Created  │
      │  (ready to save)       │
      └────────────────────────┘
                    |
                    v
         save(filename) Called
                    |
                    v
      ┌────────────────────────┐
      │  Convert Image to PNG  │
      │  Format                │
      └────────────────────────┘
                    |
                    v
      ┌────────────────────────┐
      │  Write to File         │
      │  in current directory  │
      └────────────────────────┘
                    |
                    v
      ┌────────────────────────┐
      │  File Successfully     │
      │  Saved                 │
      └────────────────────────┘
```

## Version 1 Complete Execution

```
START
  |
  v
Import qrcode as qr
  |
  v
qr.make("https://github.com/Samr7672")
  |
  v
Creates default QR code
(Black pattern on white background)
  |
  v
Store in variable: img
  |
  v
img.save("my github account.png")
  |
  v
File saved to disk
  |
  v
END

Result: "my github account.png"
- Simple black and white QR code
- Default size and quality
- Readable by any QR scanner
```

## Version 2 Complete Execution

```
START
  |
  v
Import qrcode as qr
  |
  v
Import Image from PIL
  |
  v
Create QRCode object
├─ version=1 (controls QR size)
├─ error_correction=ERROR_CORRECT_H (30%)
├─ box_size=20 (pixel size of each box)
└─ border=8 (quiet zone)
  |
  v
Add data: "https://github.com/Samr7672"
  |
  v
Encode & apply error correction
  |
  v
Generate QR code pattern
  |
  v
Make image with parameters
├─ fill_color="Blue" (QR pattern color)
└─ back_color="Black" (background color)
  |
  v
Create image object: img
  |
  v
Save as PNG: "my github account -v2.png"
  |
  v
File saved to disk
  |
  v
END

Result: "my github account -v2.png"
- Blue QR code on black background
- Custom sized with box_size=20
- Border of 8 boxes around pattern
- High error correction (30%)
```

## Parameter Impact Flowchart

```
Version Parameter Impact
     |
     v
version=1 → Small QR, ~41 bytes
version=2 → Larger QR, ~34 bytes per char
version=3 → Even larger, more data
     |
     v
Choose based on:
- Amount of data
- Desired final size
- Print resolution needed

Box Size Impact
     |
     v
box_size=10 → Smaller pixels (compact)
box_size=20 → Medium pixels (balanced)
box_size=30 → Larger pixels (visibility)
     |
     v
Choose based on:
- Print resolution
- Scanning distance
- Final image size

Border Impact
     |
     v
border=1-3 → Minimal quiet zone
border=4 (std) → Standard spacing
border=8 → Large spacing
     |
     v
Choose based on:
- Proximity to other elements
- Scanning environment
- Design requirements
```

## Error Correction Levels

```
                ERROR_CORRECT_L
                    (7%)
                      |
           Can recover ~7% of lost data
                      |
                ERROR_CORRECT_M
                   (15%)
                      |
           Can recover ~15% of lost data
                      |
                ERROR_CORRECT_Q
                   (25%)
                      |
           Can recover ~25% of lost data
                      |
                ERROR_CORRECT_H
                   (30%)
                      |
           Can recover ~30% of lost data
           (Used in Version 2)
                      |
    Choose higher level for:
    - Printed materials that may get dirty
    - Outdoor QR codes exposed to weather
    - Long-term archival use
```

## Color Selection Process

```
When creating image with custom colors:

        make_image(fill_color, back_color)
                        |
                        v
                Choose colors
                   /    |    \
                  /     |     \
                 v      v      v
            Named   Hex     RGB
            Colors  Codes   Tuples
             |       |        |
        "Blue"  "#FF00" (255,0,0)
        "Red"   "#00FF" (0,255,0)
        "White" "#0000" (0,0,255)
             |       |        |
             v       v        v
        Color value determined
                    |
                    v
        Applied to QR pattern
        and background
                    |
                    v
        Final colored image created
```

## File Output Flowchart

```
┌────────────────────────────────┐
│  QR Code Generated             │
│  (exists in memory)            │
└────────────────────────────────┘
            |
            v
┌────────────────────────────────┐
│  save(filename) Called         │
│  Example: "my github account.png"
└────────────────────────────────┘
            |
            v
┌────────────────────────────────┐
│  PNG Encoding Process          │
│  - Compress image data         │
│  - Create PNG headers          │
│  - Prepare file structure      │
└────────────────────────────────┘
            |
            v
┌────────────────────────────────┐
│  File Write to Disk            │
│  Location: Current Directory   │
│  Name: "my github account.png" │
└────────────────────────────────┘
            |
            v
┌────────────────────────────────┐
│  File Successfully Created     │
│                                │
│  Can now be:                   │
│  - Printed                     │
│  - Shared digitally            │
│  - Displayed on screens        │
│  - Scanned with QR readers     │
└────────────────────────────────┘
```

## Comparison Flow - V1 vs V2

```
                START
                  |
           _______|_______
          |               |
          v               v
       V1 SIMPLE      V2 ADVANCED
          |               |
          v               v
    Quick generation  Customizable
    Limited control   Full control
    Default colors    Custom colors
    Default size      Custom size
    Black & White     Any color combo
          |               |
          v               v
    Save PNG          Save PNG
          |               |
    my github      my github
    account.png    account -v2.png
          |               |
          v               v
        Output: Simple     Output: Styled
        B&W QR Code       Blue/Black QR
```

## Processing Pipeline

```
┌──────────────────────────────────────┐
│        INPUT STAGE                   │
├──────────────────────────────────────┤
│ URL or Text String                   │
│ "https://github.com/Samr7672"        │
└──────────────────────────────────────┘
                |
                v
┌──────────────────────────────────────┐
│        ENCODING STAGE                │
├──────────────────────────────────────┤
│ Convert to binary                    │
│ Add error correction codes (30%)     │
│ Create QR pattern matrix             │
└──────────────────────────────────────┘
                |
                v
┌──────────────────────────────────────┐
│        GENERATION STAGE              │
├──────────────────────────────────────┤
│ Generate visual pattern              │
│ Apply color scheme                   │
│ Create image buffer                  │
└──────────────────────────────────────┘
                |
                v
┌──────────────────────────────────────┐
│        OUTPUT STAGE                  │
├──────────────────────────────────────┤
│ PNG Encoding                         │
│ File writing to disk                 │
│ Save to current directory            │
└──────────────────────────────────────┘
                |
                v
┌──────────────────────────────────────┐
│        END RESULT                    │
├──────────────────────────────────────┤
│ PNG file ready for use               │
│ Scannable QR code                    │
│ 30% error recovery capability        │
└──────────────────────────────────────┘
```
