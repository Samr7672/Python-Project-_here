# Encoder Decoder - Flowchart

## Application Startup Flow

```
                        START
                          |
                          v
                  Create Tkinter Window
                    (500x300 pixels)
                          |
                          v
                   Set Window Title
                  "Encoder_Decoder"
                          |
                          v
                    Display Labels
                "ENCODE DECODE"
                "Encoder_Decoder"
                          |
                          v
              Initialize StringVar Variables
                    - Text (message)
                    - private_key (key)
                    - mode (e/d)
                    - Result (output)
                          |
                          v
                  Create Input Fields
                  ├─ MESSAGE field
                  ├─ KEY field
                  ├─ MODE field
                  └─ RESULT field
                          |
                          v
                  Create Buttons
                  ├─ RESULT button
                  ├─ RESET button
                  └─ EXIT button
                          |
                          v
                   Display GUI Window
                          |
                          v
                Wait for User Interaction
                    (mainloop)
```

## Mode Selection Flow

```
                    User Clicks RESULT
                           |
                           v
                      Mode() Function
                           |
                           v
                    Check mode.get()
                           |
                __________|__________
               |          |          |
               v          v          v
            'e'         'd'      Invalid
               |          |          |
               v          v          v
           Encode()   Decode()   Error Message
               |          |      "Invalid Mode"
               |          |          |
               |__________|__________|
                           |
                           v
                   Store in Result.set()
                           |
                           v
                Display Result in GUI
```

## Encoding Function Flow

```
┌─────────────────────────────────────┐
│       Encode(key, message)          │
└─────────────────────────────────────┘
              |
              v
        Create empty list: enc = []
              |
              v
     Loop through each character
     in the message (i = 0 to len)
              |
              v
     Get key character
     key_c = key[i % len(key)]
     (cycles through key)
              |
              v
     Calculate new character:
     ord(message[i]) + ord(key_c)
              |
              v
     Apply modulo 256
     to keep in byte range
              |
              v
     Convert back to character
     chr(value % 256)
              |
              v
     Append to enc list
              |
              v
     Next character
     (loop back if more)
              |
              v
     Join all characters
     into one string
              |
              v
     Encode with Base64
     urlsafe_b64encode()
              |
              v
     Return Base64 encoded result
              |
              v
        Display in GUI
```

## Decoding Function Flow

```
┌─────────────────────────────────────┐
│       Decode(key, message)          │
└─────────────────────────────────────┘
              |
              v
    Decode Base64 first
    base64.urlsafe_b64decode()
              |
              v
    Create empty list: dec = []
              |
              v
   Loop through each character
   in decoded message (i = 0 to len)
              |
              v
   Get key character
   key_c = key[i % len(key)]
   (cycles through key)
              |
              v
   Calculate original character:
   256 + ord(message[i]) - ord(key_c)
              |
              v
   Apply modulo 256
   to keep in byte range
              |
              v
   Convert back to character
   chr(value % 256)
              |
              v
   Append to dec list
              |
              v
   Next character
   (loop back if more)
              |
              v
   Join all characters
   into one string
              |
              v
   Return original plaintext
              |
              v
        Display in GUI
```

## Complete User Interaction Flow

```
┌──────────────────────────────┐
│   USER STARTS APPLICATION    │
└──────────────────────────────┘
             |
             v
┌──────────────────────────────┐
│   DISPLAY GUI WINDOW         │
├──────────────────────────────┤
│ - Message input field        │
│ - Key input field            │
│ - Mode input field (e/d)     │
│ - Result display field       │
│ - Buttons (RESULT/RESET/EXIT)│
└──────────────────────────────┘
             |
             v
┌──────────────────────────────┐
│  USER ENTERS DATA            │
├──────────────────────────────┤
│ 1. Type message in MESSAGE   │
│ 2. Type key in KEY           │
│ 3. Type 'e' or 'd' in MODE   │
└──────────────────────────────┘
             |
             v
┌──────────────────────────────┐
│   USER CLICKS BUTTON         │
├──────────────────────────────┤
│ Option 1: RESULT button      │
│ Option 2: RESET button       │
│ Option 3: EXIT button        │
└──────────────────────────────┘
          /  |  \
         /   |   \
        v    v    v
     RESULT RESET EXIT
       |     |     |
       v     v     v
    Process Clear  Close
    Message Fields Window
       |     |     |
       v     v     v
    Display Output App
    Result  Returns  Closes
    in GUI  Empty

    ├─→ If RESULT:
    │   ├─→ Get message, key, mode
    │   ├─→ If mode='e': Encode
    │   ├─→ If mode='d': Decode
    │   └─→ Display result
    │
    ├─→ If RESET:
    │   └─→ Clear all fields
    │
    └─→ If EXIT:
        └─→ Close application
```

## Vigenère Cipher Encoding Detail

```
MESSAGE: "Hello"
KEY:     "key"

Step 1: Prepare
   ├─ H (72) ← Message[0]
   ├─ k (107) ← Key[0 % 3]
   └─ Result: chr((72 + 107) % 256) = chr(179)

Step 2: Continue
   ├─ e (101) ← Message[1]
   ├─ e (101) ← Key[1 % 3]
   └─ Result: chr((101 + 101) % 256) = chr(202)

Step 3: Continue
   ├─ l (108) ← Message[2]
   ├─ y (121) ← Key[2 % 3]
   └─ Result: chr((108 + 121) % 256) = chr(229)

Step 4: Key cycles
   ├─ l (108) ← Message[3]
   ├─ k (107) ← Key[3 % 3] = Key[0]
   └─ Result: chr((108 + 107) % 256) = chr(215)

Step 5: Continue
   ├─ o (111) ← Message[4]
   ├─ e (101) ← Key[4 % 3] = Key[1]
   └─ Result: chr((111 + 101) % 256) = chr(212)

Final String: "Characters joined"
              ↓
         Base64 Encoding
              ↓
      Return Encoded Result
```

## Button Action Flows

### RESULT Button Flow
```
RESULT Button Clicked
        ↓
   Call Mode()
        ↓
   Get values:
   - message = Text.get()
   - key = private_key.get()
   - mode = mode.get()
        ↓
   Check mode value
   ├─ 'e' → Call Encode()
   ├─ 'd' → Call Decode()
   └─ else → "Invalid Mode"
        ↓
   Result.set(result_value)
        ↓
   Display in Result field
```

### RESET Button Flow
```
RESET Button Clicked
        ↓
   Call Reset()
        ↓
   Clear all fields:
   ├─ Text.set("")
   ├─ private_key.set("")
   ├─ mode.set("")
   └─ Result.set("")
        ↓
   All fields become empty
```

### EXIT Button Flow
```
EXIT Button Clicked
        ↓
   Call exit() function
        ↓
   root.destroy()
        ↓
   Close GUI window
        ↓
   Application terminates
```

## Data Flow in Application

```
USER INPUT
   ├─ Message (TEXT)
   ├─ Private Key (private_key)
   └─ Mode (mode)
        ↓
   PROCESSING LAYER
   ├─ Mode determination
   ├─ Function selection
   └─ Cipher operations
        ↓
   STRINGVAR VARIABLES
   ├─ Text variable
   ├─ private_key variable
   ├─ mode variable
   └─ Result variable
        ↓
   FUNCTIONS
   ├─ Encode() or Decode()
   ├─ Character manipulation
   ├─ Base64 processing
   └─ Return result
        ↓
   OUTPUT DISPLAY
   └─ Result field shows output
```
