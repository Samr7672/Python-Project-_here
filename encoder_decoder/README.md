# Encoder Decoder

A GUI-based text encryption and decryption application using the Vigenère cipher combined with Base64 encoding for secure message protection.

## Features

- 🔐 **Vigenère Cipher Encryption**: Encodes messages using a private key
- 🔓 **Vigenère Cipher Decryption**: Decodes encrypted messages with the correct key
- 🔑 **Private Key Protection**: Uses a private key to encrypt/decrypt messages
- 🖥️ **User-friendly GUI**: Built with Tkinter for easy interaction
- 📋 **Base64 Encoding**: Additional layer of encoding for security
- 🔄 **Reset Function**: Clear all fields with one click
- ❌ **Easy Exit**: Close application without hassle

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- base64 module (standard library)

## Installation

No external packages needed! Both Tkinter and base64 come with Python by default.

## Usage

1. Run the application:
```bash
python encoder_decoder.py
```

2. A GUI window will open with input fields:
   - **MESSAGE**: Enter the text you want to encode/decode
   - **KEY**: Enter a private key (password) for encryption/decryption
   - **MODE**: Enter 'e' for encode or 'd' for decode

3. Click **RESULT** to process your message

4. The encoded/decoded message will appear in the Result field

5. Use **RESET** to clear all fields or **EXIT** to close the application

## How It Works

### Encoding Process
1. Takes your message and a private key
2. For each character in the message:
   - Gets the corresponding key character (cycles through key)
   - Adds the ASCII values of message char and key char
   - Applies modulo 256 to keep it in byte range
   - Converts back to character
3. Encodes the result using Base64 for safe transmission/storage

### Decoding Process
1. Takes an encoded message and the private key
2. Decodes from Base64 format first
3. For each character in the decoded message:
   - Gets the corresponding key character (cycles through key)
   - Subtracts the ASCII value of key char from message char
   - Applies modulo 256 to keep it in byte range
   - Converts back to character
4. Returns the original plaintext message

## How to Use - Step by Step

### Encoding a Message

```
1. Open the application
2. Enter MESSAGE: "Hello World"
3. Enter KEY: "secret"
4. Enter MODE: "e"
5. Click RESULT
6. Result: "GawZDQsGHg5FFBsVCQ==" (encoded message)
```

### Decoding a Message

```
1. Open the application
2. Enter MESSAGE: "GawZDQsGHg5FFBsVCQ==" (encoded message)
3. Enter KEY: "secret" (same key used for encoding)
4. Enter MODE: "d"
5. Click RESULT
6. Result: "Hello World" (decoded message)
```

## Important Notes

⚠️ **Key Requirement**: The key used for decoding MUST be the exact same key used for encoding, or the message cannot be properly decoded.

⚠️ **Key Cycling**: If your message is longer than your key, the key repeats. For example, with key "abc" and message "abcdef", it uses "abcabc".

⚠️ **Case Sensitive**: Keys are case-sensitive. "Secret" is different from "secret".

## GUI Components

| Field | Purpose | Input |
|-------|---------|-------|
| MESSAGE | Text to encode/decode | Any text |
| KEY | Encryption/decryption key | Any text (keep safe!) |
| MODE | Operation type | 'e' for encode, 'd' for decode |
| RESULT | Encoded/decoded output | Read-only (populated by clicking RESULT) |

## Buttons

| Button | Function |
|--------|----------|
| RESULT | Execute encoding/decoding operation |
| RESET | Clear all input and output fields |
| EXIT | Close the application |

## Security Considerations

- This implementation uses a simple Vigenère cipher - suitable for educational purposes
- For production use, consider industry-standard encryption (AES, RSA, etc.)
- Keep your private keys secure and never share them
- Base64 is encoding, not encryption - provides obfuscation only

## Troubleshooting

- **Invalid Mode Error**: Make sure you enter 'e' (lowercase) for encode or 'd' (lowercase) for decode
- **Decoding doesn't work**: Verify you're using the exact same key that was used for encoding
- **Application won't start**: Ensure Tkinter is installed and working
- **Wrong output**: Check for typos in the message, key, or mode

## Future Enhancements

- Add multiple encryption algorithms (AES, RSA)
- Save encrypted messages to files
- Load encrypted messages from files
- Copy-to-clipboard functionality for results
- Display encryption strength indicator
- Add support for file encryption/decryption
- Implement key generation tool
- Add visual feedback for operation status
- Support for multiple languages

## License

Open source - Free to use and modify for educational purposes.
