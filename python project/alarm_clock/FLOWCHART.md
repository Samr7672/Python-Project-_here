# Alarm Clock Application - Flowchart

## Main Application Flow

```
                          START
                            |
                            v
                   Create Tkinter Window
                      (500x300 pixels)
                            |
                            v
                  Display Alarm Clock GUI
                            |
                ____________|____________
                |                       |
                v                       v
         Add Title Label      Add Time Selection
         "Alarm Clock"         Frame with Dropdowns
                |                  |
                v                  v
           Add Labels       Hour (00-24)
         "Set Time"         Minute (00-60)
                |           Second (00-60)
                v           |
              Frame      ___|___
                |       |       |
                v       v       v
            Initialize Initialize Initialize
            hour Var  minute Var second Var
                |       |       |
                |_______|_______|
                        |
                        v
                   Add "Set Alarm"
                    Button
                        |
                        v
                   Wait for User
                   to Click Button
                        |
                        v
                    User Clicks
                  "Set Alarm" Button
                        |
                        v
                Call Threading()
                        |
                        v
                   EVENT LOOP
                   (mainloop)
```

## Threading Function Flow

```
                    Threading() Called
                          |
                          v
                  Create New Thread
                    (target=alarm)
                          |
                          v
                      Start Thread
                    (t1.start())
                          |
                          v
        Alarm function runs in
         background (non-blocking)
                          |
                          v
                  Return to GUI
                 (GUI stays responsive)
```

## Alarm Checking Loop

```
                    alarm() Function
                    Starts Running
                          |
                          v
                    ________________
                   |                |
                   v                v
              Infinite         Sleep 1 Second
              Loop (while True)      |
                   ^                 |
                   |_________________|
                          |
                          v
                  Get Alarm Time
              set_alarm_time = HH:MM:SS
                   (from dropdowns)
                          |
                          v
                  Get Current Time
              current_time = HH:MM:SS
                   (system time)
                          |
                          v
                  Print Times to
                   Console (Debug)
                          |
                          v
              Compare Times
              current_time == set_alarm_time?
                   /              \
                Yes              No
                 |                 |
                 v                 v
         Print "Time to    Continue Loop
          Wake up"        (Check Again)
                 |           |
                 |___________|
                     |
                     v
                Back to Sleep
```

## Complete Execution Diagram

```
┌─────────────────────────────────────────┐
│       APPLICATION STARTUP               │
└─────────────────────────────────────────┘
            |
            v
    ┌───────────────┐
    │  Create GUI   │
    │   Window      │
    └───────────────┘
            |
            v
    ┌───────────────────────┐
    │  Display Dropdowns    │
    │  - Hour (00-24)       │
    │  - Minute (00-60)     │
    │  - Second (00-60)     │
    └───────────────────────┘
            |
            v
    ┌───────────────────────┐
    │  Display "Set Alarm"  │
    │      Button           │
    └───────────────────────┘
            |
            v
    ┌───────────────────────┐     ┌──────────────────┐
    │  Wait for Button      ├────→│ Button Clicked   │
    │  Click                │     └──────────────────┘
    └───────────────────────┘              |
                ^                          v
                |           ┌──────────────────────┐
                |           │ Create Background    │
                |           │ Thread               │
                |           └──────────────────────┘
                |                   |
                |                   v
    ┌───────────────────────┐  ┌──────────────────┐
    │  GUI Remains Responsive   │ Alarm Thread    │
    │  Accept More Input    │   │ Runs Continuously│
    └───────────────────────┘   └──────────────────┘
            |                            |
            |    ┌─────────────────┐     |
            |    │ Every 1 Second: │     |
            |    │ - Get curr time │     |
            |    │ - Check match   │     |
            |    │ - Print debug   │     |
            |    │ - Loop back     │     |
            |    └─────────────────┘     |
            |            |               |
            |            └───────────────┘
            |
            └──→ TIME MATCHES
                     |
                     v
            ┌─────────────────┐
            │ Print Message   │
            │ "Time to Wake up"
            │ to Console      │
            └─────────────────┘
                     |
                     v
                  Continue
                  Loop Running
```

## User Interaction Sequence

```
Step 1: Application starts
        └─ GUI window appears

Step 2: User selects alarm time
        ├─ Select hour from dropdown
        ├─ Select minute from dropdown
        └─ Select second from dropdown

Step 3: User clicks "Set Alarm" button
        └─ New thread is created

Step 4: Background thread monitors time
        └─ Checks every second

Step 5: When time matches
        ├─ Print "Time to Wake up" to console
        └─ Continue monitoring for next alarm

Step 6: Application remains running
        └─ Ready for another alarm to be set
```
