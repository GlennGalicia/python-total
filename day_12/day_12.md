# 📘 Day 12

## Tkinder Module

## Table of Contents

1. [What is Tkinder](#what-is-tkinter)
2. [Installation](#installation)
3. [Basic Concepts](#basic-concepts)
4. [Common Widgets](#common-widgets)
5. [Layout Managers](#layout-managers)
6. [Additional Resources](#additional-resources)

---

## What is Tkinter?

Tkinter is Python's standard GUI (Graphical User Interface) library. It comes pre-installed with Python, making it the easiest way to create desktop applications with windows, buttons, text fields, and more.

**Use cases:**

- Desktop applications
- Data entry forms
- Simple games
- Calculators and tools
- Settings interfaces
- Admin panels

## Installation

### Already Included!

Tkinter comes with Python, so no installation needed in most cases.

```bash
# Verify Tkinter is installed
python -m tkinter

# This should open a simple test window
```

### Project Structure

```
my-app/
├── .venv/
├── pyproject.toml
├── src/
│   ├── main.py
│   ├── gui/
│   │   ├── windows.py
│   │   └── widgets.py
│   └── utils/
│       └── helpers.py
└── README.md
```

## Basic Concepts

### 1. Creating a Simple Window

```python
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("My First App")
root.geometry("400x300")  # Width x Height

# Start the application
root.mainloop()
```

### 2. Adding a Label

```python
import tkinter as tk

root = tk.Tk()
root.title("Label Example")

# Create label
label = tk.Label(root, text="Hello, World!")
label.pack()

root.mainloop()
```

### 3. Adding a Button

```python
import tkinter as tk


def button_clicked():
    print("Button was clicked!")


root = tk.Tk()
root.title("Button Example")

# Create button
button = tk.Button(root, text="Click Me", command=button_clicked)
button.pack()

root.mainloop()
```

### 4. Text Entry Field

```python
import tkinter as tk


def show_text():
    text = entry.get()
    print(f"You entered: {text}")


root = tk.Tk()
root.title("Entry Example")

# Create entry field
entry = tk.Entry(root)
entry.pack()

# Create button to get text
button = tk.Button(root, text="Submit", command=show_text)
button.pack()

root.mainloop()
```

### 5. Updating Labels

```python
import tkinter as tk


def update_label():
    text = entry.get()
    label.config(text=f"Hello, {text}!")


root = tk.Tk()
root.title("Update Label")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet", command=update_label)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
```

## Common Widgets

### 1. Button

```python
import tkinter as tk

root = tk.Tk()

# Simple button
button1 = tk.Button(root, text="Normal Button")
button1.pack()

# Styled button
button2 = tk.Button(
    root,
    text="Styled Button",
    bg="blue",  # Background color
    fg="white",  # Text color
    font=("Arial", 12)
)
button2.pack()

root.mainloop()
```

### 2. Label

```python
import tkinter as tk

root = tk.Tk()

# Simple label
label1 = tk.Label(root, text="Simple Label")
label1.pack()

# Styled label
label2 = tk.Label(
    root,
    text="Styled Label",
    bg="yellow",
    font=("Arial", 16, "bold")
)
label2.pack()

root.mainloop()
```

### 3. Entry (Text Input)

```python
import tkinter as tk

root = tk.Tk()

# Normal entry
entry1 = tk.Entry(root)
entry1.pack()

# Password entry
entry2 = tk.Entry(root, show="*")
entry2.pack()

# Entry with default text
entry3 = tk.Entry(root)
entry3.insert(0, "Default text")
entry3.pack()

root.mainloop()
```

### 4. Text (Multi-line)

```python
import tkinter as tk

root = tk.Tk()

# Multi-line text area
text = tk.Text(root, height=5, width=30)
text.pack()


# Get text from Text widget
def get_text():
    content = text.get("1.0", "end-1c")  # Get all text
    print(content)


button = tk.Button(root, text="Get Text", command=get_text)
button.pack()

root.mainloop()
```

### 5. Checkbutton

```python
import tkinter as tk

root = tk.Tk()

# Variable to store checkbox state
var = tk.BooleanVar()


def show_state():
    if var.get():
        print("Checked")
    else:
        print("Unchecked")


checkbox = tk.Checkbutton(
    root,
    text="Accept Terms",
    variable=var,
    command=show_state
)
checkbox.pack()

root.mainloop()
```

### 6. Radiobutton

```python
import tkinter as tk

root = tk.Tk()

# Variable to store selected option
var = tk.StringVar()
var.set("option1")  # Default value


def show_choice():
    print(f"Selected: {var.get()}")


# Create radio buttons
tk.Radiobutton(root, text="Option 1", variable=var, value="option1").pack()
tk.Radiobutton(root, text="Option 2", variable=var, value="option2").pack()
tk.Radiobutton(root, text="Option 3", variable=var, value="option3").pack()

button = tk.Button(root, text="Show Choice", command=show_choice)
button.pack()

root.mainloop()
```

### 7. Listbox

```python
import tkinter as tk

root = tk.Tk()

# Create listbox
listbox = tk.Listbox(root)
listbox.pack()

# Add items
items = ["Apple", "Banana", "Orange", "Grape"]
for item in items:
    listbox.insert(tk.END, item)


# Get selected item
def show_selection():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        item = listbox.get(index)
        print(f"Selected: {item}")


button = tk.Button(root, text="Show Selection", command=show_selection)
button.pack()

root.mainloop()
```

### 8. Combobox (Dropdown)

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create combobox
combo = ttk.Combobox(root, values=["Python", "Java", "C++", "JavaScript"])
combo.pack()
combo.set("Python")  # Default value


def show_selection():
    print(f"Selected: {combo.get()}")


button = tk.Button(root, text="Show Selection", command=show_selection)
button.pack()

root.mainloop()
```

## Layout Managers

### 1. Pack (Simple Stacking)

```python
import tkinter as tk

root = tk.Tk()

# Stack vertically (default)
tk.Label(root, text="Top").pack()
tk.Label(root, text="Middle").pack()
tk.Label(root, text="Bottom").pack()

# Stack horizontally
tk.Label(root, text="Left").pack(side="left")
tk.Label(root, text="Right").pack(side="right")

root.mainloop()
```

### 2. Grid (Table Layout)

```python
import tkinter as tk

root = tk.Tk()

# Create grid layout
tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="Email:").grid(row=1, column=0)
tk.Entry(root).grid(row=1, column=1)

tk.Button(root, text="Submit").grid(row=2, column=0, columnspan=2)

root.mainloop()
```

### 3. Place (Absolute Positioning)

```python
import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Place widgets at specific coordinates
label = tk.Label(root, text="I'm at (50, 50)")
label.place(x=50, y=50)

button = tk.Button(root, text="I'm at (100, 100)")
button.place(x=100, y=100)

root.mainloop()
```

## Additional Resources

### Official Documentation
- [Tkinter Docs](https://docs.python.org/3/library/tkinter.html)
- [Tkinter ttk](https://docs.python.org/3/library/tkinter.ttk.html) - Themed widgets

### Tutorials
- [Real Python Tkinter](https://realpython.com/python-gui-tkinter/)
- [TkDocs](https://tkdocs.com/) - Modern Tkinter tutorial

### Tools
- `ttkbootstrap` - Modern themes for Tkinter
- `CustomTkinter` - Modern and customizable widgets


[<< Day 11](../day_11/day_11.md) | [Day 13 >>](../day_13/day_13.md)