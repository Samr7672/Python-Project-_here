# Snake Game - Flowchart

## Main Program Initialization

```
                        START
                          |
                          v
        Import Libraries
        ├─ turtle (graphics)
        ├─ random.randrange (random positions)
        └─ freegames (utilities)
                          |
                          v
        Initialize Game Variables
        ├─ food = vector(0, 0)
        ├─ snake = [vector(10, 0)]
        └─ aim = vector(0, -10)
                          |
                          v
        Define Functions
        ├─ change(x, y)
        ├─ inside(head)
        └─ move()
                          |
                          v
        Setup Game Window
        ├─ Size: 400x400 pixels
        ├─ Position: (370, 0)
        ├─ Hide turtle cursor
        └─ Disable automatic update
                          |
                          v
        Setup Keyboard Controls
        ├─ Right Arrow: change(20, 0)
        ├─ Left Arrow: change(-20, 0)
        ├─ Up Arrow: change(0, 20)
        └─ Down Arrow: change(0, -20)
                          |
                          v
        Start Game Loop
        move()
                          |
                          v
        Display Game Window
        done()
```

## Game Loop Flow (move() Function)

```
                    move() Called
                    (every 100ms)
                          |
                          v
        Copy current snake head
        head = snake[-1].copy()
                          |
                          v
        Move head in aim direction
        head.move(aim)
                          |
                          v
        Check Collision
        ├─ Is head outside boundaries?
        ├─ Is head inside snake body?
        └─ (Both checked: not inside(head) or head in snake)
                  /                           \
                Yes                           No
                 |                             |
                 v                             v
            COLLISION!                   Move Valid
            Draw red square              (continue)
            at collision point                |
            Update display                    v
            Return (End game)         Add head to snake
                 |
                 |
                 |_____________
                               |
                               v
                    Head == Food?
                      /           \
                    Yes            No
                     |              |
                     v              v
                Food eaten!    No food eaten
                     |              |
              Print score    Remove tail
              (len(snake))    (snake.pop(0))
                     |              |
                     v              v
              Spawn new food   Snake stays
              at random        same length
              position              |
                     |______________|
                              |
                              v
                        Clear screen
                              |
                              v
                    Draw all snake segments
                    (black squares)
                              |
                              v
                        Draw food
                        (green square)
                              |
                              v
                        Update display
                              |
                              v
              Schedule next move (100ms)
                   ontimer(move, 100)
                              |
                              v
                          Return
                         (wait 100ms)
```

## Direction Change Flow

```
            Arrow Key Pressed
                  |
        __________|__________
       |          |          |          |
       v          v          v          v
     Right       Left        Up        Down
       |          |          |          |
       v          v          v          v
   change(20,0) change(-20,0) change(0,20) change(0,-20)
       |          |          |          |
       v          v          v          v
   aim.x = 20  aim.x = -20 aim.y = 20 aim.y = -20
   aim.y = 0   aim.y = 0   aim.x = 0  aim.x = 0
       |          |          |          |
       |__________|__________|__________|
                  |
                  v
         Direction updated
         (next move() will
          use new direction)
```

## Collision Detection

```
        After moving head:

    Is head inside boundaries?
    -200 < head.x < 190 AND
    -200 < head.y < 190
            |
         ___|___
        |       |
       Yes     No (Outside walls)
        |       |
        v       v
    Check    COLLISION
    self-    detected!
   collision   |
        |      v
     ___|__   Display
    |      |  red square
   Yes    No  at head
    |      |  position
    v      v  |
   COLN  Safe v
        to   Update &
       move  Return
            (Game Over)
```

## Snake Growth Logic

```
            Head moves to
         new position
                  |
                  v
        Is head == food?
             /        \
           YES         NO
            |           |
            v           v
    FOOD EATEN!    No food interaction
            |           |
     Print score         v
     len(snake)    Remove tail
            |      (snake.pop(0))
            v      Snake length
    Add head to    stays same
    snake list         |
    (no tail removal)   |
    Snake grows         |
    by 1 segment        |
            |           |
            |___________|
                  |
                  v
            Spawn new food
            food.x = randrange(-15, 15) * 10
            food.y = randrange(-15, 15) * 10
            |
            v
    Continue drawing
    and updating game
```

## Complete Game Round Sequence

```
TIME: 0ms
    ├─ Game initializes
    └─ Snake at (10, 0)
         Food at random position
         Aim direction: (0, -10)

TIME: 100ms (Move 1)
    ├─ Copy head: (10, 0)
    ├─ Move by aim: (10, -10)
    ├─ Check collision: Safe
    ├─ Check food: No match
    ├─ Draw snake: 1 segment
    └─ Schedule next move

TIME: 200ms (Move 2)
    ├─ Copy head: (10, -10)
    ├─ Move by aim: (10, -20)
    ├─ Check collision: Safe
    ├─ Check food: No match
    ├─ Draw snake: 1 segment
    └─ Schedule next move

TIME: 300ms (Move 3)
    ├─ Player presses Right key
    ├─ Direction changes: aim = (20, 0)
    ├─ Copy head: (10, -20)
    ├─ Move by new aim: (30, -20)
    ├─ Check collision: Safe
    ├─ Check food: No match
    ├─ Draw snake: 1 segment
    └─ Schedule next move

... (moves continue)

TIME: 1000ms (Move 10)
    ├─ Copy head position
    ├─ Move by aim direction
    ├─ Head reaches food!
    ├─ Print: "Snake: 2"
    ├─ Add head to snake
    └─ Don't remove tail (GROWTH)
         Snake now: 2 segments
         New food spawned

TIME: 1100ms (Move 11)
    ├─ Snake now 2 segments
    ├─ Both segments drawn
    ├─ Continue moving
    └─ Schedule next move

... (continues until collision)

TIME: 5000ms (Move 50)
    ├─ Snake head moves
    ├─ Head hits wall OR self
    ├─ Draw red square at collision
    ├─ Update display
    └─ Return (Game ends)
         Window stays open
         User closes manually
```

