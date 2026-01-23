# Simple Calculator

A basic command-line calculator application that performs fundamental arithmetic operations including addition, subtraction, multiplication, and division.

## Features

- ➕ **Addition**: Add two numbers
- ➖ **Subtraction**: Subtract two numbers
- ✖️ **Multiplication**: Multiply two numbers
- ➗ **Division**: Divide two numbers
- 🎯 **User-friendly Interface**: Simple menu-based selection
- ⚡ **Fast Execution**: Immediate results

## Requirements

- Python 3.x
- No external libraries required

## Installation

No installation needed! Just have Python installed on your system.

## Usage

1. Run the calculator:
```bash
python calculator.py
```

2. Select an operation:
   ```
   Select operation.
   1.Add
   2.Subtract
   3.Multiply
   4.Divide
   ```

3. Enter your choice (1/2/3/4)

4. Enter two numbers when prompted:
   - First number
   - Second number

5. The result will be displayed

## Examples

### Addition
```
Select operation.
1.Add
2.Subtract
3.Multiply
4.Divide
Enter choice(1/2/3/4): 1
Enter first number: 10
Enter second number: 5
10 + 5 = 15
```

### Subtraction
```
Enter choice(1/2/3/4): 2
Enter first number: 20
Enter second number: 8
20 - 8 = 12
```

### Multiplication
```
Enter choice(1/2/3/4): 3
Enter first number: 6
Enter second number: 7
6 * 7 = 42
```

### Division
```
Enter choice(1/2/3/4): 4
Enter first number: 100
Enter second number: 5
100 / 5 = 20.0
```

## How It Works

1. The program displays a menu with four operation options
2. User selects an operation by entering 1, 2, 3, or 4
3. User enters two numbers to perform the calculation on
4. The appropriate mathematical function is called
5. The result is calculated and displayed
6. Program terminates after showing the result

## Operations

| Operation | Input | Function | Formula |
|-----------|-------|----------|---------|
| Add | 1 | `add(x, y)` | x + y |
| Subtract | 2 | `subtract(x, y)` | x - y |
| Multiply | 3 | `multiply(x, y)` | x * y |
| Divide | 4 | `divide(x, y)` | x / y |

## Notes

- Invalid input will display "Invalid input" message
- Division results in a float value (e.g., 10 / 4 = 2.5)
- Only accepts integers as input in current version
- Program exits after one calculation

## Error Handling

- **Invalid Choice**: If you enter a choice other than 1-4, the program displays "Invalid input"
- **Division by Zero**: Not currently handled - may cause an error if you divide by 0

## Future Enhancements

- Add floating-point number support
- Implement division by zero error handling
- Add more operations (modulus, exponentiation, etc.)
- Add ability to perform multiple calculations without restarting
- Create a graphical user interface (GUI) version
- Add history of previous calculations
- Input validation and error messages

## License

Open source - Free to use and modify.
