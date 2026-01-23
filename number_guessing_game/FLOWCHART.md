# Number Guessing Game - Flowchart

## Main Game Flow

```
                        START
                          |
                          v
                   Display Logo
                   (from art.py)
                          |
                          v
            Display Welcome Message:
          "Welcome to the Number
           Guessing Game!"
          "I'm thinking of a number
           between 1 and 100."
                          |
                          v
              Generate Random Number
                   (1 to 100)
                  answer = randint(1, 100)
                          |
                          v
                Call set_difficulty()
                          |
                          |
                    (See below)
                          |
                          v
            Get number of turns:
            - Easy: 10 attempts
            - Hard: 5 attempts
                          |
                          v
                   Initialize guess = 0
                          |
                          v
        ┌─────────────────────────────┐
        │    MAIN GAME LOOP           │
        │    while guess != answer    │
        └─────────────────────────────┘
                          |
                          v
         Display remaining attempts
         f"You have {turns} attempts
          remaining to guess the number."
                          |
                          v
         Get player's guess
         guess = int(input("Make a guess: "))
                          |
                          v
         Call check_answer(guess, answer, turns)
                          |
                    (See below)
                          |
                          v
             Check if turns == 0
              /                  \
            Yes                   No
             |                     |
             v                     v
        Player Lost          Check if guess
        Print:            == answer
        "You've run             /        \
        out of guesses,       Yes        No
        you lose."             |          |
             |                 v          v
             |            Player Won   Continue
             |            Print:       Loop
             |            "You got it! Prompt:
             |            The answer   "Guess
             |            was {answer}" again."
             |                 |          |
             |                 |    Back to loop
             |                 |
             |_________________|
                     |
                     v
                   RETURN
                   (End Game)
                     |
                     v
                    END
```

## Set Difficulty Function Flow

```
              set_difficulty()
                   Called
                     |
                     v
        Prompt user:
      "Choose a difficulty.
       Type 'easy' or 'hard': "
                     |
                     v
          Get user input:
             level = input()
                     |
                     v
            Check level value
              /              \
           "easy"            else
             |                 |
             v                 v
        Return 10          Return 5
     (EASY_LEVEL_TURNS) (HARD_LEVEL_TURNS)
             |                 |
             |_________________|
                     |
                     v
              Back to game()
              (turns now set)
```

## Check Answer Function Flow

```
          check_answer(guess, answer, turns)
                   Called
                     |
                     v
          Compare guess to answer
                     |
            _________|_________
           |         |         |
           v         v         v
        guess >   guess <   guess ==
        answer    answer    answer
           |         |         |
           v         v         v
       Print      Print      Print
       "Too      "Too       "You got it!
        high."    low."      The answer
           |         |      was {answer}."
           |         |         |
           v         v         v
       Decrement turns
         turns - 1
           |         |
           |_________|
                |
                v
            Return turns
             (updated)
                |
                v
         Back to game()
```

## Complete Game Sequence

```
Step 1: START
        └─→ Display logo

Step 2: WELCOME
        └─→ Display game intro
        
Step 3: RANDOM NUMBER
        └─→ Computer picks number 1-100

Step 4: DIFFICULTY
        └─→ User chooses easy (10) or hard (5)

Step 5: GAME LOOP START
        
Step 6: DISPLAY ATTEMPTS
        └─→ Show remaining tries
        
Step 7: GET GUESS
        └─→ Player enters a number
        
Step 8: CHECK ANSWER
        ├─→ Compare to actual number
        ├─→ Give feedback
        └─→ Update attempts
        
Step 9: CHECK WIN/LOSS
        ├─→ If correct: WIN (end game)
        ├─→ If 0 attempts: LOSS (end game)
        └─→ If neither: continue loop
        
Step 10: END
         └─→ Display result
```

## User Input & Decision Tree

```
              Game Starts
                    |
                    v
         set_difficulty() called
                    |
        Input: easy or hard
                /        \
              easy       hard
               /          \
              /            \
             v              v
        turns = 10      turns = 5
             |              |
             |______________|
                    |
                    v
           Main Game Loop
              (while True)
                    |
        ___________|____________
       |                        |
       v                        v
    Get guess input      Check conditions
       |                        |
       v                        v
    int(input())         guess == answer?
       |                   /        \
       v                Yes         No
    Compare value        |           |
       |                 v           v
       v            WIN         turns == 0?
    Feedback:        |           /      \
    Too high/low/    |         Yes       No
    Correct          |          |         |
       |             |          v         v
       v             |       LOSS     Continue
    Update turns     |        |        Loop
       |             |        |         |
       |_____________|________|_________|
                     |
                     v
                   EXIT
                  (Return)
```

