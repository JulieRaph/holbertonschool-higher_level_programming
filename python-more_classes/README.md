# Python - More Classes and Objects

## Resources
* [Object Oriented Programming](https://python.swaroopch.com/oop.html)
* [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
* (Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The __init__ Method,” “Data Abstraction, Data Encapsulation, and Information Hiding,” “__str__- and __repr__-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”)
* [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php)
* [classmethods and staticmethods](https://www.youtube.com/watch?v=rq8cL2XMM5M)
* [Properties vs. Getters and Setters ](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [str vs repr](https://shipit.dev/posts/python-str-vs-repr.html)

## General
* Why Python programming is awesome
* What are the special __str__ and __repr__ methods and how to use them
* What is the difference between __str__ and __repr__
* What is a class attribute
* What is the difference between a object attribute and a class attribute
* What is a class method
* What is a static method
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to object and classes
* What is and what does contain __dict__ of a class and of an instance of a class
* How does Python find the attributes of an object or class
* How to use the getattr function

## Requirements
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using wc

## Example of the pycodestyle
     """
    Function to create a rectangle

    Property:
        width: private attribute instance
        height: private attribute instance

    Raise:
        TypeError: width and height must be an integer
        ValueError: width and height mus be >= 0
        TypeError: rect_1 must be an instance of Rectangle
        TypeError: rect_2 must be an instance of Rectangle

    Public class method:
       number_of_instances = initialized to 0
       print_symbol = initialized to #

    Public instance method:
        area and perimeter of the rectangle to return

    Methods:
        str, repr, eval and print message

    Static methods:
        rect_1 and rect_2 must be an instance of Rectangle

    Class method:
        return a new rectangle width == height == size

    Return:
        rect_1 if both have the same area value
    """
## Tasks
- [x] Simple rectangle
- [x] Real definition of a rectangle
- [x] Area and Perimeter
- [x] String representation
- [x] Eval is magic
- [x] Detect instance deletion
- [x] How many instances
- [x] Change representation
- [x] Compare rectangles
- [x] A square is a rectangle        
