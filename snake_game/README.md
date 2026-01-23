# Snake Game

A classic Snake game built with Python's Turtle graphics library. Navigate your snake to eat food and grow longer while avoiding walls and colliding with yourself!

## Features

- 🐍 **Classic Snake Gameplay**: Move the snake to eat food and grow
- 🎮 **Arrow Key Controls**: Intuitive keyboard controls (Up, Down, Left, Right)
- 🎯 **Food Spawning**: Food randomly appears on the game board
- 📊 **Score Tracking**: Console displays current snake length
- 🖼️ **Graphics**: Simple but clean visual interface with turtle graphics
- 🏁 **Collision Detection**: Game ends when hitting walls or yourself
- ⚡ **Smooth Movement**: Regular game updates at 100ms intervals
- 📏 **Bounded Game Area**: 400x400 pixel play area

## Requirements

- Python 3.x
- `turtle` - Built-in Python graphics library
- `freegames` - Provides utilities for game development
- `random` - Built-in module for random number generation

## Installation

1. Install required packages:
```bash
pip install freegames
```

2. Turtle comes with Python by default, but you can ensure it's available:
```bash
python -m pip install --upgrade turtle
```

## Usage

1. Run the game:
```bash
python snake_game.py
```

2. A 400x400 game window will open with:
   - **Black squares**: Your snake
   - **Green square**: Food
   - **Game board**: Bounded area with walls

3. Control the snake using arrow keys:
   - **↑ Up Arrow**: Move up
   - **↓ Down Arrow**: Move down
   - **← Left Arrow**: Move left
   - **→ Right Arrow**: Move right

4. Gameplay:
   - Move to food (green square) to eat it and grow
   - Snake grows by one segment each time it eats food
   - Avoid hitting the walls or your own body
   - Watch the console for your current score

5. Game Over:
   - Hitting a wall displays a red square
   - Hitting yourself displays a red square
   - Game stops and window closes when you press the close button

## How It Works

### Game Variables

| Variable | Purpose |
|----------|---------|
| `food` | Vector position of the food |
| `snake` | List of vectors representing snake body segments |
| `aim` | Vector representing snake direction |

### Initial State

- **Snake**: Starts at position (10, 0) with length 1
- **Food**: Starts at (0, 0)
- **Direction**: Initially moving down (0, -10)
- **Game Area**: 400x400 pixels, centered at (370, 0)

### Game Mechanics

1. **Movement**: Snake moves 10 pixels at a time
2. **Growth**: When snake eats food, length increases by 1
3. **Food**: New food appears at random location after being eaten
4. **Collision**: Game ends if snake hits wall or itself
5. **Updates**: Game refreshes every 100 milliseconds

## Game Controls

| Key | Action |
|-----|--------|
| **Right Arrow** | Move right (+20, 0) |
| **Left Arrow** | Move left (-20, 0) |
| **Up Arrow** | Move up (0, +20) |
| **Down Arrow** | Move down (0, -20) |

## Gameplay Rules

### Win Conditions
- There is no "winning" state - play to get the highest score possible
- Score = Length of snake

### Lose Conditions
- **Hit Wall**: Snake head goes beyond boundaries (-200 to 190 on both axes)
- **Hit Self**: Snake head collides with its own body
- Game displays red square and stops

### Scoring
- **1 Food = 1 Point**: Each food eaten = snake grows by 1 segment
- **Score Display**: Console prints "Snake: [length]" when food is eaten

## Game Area Boundaries

```
        -200, 190  (top-left)
             |___________________
             |                  |
             |                  |
             |   GAME AREA      |
             |   400x400        |
             |                  |
             |__________________|
                            190, -200 (bottom-right)
```

- **Valid X range**: -200 to 190
- **Valid Y range**: -200 to 190
- **Total play area**: 380x380 pixels

## Example Gameplay

### Start
```
Window opens with:
- Snake at (10, 0) - 1 segment
- Food at random position
- Ready for arrow key input
```

### Eating Food (Round 1)
```
Snake moves towards food
Head reaches food position
Food eaten!
Console output: Snake: 2
Snake now has 2 segments
New food appears at random location
```

### Eating Food (Round 2)
```
Snake continues moving
Head reaches new food position
Food eaten!
Console output: Snake: 3
Snake now has 3 segments
```

