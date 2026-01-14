# 📘 Day 8

## Modules, Packages, Error Handling, Testing & More

## Table of Contents
1. [Modules and Packages](#modules-and-packages)
2. [Error Handling](#error-handling)
3. [Code Analysis with Pylint](#code-analysis-with-pylint)
4. [Testing with Unittest](#testing-with-unittest)
5. [Decorators](#decorators)
6. [Generators](#generators)

---

## Modules and Packages

### What is a Module?

A module is a Python file (.py) that contains code (functions, classes, variables) that you can reuse in other programs.

### Creating a Module

**File: `calculator.py`**

```python
# This is a module

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Module-level variable
PI = 3.14159
```

**Using the Module:**

**File: `main.py`**

```python
# Import the entire module
import calculator

result = calculator.add(5, 3)
print(result)  # 8

print(calculator.PI)  # 3.14159

# Import specific functions
from calculator import add, multiply

print(add(10, 5))  # 15
print(multiply(4, 3))  # 12

# Import with alias
from calculator import subtract as sub

print(sub(10, 3))  # 7

# Import everything (not recommended)
from calculator import *

print(divide(10, 2))  # 5.0
```

### What is a Package?

A package is a directory that contains multiple modules and a special `__init__.py` file.

### Creating a Package

**Directory Structure:**

```
my_package/
│
├── __init__.py          # Makes it a package
├── math_operations.py   # Module 1
├── string_operations.py # Module 2
└── utils.py            # Module 3
```

**Step 1: Create the `__init__.py` file**

**File: `my_package/__init__.py`**

```python
# This file makes the directory a package
# It can be empty or contain initialization code

print("My package is being imported!")

# You can specify what gets imported with *
__all__ = ['math_operations', 'string_operations']

# You can also import modules to make them available at package level
from .math_operations import add, subtract
from .string_operations import capitalize_text
```

**Step 2: Create module files**

**File: `my_package/math_operations.py`**

```python
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def power(base, exponent):
    return base ** exponent
```

**File: `my_package/string_operations.py`**

```python
def capitalize_text(text):
    return text.upper()


def reverse_text(text):
    return text[::-1]


def count_words(text):
    return len(text.split())
```

**File: `my_package/utils.py`**

```python
def print_separator():
    print("=" * 50)


def format_currency(amount):
    return f"${amount:,.2f}"
```

**Step 3: Using the Package**

**File: `main.py`**

```python
# Method 1: Import entire package
import my_package

# If __init__.py imports functions, you can use them directly
result = my_package.add(5, 3)
print(result)  # 8

# Method 2: Import specific modules
from my_package import math_operations, string_operations

print(math_operations.multiply(4, 5))  # 20
print(string_operations.capitalize_text("hello"))  # HELLO

# Method 3: Import specific functions from modules
from my_package.math_operations import power
from my_package.string_operations import reverse_text

print(power(2, 3))  # 8
print(reverse_text("Python"))  # nohtyP

# Method 4: Import from submodules
from my_package.utils import print_separator, format_currency

print_separator()  # ==================================================
print(format_currency(1234.56))  # $1,234.56
```

### Installing Packages

**Creating a Package for Distribution:**

**Directory Structure:**

```
my_project/
│
├── setup.py
└── my_package/
    ├── __init__.py
    ├── module1.py
    └── module2.py
```

**File: `setup.py`**

```python
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="1.0.0",
    author="Your Name",
    description="A sample package",
    packages=find_packages(),
    install_requires=[
        # List dependencies here
        # 'requests>=2.25.0',
    ],
)
```

**Installing the Package:**

```bash
# Install in development mode (editable)
pip install -e .

# Install normally
pip install .

# Install from requirements.txt
pip install -r requirements.txt
```

---

## Error Handling

Error handling allows your program to handle unexpected situations gracefully instead of crashing.

### The `try-except` Block

**Basic Syntax:**

```python
try:
    # Try this code
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except:
    # If something goes wrong, do this
    print("An error occurred!")
```

### Specific Exception Handling

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    # Handles invalid input (not a number)
    print("Please enter a valid number!")
except ZeroDivisionError:
    # Handles division by zero
    print("You cannot divide by zero!")
except Exception as e:
    # Catches any other exception
    print(f"An unexpected error occurred: {e}")
```

### The `finally` Block

**No matter what happens, the `finally` block always executes.**

```python
def read_file(filename):
    file = None
    try:
        file = open(filename, 'r')
        content = file.read()
        print(content)
        return content
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
    except Exception as e:
        print(f"Error reading file: {e}")
    finally:
        # This ALWAYS executes, even if there's a return statement
        if file:
            file.close()
            print("File closed successfully")


# Usage
read_file("data.txt")
```

### The `else` Block

Executes only if no exception occurred.

```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    # Only runs if no exception occurred
    print(f"Success! Result is: {result}")
finally:
    # Always runs
    print("Operation completed")
```

### Complete Error Handling Example

```python
def safe_calculator():
    """Calculator with complete error handling"""

    print("Simple Calculator")
    print("-" * 40)

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2
        else:
            raise ValueError(f"Invalid operator: {operator}")

    except ValueError as e:
        print(f"Input Error: {e}")
        return None
    except ZeroDivisionError as e:
        print(f"Math Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    else:
        print(f"Result: {result}")
        return result
    finally:
        print("-" * 40)
        print("Calculator session ended")


# Usage
safe_calculator()
```

### Common Exception Types

| Exception           | Description            | Example                   |
|---------------------|------------------------|---------------------------|
| `ValueError`        | Invalid value          | `int("abc")`              |
| `TypeError`         | Wrong type             | `"text" + 5`              |
| `ZeroDivisionError` | Division by zero       | `10 / 0`                  |
| `FileNotFoundError` | File doesn't exist     | `open("missing.txt")`     |
| `KeyError`          | Invalid dictionary key | `dict["missing_key"]`     |
| `IndexError`        | Invalid list index     | `list[999]`               |
| `AttributeError`    | Invalid attribute      | `"text".invalid_method()` |
| `ImportError`       | Cannot import module   | `import nonexistent`      |

---

## Code Analysis with Pylint

**Pylint** is a library that analyzes your code and reports potential problems with style (PEP-8) or invalid code.

### Installing Pylint

```bash
pip install pylint
```

### Using Pylint

**File: `example.py`**

```python
# Bad code example
def calculate(x, y):
    result = x + y
    return result


MyVariable = 10


def AnotherFunction():
    pass
```

**Running Pylint:**

```bash
pylint example.py
```

**Output:**

```
************* Module example
example.py:2:0: C0103: Function name "calculate" doesn't conform to snake_case naming style
example.py:2:15: C0326: Exactly one space required around assignment
example.py:3:10: C0326: Exactly one space required around assignment
example.py:6:0: C0103: Constant name "MyVariable" doesn't conform to UPPER_CASE naming style
example.py:7:0: C0103: Function name "AnotherFunction" doesn't conform to snake_case naming style
```

### Fixed Code

```python
# Good code following PEP-8
def calculate(x, y):
    """Calculate the sum of two numbers."""
    result = x + y
    return result


MY_VARIABLE = 10


def another_function():
    """Another function following conventions."""
    pass
```

### Pylint Configuration

Create a `.pylintrc` file:

```ini
[MASTER]
disable =
    C0111,  # missing-docstring
    C0103   # invalid-name

[FORMAT]
max-line-length = 100
indent-string = '    '
```

### Common Pylint Messages

| Code    | Message            | Meaning                                           |
|---------|--------------------|---------------------------------------------------|
| `C0103` | Invalid name       | Variable/function name doesn't follow conventions |
| `C0111` | Missing docstring  | No documentation string                           |
| `C0301` | Line too long      | Line exceeds character limit                      |
| `W0612` | Unused variable    | Variable is defined but never used                |
| `E0602` | Undefined variable | Using variable before defining it                 |
| `R0913` | Too many arguments | Function has too many parameters                  |

## Testing with Unittest

**Unittest** is a Python library that allows you to test your code and verify it works correctly.

### Basic Unittest Structure

```python
import unittest


# Function to test
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# Test class
class TestMathOperations(unittest.TestCase):

    def test_add(self):
        """Test the add function"""
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test the subtract function"""
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(0, 5), -5)


# Run tests
if __name__ == '__main__':
    unittest.main()
```

### Common Assertion Methods

| Method                    | Checks              |
|---------------------------|---------------------|
| `assertEqual(a, b)`       | a == b              |
| `assertNotEqual(a, b)`    | a != b              |
| `assertTrue(x)`           | x is True           |
| `assertFalse(x)`          | x is False          |
| `assertIsNone(x)`         | x is None           |
| `assertIn(a, b)`          | a in b              |
| `assertNotIn(a, b)`       | a not in b          |
| `assertRaises(Exception)` | Exception is raised |
| `assertGreater(a, b)`     | a > b               |
| `assertLess(a, b)`        | a < b               |

### Complete Testing Example

**File: `calculator.py`**

```python
"""Calculator module with various operations."""


class Calculator:
    """A simple calculator class."""

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, base, exponent):
        """Raise base to the power of exponent."""
        return base ** exponent
```

**File: `test_calculator.py`**

```python
"""Unit tests for calculator module."""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""

    def setUp(self):
        """Set up test fixtures - runs before each test."""
        self.calc = Calculator()
        print("Setting up test...")

    def tearDown(self):
        """Clean up after each test."""
        print("Test completed")

    def test_add(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-3, -3), 0)

    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_divide(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.333, places=3)

    def test_divide_by_zero(self):
        """Test that dividing by zero raises an error."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_power(self):
        """Test power operation."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(10, 2), 100)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Test edge cases for Calculator class."""

    def setUp(self):
        """Set up calculator instance."""
        self.calc = Calculator()

    def test_add_large_numbers(self):
        """Test addition with large numbers."""
        result = self.calc.add(999999, 1)
        self.assertEqual(result, 1000000)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(12345, 0), 0)

    def test_negative_power(self):
        """Test negative exponents."""
        result = self.calc.power(2, -2)
        self.assertAlmostEqual(result, 0.25)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
```

**Running Tests:**

```bash
python test_calculator.py
```

**Output:**

```
test_add (test_calculator.TestCalculator) ... ok
test_divide (test_calculator.TestCalculator) ... ok
test_divide_by_zero (test_calculator.TestCalculator) ... ok
test_multiply (test_calculator.TestCalculator) ... ok
test_power (test_calculator.TestCalculator) ... ok
test_subtract (test_calculator.TestCalculator) ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

### Test Organization

**Directory Structure:**

```
project/
│
├── src/
│   ├── __init__.py
│   └── calculator.py
│
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_advanced.py
│
└── run_tests.py
```

**File: `run_tests.py`**

```python
"""Run all tests in the tests directory."""

import unittest

# Discover and run all tests
loader = unittest.TestLoader()
suite = loader.discover('tests')
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
```

---

## Decorators

**Decorators** are functions that modify the behavior of other functions.

### Core Concepts

1. **A function is an object**
2. **A function can receive another function as an argument**
3. **A function can be created inside another function**

### Basic Decorator Example

```python
# Simple function
def greet(name):
    return f"Hello, {name}!"


# Function as object
greeting_function = greet
print(greeting_function("Alice"))  # Hello, Alice!


# Function receiving function as argument
def execute_function(func, value):
    result = func(value)
    return result


print(execute_function(greet, "Bob"))  # Hello, Bob!


# Function inside function
def outer_function():
    def inner_function():
        return "I'm inside!"

    return inner_function


my_func = outer_function()
print(my_func())  # I'm inside!
```

### Creating a Decorator

```python
def my_decorator(func):
    """A simple decorator."""

    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")

    return wrapper


# Using the decorator
@my_decorator
def say_hello():
    print("Hello!")


say_hello()
# Output:
# Before function execution
# Hello!
# After function execution
```

### Decorator with Arguments

```python
def my_decorator(func):
    """Decorator that handles function arguments."""

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}")
        result = func(*args, **kwargs)
        print(f"Function returned: {result}")
        return result

    return wrapper


@my_decorator
def add(a, b):
    return a + b


@my_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# Usage
result = add(5, 3)
# Output:
# Calling add with args: (5, 3)
# Function returned: 8

message = greet("Alice", greeting="Hi")
# Output:
# Calling greet with args: ('Alice',)
# Function returned: Hi, Alice!
```

---

## Generators

**Generators** are functions that return an iterator and generate values on-the-fly, saving memory.

### Why Use Generators?

Instead of creating a full list in memory, generators produce values one at a time.

```python
# Regular function - creates full list in memory
def get_numbers(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    return numbers


# Generator - produces values one at a time
def get_numbers_generator(n):
    for i in range(n):
        yield i  # 'yield' makes it a generator


# Usage
regular = get_numbers(5)
print(regular)  # [0, 1, 2, 3, 4] - all in memory

generator = get_numbers_generator(5)
print(generator)  # <generator object> - not in memory yet

# Get values one by one
for num in generator:
    print(num)  # 0, 1, 2, 3, 4
```

### Creating Generators

#### Using `yield`

```python
def countdown(n):
    """Generator that counts down from n to 1."""
    print("Starting countdown")
    while n > 0:
        yield n
        n -= 1
    print("Countdown finished!")


# Usage
counter = countdown(5)
print(next(counter))  # Starting countdown, then 5
print(next(counter))  # 4
print(next(counter))  # 3

# Or use in a loop
for num in countdown(3):
    print(num)
# Output:
# Starting countdown
# 3
# 2
# 1
# Countdown finished!
```

#### Generator Expressions

```python
# List comprehension - creates full list
squares_list = [x ** 2 for x in range(10)]
print(squares_list)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Generator expression - creates generator
squares_gen = (x ** 2 for x in range(10))
print(squares_gen)  # <generator object>

# Get values
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4
```

### Generator Methods

```python
def my_generator():
    print("Starting")
    yield 1
    print("Middle")
    yield 2
    print("Ending")
    yield 3


gen = my_generator()

# next() - get next value
print(next(gen))  # Starting, then 1


# send() - send a value to generator
def echo_generator():
    while True:
        received = yield
        print(f"Received: {received}")


echo = echo_generator()
next(echo)  # Prime the generator
echo.send("Hello")  # Received: Hello
echo.send("World")  # Received: World

# close() - stop generator
gen = my_generator()
print(next(gen))  # 1
gen.close()
# print(next(gen))  # Raises StopIteration
```

---

## Best Practices Summary

1. **Modules & Packages:**
    - Always include `__init__.py` in packages
    - Use clear, descriptive names
    - Organize related code together

2. **Error Handling:**
    - Use specific exception types
    - Always use `finally` for cleanup
    - Create custom exceptions for domain-specific errors

3. **Testing:**
    - Write tests as you code
    - Aim for high code coverage
    - Use descriptive test names

4. **Code Quality:**
    - Run Pylint regularly
    - Follow PEP-8 style guide
    - Write docstrings

5. **Decorators:**
    - Use for cross-cutting concerns
    - Keep decorators simple
    - Preserve function metadata with `functools.wraps`

6. **Generators:**
    - Use for large datasets
    - Prefer generators over lists for iteration
    - Combine with decorators for powerful pipelines

[<< Day 7](../day_07/day_07.md) | [Day 9 >>](../day_08/day_08.md)