# Text to Handwriting - Flowchart

## Main Program Flow

```
                        START
                          |
                          v
        Import Libraries
        ├─ PIL (Image, ImageDraw, ImageFont)
        ├─ textwrap (text wrapping)
        └─ os (file operations)
                          |
                          v
        Define text_to_handwriting_local() function
                          |
                          v
        Set text variable
        "Python is a high-level, interpreted..."
                          |
                          v
        Set font path
        r"C:\Users\...\my_nerve.ttf"
                          |
                          v
        Call function:
        text_to_handwriting_local(text, "demo.png", path_to_my_font)
                          |
                          v
        ┌────────────────────────────────┐
        │  TEXT TO HANDWRITING PROCESS   │
        └────────────────────────────────┘
                          |
                          v
                        END
```

## text_to_handwriting_local() Function Flow

```
    text_to_handwriting_local(text, output_file, 
                              font_path, font_size=30)
                          |
                          v
            ┌──────────────────────────────┐
            │  VALIDATION PHASE            │
            └──────────────────────────────┘
                          |
                          v
            Check if font file exists
            os.path.exists(font_path)
                    /            \
                  YES            NO
                   |              |
                   v              v
              Continue       PRINT ERROR
                   |         "CRITICAL ERROR:
                   |          Font not found..."
                   |              |
                   |              v
                   |          RETURN
                   |         (Function ends)
                   |
                   v
            ┌──────────────────────────────┐
            │  IMAGE CREATION PHASE        │
            └──────────────────────────────┘
                          |
                          v
            Create blank image
            Size: 1200 × 1500 pixels
            Color: White (255, 255, 255)
                          |
                          v
            Create drawing context
            ImageDraw.Draw(img)
                          |
                          v
            ┌──────────────────────────────┐
            │  FONT LOADING PHASE          │
            └──────────────────────────────┘
                          |
                          v
            Load TrueType font
            font_path + font_size (default: 30)
                          |
                          v
            ┌──────────────────────────────┐
            │  TEXT WRAPPING PHASE         │
            └──────────────────────────────┘
                          |
                          v
            Wrap text to 70 chars per line
            textwrap.wrap(text, width=70)
                          |
                          v
            Create lines list
            ['Line 1...', 'Line 2...', ...]
                          |
                          v
            ┌──────────────────────────────┐
            │  TEXT DRAWING PHASE          │
            └──────────────────────────────┘
                          |
                          v
            Initialize y position
            y_text = 50 (top margin)
                          |
                          v
                FOR EACH LINE:
                    |
                    v
            Draw line on image
            Position: (50, y_text)
            Color: Dark Blue (0, 0, 138)
            Font: Loaded font
                    |
                    v
            Move y position down
            y_text += font_size + 10
                    |
                    v
            Next line
                    |
                    v
            ┌──────────────────────────────┐
            │  FILE SAVING PHASE           │
            └──────────────────────────────┘
                          |
                          v
            Save image to file
            img.save(output_file)
                          |
                          v
            Print success message
            "SUCCESS: [filename] created!"
                          |
                          v
                        RETURN
```

## Font Validation Flow

```
                    START function
                          |
                          v
        Check: os.path.exists(font_path)
                    /              \
                  TRUE            FALSE
                   |                |
                   v                v
            Font found          Font missing
                   |                |
                   v                v
            Continue          Print error:
            with creation      "CRITICAL ERROR:
                   |           Font not found at
                   |           [path]"
                   |                |
                   v                v
            Create image           RETURN
            Load font              (abort)
            Draw text
                   |
                   v
            Save file
            Print success
                   |
                   v
            Return
```

## Image Creation Process

```
Step 1: Create Canvas
    Image.new('RGB', (1200, 1500), 
              color=(255, 255, 255))
        |
        v
    Blank white image created
    1200 pixels wide
    1500 pixels tall

Step 2: Prepare Drawing
    ImageDraw.Draw(img)
        |
        v
    Drawing object ready
    Can now draw text

Step 3: Load Font
    ImageFont.truetype(font_path, font_size)
        |
        v
    Font loaded with specified size

Step 4: All ready for text drawing
```

## Text Wrapping Process

```
            Original text:
    "Python is a high-level, interpreted
     programming language known for its
     clear syntax and readability, making..."
                |
                v
        textwrap.wrap(text, width=70)
                |
    Splits text every 70 characters
        (at word boundaries, not mid-word)
                |
                v
        Result - List of lines:
    [
      "Python is a high-level, interpreted",
      "programming language known for its",
      "clear syntax and readability,",
      "making it an excellent choice for",
      "both beginners and experienced",
      "developers..."
    ]
                |
                v
        Each line fits within canvas width
        with proper margins
```

