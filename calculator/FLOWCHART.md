# Simple Calculator - Flowchart

## Main Program Flow

```
                        START
                          |
                          v
                   Display Menu
               "Select operation"
                  1. Add
                  2. Subtract
                  3. Multiply
                  4. Divide
                          |
                          v
                  Input: choice
                   (1/2/3/4)
                          |
                          v
                   Input first number
                   (num1)
                          |
                          v
                   Input second number
                   (num2)
                          |
                          v
              Is choice == '1'?
                   /         \
                 Yes         No
                  |           |
                  v           v
             call add()   Is choice == '2'?
              return          /         \
                  |         Yes         No
                  |          |           |
                  |          v           v
                  |     call subtract()
                  |      return
                  |          |           Is choice == '3'?
                  |          |           /         \
                  |          |         Yes         No
                  |          |          |           |
                  |          |          v           v
                  |          |     call multiply()
                  |          |      return
                  |          |          |           Is choice == '4'?
                  |          |          |           /         \
                  |          |          |         Yes         No
                  |          |          |          |           |
                  |          |          |          v           v
                  |          |          |     call divide()   Print
                  |          |          |      return      "Invalid
                  |          |          |          |        input"
                  |          |          |          |           |
                  |__________|__________|__________|           |
                             |                                 |
                             v                                 |
                   Print: num1 op num2 = result               |
                             |                                 |
                             |_________________________________|
                                     |
                                     v
                                   END
```

## Function Calls Flow

```
┌─────────────────────────────────────┐
│          FUNCTION: add(x, y)        │
├─────────────────────────────────────┤
│  Input:  x, y (two numbers)         │
│  Process: x + y                     │
│  Output: sum result                 │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│      FUNCTION: subtract(x, y)       │
├─────────────────────────────────────┤
│  Input:  x, y (two numbers)         │
│  Process: x - y                     │
│  Output: difference result          │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│      FUNCTION: multiply(x, y)       │
├─────────────────────────────────────┤
│  Input:  x, y (two numbers)         │
│  Process: x * y                     │
│  Output: product result             │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│       FUNCTION: divide(x, y)        │
├─────────────────────────────────────┤
│  Input:  x, y (two numbers)         │
│  Process: x / y                     │
│  Output: quotient result (float)    │
└─────────────────────────────────────┘
```

## Complete Execution Sequence

```
Step 1: START
        ↓
Step 2: Display operation menu
        ↓
Step 3: Get user choice (1, 2, 3, or 4)
        ↓
Step 4: Get first number from user
        ↓
Step 5: Get second number from user
        ↓
Step 6: Decision Tree
        ├─→ If choice is '1': Execute add(num1, num2)
        ├─→ If choice is '2': Execute subtract(num1, num2)
        ├─→ If choice is '3': Execute multiply(num1, num2)
        ├─→ If choice is '4': Execute divide(num1, num2)
        └─→ Else: Invalid input message
        ↓
Step 7: Display result or error message
        ↓
Step 8: END
```

## Input and Output Flow

```
┌─────────────────────────────────────┐
│            USER INPUTS              │
└─────────────────────────────────────┘
           |
           v
    choice = input()
           |
           v
    num1 = int(input())
           |
           v
    num2 = int(input())
           |
           v
┌─────────────────────────────────────┐
│       PROCESSING LAYER              │
└─────────────────────────────────────┘
           |
           v
    Determine operation
           |
           v
    Call appropriate function
           |
           v
    Calculate result
           |
           v
┌─────────────────────────────────────┐
│        PROGRAM OUTPUT               │
└─────────────────────────────────────┘
           |
           v
    Print num1 op num2 = result
           |
           v
    Program terminates
```

## Decision Tree - Operation Selection

```
                    choice?
                      |
          ____________|____________
         |            |            |            |
         v            v            v            v
       '1'          '2'          '3'          '4'
       |            |            |            |
       v            v            v            v
      ADD       SUBTRACT     MULTIPLY      DIVIDE
       |            |            |            |
       v            v            v            v
    x + y        x - y        x * y        x / y
       |            |            |            |
       |____________|____________|____________|
                    |
                    v
             Display Result
                    |
                    v
                   END
              (else: Invalid input)
```

## Data Flow Diagram

```
User Input
    |
    ├─→ Operation Choice (1/2/3/4)
    |
    ├─→ First Number (num1)
    |
    └─→ Second Number (num2)
        |
        v
    Match Choice to Function
        |
        ├─→ '1' → add()
        ├─→ '2' → subtract()
        ├─→ '3' → multiply()
        ├─→ '4' → divide()
        └─→ else → Error Message
        |
        v
    Function Execution
        |
        v
    Return Result / Error
        |
        v
    Format Output
        |
        v
    Display to User
        |
        v
    Program Ends
```
