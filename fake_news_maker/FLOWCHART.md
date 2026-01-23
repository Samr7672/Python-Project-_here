# Fake News Generator - Flowchart

## Main Program Flow

```
                        START
                          |
                          v
                Import random module
                          |
                          v
            Initialize 4 Lists:
            - intros (7 items)
            - subjects_list (9 items)
            - actions_list (9 items)
            - consequences_list (8 items)
                          |
                          v
              Print Welcome Message:
         "The fake News Generator
          (Press Ctrl+C to stop)"
                          |
                          v
                    INFINITE LOOP
                    while True:
                          |
            ______________|______________
           |                             |
           v                             v
    Loop Body                     Ctrl+C Pressed
           |                             |
           v                             v
   ┌───────────────────────┐    Exception Handler
   │ Generate Headline     │          |
   │                       │          v
   │ 1. Random intro       │    Program Exits
   │ 2. Random subject     │    Gracefully
   │ 3. Random action      │          |
   │ 4. Random consequence │          v
   └───────────────────────┘       END
           |
           v
    Combine into f-string:
  "{intro} {subject} {action} {consequence}"
           |
           v
    Print newline + headline
           |
           v
    Print separator line
         (50 dashes)
           |
           v
    Ask user input:
  "Press Enter for more
   breaking news..."
           |
           v
      User presses Enter
           |
           v
    Back to top of loop
        (repeat)
```

## Headline Generation Process

```
┌────────────────────────────────────────────┐
│     HEADLINE GENERATION SEQUENCE           │
└────────────────────────────────────────────┘

Step 1: Select Random Intro
   Random.choice(intros)
   └─→ Returns 1 of 7 options
           |
Step 2: Select Random Subject
   Random.choice(subjects_list)
   └─→ Returns 1 of 9 options
           |
Step 3: Select Random Action
   Random.choice(actions_list)
   └─→ Returns 1 of 9 options
           |
Step 4: Select Random Consequence
   Random.choice(consequences_list)
   └─→ Returns 1 of 8 options
           |
Step 5: Combine All
   f-string: "{intro} {subject} {action} {consequence}"
           |
Step 6: Display Result
   - Print blank line
   - Print complete headline
   - Print separator (50 dashes)
```

## Random Selection Detail

```
┌─────────────────────────┐
│   random.choice(list)   │
├─────────────────────────┤
│ Function: Picks one     │
│ random item from list   │
│                         │
│ Example:                │
│ intros = [              │
│   "BREAKING NEWS:",     │
│   "SHOCKING REPORT:",   │
│   "JUST IN:",           │
│   "SCIENTISTS CONFIRM:",│
│   "VIRAL UPDATE:",      │
│   "SOURCES SAY:",       │
│   "UNBELIEVABLE:"       │
│ ]                       │
│                         │
│ Result: One random      │
│ option from the list    │
└─────────────────────────┘
```

## Loop Execution Detail

```
                   Iteration 1
                      |
        ┌─────────────────────────┐
        │ Generate Headline #1    │
        │ Display Headline #1     │
        └─────────────────────────┘
                      |
                      v
              User presses Enter
                      |
                      v
                   Iteration 2
                      |
        ┌─────────────────────────┐
        │ Generate Headline #2    │
        │ Display Headline #2     │
        └─────────────────────────┘
                      |
                      v
              User presses Enter
                      |
                      v
                   Iteration 3
                      |
        ┌─────────────────────────┐
        │ Generate Headline #3    │
        │ Display Headline #3     │
        └─────────────────────────┘
                      |
                      v
              User presses Enter
                      |
                      v
                   Continue...
                      |
                      v
              Ctrl+C pressed
                      |
                      v
              Exception caught
                      |
                      v
                    STOP
```

## User Interaction Flow