## Text Drawing Loop

```
    lines = ['Line 1', 'Line 2', 'Line 3']
    y_text = 50
    
    ┌────────────────────────┐
    │  ITERATION 1           │
    ├────────────────────────┤
    │ Line: "Python is a..." │
    │ Y position: 50         │
    │ Draw at (50, 50)       │
    │ y_text = 50 + 30 + 10  │
    │ y_text = 90            │
    └────────────────────────┘
           |
           v
    ┌────────────────────────┐
    │  ITERATION 2           │
    ├────────────────────────┤
    │ Line: "programming..." │
    │ Y position: 90         │
    │ Draw at (50, 90)       │
    │ y_text = 90 + 30 + 10  │
    │ y_text = 130           │
    └────────────────────────┘
           |
           v
    ┌────────────────────────┐
    │  ITERATION 3           │
    ├────────────────────────┤
    │ Line: "clear syntax..." │
    │ Y position: 130        │
    │ Draw at (50, 130)      │
    │ y_text = 130 + 30 + 10 │
    │ y_text = 170           │
    └────────────────────────┘
           |
           v
    All lines drawn
    Ready to save
```

## Y Position Calculation

```
    First line:
    y_text = 50 (top margin)
    
    After drawing first line:
    y_text += 30 + 10 = 50 + 40 = 90
    
    After drawing second line:
    y_text += 30 + 10 = 90 + 40 = 130
    
    After drawing third line:
    y_text += 30 + 10 = 130 + 40 = 170
    
    Pattern:
    ├─ font_size = 30
    ├─ extra_spacing = 10
    ├─ total_increment = 40
    └─ Each line 40 pixels below previous
```

## File Saving and Confirmation

```
        All text drawn on image
                |
                v
        img.save("demo.png")
                |
        File written to disk
                |
                v
        Print success message:
        "SUCCESS: demo.png has been created!"
                |
                v
        Return from function
                |
                v
        File ready for viewing
```

## Complete Execution Trace

```
TIME: 0s
    └─ Script starts
       Imports executed

TIME: 0.1s
    └─ Function defined

TIME: 0.2s
    └─ text variable set
       path_to_my_font set

TIME: 0.3s
    └─ Function called with parameters:
       text = "Python is a..."
       output_file = "demo.png"
       font_path = "C:\...\my_nerve.ttf"
       font_size = 30

TIME: 0.4s
    └─ Check font exists: ✓

TIME: 0.5s
    └─ Create 1200×1500 white image

TIME: 0.6s
    └─ Load font (my_nerve.ttf, size 30)

TIME: 0.7s
    └─ Wrap text into 70-char lines
       Result: 8 lines

TIME: 0.8s
    └─ Begin drawing loop

TIME: 0.9s
    ├─ Draw line 1 at (50, 50)
    ├─ Draw line 2 at (50, 90)
    ├─ Draw line 3 at (50, 130)
    ├─ Draw line 4 at (50, 170)
    ├─ Draw line 5 at (50, 210)
    ├─ Draw line 6 at (50, 250)
    ├─ Draw line 7 at (50, 290)
    └─ Draw line 8 at (50, 330)

TIME: 1.0s
    └─ Save image to "demo.png"

TIME: 1.1s
    └─ Print: "SUCCESS: demo.png has been created!"

TIME: 1.2s
    └─ Function returns
       Script ends
```

## Data Flow Diagram

```
┌─────────────────────────┐
│   TEXT INPUT            │
│   "Python is a..."      │
└─────────────────────────┘
            |
            v
┌─────────────────────────┐
│   FONT FILE PATH        │
│   C:\...\my_nerve.ttf   │
└─────────────────────────┘
            |
            |____|_____
            |         |
            v         v
      VALIDATE    LOAD FONT
      EXISTS?       |
        |           v
        |       TrueType Font
        |       Size: 30
        |           |
        v           v
    ┌─────────────────────────┐
    │   TEXT WRAPPING         │
    │   (70 chars/line)       │
    └─────────────────────────┘
            |
            v
    ┌─────────────────────────┐
    │   CREATE CANVAS         │
    │   1200×1500 white       │
    └─────────────────────────┘
            |
            v
    ┌─────────────────────────┐
    │   DRAW EACH LINE        │
    │   Blue text (0,0,138)   │
    │   40px vertical gap     │
    └─────────────────────────┘
            |
            v
    ┌─────────────────────────┐
    │   SAVE IMAGE            │
    │   demo.png (PNG format) │
    └─────────────────────────┘
            |
            v
    ┌─────────────────────────┐
    │   OUTPUT FILE           │
    │   demo.png (~200KB)     │
    └─────────────────────────┘
```

