# 📘 Day 5

## Functions

Functions are reusable blocks of code that perform a specific task. They help organize code, improve readability, and reduce repetition.

#### 1. Basic Function Definition

**Syntax:**

```python
def function_name(parameters):
    # Function body
    return value  # optional
```

**Examples:**

```python
# Simple function without parameters
def greet():
    print("Hello, World!")


greet()  # Output: Hello, World!


# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")


greet_person("Alice")  # Output: Hello, Alice!


# Function with return value
def add(a, b):
    return a + b


result = add(5, 3)
print(result)  # Output: 8


# Function with multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)


minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")  # Output: Min: 1, Max: 9
```

#### 2. Default Parameters

Functions can have default values for parameters, making them optional when calling the function.

**Syntax:**

```python
def function_name(param1, param2=default_value):
    # Function body
    pass
```

**Examples:**

```python
# Function with default parameter
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Hi")  # Output: Hi, Bob!
greet("Charlie", greeting="Hey")  # Output: Hey, Charlie!


# Multiple default parameters
def create_profile(name, age=18, country="USA"):
    return f"{name}, {age} years old, from {country}"


print(create_profile("John"))  # John, 18 years old, from USA
print(create_profile("Maria", 25))  # Maria, 25 years old, from USA
print(create_profile("Chen", 30, "China"))  # Chen, 30 years old, from China
```

#### 3. `*args` - Arbitrary Positional Arguments

The `*args` parameter allows a function to accept any number of positional arguments. The arguments are received as a **tuple**.

**Syntax:**

```python
def function_name(*args):
    # args is a tuple containing all positional arguments
    pass
```

**Examples:**

```python
# Basic *args usage
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(10, 20, 30, 40))  # Output: 100
print(sum_all(5))  # Output: 5


# *args with regular parameters
def describe_purchase(store, *items):
    print(f"Shopping at {store}:")
    for item in items:
        print(f"  - {item}")


describe_purchase("Walmart", "Milk", "Bread", "Eggs")


# Output:
# Shopping at Walmart:
#   - Milk
#   - Bread
#   - Eggs

# Working with *args as a tuple
def print_info(*args):
    print(f"Type: {type(args)}")  # Type: <class 'tuple'>
    print(f"Length: {len(args)}")  # Number of arguments
    print(f"Items: {args}")  # All items as tuple


print_info("Python", 3.9, True)


# Output:
# Type: <class 'tuple'>
# Length: 3
# Items: ('Python', 3.9, True)

# Using * to unpack a list/tuple
def multiply(a, b, c):
    return a * b * c


numbers = [2, 3, 4]
result = multiply(*numbers)  # Unpacks list as separate arguments
print(result)  # Output: 24
```

#### 4. `**kwargs` - Arbitrary Keyword Arguments

The `**kwargs` parameter allows a function to accept any number of keyword arguments. The arguments are received as a **dictionary**.

**Syntax:**

```python
def function_name(**kwargs):
    # kwargs is a dictionary containing all keyword arguments
    pass
```

**Examples:**

```python
# Basic **kwargs usage
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=25, city="New York")


# Output:
# name: Alice
# age: 25
# city: New York

# **kwargs with regular parameters
def create_user(username, **details):
    print(f"Username: {username}")
    print("Additional details:")
    for key, value in details.items():
        print(f"  {key}: {value}")


create_user("john_doe", email="john@example.com", age=30, country="USA")


# Output:
# Username: john_doe
# Additional details:
#   email: john@example.com
#   age: 30
#   country: USA

# Working with **kwargs as a dictionary
def display_settings(**settings):
    print(f"Type: {type(settings)}")  # Type: <class 'dict'>
    print(f"Settings: {settings}")  # Dictionary of settings


display_settings(theme="dark", font_size=14, auto_save=True)


# Output:
# Type: <class 'dict'>
# Settings: {'theme': 'dark', 'font_size': 14, 'auto_save': True}

# Using ** to unpack a dictionary
def register(name, email, age):
    print(f"Name: {name}, Email: {email}, Age: {age}")


user_data = {"name": "Alice", "email": "alice@example.com", "age": 25}
register(**user_data)  # Unpacks dictionary as keyword arguments
# Output: Name: Alice, Email: alice@example.com, Age: 25
```

#### 5. Combining All Parameter Types

You can combine regular parameters, default parameters, `*args`, and `**kwargs` in a single function. **Order matters**: positional, *args, default parameters, **kwargs.

**Syntax:**

```python
def function_name(pos_param, *args, default_param=value, **kwargs):
    pass
```

**Examples:**