### Collision with Wall
```
Player presses keys to move snake
Snake head reaches boundary
Game detects: head.x < -200 or head.x > 190
Red square appears at collision point
Game stops
```

### Collision with Self
```
Snake makes a turn that intersects with body
Game detects: head in snake
Red square appears at collision point
Game stops
```

## Functions Explained

### `change(x, y)`
Updates the snake's direction vector.
```python
def change(x, y):
    aim.x = x
    aim.y = y
```
- Called when arrow keys are pressed
- Changes aim direction without moving immediately

### `inside(head)`
Checks if the snake's head is within game boundaries.
```python
def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190
```
- Returns True if head is in valid play area
- Returns False if head hit a wall

### `move()`
Main game loop function that handles:
1. Moving snake head in current direction
2. Checking collision (walls or self)
3. Handling food eating
4. Drawing game elements
5. Scheduling next move (100ms later)

## Graphics Details

### Colors
- **Black**: Snake body segments
- **Green**: Food
- **Red**: Collision/game over indicator

### Drawing
- `square(x, y, size, color)`: Draws a square at position
- `update()`: Updates the display
- `clear()`: Clears previous frame
- `ontimer(move, 100)`: Schedules next move in 100ms

## Speed & Timing

- **Move Interval**: 100 milliseconds (10 moves per second)
- **Distance per move**: 20 pixels
- **Effective speed**: 200 pixels per second
- **Difficulty increases**: As snake gets longer

## Difficulty Progression

| Length | Difficulty |
|--------|------------|
| 1-3 | Very Easy |
| 4-10 | Easy |
| 11-20 | Medium |
| 21+ | Hard |

As the snake grows, it becomes increasingly difficult to avoid self-collision.

## Tips & Strategies

✅ **Do this:**
- Move smoothly and predictably
- Plan your path to food
- Avoid trapping yourself
- Keep snake in the middle of the board
- Use walls as guides

❌ **Don't do this:**
- Make sudden sharp turns
- Try to do 180-degree reversals
- Panic when near walls
- Assume food will stay in one place

## Personal Best Tracking

To keep track of your high score, modify the game:

```python
high_score = 0

# After game ends:
if len(snake) > high_score:
    high_score = len(snake)
    print(f"New high score: {high_score}")
```

## Customization Options

### Change Game Speed
```python
ontimer(move, 100)  # Change 100 to lower value (e.g., 50) for faster
```

### Change Game Area Size
```python
setup(400, 400, 370, 0)  # First two numbers are width/height
```

### Change Snake Color
```python
square(body.x, body.y, 9, 'black')  # Change 'black' to other color
```

### Change Food Color
```python
square(food.x, food.y, 9, 'green')  # Change 'green' to other color
```

### Change Snake Movement Distance
In `change()` function, modify the values:
```python
onkey(lambda: change(20, 0), 'Right')  # Change 20 to different value
```

## Troubleshooting

- **Window doesn't appear**: Ensure turtle graphics support on your system
- **Keys don't work**: Make sure window is focused (click on it)
- **Game runs too fast**: Increase the 100 in `ontimer(move, 100)`
- **Game runs too slow**: Decrease the 100 in `ontimer(move, 100)`
- **ModuleNotFoundError: freegames**: Run `pip install freegames`

## Game Window Controls

- **Close Button**: Click the X to close the game window
- **Focus**: Click on window to ensure keyboard input works
- **No fullscreen**: Game runs in windowed mode

## Learning Concepts

This project teaches:
- **Game loops**: Using timers and callbacks
- **Vector mathematics**: Position and direction vectors
- **Collision detection**: Boundary and object collision
- **List operations**: Managing snake segments
- **Event handling**: Keyboard input
- **Graphics programming**: Drawing with turtle module
- **Game state management**: Tracking game variables
- **Recursion**: `ontimer` calling `move()` recursively

## Future Enhancements

- Add pause/resume functionality
- Implement difficulty levels
- Create high score persistence (save to file)
- Add obstacles/walls in the middle
- Implement multiple players
- Add sound effects
- Create menu system
- Add special food items (power-ups)
- Display real-time score on screen
- Add game speed increase as snake grows
- Create alternative game modes

## Performance Notes

- Runs smoothly on most systems
- CPU usage is minimal
- Memory usage is negligible
- Suitable for older computers

## License

Open source - Free to use and modify for educational purposes.