## Canvas Layout Diagram

```
        0         50        1150      1200
        |         |          |        |
    0   ┌─────────┼──────────┬─────┐  
        │         |          |     │  
   50   │    Top  | TEXT     |     │  Margin: 50px
        │    Margin AREA      |     │  
        │         |          |     │  
  100   │    ┌────────────────┐     │  Line 1
        │    │Line 1 content  │     │  Height: 30
  140   │    └────────────────┘ Spacing: 10
        │         |          |     │  
  180   │    ┌────────────────┐     │  Line 2
        │    │Line 2 content  │     │  Height: 30
  220   │    └────────────────┘ Spacing: 10
        │         |          |     │  
  260   │    ┌────────────────┐     │  Line 3
        │    │Line 3 content  │     │  Height: 30
  ...   │    ...              │     │  ...
        │         |          |     │  
 1500   └─────────┴──────────┴─────┘  
        |         |          |        |

Width: 1200px
Height: 1500px
Text area: 50-1150px horizontal
           50-1450px vertical (approx)
Margins: 50px left, right, top
```

## Error Handling Flow

```
        text_to_handwriting_local() called
                    |
                    v
        Check: os.path.exists(font_path)
                /            \
              TRUE           FALSE
               |              |
               v              v
           Continue        PRINT:
           execution      "CRITICAL ERROR:
               |          Font not found at
               v          [path]"
           Create image       |
           Load font          v
           (Success)      RETURN
               |         (abort)
               v
           Draw text
               |
               v
           Save file
               |
               v
           PRINT:
           "SUCCESS: 
            [filename] 
            created!"
               |
               v
           RETURN
```

## Function Parameter Flow

```
    Function called:
    text_to_handwriting_local(
        text="Python is...",
        output_file="demo.png",
        font_path="C:\...\nerve.ttf",
        font_size=30  # default
    )
            |
            v
    Parameters stored locally:
    ├─ text: full text string
    ├─ output_file: target filename
    ├─ font_path: full path to .ttf
    └─ font_size: pixel size (30)
            |
            v
    Used throughout function:
    ├─ font_path: validate & load
    ├─ font_size: create font
    ├─ text: wrap & display
    └─ output_file: save image
```

## Text Rendering Pipeline

```
┌────────────────────┐
│  Input Text        │
│  (raw string)      │
└────────────────────┘
         |
         v
┌────────────────────┐
│  Text Wrapping     │
│  (70 chars/line)   │
└────────────────────┘
         |
         v
┌────────────────────┐
│  Line List         │
│  (multiple lines)  │
└────────────────────┘
         |
         v
┌────────────────────┐
│  For Each Line:    │
│  - Measure       │
│  - Position      │
│  - Render        │
└────────────────────┘
         |
         v
┌────────────────────┐
│  Rendered Image    │
│  (on canvas)       │
└────────────────────┘
         |
         v
┌────────────────────┐
│  PNG Encoding      │
│  (compression)     │
└────────────────────┘
         |
         v
┌────────────────────┐
│  Output File       │
│  demo.png saved    │
└────────────────────┘
```

## Color Processing

```
        Color specified as RGB tuple:
        (0, 0, 138) - Dark Blue
             |
             v
        ├─ R (Red): 0
        ├─ G (Green): 0
        └─ B (Blue): 138
             |
             v
        Applied to text:
        d.text((50, y), line, 
               fill=(0, 0, 138), font=font)
             |
             v
        Text rendered in dark blue
        On white background
```

## Success/Failure Outcomes

```
        Function execution
                |
        _______|_______
       |               |
       v               v
    SUCCESS          FAILURE
       |               |
       v               v
    ✓ Font exists   ✗ Font missing
    ✓ Image created ✗ Return early
    ✓ Text rendered ✗ No image
    ✓ File saved    ✗ No file
       |               |
       v               v
    Print:          Print:
    "SUCCESS:       "CRITICAL ERROR:
     demo.png       Font not found
     created!"      at [path]"
       |               |
       v               v
    File ready      Stop execution
    for viewing
```

## Performance Timeline

```
Task                    Time
────────────────────────────
Import libraries        0.1s
Define function         0.05s
Set variables           0.05s
Function call           -
  Validate font         0.1s
  Create image          0.1s
  Load font             0.2s
  Wrap text             0.05s
  Draw text             0.3s
  Save file             0.2s
  Print message         0.05s
Total execution         ~1.1s
```
