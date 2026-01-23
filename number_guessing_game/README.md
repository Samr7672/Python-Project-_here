# Number Guessing Game

A fun interactive game where you try to guess a random number between 1 and 100. Choose your difficulty level and see if you can guess the secret number before running out of attempts!

## Features

- 🎯 **Random Number Generation**: Computer picks a random number between 1 and 100
- 🎮 **Two Difficulty Levels**: Easy (10 attempts) or Hard (5 attempts)
- 📊 **Hint System**: Get feedback - "Too high" or "Too low"
- 🔢 **Attempt Counter**: Track remaining guesses
- 🎨 **ASCII Art Logo**: Displays a welcoming game logo
- 👾 **Interactive Gameplay**: Real-time feedback after each guess

## Requirements

- Python 3.x
- `art.py` module (included in the project)
- Standard library modules: `random`

## Installation

1. Ensure you have the `art.py` file in the same directory as `number_guess.py`
2. No external packages needed

## Usage

1. Run the game:
```bash
python number_guess.py
```

2. You'll see the game logo and welcome message:
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
```

3. Choose your difficulty:
```
Choose a difficulty. Type 'easy' or 'hard': easy
```

4. Start guessing! You'll get hints:
```
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low.
Guess again.
```

5. **Win**: Guess the correct number
```
You got it! The answer was 47.
```

6. **Lose**: Run out of attempts
```
You've run out of guesses, you lose.
```

## Game Rules

| Aspect | Details |
|--------|---------|
| **Target Range** | 1 to 100 (inclusive) |
| **Easy Level** | 10 attempts to guess |
| **Hard Level** | 5 attempts to guess |
| **Feedback** | "Too high" or "Too low" hints |
| **Goal** | Guess the exact number |

## How It Works

1. **Initialization**: Game displays logo and welcome message
2. **Setup**: Computer picks a random number (1-100) and asks for difficulty
3. **Game Loop**: 
   - Display remaining attempts
   - Get your guess
   - Check if guess is correct, too high, or too low
   - Update remaining attempts
   - Continue until you win or lose
4. **End Game**: Display win/loss message

## Strategies to Win

### Easy Level (10 attempts)
- Use **binary search**: Guess 50, then adjust based on feedback
- Example path:
  - Guess 50 → Too high → next guess 25
  - Guess 25 → Too low → next guess 37
  - Continue narrowing range

### Hard Level (5 attempts)
- **Must use binary search** efficiently
- Initial guesses: 50 → 25 or 75 (based on feedback)
- Keep range as small as possible
- Example winning sequence:
  - Guess 50 → Too high
  - Guess 25 → Too low
  - Guess 37 → Too low
  - Guess 43 → Too low
  - Guess 47 → Correct!

## Example Gameplay

### Easy Mode Win
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy

You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.

You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low.
Guess again.

You have 8 attempts remaining to guess the number.
Make a guess: 37
Too low.
Guess again.

You have 7 attempts remaining to guess the number.
Make a guess: 43
Too high.
Guess again.

You have 6 attempts remaining to guess the number.
Make a guess: 40
You got it! The answer was 40.
```

### Hard Mode Loss
```
Choose a difficulty. Type 'easy' or 'hard': hard

You have 5 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.

You have 4 attempts remaining to guess the number.
Make a guess: 25
Too low.
Guess again.

You have 3 attempts remaining to guess the number.
Make a guess: 37
Too low.
Guess again.

You have 2 attempts remaining to guess the number.
Make a guess: 43
Too high.
Guess again.

You have 1 attempts remaining to guess the number.
Make a guess: 40
Too low.
Guess again.

You've run out of guesses, you lose.
```

## Game Functions

### `set_difficulty()`
- Prompts user to choose 'easy' or 'hard'
- Returns number of turns (10 for easy, 5 for hard)

### `check_answer(guess, answer, turns)`
- Compares user's guess with the correct answer
- Provides feedback: "Too high", "Too low", or "You got it!"
- Returns updated turn count

### `game()`
- Main game function that orchestrates entire game
- Initializes random number
- Manages game loop
- Handles win/loss conditions

## Tips & Tricks

✅ **Do this:**
- Use binary search for efficiency
- Start with 50 (middle of 1-100 range)
- Pay attention to hints
- Do mental math to narrow the range

❌ **Don't do this:**
- Guess randomly without strategy
- Ignore "too high" or "too low" hints
- Forget to adjust your next guess based on feedback

## Difficulty Comparison

| Feature | Easy | Hard |
|---------|------|------|
| **Attempts** | 10 | 5 |
| **Strategy** | Can afford trial-and-error | Must use binary search |
| **Best Approach** | Systematic guessing | Optimal binary search |
| **Win Rate** | High | Lower (needs strategy) |

## Learning Concepts

This game teaches:
- **Random number generation**: Using `randint()`
- **Conditionals**: If/elif/else statements
- **Loops**: While loops for game continuation
- **Functions**: Organizing code into reusable functions
- **Algorithm efficiency**: Binary search vs random guessing
- **User input/output**: Interactive console input
- **Game logic**: Win/loss conditions

## Troubleshooting

- **"ModuleNotFoundError: No module named 'art'"**: Ensure `art.py` is in the same directory
- **Game crashes on input**: Make sure to enter a number, not text
- **"ValueError: invalid literal for int()"**: Input must be a whole number
- **Game doesn't respond**: Check you typed 'easy' or 'hard' (lowercase)

## Future Enhancements

- Add score calculation (bonus points for fewer guesses)
- Implement difficulty levels (Very Easy, Medium, Very Hard)
- Add leaderboard system
- Create GUI version with graphical display
- Add timer to race against time
- Implement undo/hint system
- Add multiplayer mode
- Display number of attempts used when winning
- Add replay functionality without restarting

## License

Open source - Free to use and modify for educational purposes.
