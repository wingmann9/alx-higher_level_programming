# Python - Inheritance


## Contributors
* **Ema-Eno Simon** [wingmann9](https://github.com/wingmann9/)

## Tests:
* [tests](./tests): Folder of independently-developed test files.
* [1-my_list.txt](./tests/1-my_list.txt)
* [7-base_geometry.txt](./tests/7-base_geometry.txt)


## Function Prototypes:
Prototypes for functions written in this project:

| File | Class | Prototype |
| ------------------------ | -------------------------------------------- | -------------------------------------------- |
| `0-lookup.py` |  | `def lookup(obj):` |
| `1-my_list.py` | `class MyList:` | `def print_sorted(self):` |
| `2-is_same_class.py` |  | `def is_same_class(obj, a_class):` |
| `3-is_kind_of_class.py` |  | `def is_kind_of_class(obj, a_class):` |
| `4-inherits_from.py` |  | `def inherits_from(obj, a_class):` |
| `5-base_geometry.py` | `class BaseGeometry:` |  |
| `6-base_geometry.py` | `class BaseGeometry:` |`def area(self):` |
| `7-base_geometry.py` | `class BaseGeometry:` | `def integer_validator(self, name, value):` |
| `8-rectangle.py` | `class Rectangle(BaseGeometry):` | `def __init__(self, width, height):` |
| `9-rectangle.py` | `class Rectangle(BaseGeometry):` | `def __str__(self):` |
|  |  | `def __print__(self):` |
| `10-square.py` | `class Square(Rectangle):` | `def __init__(self, size):` |
| `11-square.py` | `class Square(Rectangle):` | `def __str__(self):` |
|  |  | `def __print__(self):` |
| `100-my_int.py` | `class MyInt(int):` |  |


## Tasks
* **0. Lookup**
  * [0-lookup.py](./0-lookup.py): Python function `def lookup(obj):`that returns a list of available attributes and methods of an objects

* **1. My list**
  * [1-my_list.py](./1-my_list.py): Python class `MyList` that inherits from `list`:
    * Public instance method `def print_sorted(self):` that prints the list in11 ascending sorted order (assumes all list elements are `int`)

* **2. Exact same object**
  * [2-is_same_class.py](./2-is_same_class.py): Python function `def is_same_class(obj, a_class):` that returns `True` if an object is exactly an instance of a specified class; otherwise `False`

* **3. Same class or inherit from**
  * [3-is_kind_of_class.py](./3-is_kind_of_class.py): Python function `def is_kind_of_class(obj, a_class):`that returns `True` if an object is an instance or inherited instance of a specified class; otherwise `False`

* **4. Only sub class of**
  * [4-inherits_from.py](./4-inherits_from.py): Python function `def inherits_from(obj, a_class):`that returns `True` if an object is an inherited instance (either directly or indirectly) from a specified class; otherwise `False`

* **5. Geometry module**
  * [5-base_geometry.py](./5-base_geometry.py): An empty Python class `BaseGeometry`

* **6. Improve Geometry**
  * [6-base_geometry.py](./6-base_geometry.py): Python class `BaseGeometry` based on [5-base_geometry.py](./5-base_geometry.py):
    * Public instance method `def area(self):` that raises an `Exception` with the message `area() is not implemented`.

* **7. Integer validator**
  * [7-base_geometry.py](./7-base_geometry.py): Python class `BaseGeometry` based on [6-base_geometry.py](./6-base_geometry.py):
    * Public instance method `def integer_validator(self, name, value):` that validates the parameter `value`
    * Assumes the parameter `name` is always a string
    * The parameter `value` must be an `int`, otherwise, a `TypeError` exception is raised with the message `<name> must be an integer`
    * The parameter `value` must be greater than `0`, otherwise, a `ValueError` exception is raised with the message `<value> must be greater than 0`

* **8. Rectangle**
  * [8-rectangle.py](./8-rectangle.py): Python class `Rectangle` that inherits from `BaseGeometry` ([7-base_geometry.py](./7-base_geometry.py)):
    * Private attributes `width` and `height` - validated with `integer_validator`
    * Instantiation with `width` and `height`: `def __init__(self, width, height):`

* **9. Full rectangle**
  * [9-rectangle.py](./9-rectangle.py): Python class based on [8-rectangle.py](./8-rectangle.py):
    * Implementation of the method `area()`.
    * Special method `__str__` to print `Rectangle`s in the format `[Rectangle] <width>/<height>`

* **10. Square #1**
  * [10-square.py](./10-square.py): Python class `Square` that inherits from `Rectangle` ([9-rectangle.py](./9-rectangle.py)):
    * Private attribute `size` - validated with `integer_validator`
    * Instantiation with `size`: `def __init__(self, size):`
    * Implementation of the `area()` method.

* **11. Square #2**
  * [11-square.py](./11-square.py): Python class based on [10-square.py](./10-square.py):
    * Special method `__str__` to print squares in the format `[Square] <width>/<height>`

* **12. My integer**
  * [100-my_int.py](./100-my_int.py): Python class `MyInt` that inherits from `int`
    * Inversion of the `==` and `!=` operators

* **13. Can I?**
  * [101-add_attribute.py](./101-add_attribute.py): Python function that adds a new attribute to an object if possible
    * If an attribute cannot be added, a `TypeError` exception is raised with the message `can't add new attribute`
