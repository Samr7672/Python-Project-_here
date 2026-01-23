# Rock Paper Scissors Game - Flowchart

## Main Game Flow

```
                        START
                          |
                          v
            Initialize Game Variables
                    ├─ done = False
                    ├─ win = 0
                    ├─ lose = 0
                    ├─ tie = 0
                    ├─ user_score = 0
                    ├─ computer_score = 0
                    └─ Setup dictionaries
                          |
                          v
        ┌─────────────────────────────┐
        │    MAIN GAME LOOP           │
        │    while not done:          │
        └─────────────────────────────┘
                          |
                          v
        Display prompt:
     "Enter a choice (R, P, S):
      and enter 'q' to quit"
                          |
                          v
        Get user input
        user_choice = input()
        Convert to uppercase
                          |
                          v
        Is user_choice == "Q"?
              /                \
            Yes                No
             |                  |
             v                  v
        Display Final     Get Computer
        Scores           Choice
        Break loop       (random)
             |                  |
             v                  v
        Game Ends      Display choices:
             |         "You chose X,
             |          computer chose Y"
             |                  |
             |                  v
             |         Check Result
             |         (Tie/Win/Loss)
             |                  |
             |      ____________|____________
             |     |            |            |
             |     v            v            v
             |    TIE          WIN          LOSS
             |     |            |            |
             |     v            v            v
             |  No points    +1 User     +1 Comp
             |  awarded      Score       Score
             |     |            |            |
             |     |____________|____________|
             |              |
             |              v
             |       Print Result Message
             |       with Current Scores
             |              |
             |              v
             |       Back to prompt
             |       (next round)
             |
             |
             └──────→ END
                   (Display final scores)
```

## Detailed Decision Tree

```
                    User Input
                        |
                    ______|_____
                   |            |
                   v            v
                  Q             Other
                   |            |
                   v            v
                QUIT       Computer selects
                   |       random R/P/S
                   v            |
            Display Final       v
            Scores          Compare
                |          /   |    \
                v        TIE  WIN  LOSS
             END          |    |     |
                          v    v     v
                      Check   Check Check
                      Conditions Conditions
                          |    |     |
                          v    v     v
                       Print Print Print
                       tie   win   loss
                      message message message
                          |    |     |
                          v    v     v
                       Count Count Count
                       outcomes scores
                          |    |     |
                          |____|_____|
                              |
                              v
                          Loop back
```

## Win/Loss/Tie Logic

```
                    Comparison Logic
                          |
          ________________|________________
         |                 |                |
         v                 v                v
    user == computer   user == loses[comp]  ELSE
         |                 |                |
         v                 v                v
        TIE              WIN              WIN
         |                 |                |
    No score         user_score += 1   user_score += 1
    awarded              win += 1           win += 1
         |                 |                |
         v                 v                v
    "It's a tie!"   "You win!"        "You win!"
```

## Score Tracking Process

```
        Initialize
        user_score = 0
        computer_score = 0
             |
             v
    ┌────────────────┐
    │ Round 1        │
    ├────────────────┤
    │ Outcome: Win   │
    │ user_score += 1│
    │ Result: 1      │
    └────────────────┘
             |
             v
    ┌────────────────┐
    │ Round 2        │
    ├────────────────┤
    │ Outcome: Loss  │
    │ comp_score += 1│
    │ Result: 1, 1   │
    └────────────────┘
             |
             v
    ┌────────────────┐
    │ Round 3        │
    ├────────────────┤
    │ Outcome: Tie   │
    │ No change      │
    │ Result: 1, 1   │
    └────────────────┘
             |
             v
        Continue...
```

## Input Processing Flow

```
            user_choice = input()
                    |
                    v
        Convert to uppercase
            .upper()
                    |
                    v
        Check if "Q"
            /        \
          Yes        No
           |          |
           v          v
        EXIT      Check if R/P/S
         |         /    |    \
         v        v     v     v
        END      R     P     S
                 |     |     |
                 v     v     v
              Valid Valid Valid
              Input Input Input
                 |     |     |
                 |_____|_____|
                       |
                       v
                  Use in game
                  comparison
```

## Complete Game Round

```
Step 1: Display prompt
        "Enter a choice (R, P, S):and enter 'q' to quit"

Step 2: Get user input
        user_choice = input()
        Example: user types "R"

Step 3: Check if quit
        user_choice == "Q"?
        Example: "R" ≠ "Q" → Continue

Step 4: Get computer choice
        computer_choice = random.choice(["R", "P", "S"])
        Example: computer gets "P"

Step 5: Display choices
        "You chose R, computer chose P"

Step 6: Determine outcome
        Compare R vs P
        Rock loses to Paper
        User loses!

Step 7: Update scores
        computer_score += 1
        Old: computer had 0 points
        New: computer has 1 point

Step 8: Display result
        "You lose! you choose R, computer chose P.
         You have 0 points and computer has 1 points"

Step 9: Loop back
        Back to Step 1
```

