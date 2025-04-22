PYTHON - EVERYTHING IS OBJECT

### Understanding Mutable and Immutable Objects in Python

#### Introduction  
In this project, I explored fundamental Python concepts, including the distinction between mutable and immutable objects, their impact on memory management, and how Python handles arguments passed to functions. These concepts are essential for writing efficient Python code and avoiding subtle errors related to data manipulation.

#### ID and Type  
In Python, every object has a unique identifier accessible via the `id()` function. This identifier corresponds to the memory location of the object. The type of an object, obtained with `type()`, determines the nature of the object (e.g., `int`, `list`, `str`, etc.). These two properties help us understand how Python manages objects in memory.

**Example:**
```python
x = 42
print(id(x))  # Displays the unique identifier of the object 42
print(type(x))  # Displays <class 'int'>
```

#### Mutable Objects  
Mutable objects, such as lists (`list`), dictionaries (`dict`), and sets (`set`), can be modified after their creation. This means their content can change without their identifier (`id`) changing.

**Example:**
```python
my_list = [1, 2, 3]
print(id(my_list))  # Initial identifier
my_list.append(4)  # Modify the list
print(my_list)  # [1, 2, 3, 4]
print(id(my_list))  # The identifier remains the same
```

#### Immutable Objects  
Immutable objects, such as strings (`str`), tuples (`tuple`), and numbers (`int`, `float`), cannot be modified after their creation. Any attempt to modify them creates a new object with a new identifier.

**Example:**
```python
my_str = "Hello"
print(id(my_str))  # Initial identifier
my_str += " World"  # Creates a new object
print(my_str)  # "Hello World"
print(id(my_str))  # The identifier has changed
```

#### Why Does It Matter?  
The distinction between mutable and immutable objects is crucial because Python treats them differently. Mutable objects can be modified in place, which can lead to unexpected side effects if multiple references point to the same object. In contrast, immutable objects are safe to share across different parts of the code since they cannot be modified.

**Example:**
```python
# Side effect with a mutable object
a = [1, 2, 3]
b = a  # b points to the same object as a
b.append(4)
print(a)  # [1, 2, 3, 4] - a is also modified

# No side effect with an immutable object
x = 10
y = x  # y points to the same object as x
y += 5  # Creates a new object for y
print(x)  # 10 - x remains unchanged
```

#### How Arguments Are Passed to Functions  
In Python, arguments are passed by reference. This means functions receive a reference to the object, not a copy. For mutable objects, this implies that modifications made inside the function affect the original object. For immutable objects, any attempt to modify them creates a new object, leaving the original unchanged.

**Example:**
```python
# With a mutable object
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4] - The original list is modified

# With an immutable object
def modify_number(num):
    num += 5

my_num = 10
modify_number(my_num)
print(my_num)  # 10 - The original number remains unchanged
```

#### Conclusion  
This project helped me better understand Python's fundamental concepts related to mutable and immutable objects, as well as their impact on memory management and function behavior. These insights are essential for writing robust, readable, and efficient Python code. The practical examples clearly illustrate these concepts and demonstrate how to apply them in real-world scenarios.