# 📘 Day 7

## OOP

## Table of Contents

1. [Introduction to OOP](#introduction-to-oop)
2. [The 6 Basic Principles of OOP](#the-6-basic-principles-of-oop)
3. [Class Attributes vs Instance Attributes](#class-attributes-vs-instance-attributes)
4. [Decorators in OOP](#decorators-in-oop)
5. [Best Practices](#best-practices)

---

### Introduction to OOP

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects that contain both data (attributes) and behavior (methods). It helps create more maintainable, reusable, and scalable code.

### Basic Structure of a Class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    def bark(self):  # Instance method
        return f"{self.name} says: Woof!"


# Creating an instance (object)
my_dog = Dog("Max", 3)
print(my_dog.bark())  # Output: Max says: Woof!
```

---

### The 6 Basic Principles of OOP

#### 1. Inheritance 🧬

Inheritance allows a class to inherit attributes and methods from another class (parent class).

#### Types of Inherited Methods:

a) Methods inherited from parent class

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"


class Dog(Animal):  # Dog inherits from Animal
    pass


# Using inherited methods
dog = Dog("Max")
print(dog.eat())  # Output: Max is eating
print(dog.sleep())  # Output: Max is sleeping
```

b) Inherited and overridden methods

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"


class Dog(Animal):
    # Overriding the parent method
    def make_sound(self):
        return f"{self.name} says: Woof!"


class Cat(Animal):
    # Overriding the parent method
    def make_sound(self):
        return f"{self.name} says: Meow!"


dog = Dog("Max")
cat = Cat("Luna")
print(dog.make_sound())  # Output: Max says: Woof!
print(cat.make_sound())  # Output: Luna says: Meow!
```

c) Own methods (specific to child class)

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating"


class Dog(Animal):
    # Method specific to Dog class
    def fetch(self, item):
        return f"{self.name} is fetching the {item}"

    # Another specific method
    def wag_tail(self):
        return f"{self.name} is wagging its tail"


dog = Dog("Max")
print(dog.eat())  # Inherited method
print(dog.fetch("ball"))  # Own method
print(dog.wag_tail())  # Own method
```

### 2. Polymorphism 🔄

**Poly** = many, **Morphism** = forms

The same method can behave differently depending on the object it's acting upon.

```python
class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Same method name, different behavior
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4)
]

for shape in shapes:
    print(f"Area: {shape.area()}")

# Output:
# Area: 78.53975
# Area: 24
# Area: 6.0
```

### 3. Cohesion 🎯

Each function/method should perform only one specific task.

```python
# ❌ BAD: Low cohesion - method does too many things
class User:
    def process_user(self, name, email):
        # Validates email
        if "@" not in email:
            return False
        # Saves to database
        self.save_to_db(name, email)
        # Sends welcome email
        self.send_email(email)
        # Logs the action
        self.log_action("User created")


# ✅ GOOD: High cohesion - each method does one thing
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def validate_email(self):
        return "@" in self.email

    def save_to_database(self):
        # Only saves to database
        print(f"Saving {self.name} to database")

    def send_welcome_email(self):
        # Only sends email
        print(f"Sending welcome email to {self.email}")

    def log_action(self, action):
        # Only logs actions
        print(f"Log: {action}")


# Usage
user = User("John", "john@email.com")
if user.validate_email():
    user.save_to_database()
    user.send_welcome_email()
    user.log_action("User created")
```

### 4. Abstraction 🎛️

Hide complex internal workings and show only simple interfaces (like car window buttons - complex inside, simple outside).

```python
from abc import ABC, abstractmethod


# Abstract class defining the interface
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        # Complex internal process hidden
        self._check_fuel()
        self._ignite_spark_plugs()
        self._start_combustion()
        print("Car engine started")  # Simple output

    def stop_engine(self):
        print("Car engine stopped")  # Simple output

    # Hidden internal methods (private)
    def _check_fuel(self):
        print("Checking fuel levels...")

    def _ignite_spark_plugs(self):
        print("Igniting spark plugs...")

    def _start_combustion(self):
        print("Starting combustion...")


# User only sees simple interface
car = Car()
car.start_engine()  # Simple call, complex process hidden
car.stop_engine()  # Simple call
```

### 5. Coupling 🔗

Minimize strong dependencies between classes.

```python
# ❌ BAD: High coupling - classes are tightly dependent
class EmailService:
    def send_email(self, to, message):
        print(f"Sending email to {to}: {message}")


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.email_service = EmailService()  # Tight coupling

    def register(self):
        self.email_service.send_email(self.email, "Welcome!")


# ✅ GOOD: Low coupling - dependency injection
class EmailService:
    def send_email(self, to, message):
        print(f"Sending email to {to}: {message}")


class SMSService:
    def send_sms(self, to, message):
        print(f"Sending SMS to {to}: {message}")


class User:
    def __init__(self, name, contact, notification_service):
        self.name = name
        self.contact = contact
        self.notification_service = notification_service  # Injected dependency

    def register(self):
        if hasattr(self.notification_service, 'send_email'):
            self.notification_service.send_email(self.contact, "Welcome!")
        elif hasattr(self.notification_service, 'send_sms'):
            self.notification_service.send_sms(self.contact, "Welcome!")


# Usage - easy to switch services
email_service = EmailService()
sms_service = SMSService()

user1 = User("John", "john@email.com", email_service)
user2 = User("Jane", "+1234567890", sms_service)

user1.register()  # Uses email
user2.register()  # Uses SMS
```

### 6. Encapsulation 🔒

Hide internal states of an object from the outside.

```python
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = initial_balance  # Private attribute

    # Public method to access balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"

    # Public method to withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"

    # Private method (internal use only)
    def __calculate_interest(self):
        return self.__balance * 0.05


# Usage
account = BankAccount("123456", 1000)

# ✅ Allowed: using public methods
print(account.get_balance())  # 1000
print(account.deposit(500))  # Deposited $500. New balance: $1500

# ❌ Not recommended: direct access to private attributes
# print(account.__balance)  # This would raise an AttributeError

# Attempting to access (Python name mangling)
# print(account._BankAccount__balance)  # Works but discouraged
```

---

### Class Attributes vs Instance Attributes

#### Class Attributes

Shared by all instances of the class.

```python
class Dice:
    # Class attribute - same for all dice
    number_of_faces = 6
    dice_created = 0

    def __init__(self, color):
        # Instance attribute - different for each dice
        self.color = color
        Dice.dice_created += 1  # Modifying class attribute

    def roll(self):
        import random
        return random.randint(1, self.number_of_faces)


# Creating instances
dice1 = Dice("red")
dice2 = Dice("blue")
dice3 = Dice("green")

# Class attribute is same for all
print(dice1.number_of_faces)  # 6
print(dice2.number_of_faces)  # 6
print(dice3.number_of_faces)  # 6

# Instance attributes are different
print(dice1.color)  # red
print(dice2.color)  # blue
print(dice3.color)  # green

# Class attribute tracks all instances
print(Dice.dice_created)  # 3
```

#### Visual Comparison

```python
class Rectangle:
    # Class attributes (shared)
    shape_type = "Rectangle"
    rectangles_created = 0

    def __init__(self, width, height, color):
        # Instance attributes (unique to each object)
        self.width = width
        self.height = height
        self.color = color
        Rectangle.rectangles_created += 1

    def area(self):
        return self.width * self.height


rect1 = Rectangle(10, 5, "red")
rect2 = Rectangle(8, 4, "blue")

print(f"Shape type: {Rectangle.shape_type}")  # Same for all
print(f"Total created: {Rectangle.rectangles_created}")  # 2

print(f"Rect1: {rect1.width}x{rect1.height}, {rect1.color}")  # 10x5, red
print(f"Rect2: {rect2.width}x{rect2.height}, {rect2.color}")  # 8x4, blue
```

---

### Decorators in OOP

#### 1. Instance Methods (default)

Access and modify object attributes and other methods.

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    # Instance method - uses 'self'
    def study(self, hours):
        print(f"{self.name} studied for {hours} hours")
        self.improve_grade(hours)

    def improve_grade(self, hours):
        improvement = hours * 2
        self.grade += improvement
        print(f"Grade improved to: {self.grade}")


student = Student("Alice", 70)
student.study(3)
# Output:
# Alice studied for 3 hours
# Grade improved to: 76
```

#### 2. Class Methods (@classmethod)

Work with class attributes, receive `cls` as first parameter.

```python
class Employee:
    # Class attributes
    company_name = "TechCorp"
    employee_count = 0
    raise_percentage = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    # Instance method
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_percentage)

    # Class method - modifies class attributes
    @classmethod
    def set_raise_percentage(cls, new_percentage):
        cls.raise_percentage = new_percentage
        print(f"Raise percentage changed to: {new_percentage}")

    @classmethod
    def from_string(cls, employee_string):
        # Alternative constructor
        name, salary = employee_string.split('-')
        return cls(name, int(salary))

    @classmethod
    def get_employee_count(cls):
        return f"Total employees: {cls.employee_count}"


# Using class methods
Employee.set_raise_percentage(1.10)  # Changes for all employees

# Using alternative constructor
emp1 = Employee.from_string("John-50000")
emp2 = Employee.from_string("Jane-60000")

print(Employee.get_employee_count())  # Total employees: 2

emp1.apply_raise()
print(emp1.salary)  # 55000 (50000 * 1.10)
```

#### 3. Static Methods (@staticmethod)

Regular functions that belong to a class but don't access instance or class attributes.

```python
class MathOperations:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathOperations.factorial(n - 1)


# Can call without creating an instance
print(MathOperations.add(5, 3))  # 8
print(MathOperations.multiply(4, 7))  # 28
print(MathOperations.is_even(10))  # True
print(MathOperations.factorial(5))  # 120

# Can also call from an instance (though not common)
math = MathOperations()
print(math.add(2, 3))  # 5
```

### Comparison of All Three

```python
class Pizza:
    # Class attribute
    total_pizzas_made = 0

    def __init__(self, size, toppings):
        self.size = size  # Instance attribute
        self.toppings = toppings  # Instance attribute
        Pizza.total_pizzas_made += 1

    # Instance method - works with specific pizza instance
    def describe(self):
        return f"A {self.size} pizza with {', '.join(self.toppings)}"

    # Class method - works with class-level data
    @classmethod
    def get_total_pizzas(cls):
        return f"Total pizzas made: {cls.total_pizzas_made}"

    @classmethod
    def margherita(cls, size):
        # Factory method - creates specific type of pizza
        return cls(size, ["tomato", "mozzarella", "basil"])

    # Static method - utility function related to pizza
    @staticmethod
    def is_valid_size(size):
        valid_sizes = ["small", "medium", "large"]
        return size.lower() in valid_sizes

    @staticmethod
    def calculate_slices(size):
        slices = {"small": 6, "medium": 8, "large": 10}
        return slices.get(size.lower(), 8)


# Using instance method
pizza1 = Pizza("large", ["pepperoni", "mushrooms"])
print(pizza1.describe())  # A large pizza with pepperoni, mushrooms

# Using class method
pizza2 = Pizza.margherita("medium")
print(pizza2.describe())  # A medium pizza with tomato, mozzarella, basil
print(Pizza.get_total_pizzas())  # Total pizzas made: 2

# Using static method
print(Pizza.is_valid_size("large"))  # True
print(Pizza.is_valid_size("gigantic"))  # False
print(Pizza.calculate_slices("large"))  # 10
```

---

## Best Practices

### 1. Use Meaningful Names

```python
# ❌ Bad
class C:
    def m(self, x):
        pass


# ✅ Good
class Customer:
    def make_purchase(self, amount):
        pass
```

### 2. Follow Single Responsibility Principle

```python
# Each class should have one reason to change
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class UserValidator:
    @staticmethod
    def validate_email(email):
        return "@" in email


class UserDatabase:
    def save_user(self, user):
        # Save logic here
        pass
```

### 3. Use Properties for Controlled Access

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32


temp = Temperature(25)
print(temp.celsius)  # 25
print(temp.fahrenheit)  # 77.0
temp.celsius = 30  # Uses setter
```

### 4. Document Your Code

```python
class Rectangle:
    """
    A class representing a rectangle shape.
    
    Attributes:
        width (float): The width of the rectangle
        height (float): The height of the rectangle
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.
        
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle
        """
        return self.width * self.height
```

---

## Summary

**The 6 OOP Principles:**

1. **Inheritance**: Reuse code from parent classes
2. **Polymorphism**: Same method, different behaviors
3. **Cohesion**: Each method does one thing
4. **Abstraction**: Hide complexity, show simplicity
5. **Coupling**: Minimize dependencies
6. **Encapsulation**: Hide internal states

**Decorators:**

- **Instance methods** (`self`): Work with object data
- **Class methods** (`@classmethod`, `cls`): Work with class data
- **Static methods** (`@staticmethod`): Utility functions

**Attributes:**

- **Class attributes**: Shared by all instances
- **Instance attributes**: Unique to each object

[<< Day 6](../day_06/day_06.md) | [Day 8 >>](../day_08/day_08.md)