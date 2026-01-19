# 📘 Day 2

## Variables and Data Types

```py
# Integer
age = 25  # age is an integer
# Float
height = 5.9  # height is a float
# String
name = "John Doe"  # name is a string
# Boolean
is_student = True  # is_student is a boolean
```

Check Data types: To check the data type of certain data/variable we use the _type_
**Examples:**

- `type(age)` will return `<class 'int'>`
- `type(height)` will return `<class 'float'>`
- `type(name)` will return `<class 'str'>`

## Basic Arithmetic Operations

```py
a = 10
b = 3

# Addition
sum_result = a + b  # 13
# Subtraction
diff_result = a - b  # 7
# Multiplication
prod_result = a * b  # 30
# Division
div_result = a / b  # 3.3333...
# Floor Division
floor_div_result = a // b  # 3
# Modulus
mod_result = a % b  # 1
# Exponentiation
exp_result = a ** b  # 1000
# Rounding
rounded_value = round(3.14159, 2)  # 3.
```

## String Formatting

String formatting allows you to create strings with dynamic content.

```py
name = "Alice"
age = 30
# Using f-strings
greet = f"My name is {name} and I am {age} years old."

# Using format method
greeting = "My name is {} and I am {} years old.".format(name, age)
```

## Type Conversions: Integer, Float, String

```py
# Converting integer to float, string
int_num = 10
float_num = float(int_num)
str_num = str(int_num)

# Converting float to integer, string
float_value = 15.5
int_value1 = int(float_value)
str_value1 = str(float_value)

# Converting string to integer, float
str_value2 = "20"
int_value2 = int(str_value2)
float_value = float(str_value2)
```

[<< Day 1](../day_01/day_01.md) | [Day 3 >>](../day_03/day_03.md)