```python
# Combining all parameter types
def process_order(order_id, *items, discount=0, **customer_info):
    print(f"Order ID: {order_id}")
    print(f"Items: {items}")
    print(f"Discount: {discount}%")
    print(f"Customer Info: {customer_info}")


process_order(
    12345,
    "Laptop", "Mouse", "Keyboard",
    discount=10,
    name="John Doe",
    email="john@example.com"
)


# Output:
# Order ID: 12345
# Items: ('Laptop', 'Mouse', 'Keyboard')
# Discount: 10%
# Customer Info: {'name': 'John Doe', 'email': 'john@example.com'}

# Practical example: Flexible data processor
def process_data(data_source, *transformations, verbose=False, **options):
    print(f"Processing data from: {data_source}")

    if verbose:
        print(f"Applying {len(transformations)} transformations")
        for i, transform in enumerate(transformations, 1):
            print(f"  {i}. {transform}")

    if options:
        print("Options:")
        for key, value in options.items():
            print(f"  {key} = {value}")


process_data(
    "database.db",
    "normalize", "filter", "aggregate",
    verbose=True,
    encoding="utf-8",
    max_rows=1000
)
# Output:
# Processing data from: database.db
# Applying 3 transformations
#   1. normalize
#   2. filter
#   3. aggregate
# Options:
#   encoding = utf-8
#   max_rows = 1000
```

#### 6. Lambda Functions

Lambda functions are small anonymous functions defined with the `lambda` keyword. They can have any number of arguments but only one expression.

**Syntax:**

```python
lambda arguments: expression
```

**Examples:**

```python
# Simple lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(3, 7))  # Output: 10

# Lambda in sorting
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort by grade
sorted_students = sorted(students, key=lambda x: x["grade"])
print(sorted_students)
# Output: [{'name': 'Charlie', 'grade': 78}, {'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}]

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8, 10]

# Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]
```

#### 7. Docstrings

Docstrings are string literals that document what a function does. They're placed as the first statement in a function.

**Examples:**

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns:
        float: The area of the rectangle
    """
    return length * width


# Access docstring
print(calculate_area.__doc__)


# Better formatted docstring
def process_user_data(user_id, *fields, validate=True, **options):
    """
    Process user data with optional validation.

    Args:
        user_id (int): The unique identifier for the user
        *fields: Variable number of field names to process
        validate (bool): Whether to validate data (default: True)
        **options: Additional processing options

    Returns:
        dict: Processed user data

    Example:
        >>> process_user_data(123, "name", "email", validate=True, format="json")
    """
    pass
```

#### Complete Example

```python
# Real-world example: Restaurant order system
def create_order(order_id, *dishes, discount=0, tip=0, **customer_details):
    """
    Create a restaurant order with dishes and customer information.

    Args:
        order_id (int): Unique order identifier
        *dishes (str): Variable number of dish names
        discount (float): Discount percentage (default: 0)
        tip (float): Tip amount (default: 0)
        **customer_details: Additional customer information

    Returns:
        dict: Complete order information
    """
    # Base prices for dishes
    menu_prices = {
        "burger": 8.99,
        "pizza": 12.99,
        "salad": 6.99,
        "pasta": 10.99,
        "soda": 2.99
    }

    # Calculate subtotal
    subtotal = sum(menu_prices.get(dish.lower(), 0) for dish in dishes)

    # Apply discount
    discount_amount = subtotal * (discount / 100)
    total = subtotal - discount_amount + tip

    # Create order dictionary
    order = {
        "order_id": order_id,
        "dishes": dishes,
        "subtotal": round(subtotal, 2),
        "discount": round(discount_amount, 2),
        "tip": tip,
        "total": round(total, 2),
        "customer": customer_details
    }

    return order


# Example usage
order = create_order(
    1001,
    "burger", "pizza", "soda", "soda",
    discount=10,
    tip=5.00,
    name="John Doe",
    phone="555-1234",
    table=7
)

print(f"Order #{order['order_id']}")
print(f"Dishes: {', '.join(order['dishes'])}")
print(f"Subtotal: ${order['subtotal']}")
print(f"Discount: ${order['discount']}")
print(f"Tip: ${order['tip']}")
print(f"Total: ${order['total']}")
print(f"Customer: {order['customer']['name']} - Table {order['customer']['table']}")

# Output:
# Order #1001
# Dishes: burger, pizza, soda, soda
# Subtotal: $28.95
# Discount: $2.89
# Tip: $5.0
# Total: $31.06
# Customer: John Doe - Table 7
```

[<< Day 4](../day_04/day_04.md) | [Day 6 >>](../day_06/day_06.md)