# 📘 Day 6

## File Management

In Python, file management is primarily done with the `open()`, `read()`, `write()`, and `close()` functions. These allow you to read and write data to files on the system.

#### 1. `open()` - Opening files

The `open()` function is used to open a file and returns a file object.

**Syntax:**
```python
file = open(filename, mode)
```

**Main modes:**
- `'r'` - Read - Default. Error if the file doesn't exist.
- `'w'` - Write - Creates the file if it doesn't exist, overwrites if it exists.
- `'a'` - Append - Creates the file if it doesn't exist, appends to the end if it exists.
- `'r+'` - Read and write.
- `'b'` - Binary mode (example: `'rb'`, `'wb'`).

**Example:**
```python
# Open file for reading
file = open('data.txt', 'r')

# Open file for writing
file = open('output.txt', 'w')

# Open file for appending content
file = open('log.txt', 'a')
```

#### 2. `read()` - Reading files

The `read()` method reads the complete content of the file or a specific number of characters.

**Syntax:**
```python
content = file.read(size)  # size is optional
```

**Examples:**
```python
# Read all content
file = open('data.txt', 'r')
content = file.read()
print(content)
file.close()

# Read the first 10 characters
file = open('data.txt', 'r')
first_10 = file.read(10)
print(first_10)
file.close()

# Read line by line
file = open('data.txt', 'r')
line = file.readline()  # Reads one line
print(line)
file.close()

# Read all lines into a list
file = open('data.txt', 'r')
lines = file.readlines()  # Returns list of lines
for line in lines:
    print(line.strip())  # strip() removes newlines
file.close()
```

#### 3. `write()` - Writing to files

The `write()` method writes a string of text to the file.

**Syntax:**
```python
file.write(text)
```

**Examples:**
```python
# Write to a file (overwrites existing content)
file = open('output.txt', 'w')
file.write('Hello, world!\n')
file.write('This is a second line.\n')
file.close()

# Append content to the end of the file
file = open('log.txt', 'a')
file.write('New log entry.\n')
file.close()

# Write multiple lines using writelines()
file = open('list.txt', 'w')
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
file.writelines(lines)
file.close()
```

#### 4. `close()` - Closing files

The `close()` method closes the file and frees system resources.

**Example:**
```python
file = open('data.txt', 'r')
content = file.read()
file.close()  # Important: always close the file
```

#### Best practice: Using `with`

The most recommended way to work with files is using the `with` statement, which automatically closes the file even if an error occurs.

**Syntax:**
```python
with open(filename, mode) as file:
    # File operations
    pass
# The file is automatically closed when exiting the with block
```

**Examples:**
```python
# Reading with with
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)
# No need to call close()

# Writing with with
with open('output.txt', 'w') as file:
    file.write('File content\n')
    file.write('Second line\n')

# Reading and processing line by line
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

#### Complete example

```python
# Write data to a file
with open('students.txt', 'w') as file:
    file.write('John,20,Engineering\n')
    file.write('Mary,22,Medicine\n')
    file.write('Peter,21,Architecture\n')

# Read and process the data
with open('students.txt', 'r') as file:
    for line in file:
        name, age, major = line.strip().split(',')
        print(f'Name: {name}, Age: {age}, Major: {major}')
```

---

### `pathlib` Module

`pathlib` is a modern Python module (since version 3.4) that provides an object-oriented way to work with file and directory paths. It's more intuitive and powerful than using `os.path` functions.

#### Importing pathlib

```python
from pathlib import Path
```

#### Creating Path objects

```python
# Current directory path
current_path = Path.cwd()
print(current_path)

# User's home directory path
home_path = Path.home()
print(home_path)

# Create a specific path
file = Path('data.txt')
full_path = Path('/Users/user/documents/file.txt')

# Create paths by combining parts
directory = Path('projects')
subdirectory = directory / 'python' / 'scripts'
print(subdirectory)  # projects/python/scripts
```

#### Useful Path properties

```python
file = Path('/Users/user/documents/project/main.py')

# File name with extension
print(file.name)  # main.py

# Name without extension
print(file.stem)  # main

# File extension
print(file.suffix)  # .py

# Parent directory
print(file.parent)  # /Users/user/documents/project

