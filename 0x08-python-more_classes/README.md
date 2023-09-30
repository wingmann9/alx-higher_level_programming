# Python - More Classes and Objects

This project extends the user knowledge on  Objects, Data Abstraction, Data Encapsulation, and Information hiding in Python.


## Contributors
* **wingmann** [wingmann9](https://github.com/wingmann9/)

## Function Prototypes:
Prototypes for functions written in this project:

| Class | Prototype |
| ------------------------ | -------------------------------------------- |
| `class Rectangle` |  |
|  | `def __init__(self, width=0, height=0):` |
|  | `def width(self):` |
|  | `def width(self, value):` |
|  | `def height(self):` |
|  | `def height(self, value):` |
|  | `def area(self):` |
|  | `def perimeter(self):` |
|  | `def __str__(self):` |
|  | `def __print__(self):` |
|  | `def __repr__(self):` |
|  | `def __del__(self):` |
|  | `def bigger_or_equal(rect_1, rect_2):` |
|  | `def square(cls, size=0):` |


## Tasks:

* **0. Simple rectangle**
  * [0-rectangle.py](./0-rectangle.py): Empty python class that defines a rectangle
  * Not allowed to import any module


* **1. Real definition of a rectangle**
  * [1-rectangle.py](./1-rectangle.py): Python class built on [0-rectangle.py](./0-rectangle.py) that defines a rectangle with:
  * Private instance attribute `width`:
    * Property `def width(self):` to retrieve it
    * Property setter `def width(self, value):` to set it
  * Private instance attribute `height`:
    * Property `def height(self):` to retrieve it
    * Property setter `def height(self, value):` to set it
  * Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0)`
  * If either `width` or `height` is not an integer, a `TypeError` is raised with the message `width must be an integer` or `height must be an integer`
  * If either `width` or `height` is less than `0`, a `ValueError` is raised with the message `width must be >= 0` or `height must be >= 0`


* **2. Area and Perimeter**
  * [2-retangle.py](./2-rectangle.py): Python class based on [1-rectangle.py](./1-rectangle.py) that defines a rectangle:
  * Public instance method `def area(self):` that returns the rectangle area
  * Public instance method `def perimeter(self):` that returns the rectangle perimeter:
    * If `width` or `height` is equal to `0`, perimeter is equal to `0`


* **3. String representation**
  * [3-retangle.py](./3-rectangle.py): Python class based on [2-rectangle.py](./2-rectangle.py) that defines a rectangle:
  * `print()` and `str()` should print the rectangle with the character `#`:
    * If `width` or `height` is equal to `0`, return an empty string


* **4. Eval is magic**
  * [4-retangle.py](./4-rectangle.py): Python class based on [3-rectangle.py](./3-rectangle.py) that defines a rectangle:
  * `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`


* **5. Detect instance deletion**
  * [5-retangle.py](./5-rectangle.py): Python class based on [4-rectangle.py](./4-rectangle.py) that defines a rectangle:
  * Print the message `Bye rectangle ...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle is deleted`


* **6. How many instances**
  * [6-retangle.py](./6-rectangle.py): Python class based on [5-rectangle.py](./5-rectangle.py) that defines a rectangle:
  * Public class attribute `number_of_instances`:
    * Initialized to `0`
    * Incremented during each new instance instantiation
    * Decremented during each instance deletion


* **7. Change representation**
  * [7-retangle.py](./7-rectangle.py): Python class based on [6-rectangle.py](./6-rectangle.py) that defines a rectangle:
  * Public class attribute `print_symbol`:
    * Initialized to `#`
    * Use as symbol to string representation
    * Can be any type


* **8. Compare rectangles**
  * [8-retangle.py](./8-rectangle.py): Python class based on [7-rectangle.py](./7-rectangle.py) that defines a rectangle:
  * Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
    * `rect_1` and `rect_2` must be an instance of `Rectangle`, otherwise:
    * raise a `TypeError` exception with message `rect_1 must be an instance of Rectangle` or `rect_2 must be an instance of Rectangle` respectively
    * Return `rect_1` if both have the same area value


* **9. A square is a rectangle**
  * [9-retangle.py](./9-rectangle.py): Python class based on [8-rectangle.py](./8-rectangle.py) that defines a rectangle:
  * Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`


## Advanced Task
* **10. N queens**
  * [101-nqueens.py](./101-nqueens.py): Python program that solves the [N queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle)
  * Usage: `./101-nqueens.py N`
  * Determines all possible solutions for placing N non-attacking queens on an NxN chessboard
  * Exactly 2 arguments should be provided otherwise print `Usage: nqueens N` and exit with the status `1`
  * If `N` is not an integer, print `N must be a number` and exit with the status `1`
  * If `N` is less than `4`, print `N must be at least 4` and exit with the status `1`


