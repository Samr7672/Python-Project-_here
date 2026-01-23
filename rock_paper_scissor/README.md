# Rock Paper Scissors Game

A classic interactive Rock-Paper-Scissors game where you play against the computer. Keep track of your score as you compete in multiple rounds until you decide to quit.

## Features

- 🎮 **Interactive Gameplay**: Play multiple rounds against the computer
- 🤖 **AI Opponent**: Computer makes random choices
- 📊 **Score Tracking**: Keep track of wins, losses, and ties
- 🎯 **Real-time Feedback**: Get instant results after each round
- ⌨️ **Easy Controls**: Simple input using R (Rock), P (Paper), S (Scissors)
- 🏁 **Play Until You Quit**: Continue playing as many rounds as you want
- 📈 **Final Statistics**: View final scores when exiting

## Requirements

- Python 3.x
- No external libraries required (uses only built-in `random` module)

## Installation

No installation needed! Just have Python 3 installed on your system.

## Usage

1. Run the game:
```bash
python rock_paper_scissor_game.py
```

2. You'll see the prompt:
```
Enter a choice (R, P, S):and enter 'q' to quit
```

3. Make your choice:
   - **R** = Rock
   - **P** = Paper
   - **S** = Scissors
   - **Q** = Quit the game

4. The computer makes its choice and results display:
```
You chose R, computer chose P
You lose! you choose R, computer chose P. You have 0 points and computer has 1 points
```

5. Repeat until you type **Q** to quit

6. When you quit, final scores display:
```
You have 3 points and computer has 2 points
```

## Game Rules

| Your Choice | Beats | Loses To |
|-------------|-------|----------|
| **Rock (R)** | Scissors | Paper |
| **Paper (P)** | Rock | Scissors |
| **Scissors (S)** | Paper | Rock |

### Scoring
- **Win**: You get 1 point
- **Loss**: Computer gets 1 point
- **Tie**: No points awarded

## How It Works

1. **Initialization**: Sets up game variables and dictionaries
2. **Game Loop**: Repeats until player quits (presses Q)
3. **Player Input**: Asks for R, P, S, or Q
4. **Computer Choice**: Randomly selects R, P, or S
5. **Comparison**: Determines win/loss/tie based on game rules
6. **Score Update**: Updates scores accordingly
7. **Display Results**: Shows outcome and current scores
8. **Exit**: Shows final scores when player quits

## Game Variables Explained

| Variable | Purpose |
|----------|---------|
| `done` | Flag to control game loop (not actively used) |
| `win`, `lose`, `tie` | Counters for game outcomes |
| `user_score` | Points earned by player |
| `computer_score` | Points earned by computer |
| `names` | Dictionary mapping choice names to letters |
| `loses` | Dictionary showing what beats what |
| `wins` | Dictionary showing what each choice beats |

## Example Gameplay

### Round 1
```
Enter a choice (R, P, S):and enter 'q' to quit R
You chose R, computer chose S
You win! you choose R, computer chose S. You have 1 points and computer has 0 points
```

### Round 2
```
Enter a choice (R, P, S):and enter 'q' to quit P
You chose P, computer chose P
It's a tie! you choose P, computer chose P. You have 1 points and computer has 0 points
```

### Round 3
```
Enter a choice (R, P, S):and enter 'q' to quit S
You chose S, computer chose R
You lose! you choose S, computer chose R. You have 1 points and computer has 1 points
```

### Quit
```
Enter a choice (R, P, S):and enter 'q' to quit Q
You have 1 points and computer has 1 points
```

## Strategy Tips

✅ **Statistics & Probability:**
- Rock, Paper, and Scissors are equally likely (33% each)
- In a random game, ties occur ~33% of the time
- Perfect strategy is impossible against random choices

✅ **Playing Tips:**
- The computer plays truly randomly - no pattern to exploit
- Focus on having fun rather than winning
- Try alternating your choices to keep it interesting

❌ **Common Mistakes:**
- Expecting the computer to follow a pattern (it won't)
- Staying with one choice too long
- Not keeping track of your score

## Scoring Examples

### Scenario: 10 Rounds Played
```
Round 1: You win       → Your score: 1, Computer: 0
Round 2: You lose      → Your score: 1, Computer: 1
Round 3: You tie       → Your score: 1, Computer: 1
Round 4: You win       → Your score: 2, Computer: 1
Round 5: You lose      → Your score: 2, Computer: 2
Round 6: You win       → Your score: 3, Computer: 2
Round 7: You lose      → Your score: 3, Computer: 3
Round 8: You tie       → Your score: 3, Computer: 3
Round 9: You win       → Your score: 4, Computer: 3
Round 10: Q (quit)     → Final: You 4, Computer 3
```

## Input Validation

| Input | Result |
|-------|--------|
| R | Rock - Valid |
| P | Paper - Valid |
| S | Scissors - Valid |
| Q | Quit game - Valid |
| r | Converted to R - Valid |
| p | Converted to P - Valid |
| s | Converted to S - Valid |
| q | Converted to Q - Valid |
| Other | Game may crash or behave unexpectedly |

## Known Issues & Limitations

⚠️ **Issue**: Invalid input can cause errors
- Only R, P, S, Q are properly handled
- Other inputs may cause KeyError

⚠️ **Issue**: Logic redundancy
- Win/loss conditions are checked multiple times
- Some conditions may never be reached

⚠️ **Issue**: Case sensitivity is handled
- Input is converted to uppercase
- Works for all proper inputs

## Future Enhancements

- Add input validation to prevent crashes
- Implement best-of-N series mode
- Add difficulty levels (easy, medium, hard)
- Display win/loss percentages
- Add visual representation of choices
- Implement move history/statistics
- Create multiplayer mode (two players)
- Add rewards/achievement system
- Build GUI version with graphics
- Add sound effects and animations

## Winning Strategy Analysis

Since the computer plays randomly, the optimal strategy is:
1. Play randomly yourself (each choice 33% of the time)
2. Focus on having fun
3. Accept that ~33% will be ties, ~33% wins, ~33% losses
4. Try to beat your personal high score

## Learning Concepts

This project teaches:
- **Dictionaries**: Using dictionaries for lookups
- **Random selection**: Using `random.choice()`
- **Conditionals**: If/elif chains for game logic
- **Loops**: While loops for game continuation
- **Score tracking**: Maintaining game state
- **Game logic**: Implementing game rules
- **User input**: Interactive console input
- **String manipulation**: Converting input to uppercase

## License

Open source - Free to use and modify for educational purposes.
