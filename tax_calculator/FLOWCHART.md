# Tax Calculator - Flowchart

## Main Program Initialization

```
                        START
                          |
                          v
        Import customtkinter module
                          |
                          v
        Define tax_calculator class
                          |
                          v
        Create instance: tc = tax_calculator()
                          |
                          v
        ┌─────────────────────────────┐
        │    __init__() CALLED        │
        └─────────────────────────────┘
                          |
                          v
        Create CTk window
        self.window = ctk.CTk()
                          |
                          v
        Set window title
        "Tax Calculator"
                          |
                          v
        Set window size
        280 × 200 pixels
                          |
                          v
        Make window non-resizable
        resizable(False, False)
                          |
                          v
        Define padding dictionary
        padx=20, pady=10
                          |
                          v
        ┌─────────────────────────────┐
        │  CREATE GUI COMPONENTS      │
        └─────────────────────────────┘
                          |
                          v
        Create Income Label
        "income"
                          |
                          v
        Create Income Entry Field
        (empty, waiting for input)
                          |
                          v
        Create Percent Label
        "Percent"
                          |
                          v
        Create Percent Entry Field
        (empty, waiting for input)
                          |
                          v
        Create Tax Label
        "Tax"
                          |
                          v
        Create Tax Entry Field
        (default value: '0')
                          |
                          v
        Create Calculate Button
        (linked to calculate_tax function)
                          |
                          v
        ┌─────────────────────────────┐
        │  LAYOUT COMPONENTS          │
        │  (Grid positioning)         │
        └─────────────────────────────┘
                          |
                          v
        Position all components
        with padding
                          |
                          v
        Call tc.run()
                          |
                          v
        ┌─────────────────────────────┐
        │    DISPLAY WINDOW           │
        │    self.window.mainloop()   │
        └─────────────────────────────┘
                          |
                          v
        Window displays
        Waiting for user input
```

## Window Layout Grid

```
        COLUMN 0    COLUMN 1
ROW 0:  [Income]    [Income Entry]
ROW 1:  [Percent]   [Percent Entry]
ROW 2:  [Tax]       [Tax Entry]
ROW 3:  (blank)     [Calculate Button]

Grid Layout:
┌─────────────────────────────┐
│ income          [_______]   │
│ Percent         [_______]   │
│ Tax             [______0]   │
│                 [Calculate] │
└─────────────────────────────┘
```

## Calculate Button Click Flow

```
            User Clicks
        "Calculate" Button
                |
                v
        calculate_tax() called
                |
                v
        ┌──────────────────────────┐
        │  TRY BLOCK EXECUTES      │
        └──────────────────────────┘
                |
                v
        Get income from entry field
        income = float(income_entry.get())
                |
                v
        Get percentage from entry field
        percent = float(percent_entry.get())
                |
                v
        Calculate tax amount
        tax = income × (percent / 100)
                |
                v
        Format as currency
        '$[amount],[comma-separated].[2 decimals]'
                |
                v
        Call update_entry() with result
        update_entry(formatted_string)
                |
        _______|_______
       |               |
       v               v
    SUCCESS         ERROR
    (both are         (ValueError)
     valid numbers)   (invalid input)
       |               |
       v               v
    Display       EXCEPT block
    calculated    executes
    tax               |
                      v
                  Call update_entry()
                  with error message
                  "invalid Inputs"
                      |
                      v
                  Display error
                      |
                      |
       _______________|
       |
       v
    Function returns
```

## Input Validation Flow

```
        User enters values
                |
        _______|_______
       |               |
       v               v
    Both fields    One or both
    have numbers   empty or
                   non-numeric
       |               |
       v               v
    float() works  float() raises
    successfully   ValueError
       |               |
       v               v
    Calculation  Exception
    performed    caught
       |               |
       v               v
    Update tax   Update tax
    with result  with error
    "$X,XXX.XX"  "invalid Inputs"
```

## Calculate Tax Function Flow

```
    def calculate_tax(self):
            |
            v
    try:
            |
        ____|____
       |        |
       v        v
    Get income Convert
    from entry to float
       |
       v
    Get percent Convert
    from entry to float
       |
       v
    Calculate:
    tax = income * (percent / 100)
       |
       v
    Format result:
    f'${income*(percent/100):,.2f}'
       |
       v
    Call update_entry()
    with formatted string
       |
       v
    except ValueError:
       |
       v
    Call update_entry()
    with "invalid Inputs"
       |
       v
    Return
```

## Update Entry Function Flow

```
    def update_entry(self, text):
            |
            v
    tax_entry.delete(0, END)
    (clear all content)
            |
            v
    tax_entry.insert(0, text)
    (insert new value at position 0)
            |
            v
    Return
```

## Data Flow - Calculation Example

```
USER ENTERS:
Income: 50000
Percent: 20

    |
    v

CALCULATION:
income = float("50000") = 50000.0
percent = float("20") = 20.0

    |
    v

TAX CALCULATION:
tax = 50000.0 * (20.0 / 100)
tax = 50000.0 * 0.20
tax = 10000.0

    |
    v

FORMATTING:
f'${10000.0:,.2f}'
└─ Format as currency
   with commas
   and 2 decimals

    |
    v

RESULT:
"$10,000.00"

    |
    v

DISPLAY:
Tax field shows: $10,000.00
```

## Complete User Interaction Flow

