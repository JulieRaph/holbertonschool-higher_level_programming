# PYTHON - TEST-Driven DEVELOPMENT

## Resources
* [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html)
* [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
* [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)

## Generals
* Why Python programming is awesome
* What’s an interactive test
* Why tests are important
* How to write Docstrings to create tests
* How to write documentation for each module and function
* What are the basic option flags to create tests
* How to find edge cases

## Requirements
### Python Script
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using wc

### Python Test Cases
* All your test files should be inside a folder tests
* All your test files should be text files (extension: .txt)
* All your tests should be executed by using this command: python3 -m doctest ./tests/*
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case – The Checker is checking for tests!

## Examples of the test file
> Test cases for say_my_name function
> 
> say_my_name = __import__('3-say_my_name').say_my_name
> 
> Test first_name and last_name
> 
> say_my_name("John", "Smith")
> 
> My name is John Smith
> 
> ---------------------------------
> Test only first_name
> 
> say_my_name("Bob")
> 
> My name is Bob 
> 
> ---------------------------------
> Test if first_name is not a string
> 
> say_my_name(12, "White")
> 
> Traceback (most recent call last):
> 
> TypeError: first_name must be a string
> 
> ---------------------------------
> Test if last_name is not a string
> 
> say_my_name("Walter", 12)
> 
> Traceback (most recent call last):
> 
> TypeError: last_name must be a string
> 
> ---------------------------------
> Test if nothing is passed
> 
> say_my_name()
> 
> Traceback (most recent call last):
> 
> TypeError: say_my_name() missing 1 required positional argument: 'first_name'

## Tasks
- [x] Integers addition
- [x] Divide a matrix
- [x] Say my name
- [x] Print square
- [x] Text indentation
- [x] Max integer - Unittest     
