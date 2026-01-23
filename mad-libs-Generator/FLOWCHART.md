# Mad Libs Generator - Flowchart

## Application Flow Diagram

```
                          ┌─────────────────────┐
                          │  Start Application  │
                          └──────────┬──────────┘
                                     │
                          ┌──────────▼──────────┐
                          │  Initialize Tkinter │
                          │  Create GUI Window  │
                          └──────────┬──────────┘
                                     │
                          ┌──────────▼──────────┐
                          │  Display Main Menu  │
                          │  With 4 Buttons     │
                          └──────────┬──────────┘
                                     │
                    ┌────────────────┼────────────────┐
                    │                │                │
         ┌──────────▼────────┐   ┌───▼──────────┐   ┌▼─────────────────┐
         │ Button 1: The     │   │ Button 2:    │   │ Button 3: Apple  │
         │ Photographer      │   │ The Butterfly│   │ and Apple        │
         └──────────┬────────┘   └───┬──────────┘   └─────┬────────────┘
                    │                │                     │
                    │                │                ┌────▼──────────┐
                    │                │                │ Button 4:     │
                    │                │                │ Software Eng. │
                    │                │                └────┬──────────┘
                    │                │                     │
                    └────────────────┼─────────────────────┘
                                     │
                          ┌──────────▼──────────┐
                          │  User Selects Story │
                          └──────────┬──────────┘
                                     │
                    ┌────────────────┼────────────────┐────────────────┐
                    │                │                │                │
         ┌──────────▼────────┐   ┌───▼──────────┐   ┌▼──────────┐   ┌──▼───────────┐
         │ Madlib1()         │   │ Madlib2()    │   │Madlib3()  │   │ Madlib4()    │
         │                   │   │              │   │           │   │              │
         │ Input Loop:       │   │ Input Loop:  │   │ Input:    │   │ Input:       │
         │ - Animal          │   │ - Adjective  │   │ - Person  │   │ - Software   │
         │ - Profession      │   │ - Color      │   │ - Color   │   │ - Bug type   │
         │ - Cloth           │   │ - Thing      │   │ - Food    │   │ - Hacker     │
         │ - Things          │   │ - Place      │   │ - Place   │   │ - Action     │
         │ - Name            │   │ - Person     │   │ - Verb    │   │ - Object     │
         │ - Place           │   │ - Adjective  │   │ - Adverb  │   │ - Feeling    │
         │ - Verb            │   │ - Insect     │   │ - Food    │   │ - Hero       │
         │ - Food            │   │ - Food       │   │ - Things  │   │              │
         └──────────┬────────┘   │ - Verb       │   └─────┬─────┘   └──┬────────────┘
                    │            └───┬──────────┘         │            │
                    │                │                     │            │
                    └────────────────┼─────────────────────┴────────────┘
                                     │
                          ┌──────────▼──────────┐
                          │ Collect All Inputs  │
                          │ From User           │
                          └──────────┬──────────┘
                                     │
                          ┌──────────▼──────────┐
                          │ Build Story String  │
                          │ (Concatenate words) │
                          └──────────┬──────────┘
                                     │
                          ┌──────────▼──────────┐
                          │ Print Story to      │
                          │ Console             │
                          └──────────┬──────────┘
                                     │
                          ┌──────────▼──────────┐
                          │ Return to Main Menu │
                          │ (Keep window open)  │
                          └──────────┬──────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    │                                 │
         ┌──────────▼────────┐         ┌──────────────▼──┐
         │ User Clicks New   │         │ User Closes     │
         │ Story Button      │         │ Window          │
         │ Go back to story  │         │                 │
         │ selection         │         │ Exit Program    │
         └─────────────┬─────┘         └──────────────┬──┘
                       │                               │
                       └───────────────┬────────────────┘
                                       │
                            ┌──────────▼──────────┐
                            │   End Application   │
                            └─────────────────────┘
```

## Key Components

### 1. **GUI Initialization**
   - Creates Tkinter root window
   - Sets window size to 500x300 pixels
   - Displays title and instructions

### 2. **Story Selection**
   - 4 buttons for different story templates
   - Each button linked to a different madlib function

### 3. **Input Collection**
   - Each story function prompts for specific word types
   - Uses standard `input()` function for user prompts
   - Stores inputs in variables

### 4. **Story Generation**
   - Concatenates user inputs with template text
   - Creates unique story based on inputs
   - Prints complete story to console

### 5. **User Loop**
   - Application remains open after story display
   - User can select another story or close window
   - Maintains state throughout session

## Process Flow Summary

1. **Start** → 2. **Initialize GUI** → 3. **Display Menu** → 4. **User Selects Story**
   → 5. **Collect Inputs** → 6. **Generate Story** → 7. **Display Story** 
   → 8. **Return to Menu** → Loop or End

---

**Note**: The application uses a simple concatenation approach to build stories. All input collection happens through command-line prompts while the GUI window remains open in the background.
