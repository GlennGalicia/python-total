# 📘 Day 9

## Standard Libraries: Collections, Files, Time, Math & More

## Table of Contents

1. [Collections Module](#collections-module)
2. [File Management with os and shutil](#file-management-with-os-and-shutil)
3. [DateTime Module](#datetime-module)
4. [Timeit Module](#timeit-module)
5. [Math Module](#math-module)
6. [Regular Expressions](#regular-expressions)
7. [Zipfile Module](#zipfile-module)

---

## Collections Module

The `collections` module provides specialized container datatypes.

### Counter

**Counter** counts hashable objects. It's like a dictionary where elements are keys and counts are values.

```python
from collections import Counter

# Counting elements in a list
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
fruit_count = Counter(fruits)
print(fruit_count)
# Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Counting characters in a string
text = "hello world"
char_count = Counter(text)
print(char_count)
# Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Creating Counter from dictionary
inventory = Counter({'apples': 5, 'oranges': 3, 'bananas': 2})
print(inventory)
# Output: Counter({'apples': 5, 'oranges': 3, 'bananas': 2})
```

**Useful Counter Methods:**

```python
from collections import Counter

votes = Counter(['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Alice'])

# most_common(n) - Get n most common elements
print(votes.most_common(2))
# Output: [('Alice', 3), ('Bob', 2)]

# elements() - Return an iterator over elements
print(list(votes.elements()))
# Output: ['Alice', 'Alice', 'Alice', 'Bob', 'Bob', 'Charlie']

# update() - Add counts
more_votes = ['Charlie', 'Charlie', 'Alice']
votes.update(more_votes)
print(votes)
# Output: Counter({'Alice': 4, 'Charlie': 3, 'Bob': 2})

# subtract() - Subtract counts
votes.subtract(['Alice', 'Bob'])
print(votes)
# Output: Counter({'Alice': 3, 'Charlie': 3, 'Bob': 1})

# Mathematical operations
counter1 = Counter(['a', 'b', 'c', 'a'])
counter2 = Counter(['a', 'c', 'd'])

print(counter1 + counter2)  # Add counts
# Output: Counter({'a': 3, 'c': 2, 'b': 1, 'd': 1})

print(counter1 - counter2)  # Subtract (keep only positive)
# Output: Counter({'a': 1, 'b': 1})

print(counter1 & counter2)  # Intersection (minimum)
# Output: Counter({'a': 1, 'c': 1})

print(counter1 | counter2)  # Union (maximum)
# Output: Counter({'a': 2, 'b': 1, 'c': 1, 'd': 1})
```

**Practical Example: Word Frequency**

```python
from collections import Counter

text = """
Python is a great programming language.
Python is easy to learn and Python is powerful.
Many developers love Python for its simplicity.
"""

# Clean and count words
words = text.lower().split()
word_count = Counter(words)

# Get top 5 most common words
print("Top 5 most common words:")
for word, count in word_count.most_common(5):
    print(f"{word}: {count}")

# Output:
# python: 4
# is: 3
# a: 1
# great: 1
# programming: 1
```

### namedtuple

**namedtuple** creates tuple subclasses with named fields, making code more readable.

```python
from collections import namedtuple

# Create a Point namedtuple
Point = namedtuple('Point', ['x', 'y'])

# Create instances
p1 = Point(10, 20)
p2 = Point(x=5, y=15)

# Access by name (more readable)
print(p1.x, p1.y)  # 10 20

# Access by index (still works like tuple)
print(p2[0], p2[1])  # 5 15

# Unpack like tuple
x, y = p1
print(x, y)  # 10 20

# Immutable (like regular tuple)
# p1.x = 30  # AttributeError!
```

**Different Ways to Create namedtuple:**

```python
from collections import namedtuple

# Method 1: Space-separated string
Person = namedtuple('Person', 'name age city')

# Method 2: List of strings
Person = namedtuple('Person', ['name', 'age', 'city'])

# Method 3: Comma-separated string
Person = namedtuple('Person', 'name, age, city')

# Create instance
person1 = Person('Alice', 30, 'New York')
print(person1.name)  # Alice
print(person1.age)  # 30
print(person1.city)  # New York
```

**Useful namedtuple Methods:**

```python
from collections import namedtuple

Car = namedtuple('Car', ['brand', 'model', 'year'])
my_car = Car('Toyota', 'Camry', 2020)

# _asdict() - Convert to dictionary
car_dict = my_car._asdict()
print(car_dict)
# Output: {'brand': 'Toyota', 'model': 'Camry', 'year': 2020}

# _replace() - Create new instance with modified values
new_car = my_car._replace(year=2021)
print(new_car)
# Output: Car(brand='Toyota', model='Camry', year=2021)

# _fields - Get field names
print(Car._fields)
# Output: ('brand', 'model', 'year')

# _make() - Create from iterable
car_data = ['Honda', 'Civic', 2019]
car2 = Car._make(car_data)
print(car2)
# Output: Car(brand='Honda', model='Civic', year=2019)
```

**Practical Example: Database Records**

```python
from collections import namedtuple

# Define database record structure
Employee = namedtuple('Employee', ['id', 'name', 'department', 'salary'])

# Create employee records
employees = [
    Employee(1, 'Alice', 'Engineering', 80000),
    Employee(2, 'Bob', 'Marketing', 65000),
    Employee(3, 'Charlie', 'Engineering', 90000),
    Employee(4, 'Diana', 'Sales', 70000)
]

# Filter engineers
engineers = [emp for emp in employees if emp.department == 'Engineering']
print(engineers)

# Calculate average salary
avg_salary = sum(emp.salary for emp in employees) / len(employees)
print(f"Average salary: ${avg_salary:,.2f}")

# Find highest paid employee
highest_paid = max(employees, key=lambda emp: emp.salary)
print(f"Highest paid: {highest_paid.name} - ${highest_paid.salary:,}")
```

---

## File Management with os and shutil

### os Module

The `os` module provides functions for interacting with the operating system.

```python
import os

# Get current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# List files and directories
files = os.listdir('.')
print(f"Files in current directory: {files}")

# Check if path exists
if os.path.exists('myfile.txt'):
    print("File exists")

# Check if it's a file or directory
print(os.path.isfile('myfile.txt'))  # True if file
print(os.path.isdir('myfolder'))  # True if directory

# Get file size
if os.path.exists('myfile.txt'):
    size = os.path.getsize('myfile.txt')
    print(f"File size: {size} bytes")

# Join paths (platform independent)
filepath = os.path.join('folder', 'subfolder', 'file.txt')
print(filepath)  # folder/subfolder/file.txt (or folder\subfolder\file.txt on Windows)

# Split path
directory, filename = os.path.split('/path/to/file.txt')
print(f"Directory: {directory}, Filename: {filename}")

# Get file extension
name, extension = os.path.splitext('document.pdf')
print(f"Name: {name}, Extension: {extension}")
```

### Creating and Removing Directories

```python
import os

# Create a single directory
os.mkdir('new_folder')

# Create nested directories
os.makedirs('parent/child/grandchild')

# Remove empty directory
os.rmdir('empty_folder')

# Note: os.rmdir() only works with empty directories!
# For non-empty directories, use shutil.rmtree()
```

### Deleting Files

```python
import os

# Delete a file
os.unlink('file_to_delete.txt')

# Alternative (same as unlink)
os.remove('another_file.txt')

# Check before deleting
if os.path.exists('myfile.txt'):
    os.unlink('myfile.txt')
    print("File deleted")
else:
    print("File doesn't exist")
```

### Walking Through Directory Tree

```python
import os

# os.walk() - traverse directory tree
for dirpath, dirnames, filenames in os.walk('.'):
    print(f"\nCurrent directory: {dirpath}")
    print(f"Subdirectories: {dirnames}")
    print(f"Files: {filenames}")

    # Process each file
    for filename in filenames:
        filepath = os.path.join(dirpath, filename)
        print(f"  - {filepath}")
```

**Practical Example: Find All Python Files**

```python
import os


def find_python_files(directory):
    """Find all .py files in directory and subdirectories."""
    python_files = []

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.py'):
                filepath = os.path.join(dirpath, filename)
                python_files.append(filepath)

    return python_files


# Usage
py_files = find_python_files('.')
print(f"Found {len(py_files)} Python files:")
for file in py_files:
    print(f"  - {file}")
```

### shutil Module

The `shutil` module provides high-level file operations.

```python
import shutil
import os

# Copy file
shutil.copy('source.txt', 'destination.txt')

# Copy file with metadata (permissions, timestamps)
shutil.copy2('source.txt', 'destination.txt')

# Copy entire directory tree
shutil.copytree('source_folder', 'destination_folder')

# Move file or directory
shutil.move('old_location.txt', 'new_location.txt')

# Move to different directory
shutil.move('file.txt', 'target_folder/')

# Rename by moving
shutil.move('old_name.txt', 'new_name.txt')

# Delete entire directory tree (including contents)
shutil.rmtree('folder_to_delete')

# Get disk usage
total, used, free = shutil.disk_usage('/')
print(f"Total: {total // (2 ** 30)} GB")
print(f"Used: {used // (2 ** 30)} GB")
print(f"Free: {free // (2 ** 30)} GB")
```

### send2trash (Safe Delete)

```python
# First install: pip install send2trash
from send2trash import send2trash

# Move to trash instead of permanent delete (safer!)
send2trash('file.txt')
send2trash('folder_name')

# You can restore from trash later if needed
```

**Complete File Management Example:**

```python
import os
import shutil
from datetime import datetime


def organize_files(source_dir):
    """Organize files by extension into folders."""

    # Create organized directory
    organized_dir = os.path.join(source_dir, 'organized')
    os.makedirs(organized_dir, exist_ok=True)

    # Walk through source directory
    for dirpath, dirnames, filenames in os.walk(source_dir):
        # Skip the organized directory itself
        if 'organized' in dirpath:
            continue

        for filename in filenames:
            # Get file extension
            name, ext = os.path.splitext(filename)
            ext = ext[1:].lower()  # Remove dot and lowercase

            if not ext:
                ext = 'no_extension'

            # Create folder for this extension
            ext_folder = os.path.join(organized_dir, ext)
            os.makedirs(ext_folder, exist_ok=True)

            # Move file
            source = os.path.join(dirpath, filename)
            destination = os.path.join(ext_folder, filename)

            try:
                shutil.move(source, destination)
                print(f"Moved: {filename} -> {ext_folder}")
            except Exception as e:
                print(f"Error moving {filename}: {e}")

# Usage
# organize_files('my_messy_folder')
```

---

## DateTime Module

The `datetime` module provides classes for working with dates and times.

### date

```python
from datetime import date

# Get current date
today = date.today()
print(today)  # 2026-01-19

# Create specific date
birthday = date(1990, 5, 15)
print(birthday)  # 1990-05-15

# Access components
print(today.year)  # 2026
print(today.month)  # 1
print(today.day)  # 19

# Day of week (0=Monday, 6=Sunday)
print(today.weekday())  # 0-6
print(today.isoweekday())  # 1-7

# Format date
print(today.strftime('%B %d, %Y'))  # January 19, 2026
print(today.strftime('%m/%d/%y'))  # 01/19/26
```

### time

```python
from datetime import time

# Create time
morning = time(9, 30, 0)  # 9:30:00
print(morning)  # 09:30:00

afternoon = time(14, 45, 30)  # 2:45:30 PM
print(afternoon)  # 14:45:30

# With microseconds
precise = time(12, 30, 45, 123456)
print(precise)  # 12:30:45.123456

# Access components
print(afternoon.hour)  # 14
print(afternoon.minute)  # 45
print(afternoon.second)  # 30
print(afternoon.microsecond)  # 0

# Format time
print(morning.strftime('%I:%M %p'))  # 09:30 AM
print(afternoon.strftime('%H:%M'))  # 14:45
```

### datetime

```python
from datetime import datetime

# Get current date and time
now = datetime.now()
print(now)  # 2026-01-19 14:30:45.123456

# Create specific datetime
dt = datetime(2025, 12, 25, 18, 30, 0)
print(dt)  # 2025-12-25 18:30:00

# Access components
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)

# Get just date or time
print(now.date())  # 2026-01-19
print(now.time())  # 14:30:45.123456

# Format datetime
print(now.strftime('%Y-%m-%d %H:%M:%S'))  # 2026-01-19 14:30:45
print(now.strftime('%B %d, %Y at %I:%M %p'))  # January 19, 2026 at 02:30 PM

# Parse string to datetime
date_string = '2025-12-25 18:30:00'
parsed_date = datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
print(parsed_date)  # 2025-12-25 18:30:00
```

**Common Format Codes:**

| Code | Meaning          | Example |
|------|------------------|---------|
| `%Y` | Year (4 digits)  | 2026    |
| `%y` | Year (2 digits)  | 26      |
| `%m` | Month (01-12)    | 01      |
| `%B` | Month name       | January |
| `%b` | Month abbr.      | Jan     |
| `%d` | Day (01-31)      | 19      |
| `%A` | Weekday          | Monday  |
| `%a` | Weekday abbr.    | Mon     |
| `%H` | Hour 24h (00-23) | 14      |
| `%I` | Hour 12h (01-12) | 02      |
| `%M` | Minute (00-59)   | 30      |
| `%S` | Second (00-59)   | 45      |
| `%p` | AM/PM            | PM      |

---

## Timeit Module

The `timeit` module measures execution time of code snippets.

### Basic Usage

```python
import timeit

# Method 1: Using string
code = """
result = 0
for i in range(1000):
    result += i
"""

execution_time = timeit.timeit(code, number=1000)
print(f"Execution time: {execution_time:.6f} seconds")

# Method 2: Using lambda
time_taken = timeit.timeit(lambda: sum(range(1000)), number=1000)
print(f"Time taken: {time_taken:.6f} seconds")
```

### Compare Different Approaches

```python
import timeit

# Setup code (runs once)
setup = "numbers = list(range(1000))"

# Method 1: Using for loop
method1 = """
result = 0
for num in numbers:
    result += num
"""

# Method 2: Using sum()
method2 = """
result = sum(numbers)
"""

# Method 3: Using reduce
method3 = """
from functools import reduce
result = reduce(lambda x, y: x + y, numbers)
"""

# Time each method
time1 = timeit.timeit(method1, setup=setup, number=10000)
time2 = timeit.timeit(method2, setup=setup, number=10000)
time3 = timeit.timeit(method3, setup=setup, number=10000)

print(f"For loop: {time1:.6f} seconds")
print(f"sum(): {time2:.6f} seconds")
print(f"reduce(): {time3:.6f} seconds")

# Find fastest
fastest = min(time1, time2, time3)
print(f"\nFastest method: {fastest:.6f} seconds")
```

### Using timeit with Functions

```python
import timeit


def method1():
    """Using list comprehension"""
    return [x ** 2 for x in range(100)]


def method2():
    """Using map"""
    return list(map(lambda x: x ** 2, range(100)))


def method3():
    """Using for loop"""
    result = []
    for x in range(100):
        result.append(x ** 2)
    return result


# Time each function
time1 = timeit.timeit(method1, number=10000)
time2 = timeit.timeit(method2, number=10000)
time3 = timeit.timeit(method3, number=10000)

print(f"List comprehension: {time1:.6f}s")
print(f"Map: {time2:.6f}s")
print(f"For loop: {time3:.6f}s")
```

### repeat() for Multiple Runs

```python
import timeit

code = "sum(range(1000))"

# Run 5 times, each with 1000 iterations
results = timeit.repeat(code, number=1000, repeat=5)

print("Results from 5 runs:")
for i, time in enumerate(results, 1):
    print(f"Run {i}: {time:.6f} seconds")

print(f"\nBest time: {min(results):.6f} seconds")
print(f"Average time: {sum(results) / len(results):.6f} seconds")
```

---

## Math Module

The `math` module provides mathematical functions.

### Basic Functions

```python
import math

# Constants
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045
print(math.tau)  # 6.283185307179586 (2*pi)
print(math.inf)  # Infinity
print(math.nan)  # Not a Number

# Rounding
print(math.ceil(4.3))  # 5 (round up)
print(math.floor(4.7))  # 4 (round down)
print(math.trunc(4.7))  # 4 (remove decimal)

# Absolute value
print(math.fabs(-5.5))  # 5.5

# Power and roots
print(math.pow(2, 3))  # 8.0 (2³)
print(math.sqrt(16))  # 4.0 (√16)
print(math.cbrt(27))  # 3.0 (∛27)

# Logarithms
print(math.log(10))  # 2.302... (natural log)
print(math.log10(100))  # 2.0 (base 10)
print(math.log2(8))  # 3.0 (base 2)

# Trigonometry (angles in radians)
print(math.sin(math.pi / 2))  # 1.0
print(math.cos(0))  # 1.0
print(math.tan(math.pi / 4))  # 1.0

# Convert between degrees and radians
print(math.degrees(math.pi))  # 180.0
print(math.radians(180))  # 3.141592...

# Factorial
print(math.factorial(5))  # 120 (5! = 5×4×3×2×1)

# GCD (Greatest Common Divisor)
print(math.gcd(48, 18))  # 6

# Check special values
print(math.isnan(float('nan')))  # True
print(math.isinf(math.inf))  # True
print(math.isfinite(10))  # True
```

---

## Regular Expressions

Regular expressions (regex) are patterns used to match text.

### Basic Patterns

```python
import re

text = "The phone numbers are 123-456-7890 and 098-765-4321"

# \d - Digit (0-9)
digits = re.findall(r'\d', text)
print(digits)  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ...]

# \w - Alphanumeric character (a-z, A-Z, 0-9, _)
words = re.findall(r'\w+', text)
print(words)  # ['The', 'phone', 'numbers', 'are', '123', ...]

# \s - Whitespace
spaces = re.findall(r'\s', text)
print(spaces)  # [' ', ' ', ' ', ' ', ...]

# \D - NOT a digit
non_digits = re.findall(r'\D', text)
print(non_digits)  # ['T', 'h', 'e', ' ', 'p', 'h', 'o', 'n', 'e', ...]

# \W - NOT alphanumeric
non_alphanumeric = re.findall(r'\W', text)
print(non_alphanumeric)  # [' ', ' ', ' ', ' ', '-', '-', ...]

# \S - NOT whitespace
non_whitespace = re.findall(r'\S+', text)
print(non_whitespace)  # ['The', 'phone', 'numbers', 'are', ...]
```

### Quantifiers

```python
import re

text = "Contact: 123-456-7890, email: test@example.com"

# + : 1 or more times
phone = re.findall(r'\d+', text)
print(phone)  # ['123', '456', '7890']

# {n} : Exactly n times
three_digits = re.findall(r'\d{3}', text)
print(three_digits)  # ['123', '456', '789']

# {n,m} : Between n and m times
ranges = re.findall(r'\d{2,4}', text)
print(ranges)  # ['123', '456', '7890']

# {n,} : n or more times
four_or_more = re.findall(r'\d{4,}', text)
print(four_or_more)  # ['7890']

# * : 0 or more times
pattern = re.findall(r'\d*', text)
print(pattern)  # Includes empty strings

# ? : 0 or 1 time (optional)
optional = re.findall(r'colou?r', 'color colour')
print(optional)  # ['color', 'colour']
```

### Common Regex Patterns

```python
import re

# Email validation
email_pattern = r'\w+@\w+\.\w+'
emails = re.findall(email_pattern, "Contact: john@email.com, jane@test.org")
print(emails)  # ['john@email.com', 'jane@test.org']

# Phone number (XXX-XXX-XXXX)
phone_pattern = r'\d{3}-\d{3}-\d{4}'
phones = re.findall(phone_pattern, "Call 123-456-7890 or 098-765-4321")
print(phones)  # ['123-456-7890', '098-765-4321']

# URL
url_pattern = r'https?://\w+\.\w+'
urls = re.findall(url_pattern, "Visit https://example.com or http://test.org")
print(urls)  # ['https://example.com', 'http://test.org']

# Date (YYYY-MM-DD)
date_pattern = r'\d{4}-\d{2}-\d{2}'
dates = re.findall(date_pattern, "Events: 2026-01-15 and 2026-12-25")
print(dates)  # ['2026-01-15', '2026-12-25']

# Credit card (XXXX-XXXX-XXXX-XXXX)
card_pattern = r'\d{4}-\d{4}-\d{4}-\d{4}'
cards = re.findall(card_pattern, "Card: 1234-5678-9012-3456")
print(cards)  # ['1234-5678-9012-3456']
```

### Regex Functions

```python
import re

text = "The price is $29.99 and $49.99"

# findall() - Find all matches
prices = re.findall(r'\$\d+\.\d{2}', text)
print(prices)  # ['$29.99', '$49.99']

# search() - Find first match (returns Match object)
match = re.search(r'\$\d+\.\d{2}', text)
if match:
    print(match.group())  # $29.99
    print(match.start())  # 13 (position)
    print(match.end())  # 19

# match() - Match from beginning of string
result = re.match(r'The', text)
print(result.group() if result else "No match")  # The

# split() - Split string by pattern
parts = re.split(r'\s+', text)
print(parts)  # ['The', 'price', 'is', '$29.99', 'and', '$49.99']

# sub() - Replace pattern
new_text = re.sub(r'\$\d+\.\d{2}', '[PRICE]', text)
print(new_text)  # The price is [PRICE] and [PRICE]

# finditer() - Iterator of Match objects
for match in re.finditer(r'\$\d+\.\d{2}', text):
    print(f"Found {match.group()} at position {match.start()}")
```

---

## Zipfile Module

The `zipfile` module allows you to create, read, and extract ZIP archives.

### Creating ZIP Files

```python
import zipfile
import os

# Create a new ZIP file
with zipfile.ZipFile('myarchive.zip', 'w') as zipf:
    # Add single file
    zipf.write('file1.txt')

    # Add file with different name in archive
    zipf.write('file2.txt', arcname='renamed_file.txt')

    # Add file with compression
    zipf.write('file3.txt', compress_type=zipfile.ZIP_DEFLATED)

print("ZIP file created successfully")

# Add multiple files
files_to_zip = ['file1.txt', 'file2.txt', 'file3.txt']

with zipfile.ZipFile('multiple_files.zip', 'w') as zipf:
    for file in files_to_zip:
        if os.path.exists(file):
            zipf.write(file)
            print(f"Added {file}")
```

### Reading ZIP Files

```python
import zipfile

# Open and read ZIP file
with zipfile.ZipFile('myarchive.zip', 'r') as zipf:
    # List all files in archive
    print("Files in archive:")
    for filename in zipf.namelist():
        print(f"  - {filename}")

    # Get info about files
    for info in zipf.infolist():
        print(f"\nFile: {info.filename}")
        print(f"  Size: {info.file_size} bytes")
        print(f"  Compressed: {info.compress_size} bytes")
        print(f"  Modified: {info.date_time}")

    # Read specific file
    with zipf.open('file1.txt') as f:
        content = f.read()
        print(f"\nContent of file1.txt:")
        print(content.decode())
```

### Extracting ZIP Files

```python
import zipfile

# Extract all files
with zipfile.ZipFile('myarchive.zip', 'r') as zipf:
    # Extract to current directory
    zipf.extractall()
    print("All files extracted")

# Extract to specific directory
with zipfile.ZipFile('myarchive.zip', 'r') as zipf:
    zipf.extractall('extracted_files/')
    print("Files extracted to 'extracted_files/'")

# Extract specific file
with zipfile.ZipFile('myarchive.zip', 'r') as zipf:
    zipf.extract('file1.txt', 'specific_folder/')
    print("file1.txt extracted")
```

### Adding Files to Existing ZIP

```python
import zipfile

# Append to existing ZIP
with zipfile.ZipFile('myarchive.zip', 'a') as zipf:
    zipf.write('new_file.txt')
    print("File added to existing archive")
```

### Checking ZIP File Integrity

```python
import zipfile


# Test if ZIP is valid
def test_zip(zip_path):
    """Test ZIP file integrity."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            # Test all files
            bad_file = zipf.testzip()

            if bad_file:
                print(f"Bad file in archive: {bad_file}")
            else:
                print("ZIP file is valid")
                return True
    except zipfile.BadZipFile:
        print("Invalid ZIP file")
        return False


test_zip('myarchive.zip')
```

### Password-Protected ZIP

```python
import zipfile

# Create password-protected ZIP
with zipfile.ZipFile('protected.zip', 'w') as zipf:
    zipf.write('sensitive.txt')
    # Set password (write mode)
    zipf.setpassword(b'mypassword')

# Extract password-protected ZIP
with zipfile.ZipFile('protected.zip', 'r') as zipf:
    # Set password (read mode)
    zipf.setpassword(b'mypassword')
    zipf.extractall('extracted/')
    print("Password-protected ZIP extracted")
```

---

## Quick Reference

### Collections

- `Counter()` - Count elements
- `defaultdict(type)` - Default values for missing keys
- `namedtuple('Name', ['field1', 'field2'])` - Named tuples

### File Management

- `os.walk(path)` - Traverse directories
- `os.unlink(file)` - Delete file
- `os.rmdir(dir)` - Delete empty directory
- `shutil.move(src, dst)` - Move file/directory
- `shutil.rmtree(dir)` - Delete directory tree
- `send2trash(path)` - Move to trash

### DateTime

- `date.today()` - Current date
- `datetime.now()` - Current date and time
- `timedelta(days=1)` - Time duration
- `strftime(format)` - Format as string
- `strptime(string, format)` - Parse string

### Timeit

- `timeit.timeit(code, number=1000)` - Time code execution
- `timeit.repeat(code, repeat=5)` - Multiple timing runs

### Regular Expressions

- `\d` - Digit, `\w` - Alphanumeric, `\s` - Whitespace
- `+` - 1 or more, `*` - 0 or more, `?` - 0 or 1
- `{n}` - Exactly n, `{n,m}` - Between n and m
- `re.findall()`, `re.search()`, `re.sub()`

### Zipfile

- `ZipFile(name, 'w')` - Create
- `ZipFile(name, 'r')` - Read
- `zipf.write(file)` - Add file
- `zipf.extractall()` - Extract all
- `zipf.namelist()` - List contents

[<< Day 8](../day_08/day_08.md) | [Day 10 >>](../day_10/day_10.md)