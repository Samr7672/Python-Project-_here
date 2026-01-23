# AI Chatbot (Peter) - Flowchart

```
                            START
                              |
                              v
                    Say "Hey Peter"
                         |
                         v
                    Recognition Failed?
                    /               \
                  Yes               No
                   |                 |
                   v                 v
            Print Message      Initialize Loop
         "Not Activated"       
                   |            
                   v            
                  END
                              |
                              v
                        Listen for Command
                              |
                              v
                        Recognize Command
                              |
                  ____________|____________
                 |             |            |
                 v             v            v
           Check Command   Unknown Command  Done?
              Match            |            |
           /    |    \         v            |
          /     |     \    Wait 5 sec   "Exit" in
         /      |      \       |         Command
        /       |       \      |           |
       v        v        v     |           v
   Condition Condition Condition|      Say "Thank You"
       1        2         3     |           |
       |        |         |     v           v
       v        v         v   Loop     END
   Action1  Action2   Action3  Back
       |        |         |
       v        v         v
   Execute  Execute   Execute
   Commands Commands  Commands
       |        |         |
       |________|_________|
              |
              v
           Speak Response
              |
              v
           Wait 5 seconds
              |
              v
           Loop Back to
        "Listen for Command"
```

## Command Flow Details

### Main Flow
```
START
  ↓
Wait for Activation: "Hey Peter"
  ↓
Enter Command Loop
  ├─ Listen for Audio
  ├─ Convert Speech to Text
  ├─ Check Command
  │  ├─ Name → Respond with "My name is Samr"
  │  ├─ Age → Respond with "I am twenty years old"
  │  ├─ Time → Get current time → Respond
  │  ├─ Open YouTube → Launch browser
  │  ├─ Open Webpage → Launch GitHub
  │  ├─ Joke → Generate joke → Speak
  │  ├─ Play Song → Start Music Player
  │  └─ Exit → Speak goodbye → Break loop
  ├─ Wait 5 seconds
  └─ Repeat loop
  ↓
END
```

## Processing Pipeline

```
┌─────────────────────────────────────────────┐
│         SPEECH RECOGNITION FLOW             │
└─────────────────────────────────────────────┘
         User speaks → Microphone
              ↓
      Record Audio Stream
              ↓
     Reduce Background Noise
              ↓
     Send to Google API
              ↓
      Convert to Text
              ↓
        Recognition Error?
        /              \
      Yes              No
       ↓                ↓
   Return ""     Return Text Data
       ↓                ↓
    Continue      Process Command

┌─────────────────────────────────────────────┐
│         TEXT-TO-SPEECH FLOW                 │
└─────────────────────────────────────────────┘
    Initialize Engine
         ↓
   Set Voice (Male/Female)
         ↓
   Set Speaking Rate
         ↓
   Generate Speech
         ↓
   Play Audio Output
         ↓
        Done
```
