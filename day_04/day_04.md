# 📘 Day 4

## Comparison Operators, Logical Operators and Loops

## Table of Contents

1. [Comparison Operators](#comparison-operators)
2. [Logical Operators](#logical-operators)
3. [Control Flow](#control-flow)

---

#### Comparison Operators

Comparison operators are used to compare two values and return a boolean value (`True` or `False`).

List of Comparison Operators

| Operator | Description              | Example           |
|----------|--------------------------|-------------------|
| `==`     | Equal to                 | `5 == 5` → `True` |
| `!=`     | Not equal to             | `5 != 3` → `True` |
| `>`      | Greater than             | `7 > 3` → `True`  |
| `<`      | Less than                | `3 < 7` → `True`  |
| `>=`     | Greater than or equal to | `5 >= 5` → `True` |
| `<=`     | Less than or equal to    | `4 <= 6` → `True` |

##### Practical Examples

```python
# Comparing numbers
age = 18
print(age >= 18)  # True - is greater than or equal to 18

# Comparing strings
name = "Ana"
print(name == "Ana")  # True
print(name != "Pedro")  # True

# Comparing in real context
price = 50
discount_applied = price < 100
print(discount_applied)  # True

# Multiple comparisons
temperature = 25
is_nice_weather = temperature > 20 and temperature < 30
print(is_nice_weather)  # True
```

---

#### Logical Operators

Logical operators are used to combine conditional expressions.

Types of Logical Operators

##### 1. `and` (Logical AND)

Returns `True` only if **both** conditions are true.

```python
age = 25
has_license = True

can_drive = age >= 18 and has_license
print(can_drive)  # True

# Example with False
age = 16
can_drive = age >= 18 and has_license
print(can_drive)  # False (because age < 18)
```

##### 2. `or` (Logical OR)

Returns `True` if **at least one** condition is true.

```python
is_weekend = True
is_holiday = False

can_rest = is_weekend or is_holiday
print(can_rest)  # True

# Example where both are False
is_weekend = False
is_holiday = False
can_rest = is_weekend or is_holiday
print(can_rest)  # False
```

##### 3. `not` (Logical NOT)

Inverts the boolean value.

```python
is_raining = False
can_go_out = not is_raining
print(can_go_out)  # True

# Another example
system_active = True
system_off = not system_active
print(system_off)  # False
```

##### Truth Table

| A     | B     | A and B | A or B | not A |
|-------|-------|---------|--------|-------|
| True  | True  | True    | True   | False |
| True  | False | False   | True   | False |
| False | True  | False   | True   | True  |
| False | False | False   | False  | True  |

##### Combined Examples

```python
# Check if a number is in a range
number = 15
in_range = number >= 10 and number <= 20
print(in_range)  # True

# Access system
username = "admin"
password = "1234"
has_access = (username == "admin" and password == "1234") or username == "superadmin"
print(has_access)  # True

# Complex validation
age = 17
is_student = True
has_discount = (age < 18 or age > 65) and is_student
print(has_discount)  # True
```

---

#### Control Flow

Control flow allows your program to make decisions and execute different blocks of code based on conditions.

##### 1. `if` Statement

Executes a block of code only if the condition is `True`.

```python
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")

# Output: 
# You are an adult
# You can vote
```

##### 2. `if-else` Statement

Executes one block if the condition is `True`, and another block if it's `False`.

```python
temperature = 15

if temperature > 25:
    print("It's hot, wear light clothes")
else:
    print("It's cold, bundle up")

# Output: It's cold, bundle up
```

##### 3. `if-elif-else` Statement

Allows checking multiple conditions.

```python
grade = 85

if grade >= 90:
    print("Excellent - A")
elif grade >= 80:
    print("Very Good - B")
elif grade >= 70:
    print("Good - C")
elif grade >= 60:
    print("Pass - D")
else:
    print("Fail - F")

# Output: Very Good - B
```

##### 4. Nested Conditionals

You can place an `if` inside another `if`.

```python
age = 25
has_license = True

if age >= 18:
    print("You are an adult")
    if has_license:
        print("You can drive")
    else:
        print("You need to get a license")
else:
    print("You are a minor")

# Output:
# You are an adult
# You can drive
```

##### 5. Ternary Operator

A compact way to write `if-else` in a single line.

```python
age = 20
message = "Adult" if age >= 18 else "Minor"
print(message)  # Adult

# Example with numbers
a = 10
b = 20
greater = a if a > b else b
print(greater)  # 20
```

[<< Day 3](../day_03/day_03.md) | [Day 5 >>](../day_05/day_05.md)