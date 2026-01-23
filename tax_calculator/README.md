# Tax Calculator

A simple GUI-based tax calculator built with CustomTkinter. Calculate income tax easily by entering your income and tax percentage to get the tax amount.

## Features

- 🖥️ **Modern GUI Interface**: Built with CustomTkinter for a sleek, modern look
- 💰 **Income Input**: Enter your income amount
- 📊 **Tax Percentage**: Specify the tax rate percentage
- 🧮 **Automatic Calculation**: Instantly calculates tax amount
- 💵 **Formatted Output**: Displays result with currency formatting ($)
- ⚠️ **Error Handling**: Catches invalid input and displays error messages
- 📏 **Fixed Window Size**: 280x200 pixel window (non-resizable)

## Requirements

- Python 3.x
- `customtkinter` - Modern GUI framework for Python

## Installation

1. Install required package:
```bash
pip install customtkinter
```

2. (Optional) For best appearance on different systems:
```bash
pip install customtkinter --upgrade
```

## Usage

1. Run the calculator:
```bash
python tax_calculator.py
```

2. A GUI window will open with three input fields:
   - **Income**: Enter your annual income (e.g., 50000)
   - **Percent**: Enter the tax rate as a percentage (e.g., 20 for 20%)
   - **Tax**: Display area showing calculated tax amount

3. Enter your values:
   ```
   Income: 50000
   Percent: 20
   ```

4. Click the **Calculate** button

5. The **Tax** field displays the result:
   ```
   $10,000.00
   ```

## How It Works

### Calculation Formula

```
Tax Amount = Income × (Percentage / 100)
```

### Example

| Input | Value |
|-------|-------|
| Income | $50,000 |
| Tax Rate | 20% |
| **Calculated Tax** | **$10,000** |

### Detailed Process

1. **Get Income**: Reads value from income entry field
2. **Get Percentage**: Reads tax percentage from percent entry field
3. **Calculate**: Multiplies income by (percentage/100)
4. **Format**: Converts to currency format with thousands separator
5. **Display**: Shows result in tax entry field

## GUI Components

### Window Properties

| Property | Value |
|----------|-------|
| **Title** | Tax Calculator |
| **Size** | 280×200 pixels |
| **Resizable** | No |
| **Padding** | 20px horizontal, 10px vertical |

### Input Fields

| Field | Purpose | Input Type |
|-------|---------|-----------|
| **Income** | Annual income amount | Numeric |
| **Percent** | Tax rate percentage | Numeric |
| **Tax** | Calculated tax result | Read-only display |

### Button

| Button | Function |
|--------|----------|
| **Calculate** | Triggers tax calculation |

## Error Handling

The calculator catches invalid inputs and displays error messages:

| Input Type | Behavior |
|-----------|----------|
| Valid numbers | Calculation performed |
| Empty fields | "invalid Inputs" message |
| Non-numeric text | "invalid Inputs" message |
| Negative numbers | Calculation performed (result shown) |
| Decimal numbers | Supported (e.g., 50000.50) |

### Example Error Scenarios

```
Income: abc → "invalid Inputs"
Percent: [empty] → "invalid Inputs"
Income: 50000, Percent: twenty → "invalid Inputs"
```

## Output Formatting

The tax amount is displayed with:
- **Currency Symbol**: $ prefix
- **Thousands Separator**: Commas for readability
- **Decimal Places**: 2 decimal places
- **Example**: $10,000.00

## Example Calculations

### Example 1: Federal Income Tax
```
Income: $75,000
Tax Rate: 22% (federal bracket)
Calculated Tax: $16,500.00
```

### Example 2: Sales Tax
```
Income/Purchase: $150
Tax Rate: 8.5% (sales tax)
Calculated Tax: $12.75
```

### Example 3: State Income Tax
```
Income: $100,000
Tax Rate: 5.75% (state)
Calculated Tax: $5,750.00
```

## Class Structure

### `tax_calculator` Class