## Data Structure Changes

```
Initial State:
    snake = [vector(10, 0)]
    Length: 1
    
After 1st food eaten:
    snake = [vector(10, -10), vector(10, 0)]
    Length: 2
    (new head added, no tail removed)
    
After 2nd food eaten:
    snake = [vector(10, -10), vector(10, -20), vector(10, -10)]
    Length: 3
    (new head added, no tail removed)
    
Without eating food (normal move):
    Before: snake = [seg1, seg2, seg3, head]
    Length: 4
    After:  snake = [seg2, seg3, head, newhead]
    Length: 4
    (new head added, old tail removed)
```

## Game Window Display

```
┌─────────────────────────────────┐
│      GAME WINDOW (400x400)      │
├─────────────────────────────────┤
│                                 │
│  (-200,190)                     │
│     ·─────────────────────      │
│     │                         │ │
│     │    ■ Snake (Black)      │ │
│     │         ● Food (Green)  │ │
│     │                         │ │
│     │   Game Area: 380x380    │ │
│     │                         │ │
│     │─────────────────────·    │
│                       (190,-200)│
│                                 │
└─────────────────────────────────┘

■ = Snake segments (9x9 squares)
● = Food (9x9 square)
```

## Boundary Detection

```
            Check X coordinate
                    |
         ___________|___________
        |                       |
        v                       v
    head.x > 190?          head.x < -200?
    (right wall)           (left wall)
        |                       |
       YES → COLLISION      YES → COLLISION
        |                       |
        v                       v
    Check Y coordinate
            |
 ___________|___________
|                       |
v                       v
head.y > 190?        head.y < -200?
(bottom wall)        (top wall)
    |                    |
   YES              YES
    |                |
    v                v
COLLISION         COLLISION

Final check:
If X in bounds AND Y in bounds:
    → inside() returns True
Else:
    → inside() returns False → COLLISION
```

## Food Spawning

```
When food is eaten:
        |
        v
Calculate new X:
food.x = randrange(-15, 15) * 10
        |
    Possible values:
    -15 * 10 = -150
    -14 * 10 = -140
    ...
    0 * 10 = 0
    ...
    14 * 10 = 140
        |
        v
Calculate new Y:
food.y = randrange(-15, 15) * 10
        |
    Possible values:
    -150 to 140 (multiple of 10)
        |
        v
Food placed at new position
Ready to be eaten
```

## Visual Update Cycle

```
START MOVE:
    |
    v
CLEAR SCREEN
    |
    v
DRAW SNAKE
(for each segment in snake list):
    - Draw black square at position
    - Size: 9x9 pixels
    |
    v
DRAW FOOD
    - Draw green square
    - Size: 9x9 pixels
    |
    v
UPDATE DISPLAY
    - Show all drawn elements
    - Wait for next move
    |
    v
SCHEDULE NEXT MOVE
    ontimer(move, 100)
    |
    v
100ms DELAY
    |
    v
NEXT MOVE EXECUTES
```

## Scoring System

```
        Food eaten
            |
            v
    Print to console:
    "Snake: [current length]"
            |
            v
    Example outputs:
    Snake: 1 (at start)
    Snake: 2 (after 1st food)
    Snake: 3 (after 2nd food)
    Snake: 4 (after 3rd food)
    ...
            |
            v
    Console displays score
    Game continues
```

## Complete Collision Flow

```
                snake moves
                    |
                    v
        Check boundaries first:
        -200 < head.x < 190?
        -200 < head.y < 190?
                   /    \
                 Yes    No (Outside)
                  |       |
                  v       v
              Check     WALL
              self-   COLLISION
            collision    |
              /    \     v
            Yes    No   Draw red
             |      |   Display
             v      v   Return
            SELF   SAFE
           COLL.   MOVE
             |      |
             v      v
         Draw red  Continue
         Display   game
         Return
        (Game Over)
```

## Game State Lifecycle

```
INITIALIZATION
    ├─ Variables set
    ├─ Window created
    ├─ Controls configured
    └─ Ready to play

ACTIVE GAMEPLAY
    ├─ move() called every 100ms
    ├─ User presses keys to change direction
    ├─ Snake moves and grows
    ├─ Food appears and is eaten
    └─ Continue until collision

COLLISION DETECTED
    ├─ Red square drawn
    ├─ Display updated
    ├─ move() returns (no more calls)
    └─ Game loop stops

WAITING FOR CLOSE
    ├─ Window remains visible
    ├─ No more updates
    ├─ User can view final state
    └─ Click X to close window

GAME CLOSED
    └─ Program ends
```

## Timing Diagram

```
Time (ms)    Event
─────────────────────────────────
0            Game starts
             setup() called
             
100          move() #1
200          move() #2
300          move() #3
             (user presses key)
             direction changes
             
400          move() #4
500          move() #5
             (food eaten)
             snake grows
             
600          move() #6
700          move() #7
800          move() #8
900          move() #9
1000         move() #10
             (collision detected)
             game stops
             
Forever      Window open,
             awaiting close
```