## Dictionary Lookup Flow

```
        loses Dictionary:
        ├─ "R" → "S" (Rock loses to Scissors)
        ├─ "P" → "R" (Paper loses to Rock)
        └─ "S" → "P" (Scissors loses to Paper)

        Computer chose "P"
             |
             v
        loses["P"] = "R"
             |
             v
        Computer's choice loses to "R"
             |
             v
        If user chose "R":
             user_choice == loses[computer_choice]
             "R" == "R"
             TRUE → User wins!
```

## Game Round Sequence Example

```
ROUND 1: Player wins
     |
     ├─ Player input: R
     ├─ Computer choice: S
     ├─ Rock beats Scissors
     ├─ user_score: 0 → 1
     ├─ computer_score: 0 (unchanged)
     └─ Display: "You win!"
          |
          v
ROUND 2: Tie
     |
     ├─ Player input: P
     ├─ Computer choice: P
     ├─ Same choice
     ├─ user_score: 1 (unchanged)
     ├─ computer_score: 0 (unchanged)
     └─ Display: "It's a tie!"
          |
          v
ROUND 3: Player loses
     |
     ├─ Player input: S
     ├─ Computer choice: R
     ├─ Rock beats Scissors
     ├─ user_score: 1 (unchanged)
     ├─ computer_score: 0 → 1
     └─ Display: "You lose!"
          |
          v
ROUND 4: Player quits
     |
     ├─ Player input: Q
     ├─ Final user_score: 1
     ├─ Final computer_score: 1
     └─ Display final scores and END
```

## Outcome Determination Matrix

```
            R        P        S
         ┌────────────────────────┐
    R    │  TIE    LOSE   WIN    │
         │ (same) (P>R) (R>S)    │
         ├────────────────────────┤
    P    │  WIN    TIE    LOSE   │
         │(P>R)  (same)  (S>P)   │
         ├────────────────────────┤
    S    │ LOSE   WIN    TIE     │
         │(R>S)  (S>P)  (same)   │
         └────────────────────────┘

Player | Computer | Result
   R   |    R     | TIE
   R   |    P     | LOSE (Paper covers Rock)
   R   |    S     | WIN (Rock crushes Scissors)
   P   |    R     | WIN (Paper covers Rock)
   P   |    P     | TIE
   P   |    S     | LOSE (Scissors cuts Paper)
   S   |    R     | LOSE (Rock crushes Scissors)
   S   |    P     | WIN (Scissors cuts Paper)
   S   |    S     | TIE
```

## Data Flow Diagram

```
INPUT
(User chooses R/P/S or Q)
     |
     v
PROCESSING
├─ Check if quit (Q)
├─ Get random computer choice
├─ Compare choices
├─ Determine outcome
└─ Update scores
     |
     v
STORAGE (Variables)
├─ user_score (updated if needed)
├─ computer_score (updated if needed)
├─ win/lose/tie counters
└─ Current round choices
     |
     v
OUTPUT
├─ Display choices made
├─ Display outcome
├─ Display current scores
└─ Prompt for next round
```

## Game Loop Control Flow

```
while not done:
     |
     v
Get user input
     |
     v
Is input "Q"?
    /       \
  YES       NO
   |         |
   v         v
Break    Play Round
Loop      |
   |       v
   |    Update scores
   |      |
   |      v
   |    Display result
   |      |
   |      v
   |    Back to while
   |    condition check
   |
   v
Display final scores
   |
   v
Game ends
```

## Message Display Flow

```
┌────────────────────────────────────┐
│  Game Outcome Messages             │
└────────────────────────────────────┘
     |
     |_____ Tie
     |      └─→ "It's a tie! you choose X,
     |          computer chose Y. You have N
     |          points and computer has M points"
     |
     |_____ Win
     |      └─→ "You win! you choose X,
     |          computer chose Y. You have N
     |          points and computer has M points"
     |
     └_____ Lose
            └─→ "You lose! you choose X,
                computer chose Y. You have N
                points and computer has M points"
```

## Complete Execution Trace

```
START
  ├─ Initialize: done=False, scores=0,0
  │
  ├─ LOOP 1: Enter R
  │  ├─ Computer: S
  │  ├─ R beats S: WIN
  │  ├─ Score: 1-0
  │  └─ Back to input
  │
  ├─ LOOP 2: Enter P
  │  ├─ Computer: R
  │  ├─ P beats R: WIN
  │  ├─ Score: 2-0
  │  └─ Back to input
  │
  ├─ LOOP 3: Enter S
  │  ├─ Computer: P
  │  ├─ S beats P: WIN
  │  ├─ Score: 3-0
  │  └─ Back to input
  │
  ├─ LOOP 4: Enter Q
  │  ├─ Check: Q == "Q" → TRUE
  │  ├─ Display: "You have 3 points and
  │  │           computer has 0 points"
  │  └─ Break loop
  │
  └─ END
     Final scores shown
```
