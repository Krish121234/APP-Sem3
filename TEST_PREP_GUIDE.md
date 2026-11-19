# Python Test Preparation Guide

## Table of Contents
1. [Basic OOP](#1-basic-oop)
2. [File Handling & Exceptions](#2-file-handling--exceptions)
3. [Advanced OOP Concepts](#3-advanced-oop-concepts)
4. [Decorators](#4-decorators)
5. [Properties & Validation](#5-properties--validation)
6. [Iterators & Generators](#6-iterators--generators)
7. [Context Managers](#7-context-managers)
8. [Advanced Features](#8-advanced-features)
9. [Dynamic Programming](#9-dynamic-programming)
10. [Design Patterns](#10-design-patterns)

---

## 1. Basic OOP

### What is a Class?
A class is a blueprint for creating objects. It bundles data (attributes) and functions (methods) together.

### Key Concepts
- **Class**: The blueprint/template
- **Object/Instance**: A specific item created from the class
- **Constructor (`__init__`)**: Special method that runs when creating an object
- **`self`**: Reference to the current instance

### Example from your code:
```python
class Car:
    def __init__(self, brand, price):
        self.brand = brand      # Instance attribute
        self.price = price      # Instance attribute
    
    def increment_price(self, amount):
        self.price += amount
    
    def decrement_price(self, amount):
        self.price -= amount

# Creating objects
car1 = Car("Toyota", 25000)
car2 = Car("Honda", 30000)

car1.increment_price(5000)  # car1.price is now 30000
print(car1.brand, car1.price)  # Toyota 30000
```

### Key Points:
- Each object has its own copy of attributes
- Methods are functions inside a class that operate on `self`
- `__init__` is called automatically when you create an object

---

## 2. File Handling & Exceptions

### File Handling Basics

```python
# Opening and reading a file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Better way: using 'with' statement (automatically closes file)
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here
```

**File modes:**
- `"r"` - Read (default)
- `"w"` - Write (overwrites existing)
- `"a"` - Append
- `"r+"` - Read and write

### Exception Handling

Prevents your program from crashing when errors occur.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This always runs, error or not")
```

**Common exceptions:**
- `ZeroDivisionError` - Division by zero
- `ValueError` - Invalid value (e.g., `int("hello")`)
- `FileNotFoundError` - File doesn't exist
- `KeyError` - Dictionary key doesn't exist
- `IndexError` - List index out of range

---

## 3. Advanced OOP Concepts

### Magic/Dunder Methods
Special methods with double underscores that Python calls automatically.

```python
class Report:
    def __init__(self, title, data):
        self.title = title
        self.data = data
    
    def __str__(self):
        # Called by print() and str()
        return f"Report: {self.title}"
    
    def __add__(self, other):
        # Called when using + operator
        combined = Report(
            f"{self.title} + {other.title}",
            self.data + other.data
        )
        return combined
    
    def __len__(self):
        # Called by len()
        return len(self.data)

r1 = Report("Q1", [100, 200])
r2 = Report("Q2", [150, 250])

print(r1)           # Report: Q1
r3 = r1 + r2        # Uses __add__
print(r3.title)     # Q1 + Q2
print(len(r1))      # 2
```

**Common magic methods:**
- `__init__` - Constructor
- `__str__` - String representation for users
- `__repr__` - String representation for developers
- `__add__`, `__sub__`, `__mul__` - Operator overloading
- `__len__` - Length
- `__getitem__` - Indexing `obj[key]`
- `__call__` - Make object callable like a function

### Class Methods vs Instance Methods

```python
class Book:
    organization = "City Library"  # Class variable (shared by all instances)
    
    def __init__(self, title, author):
        self.title = title      # Instance variable (unique to each object)
        self.author = author
    
    # Instance method - works with a specific object
    def display(self):
        return f"{self.title} by {self.author}"
    
    # Class method - works with the class itself
    @classmethod
    def set_org(cls, new_org):
        cls.organization = new_org
    
    # Alternative constructor (class method)
    @classmethod
    def from_string(cls, book_string):
        title, author = book_string.split(" by ")
        return cls(title, author)

# Using instance method
book1 = Book("1984", "Orwell")
print(book1.display())  # 1984 by Orwell

# Using class method to change shared data
Book.set_org("State Library")
print(Book.organization)  # State Library

# Using alternative constructor
book2 = Book.from_string("Brave New World by Huxley")
print(book2.title)  # Brave New World
```

### Composition
Building complex objects by combining simpler ones.

```python
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.is_borrowed = False

class Patron:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []  # List of Book objects

class Library:
    def __init__(self):
        self.books = []     # List of Book objects
        self.patrons = []   # List of Patron objects
    
    def add_book(self, book):
        self.books.append(book)
    
    def borrow_book(self, patron_id, isbn):
        # Find patron
        patron = next((p for p in self.patrons if p.id == patron_id), None)
        if not patron:
            return "Patron not found"
        
        # Find book
        book = next((b for b in self.books if b.isbn == isbn), None)
        if not book:
            return "Book not found"
        
        if book.is_borrowed:
            return "Book already borrowed"
        
        book.is_borrowed = True
        patron.borrowed_books.append(book)
        return "Book borrowed successfully"
```

**Key point:** Library contains Books and Patrons (composition), rather than inheriting from them.

### `__slots__` for Memory Optimization

```python
# Without __slots__ (uses more memory)
class PersonNormal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# With __slots__ (saves memory)
class PersonOptimized:
    __slots__ = ('name', 'age')  # Only these attributes allowed
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = PersonOptimized("Alice", 25)
p.name = "Bob"  # OK
# p.email = "test@example.com"  # AttributeError! Not in __slots__
```

**When to use:**
- Creating thousands/millions of objects
- Memory is limited
- You know all attributes in advance

---

## 4. Decorators

### What is a Decorator?
A decorator modifies or enhances a function without changing its code. It "wraps" a function.

### Basic Function Decorator

```python
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} finished")
        return result
    return wrapper

@log_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
# Output:
# Calling greet
# Hello, Alice!
# greet finished
```

**What happens:**
1. `@log_decorator` is shorthand for `greet = log_decorator(greet)`
2. Now `greet` is actually the `wrapper` function
3. When you call `greet("Alice")`, you're calling `wrapper("Alice")`
4. `wrapper` adds extra behavior, then calls the original function

### Parameterized Decorators (3 Levels)

```python
# Level 1: Decorator factory (takes parameters)
def repeat(times):
    # Level 2: Actual decorator (takes function)
    def decorator(func):
        # Level 3: Wrapper (takes function arguments)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)  # Call the factory first
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Hello!
# Hello!
# Hello!
```

**Understanding the nesting:**
1. `repeat(3)` returns `decorator`
2. `@decorator` wraps `say_hello`
3. Calling `say_hello()` calls `wrapper()`

### Class-Based Decorators

```python
class UpperFormatter:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        return result.upper()

@UpperFormatter
def get_message():
    return "hello world"

print(get_message())  # HELLO WORLD
```

**How it works:**
- `@UpperFormatter` creates an instance: `get_message = UpperFormatter(get_message)`
- Calling `get_message()` calls the `__call__` method

### Built-in Decorators You Should Know

```python
from functools import lru_cache
import time

# @lru_cache - Memoization (caching results)
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# @classmethod - Works with the class, not instance
class MyClass:
    @classmethod
    def class_method(cls):
        print(f"Called on {cls}")

# @staticmethod - No access to class or instance
class Math:
    @staticmethod
    def add(a, b):
        return a + b

# @property - Getters/setters (see next section)
```

---

## 5. Properties & Validation

### The Problem Without Properties

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  # What if someone sets -500?

temp = Temperature(25)
temp.celsius = -500  # Physically impossible! No validation
```

### Solution: Using @property

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Private attribute (convention)
    
    @property
    def celsius(self):
        """Getter - called when reading the value"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter - called when setting the value"""
        if value < -273.15:  # Absolute zero
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property"""
        return self._celsius * 9/5 + 32

# Using it
temp = Temperature(25)
print(temp.celsius)      # 25 (calls getter)
print(temp.fahrenheit)   # 77.0 (computed on the fly)

temp.celsius = 30        # OK (calls setter with validation)
# temp.celsius = -500    # ValueError!
```

**Key benefits:**
- Looks like normal attribute access (`temp.celsius`)
- Automatically validates data
- Can compute values on the fly
- Can make read-only properties (no setter)

---

## 6. Iterators & Generators

### Custom Iterator (Iterator Protocol)

An iterator is an object that returns one item at a time.

```python
class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        """Returns the iterator object (usually self)"""
        return self
    
    def __next__(self):
        """Returns the next item, or raises StopIteration when done"""
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

# Using it
for num in Countdown(5):
    print(num)  # 5, 4, 3, 2, 1
```

**How it works:**
1. `for` loop calls `__iter__()` to get the iterator
2. Repeatedly calls `__next__()` until `StopIteration`

### Generators (Easier Way)

```python
def countdown(start):
    while start > 0:
        yield start  # Pauses here and returns value
        start -= 1

# Using it (same as iterator)
for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1
```

**Generator vs Iterator:**
- Generator: Use `yield`, simpler, less code
- Iterator: More control, can store complex state

### Generator with .send() (Coroutine Style)

```python
def running_average():
    total = 0
    count = 0
    average = None
    
    while True:
        value = yield average  # Receives value via .send()
        if value is None:
            break
        total += value
        count += 1
        average = total / count

# Using it
avg = running_average()
next(avg)  # Prime the generator (required!)

print(avg.send(10))  # 10.0
print(avg.send(20))  # 15.0
print(avg.send(30))  # 20.0
```

**How .send() works:**
1. `yield` pauses and waits
2. `.send(value)` resumes and passes `value` to the `yield` expression
3. Generator continues until next `yield`

---

## 7. Context Managers

### What is a Context Manager?
Ensures setup and cleanup happen automatically (like `with open()`).

### Using @contextmanager

```python
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    print(f"Opening {filename}")
    file = open(filename, mode)
    try:
        yield file  # Everything before yield = setup
    finally:        # Everything after yield = cleanup
        print(f"Closing {filename}")
        file.close()

# Using it
with file_manager("test.txt", "w") as f:
    f.write("Hello")
# File automatically closed, even if an error occurs
```

**Real-world uses:**
- Database connections
- Network sockets
- Locks and semaphores
- Temporary file/directory management

### Class-Based Context Manager

```python
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"Elapsed: {self.end - self.start:.2f}s")

with Timer():
    # Your code here
    time.sleep(1)
# Automatically prints elapsed time
```

---

## 8. Advanced Features

### Pattern Matching (Python 3.10+)

Like `switch/case` but more powerful.

```python
def execute_command(command):
    parts = command.split()
    
    match parts:
        case ["quit" | "exit"]:
            return "Goodbye!"
        
        case ["go", direction] if direction in ["north", "south", "east", "west"]:
            return f"Moving {direction}"
        
        case ["take", *items]:
            return f"Taking: {', '.join(items)}"
        
        case _:
            return "Unknown command"

print(execute_command("go north"))      # Moving north
print(execute_command("take sword shield"))  # Taking: sword, shield
print(execute_command("jump"))          # Unknown command
```

**Features:**
- `|` for OR patterns
- `*items` for capturing multiple values
- `if` guards for conditions
- `_` for default case

### Metaclasses

Controls how classes are created (advanced topic).

```python
class UpperAttrMeta(type):
    def __new__(cls, name, bases, dct):
        # Modify all non-dunder attributes to uppercase
        uppercase_dct = {}
        for key, value in dct.items():
            if not key.startswith('__'):
                uppercase_dct[key.upper()] = value
            else:
                uppercase_dct[key] = value
        
        return super().__new__(cls, name, bases, uppercase_dct)

class MyClass(metaclass=UpperAttrMeta):
    normal_attr = "value"
    another = 42

print(MyClass.NORMAL_ATTR)  # "value" (uppercase!)
print(MyClass.ANOTHER)      # 42
# print(MyClass.normal_attr)  # AttributeError!
```

**When to use:** Almost never! Only for frameworks/libraries that need to control class creation.

### Async Programming with asyncio

```python
import asyncio

async def fetch_data(name, delay):
    print(f"{name}: Starting...")
    await asyncio.sleep(delay)  # Simulates I/O
    print(f"{name}: Done!")
    return f"Data from {name}"

async def main():
    async with asyncio.TaskGroup() as group:
        task1 = group.create_task(fetch_data("API-1", 2))
        task2 = group.create_task(fetch_data("API-2", 1))
        task3 = group.create_task(fetch_data("API-3", 3))
    
    # All tasks complete before here
    print("All done!")

asyncio.run(main())

# Output:
# API-1: Starting...
# API-2: Starting...
# API-3: Starting...
# API-2: Done! (after 1 sec)
# API-1: Done! (after 2 sec)
# API-3: Done! (after 3 sec)
# All done!
```

**Key concepts:**
- `async def` - Defines an async function (coroutine)
- `await` - Waits for an async operation
- `asyncio.TaskGroup` - Runs multiple tasks concurrently
- Total time: 3 seconds (not 6!) because they run in parallel

### Abstract Base Classes (ABC)

Forces subclasses to implement certain methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass  # Subclass MUST implement this
    
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

# Cannot create Shape directly
# shape = Shape()  # TypeError!

circle = Circle(5)
print(circle.area())  # 78.53975
```

**Why use ABC:**
- Enforces a contract/interface
- Prevents creating incomplete subclasses
- Makes code self-documenting

---

## 9. Dynamic Programming

### What is Dynamic Programming?
An optimization technique that solves complex problems by breaking them into simpler subproblems and storing results to avoid redundant work.

**Two approaches:**
1. **Memoization (Top-Down)**: Recursion + caching
2. **Tabulation (Bottom-Up)**: Iterative table-filling

### Example 1: Fibonacci

#### Without Optimization (Very Slow!)

```python
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# fib(40) takes several seconds!
# Recalculates fib(20) thousands of times
```

#### With Memoization (Fast!)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# fib(40) is instant!
# Each value calculated only once
```

**Time complexity:**
- Without cache: O(2^n) - exponential
- With cache: O(n) - linear

### Example 2: Longest Common Subsequence (LCS)

Given two strings, find the longest sequence that appears in both (not necessarily contiguous).

Example: `"ABCDGH"` and `"AEDFHR"` → `"ADH"` (length 3)

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                # Characters match - add 1 to diagonal
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # No match - take max of left or top
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # The answer is in the bottom-right corner
    return dp[m][n]

print(lcs("ABCDGH", "AEDFHR"))  # 3
```

**How it works:**
```
      ""  A  E  D  F  H  R
""     0  0  0  0  0  0  0
A      0  1  1  1  1  1  1
B      0  1  1  1  1  1  1
C      0  1  1  1  1  1  1
D      0  1  1  2  2  2  2
G      0  1  1  2  2  2  2
H      0  1  1  2  2  3  3
```

**Reconstructing the actual subsequence:**

```python
def lcs_with_sequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill table (same as before)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Backtrack to find the sequence
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            result.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(result))

print(lcs_with_sequence("ABCDGH", "AEDFHR"))  # "ADH"
```

### Example 3: 0/1 Knapsack Problem

Given items with weights and values, and a knapsack with capacity W, maximize value without exceeding capacity.

**Constraint:** Each item can be taken 0 or 1 times (not fractional).

#### Top-Down (Memoization)

```python
from functools import lru_cache

def knapsack_top_down(values, weights, capacity):
    n = len(values)
    
    @lru_cache(maxsize=None)
    def dp(i, w):
        # Base case: no items left or no capacity
        if i == 0 or w == 0:
            return 0
        
        # If item doesn't fit, skip it
        if weights[i-1] > w:
            return dp(i-1, w)
        
        # Choose max of: skip item, or take item
        skip = dp(i-1, w)
        take = values[i-1] + dp(i-1, w - weights[i-1])
        return max(skip, take)
    
    return dp(n, capacity)

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(knapsack_top_down(values, weights, capacity))  # 220
```

#### Bottom-Up (Tabulation)

```python
def knapsack_bottom_up(values, weights, capacity):
    n = len(values)
    
    # Create DP table: dp[i][w] = max value using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # Option 1: Don't take item i
            dp[i][w] = dp[i-1][w]
            
            # Option 2: Take item i (if it fits)
            if weights[i-1] <= w:
                take_value = values[i-1] + dp[i-1][w - weights[i-1]]
                dp[i][w] = max(dp[i][w], take_value)
    
    return dp[n][capacity]

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print(knapsack_bottom_up(values, weights, capacity))  # 220
```

**DP Table Example:**
```
Capacity:  0  10  20  30  40  50
Item 0:    0   0   0   0   0   0
Item 1:    0  60  60  60  60  60
Item 2:    0  60 100 160 160 160
Item 3:    0  60 100 160 180 220
```

**Top-Down vs Bottom-Up:**
- **Top-Down**: Easier to think about (recursive), only computes needed states
- **Bottom-Up**: Usually faster (no recursion overhead), fills entire table

---

## 10. Design Patterns

### Strategy Pattern

**Problem:** You have multiple ways to do something, and want to choose at runtime.

**Solution:** Create separate strategy classes with the same interface, and a context class that delegates to the chosen strategy.

```python
# Strategy classes (different payment methods)
class CreditCard:
    def pay(self, amount):
        print(f"Paid ${amount} with Credit Card")

class DebitCard:
    def pay(self, amount):
        print(f"Paid ${amount} with Debit Card")

class UPI:
    def pay(self, amount):
        print(f"Paid ${amount} with UPI")

class NetBanking:
    def pay(self, amount):
        print(f"Paid ${amount} with Net Banking")

# Context class (uses a strategy)
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def process_payment(self, amount):
        self.strategy.pay(amount)

# Using it
payment_method = input("Choose: credit/debit/upi/netbanking: ")

if payment_method == "credit":
    strategy = CreditCard()
elif payment_method == "debit":
    strategy = DebitCard()
elif payment_method == "upi":
    strategy = UPI()
else:
    strategy = NetBanking()

processor = PaymentProcessor(strategy)
processor.process_payment(100)
```

**Key points:**
- All strategies have the same method (`pay`)
- Context doesn't know implementation details
- Easy to add new strategies without changing existing code
- Composition over inheritance

### Iterator Pattern (Already covered in section 6)

See the `Countdown` class example - that's the Iterator Pattern!

---

## Summary of Key Concepts

### 1. OOP Pillars
- **Encapsulation**: Bundle data and methods (`@property` for validation)
- **Composition**: Objects contain other objects (Library has Books)
- **Polymorphism**: Different classes with same interface (Strategy Pattern, ABC)

### 2. When to Use What

| Concept | When to Use |
|---------|-------------|
| `@property` | Validate data, computed values, read-only attributes |
| `@classmethod` | Alternative constructors, modify class-level data |
| `@staticmethod` | Utility functions related to the class |
| `@lru_cache` | Expensive recursive functions (Fibonacci, DP) |
| Decorator | Add behavior to functions (logging, timing, validation) |
| Generator | Lazy sequences, memory-efficient iteration |
| Iterator | Complex iteration logic, maintain state |
| Context Manager | Setup/cleanup (files, connections, locks) |
| ABC | Enforce interface contracts in subclasses |
| Strategy Pattern | Multiple algorithms, choose at runtime |

### 3. Dynamic Programming Checklist

**When to use DP:**
- Overlapping subproblems (same calculation repeated)
- Optimal substructure (optimal solution uses optimal subsolutions)

**Approach:**
1. Define what `dp[i]` or `dp[i][j]` represents
2. Find the recurrence relation (formula)
3. Determine base cases
4. Decide: top-down (recursion + cache) or bottom-up (table)?
5. For bottom-up: determine table size and filling order

**Common patterns:**
- **1D DP**: Fibonacci, climbing stairs
- **2D DP**: LCS, knapsack, edit distance
- **Optimization**: If you only need previous row, use 1D array instead of 2D

---

## Quick Reference - Common Gotchas

1. **Forgetting `self`** in instance methods
2. **Mutable default arguments**: `def func(items=[])` - the list persists!
3. **Not priming generators before `.send()`**: Always call `next(gen)` first
4. **Forgetting `@` before decorator names**
5. **Confusing `cls` and `self`**: `cls` for class methods, `self` for instance methods
6. **Not raising `StopIteration`** in custom iterators
7. **Forgetting to return something** from `__enter__` in context managers
8. **Modifying list while iterating**: Use list copy or list comprehension
9. **Integer division**: Use `//` for floor division, `/` gives float
10. **Indentation errors** (especially in nested functions)

---

## Next Steps

Now that you understand the concepts:

1. **Practice coding each pattern** from scratch without looking
2. **Solve variations**: Change Fibonacci to factorial, LCS to edit distance
3. **Combine concepts**: Write a decorator that uses a context manager
4. **Debug broken code**: I'll give you code with bugs to find
5. **Mock test**: Time yourself on mixed questions

Ready for practice problems?