#### `__init__(self)`
Initializes the GUI window and all components:
- Creates CTkinter window
- Sets window properties
- Creates labels and entry fields
- Configures padding and layout

#### `calculate_tax(self)`
Performs tax calculation:
- Gets income from income entry
- Gets percentage from percent entry
- Calculates tax amount
- Handles errors with try/except
- Updates display with result

#### `update_entry(self, text)`
Updates the tax display field:
- Clears existing content
- Inserts new calculated value

#### `run(self)`
Starts the GUI event loop:
- Displays the window
- Waits for user interaction

## Customization Options

### Change Window Size
```python
self.window.geometry("350x250")  # Width x Height
```

### Change Window Title
```python
self.window.title("Income Tax Calculator")
```

### Change Padding
```python
self.padding = {'padx': 30, 'pady': 15}
```

### Make Window Resizable
```python
self.window.resizable(True, True)
```

### Change Default Tax Value
```python
self.tax_entry.insert(0, '0')  # Change '0' to desired default
```

## Tips & Best Practices

✅ **Do this:**
- Enter income as whole number or decimal (e.g., 50000 or 50000.50)
- Use tax percentage as number (e.g., 20 for 20%)
- Clear fields between different calculations
- Double-check entries before clicking Calculate

❌ **Don't do this:**
- Include currency symbols in input ($50000)
- Include percent sign in percentage input (20%)
- Use commas in numbers (50,000)
- Leave fields empty when calculating

## Common Tax Rates (Reference)

| Tax Type | Typical Rate |
|----------|--------------|
| Federal Income Tax (US) | 10-37% |
| State Income Tax (US) | 0-13% |
| Sales Tax (US) | 0-10% |
| VAT (Europe) | 15-25% |
| Capital Gains Tax | 15-20% |
| Payroll Tax | 15.3% |

## Troubleshooting

- **"customtkinter not found"**: Run `pip install customtkinter`
- **Window doesn't appear**: Check if another window is behind it
- **Calculation shows "invalid Inputs"**: Ensure both fields have numeric values
- **Numbers show incorrectly**: Check input format (no $ or % symbols)
- **GUI looks different**: CustomTkinter appearance varies by system theme

## Advanced Features (To Implement)

### Calculate Net Income
```python
def calculate_net(self):
    tax = float(self.tax_entry.get().replace('$', '').replace(',', ''))
    income = float(self.income_entry.get())
    net = income - tax
    print(f"Net Income: ${net:,.2f}")
```

### Multiple Tax Rates
```python
def calculate_multiple(self, federal_rate, state_rate):
    total_rate = federal_rate + state_rate
    # Calculate with combined rate
```

### Tax Brackets
```python
def progressive_tax(self):
    # Implement US progressive tax bracket system
    pass
```

## Learning Concepts

This project teaches:
- **GUI Programming**: Building interfaces with CustomTkinter
- **Object-Oriented Programming**: Class structure and methods
- **Event Handling**: Button clicks and user input
- **String Formatting**: Currency formatting with commas and decimals
- **Error Handling**: Try/except for input validation
- **Grid Layout**: Organizing GUI elements in rows/columns
- **Type Conversion**: Converting strings to floats
- **Method Definitions**: Creating reusable functions

## Future Enhancements

- Add support for multiple income sources
- Implement tax bracket calculations
- Save calculation history
- Add deduction calculator
- Support multiple countries/currencies
- Create visualization charts
- Add file export functionality
- Implement tax comparison tool
- Add yearly vs. monthly calculation
- Create dark/light theme toggle

## Performance Notes

- Lightweight and responsive
- Instant calculation
- Minimal memory usage
- Smooth GUI experience

## Code Notes

⚠️ **Known Issues in Current Code:**
- Some attribute naming inconsistencies (e.g., `percent_label_label`)
- Button created as label instead of CTkButton
- All entry fields use same grid position (row=0, column=0)

## License

Open source - Free to use and modify for educational purposes.
