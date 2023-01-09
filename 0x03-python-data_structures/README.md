# Python - Data Structures: Lists, Tuples

This project places emphasis on list, tuples, comphresion list; their functions and how to use and manipulate these python functions.

## Tasks :

* **0. Print a list of integers**
  * [0-print_list_integer.py](./0-print_list_integer.py): Python function that prints all integers of a list.
  * Prototype: `def print_list_integer(my_list=[]):` 
  * Format: one integer per line.
  * Not allowed to import any module
  * Assume that the list only contains integers
  * Not allowed to cast integers into strings
  * Use `str.format()` to print integers

* **1. Secure access to an element in a list**
  * [1-element_at.py](./1-element_at.py): Python function that retrieve an element from a list like in C
  * Prototype: `def element_at(my_list, idx):`
  * If `idx` is negative, the function should return `None`
  * If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
  * Not allowed to import any module
  * Not allowed to use `try/except`

* **2. Replace element**
  * [2-replace_in_list.py](./2-replace_in_list.py): Python function that replaces an element of a list at a specific position (like in C).
  * Prototype: `def replace_in_list(my_list, idx, element):`
  * If `idx` is negative, the function should not modify anything, and returns the original list
  * If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
  * Not allowed to import any module
  * Not allowed to use try/except

* **3. Print a list of integers... in reverse!**
  * [3-print_reversed_list_integer.py](./3-print_reversed_list_integer.py): Python function that prints all integers of a list, in reverse order.
  * Prototype: `def print_reversed_list_integer(my_list=[]):`
  * Format: one integer per line.
  * Not allowed to import any module
  * Assume that the list only contains integers
  * Not allowed to cast integers into strings
  * Use `str.format()` to print integers

* **4. Replace in a copy**
  * [4-new_in_list.py](./4-new_in_list.py): Python function that replaces an element in a list at a specific position without modifying the original list (like in C).
  * Prototype: `def new_in_list(my_list, idx, element):`
  * If `idx` is negative, the function should return a copy of the original list
  * If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original list
  * Not allowed to import any module
  * Not allowed to use `try/except`

* **5. Can you C me now?**
  * [5-no_c.py](./5-no_c.py): Python function that removes all characters `c` and `C` from a string.
  * Prototype: `def no_c(my_string):`
  * Function should return the new string
  * Not allowed to import any module
  * Not allowed to use `str.replace()`

* **6. Lists of lists = Matrix**
  * [6-print_matrix_integer.py](./6-print_matrix_integer.py): Python function that prints a matrix of integers.
  * Prototype: `def print_matrix_integer(matrix=[[]]):`
  * Not allowed to import any module
  * Assume that the list only contains integers
  * Not allowed to cast integers into strings
  * Use `str.format()` to print integers

* **7. Tuples addition**
  * [7-add_tuple.py](./7-add_tuple.py): Python function that adds 2 tuples.
  * Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
  * Returns a tuple with 2 integers:
	* The first element should be the addition of the first element of each argument
	* The second element should be the addition of the second element of each argument
  * Not allowed to import any module
  * Assume that the two tuples will only contain integers
  * If a tuple is smaller than 2, use the value `0` for each missing integer
  * If a tuple is bigger than 2, use only the first 2 integers

* **8. More returns!**
  * [8-multiple_returns.py](./8-multiple_returns.py): Python function that returns a tuple with the length of a string and its first character.
  * Prototype: `def multiple_returns(sentence):`
  * If the sentence is empty, the first character should be equal to `None`
  * Not allowed to import any module

* **9. Find the max**
  * [9-max_integer.py](./9-max_integer.py): Python function that finds the biggest integer of a list.
  * Prototype: `def max_integer(my_list=[]):`
  * If the list is empty, return `None`
  * Assume that the list only contains integers
  * Not allowed to import any module
  * Not allowed to use the builtin `max()`

* **10. Only by 2**
  * [10-divisible_by_2.py](./10-divisible_by_2.py): Python function that finds all multiples of 2 in a list.
  * Prototype: `def divisible_by_2(my_list=[]):`
  * Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
  * New list should have the same size as the original list
  * Not allowed to import any module

* **11. Delete at**
  * [11-delete_at.py](./11-delete_at.py): Python function that deletes the item at a specific position in a list.
  * Prototype: `def delete_at(my_list=[], idx=0):`
  * If `idx` is negative or out of range, nothing change (returns the same list)
  * Not allowed to use `pop()`
  * Not allowed to import any module

* **12. Switch**
  * [12-switch.py](./12-switch.py): Complete the source code in order to switch value of `a` and `b`
  * Source code `here`
  * Code should be inserted where the comment is (line 4)
  * Program should be exactly 5 lines long

* **13. Linked list palindrome**
  * [13-is_palindrome.c](./13-is_palindrome.c): C function that checks if a singly linked list is a palindrome.
  * Prototype: `int is_palindrome(listint_t **head);`
  * Return: `0` if it is not a palindrome, `1` if it is a palindrome
  * An empty list is considered a palindrome
  * Extra files:
	* [linked_lists.c](./linked_lists.c): C functions handling linked lists provided for testing [13-is_palindrome.c](./13-is_palindrome.c)
	* [lists.h](./lists.h): Header file containing definitions and prototypes for all types and functions used in [linked_lists.c](./linked_lists.c) and [13-main.c](./13-main.c).

* **14.	CPython #0: Python lists**
  * [100-print_python_list_info.c](./100-print_python_list_info.c): C function that prints some basic info about Python lists.
  * Prototype: `void print_python_list_info(PyObject *p);`
  * Python version: 3.4
  * Shared library will be compiled with this command line: `gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c`
  * OS: `Ubuntu 14.04 LTS`