## Turn Management Flow

```
           Initial turns
         (from difficulty)
                |
              Easy: 10
              Hard: 5
                |
         _______|_______
        |               |
        v               v
    Make Guess 1   Make Guess 2
        |               |
    check_answer()  check_answer()
        |               |
    turns = 9       turns = 8
        |               |
        v               v
    Display 9       Display 8
        |               |
        v               v
    Guess again?   Guess again?
        |               |
    Continue...   Continue...

    This continues until:
    - turns == 0 (LOSE)
    - guess == answer (WIN)
    - Either condition stops the loop
```

## Example Gameplay Trace

```
Game State Progression - Easy Mode Win

┌─────────────────────────────────┐
│ Initialization                  │
├─────────────────────────────────┤
│ answer = 42 (randomly chosen)   │
│ turns = 10 (easy mode)          │
│ guess = 0                       │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ Round 1                         │
├─────────────────────────────────┤
│ Display: "You have 10 attempts" │
│ Player input: 50                │
│ check_answer: 50 > 42           │
│ Output: "Too high."             │
│ turns = 9                       │
│ guess != answer → Continue      │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ Round 2                         │
├─────────────────────────────────┤
│ Display: "You have 9 attempts"  │
│ Player input: 25                │
│ check_answer: 25 < 42           │
│ Output: "Too low."              │
│ turns = 8                       │
│ guess != answer → Continue      │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ Round 3                         │
├─────────────────────────────────┤
│ Display: "You have 8 attempts"  │
│ Player input: 37                │
│ check_answer: 37 < 42           │
│ Output: "Too low."              │
│ turns = 7                       │
│ guess != answer → Continue      │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ Round 4                         │
├─────────────────────────────────┤
│ Display: "You have 7 attempts"  │
│ Player input: 42                │
│ check_answer: 42 == 42          │
│ Output: "You got it!            │
│          The answer was 42."    │
│ guess == answer                 │
│ Loop terminates → WIN           │
└─────────────────────────────────┘
```

## Data Flow Diagram

```
┌──────────────────────┐
│   INITIALIZATION     │
├──────────────────────┤
│ answer (random)      │
│ turns (from input)   │
│ guess = 0            │
└──────────────────────┘
         |
         v
┌──────────────────────┐
│  GAME LOOP           │
├──────────────────────┤
│ Display turns        │
│ Get guess            │
│ Check guess vs answer│
└──────────────────────┘
         |
    _____|_____
   |          |
   v          v
 FEEDBACK  UPDATE
   |          |
   |    turns - 1
   |          |
   |__________|
        |
        v
   CHECK CONDITIONS
   ├─ guess == answer?
   │  └─→ WIN
   └─ turns == 0?
      └─→ LOSE
        |
        v
   RESULT
```

## Condition Evaluation Diagram

```
                 Main Loop
                (while guess != answer)
                      |
                ______|______
               |              |
               v              v
          Condition True   Condition False
          (guess != answer) (guess == answer)
               |              |
               v              v
          Continue       Exit Loop
          Execution      Game Ends
               |              |
          Process next   Check attempts
          guess           |
               |       ____|____
               |      |         |
               |      v         v
               |    All out?  Still trying?
               |     |          |
               |     v          v
               |   LOSE        WIN
               |     |          |
               |_____|__________|
                      |
                      v
                  DISPLAY RESULT
                  RETURN TO MAIN
```

## Difficulty Impact Flowchart

```
        User Chooses Difficulty
              |
         _____|_____
        |           |
        v           v
      easy         hard
        |           |
        v           v
    turns=10    turns=5
        |           |
        v           v
    Strategy:   Strategy:
    Can use    Must use
    trial &    efficient
    error      binary search
        |           |
        v           v
    10 attempts  5 attempts
    to find      to find
    answer       answer
        |           |
        v           v
    Higher      Lower
    chance      chance
    of winning  of winning
```