```
┌────────────────────────────────────┐
│         PROGRAM START              │
└────────────────────────────────────┘
           |
           v
┌────────────────────────────────────┐
│   Display Welcome Message          │
│  "The fake News Generator..."      │
└────────────────────────────────────┘
           |
           v
┌────────────────────────────────────┐
│   Generate & Display Headline #1   │
└────────────────────────────────────┘
           |
           v
┌────────────────────────────────────┐
│  Prompt: Press Enter for more...   │
└────────────────────────────────────┘
           |
    _______|_______
   |               |
   v               v
User             User
Presses Enter    Presses Ctrl+C
   |               |
   v               v
Continue        Exception
Loop            Handler
   |               |
   v               v
Generate        Graceful
Next            Exit
Headline           |
   |               v
   |            Program
   |            Ends
   |
   └─→ Back to prompt
       (repeat cycle)
```

## Data Flow Diagram

```
┌─────────────────────────┐
│   4 Lists Initialized   │
├─────────────────────────┤
│ • intros[]              │
│ • subjects_list[]       │
│ • actions_list[]        │
│ • consequences_list[]   │
└─────────────────────────┘
           |
           v
┌─────────────────────────┐
│  Random Selection       │
├─────────────────────────┤
│ Each iteration picks:   │
│ • 1 intro              │
│ • 1 subject            │
│ • 1 action             │
│ • 1 consequence        │
└─────────────────────────┘
           |
           v
┌─────────────────────────┐
│  String Combination     │
├─────────────────────────┤
│  f-string formatting    │
│  combines all 4         │
│  components into        │
│  single headline        │
└─────────────────────────┘
           |
           v
┌─────────────────────────┐
│  Output Display         │
├─────────────────────────┤
│ • Blank line           │
│ • Complete headline    │
│ • Separator line       │
│ • User prompt          │
└─────────────────────────┘
           |
           v
┌─────────────────────────┐
│   Wait for Input        │
├─────────────────────────┤
│ User presses Enter or   │
│ Ctrl+C to exit         │
└─────────────────────────┘
```

## Combination Calculation

```
Total Possible Headlines = Intros × Subjects × Actions × Consequences
                         = 7 × 9 × 9 × 8
                         = 4,536 unique combinations

This means the generator can create
4,536 different unique fake news headlines!

Example combinations:
   Intro (1/7) × Subject (1/9) × Action (1/9) × Consequence (1/8)
        |             |              |                 |
        v             v              v                 v
  "BREAKING NEWS:" × "A local" × "accidentally" × "in a traffic"
                      "Chaiwala"  "invents"      "jam."
                                  "invisible"
                                  "samosas"
```

## Sample Execution Trace

```
Iteration 1:
   intro = "BREAKING NEWS:" (random choice from intros)
   subject = "A Bollywood Star" (random choice from subjects_list)
   action = "bans gravity for 24 hours" (random choice from actions_list)
   consequence = "during a live TV debate." (random choice from consequences_list)
   
   headline = "BREAKING NEWS: A Bollywood Star bans gravity for 24 hours during a live TV debate."
   
   OUTPUT:
   BREAKING NEWS: A Bollywood Star bans gravity for 24 hours during a live TV debate.
   --------------------------------------------------
   
   Input: "Press Enter for more breaking news..."

Iteration 2:
   intro = "SHOCKING REPORT:" (different random)
   subject = "An AI Robot" (different random)
   action = "finds a secret tunnel to Mars" (different random)
   consequence = "and now everyone is confused." (different random)
   
   headline = "SHOCKING REPORT: An AI Robot finds a secret tunnel to Mars and now everyone is confused."
   
   OUTPUT:
   SHOCKING REPORT: An AI Robot finds a secret tunnel to Mars and now everyone is confused.
   --------------------------------------------------
   
   Input: "Press Enter for more breaking news..."

(Continue until Ctrl+C is pressed...)
```

## Exception Handling

```
                   Normal Execution
                         |
                    while True:
                         |
              ____________|____________
             |                        |
             v                        v
       User Presses Enter     User Presses Ctrl+C
             |                        |
             v                        v
       Continue Loop         KeyboardInterrupt
             |               Exception Raised
             |                        |
             v                        v
       Generate Next            Program Exits
       Headline                  Gracefully
             |                        |
             v                        v
         Display            No error message
             |               (clean exit)
             v
         Back to wait
         for input
```