# All parent directories
print(list(file.parents))

# Absolute path
print(file.absolute())

# Check if it's absolute
print(file.is_absolute())  # True
```

#### Checking existence and type

```python
path = Path('data.txt')

# Check if exists
if path.exists():
    print('The file exists')

# Check if it's a file
if path.is_file():
    print('It is a file')

# Check if it's a directory
if path.is_dir():
    print('It is a directory')

# Check if it's a symbolic link
if path.is_symlink():
    print('It is a symbolic link')
```

#### Reading and writing with pathlib

```python
# Read all file content
path = Path('data.txt')
content = path.read_text()
print(content)

# Read binary content
binary_content = path.read_bytes()

# Write text to a file
path = Path('output.txt')
path.write_text('Hello, world!\nThis is a new line.')

# Write binary content
path.write_bytes(b'Binary content')

# Open file with open (as context)
path = Path('data.txt')
with path.open('r') as file:
    for line in file:
        print(line.strip())
```

#### Directory operations

```python
# Create a directory
directory = Path('new_directory')
directory.mkdir(exist_ok=True)  # exist_ok=True avoids error if already exists

# Create nested directories
path = Path('project/src/utils')
path.mkdir(parents=True, exist_ok=True)  # parents=True creates necessary parents

# List files in a directory
directory = Path('.')
for item in directory.iterdir():
    print(item)

# Search files with pattern (glob)
# Search all .txt files in current directory
for file in directory.glob('*.txt'):
    print(file)

# Search recursively in subdirectories
for file in directory.rglob('*.py'):  # Finds all .py files recursively
    print(file)

# Remove an empty directory
directory.rmdir()
```

#### Path manipulation

```python
# Change file extension
file = Path('document.txt')
new_file = file.with_suffix('.md')
print(new_file)  # document.md

# Change file name
new_name = file.with_name('report.txt')
print(new_name)  # report.txt

# Resolve path (convert to absolute path)
path = Path('data.txt')
absolute_path = path.resolve()
print(absolute_path)

# Join paths
base = Path('/home/user')
full = base / 'documents' / 'project' / 'main.py'
print(full)
```

#### File information

```python
file = Path('data.txt')

# File size in bytes
if file.exists():
    size = file.stat().st_size
    print(f'Size: {size} bytes')

    # Last modification date
    from datetime import datetime
    timestamp = file.stat().st_mtime
    date = datetime.fromtimestamp(timestamp)
    print(f'Last modified: {date}')

# Delete a file
if file.exists():
    file.unlink()  # Deletes the file

# Rename or move a file
file = Path('old_name.txt')
if file.exists():
    file.rename('new_name.txt')
```

#### Complete example with pathlib

```python
from pathlib import Path

# Create project structure
project = Path('my_project')
project.mkdir(exist_ok=True)

# Create subdirectories
(project / 'src').mkdir(exist_ok=True)
(project / 'tests').mkdir(exist_ok=True)
(project / 'docs').mkdir(exist_ok=True)

# Create a README file
readme = project / 'README.md'
readme.write_text('# My Project\n\nProject description.')

# Create a Python file
python_file = project / 'src' / 'main.py'
python_file.write_text('''def main():
    print("Hello from my project")

if __name__ == "__main__":
    main()
''')

# List all created files
print('Files in the project:')
for file in project.rglob('*'):
    if file.is_file():
        print(f'  {file.relative_to(project)} ({file.stat().st_size} bytes)')
```

#### Comparison: pathlib vs os.path

```python
# Traditional way with os.path
import os

path = os.path.join('/Users', 'user', 'documents', 'file.txt')
if os.path.exists(path):
    name = os.path.basename(path)
    extension = os.path.splitext(name)[1]

# Modern way with pathlib (more readable)
from pathlib import Path

path = Path('/Users') / 'user' / 'documents' / 'file.txt'
if path.exists():
    name = path.name
    extension = path.suffix
```

**Advantages of pathlib:**
- Cleaner, object-oriented syntax
- `/` operator to join paths naturally
- Built-in methods for common operations
- Cross-platform (handles differences between Windows, Linux, macOS automatically)
- Easier to read and maintain

[<< Day 5](../day_05/day_05.md) | [Day 7 >>](../day_07/day_07.md)