```
┌─────────────────────────┐
│  WINDOW OPENS           │
│  (GUI displayed)        │
└─────────────────────────┘
            |
            v
┌─────────────────────────┐
│  USER ENTERS DATA       │
│  Income: 50000          │
│  Percent: 20            │
│  Tax: 0 (default)       │
└─────────────────────────┘
            |
            v
┌─────────────────────────┐
│  USER CLICKS CALCULATE  │
└─────────────────────────┘
            |
            v
┌─────────────────────────┐
│  CALCULATION OCCURS     │
│  50000 * (20/100)       │
│  = 10000                │
└─────────────────────────┘
            |
            v
┌─────────────────────────┐
│  FORMATTING APPLIED     │
│  10000 → "$10,000.00"   │
└─────────────────────────┘
            |
            v
┌─────────────────────────┐
│  TAX FIELD UPDATED      │
│  Tax: $10,000.00        │
└─────────────────────────┘
            |
            v
┌─────────────────────────┐
│  READY FOR NEXT INPUT   │
│  (user can calculate    │
│   again or close)       │
└─────────────────────────┘
```

## Error Handling Flow

```
        calculate_tax() called
                |
                v
        Try to convert income to float
                |
         _______|_______
        |               |
       YES              NO
        |               |
        v               v
    Success        ValueError
    Continue       raised
    with income        |
        |              v
        v          Jump to
    Try to         except block
    convert            |
    percent            v
        |          update_entry(
        |          "invalid Inputs")
     ___|___            |
    |       |           v
   YES     NO       Tax field shows
    |       |       error message
    v       v       |
Success  Error      v
   |       |     Return from
   |       v     function
   |    update_entry(
   |    "invalid Inputs")
   |       |
   v       v
Calculate  Display
tax        error
   |       |
   v       v
update_entry   Return
(formatted)    from
   |           function
   v
Display
result
```

## String Formatting Detail

```
        tax = 10000.0
             |
             v
    f'${tax:,.2f}'
    
    Breaking it down:
    ├─ $ = literal dollar sign
    ├─ {tax} = variable value
    ├─ : = format specifier
    ├─ , = thousands separator
    └─ .2f = 2 decimal places, float
    
             |
             v
    Result: "$10,000.00"
    
    More examples:
    ├─ 5000.0 → "$5,000.00"
    ├─ 150.5 → "$150.50"
    ├─ 1234567.89 → "$1,234,567.89"
    └─ 999.999 → "$999.00" (rounded)
```

## Run Function Flow

```
    def run(self):
            |
            v
    self.window.mainloop()
            |
            v
    Event loop starts
    (window displays)
            |
            v
    Listen for events:
    ├─ Window close (X button)
    ├─ Button clicks
    ├─ Entry field changes
    └─ Other user actions
            |
            v
    When event occurs:
    └─ Execute corresponding function
      (e.g., calculate_tax())
            |
            v
    When window closes:
    └─ Exit event loop
      Terminate program
```

## Class Method Execution Order

```
if __name__ == '__main__':
        |
        v
tc = tax_calculator()
        |
        v
__init__() executes
(window and components created)
        |
        v
tc.run()
        |
        v
mainloop() starts
(window displayed, waiting)
        |
        v
User interaction
(enters data, clicks button)
        |
        v
Callback functions execute
calculate_tax() called
        |
        v
update_entry() called
        |
        v
Window updates
        |
        v
Wait for next event
        |
        v
User closes window
        |
        v
mainloop() exits
        |
        v
Program ends
```

## Component Creation Sequence

```
Step 1: Window Creation
    ├─ CTk() instantiated
    ├─ Title set
    ├─ Size set
    └─ Resizable disabled

Step 2: Label Creation
    ├─ Income label created
    ├─ Percent label created
    └─ Tax label created

Step 3: Entry Field Creation
    ├─ Income entry created
    ├─ Percent entry created
    └─ Tax entry created (default: '0')

Step 4: Button Creation
    ├─ Calculate button created
    └─ Linked to calculate_tax function

Step 5: Grid Layout
    ├─ All components positioned
    ├─ Padding applied
    └─ Window ready to display

Step 6: Event Loop
    ├─ Window shown
    ├─ Listening for events
    └─ Ready for interaction
```

## Complete Execution Timeline

```
TIME: 0s
    └─ Script starts
       if __name__ == '__main__':

TIME: 0.1s
    └─ tax_calculator instance created
       __init__() executes

TIME: 0.2s
    └─ Window and components created
       GUI initialized

TIME: 0.3s
    └─ tc.run() called
       mainloop() starts
       Window displays

TIME: 0.3s - User interaction
    ├─ User enters: Income = 50000
    ├─ User enters: Percent = 20
    └─ Window waits

TIME: X seconds (when user clicks Calculate)
    ├─ calculate_tax() triggered
    ├─ Try block executes
    ├─ income = 50000.0
    ├─ percent = 20.0
    ├─ tax = 10000.0
    ├─ Formatted: "$10,000.00"
    ├─ update_entry() called
    └─ Tax field updated: $10,000.00

TIME: Y seconds (when user closes window)
    ├─ Close button clicked
    ├─ mainloop() exits
    └─ Program terminates
```

## GUI State Management

```
INITIAL STATE:
    Income: [empty]
    Percent: [empty]
    Tax: [0]
    Button: Calculate (inactive)

AFTER USER INPUT:
    Income: [50000]
    Percent: [20]
    Tax: [0]
    Button: Calculate (ready to click)

AFTER BUTTON CLICK:
    Income: [50000]
    Percent: [20]
    Tax: [$10,000.00]
    Button: Calculate (ready to click again)

READY FOR NEW CALCULATION:
    User can change inputs
    Or click Calculate again
```

## Exception Flow Detail

```
        income_entry.get() returns "50000"
        percent_entry.get() returns "abc"
                |
                v
        float("50000") → 50000.0 ✓
                |
                v
        float("abc") → ValueError ✗
                |
                v
        Exception caught
        Jump to except ValueError:
                |
                v
        update_entry("invalid Inputs")
                |
                v
        Tax field shows:
        "invalid Inputs"
                |
                v
        Function returns
        User sees error message
```
