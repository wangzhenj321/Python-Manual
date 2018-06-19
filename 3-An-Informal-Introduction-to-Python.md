Comments in Python start with the hash character, `#`.

## 3.1 Using Python as a Calculator

### 3.1.1 Numbers

The integer numbers (e.g. 2, 4, 20) have type `int`, the ones with a fractional part (e.g. 5.0, 1.6) have type `float`.

To do floor division and get an integer result (discarding any fractional result) you can use the `//` operator.

In interactive mode, the last printed expression is assigned to the variable `_`.

In addition to `int` and `float`, Python supports other types of numbers, such as `Decimal` and `Fraction`. Python also has built-in support for `complex numbers`, and uses the `j` or `J` suffix to indicate the imaginary part (e.g. `3+5j`).

### 3.1.2 Strings

```python
>>> '"Isn\'t," she said.'
'"Isn\'t," she said.'
>>> print('"Isn\'t," she said.')
"Isn't," she said.
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

```python
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

```python
>>> 3 * 'un' + 'ium'
>>> 'Py' 'thon'
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> prefix = 'Py'
>>> prefix 'thon'  # can't concatenate a variable and a string literal
  ...
SyntaxError: invalid syntax
>>> ('un' * 3) 'ium'
  ...
SyntaxError: invalid syntax
```

> There is no separate character type; a character is simply a string of size one.

```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
```

```python
>>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
'Py'
```

Out of range slice indexes are handled gracefully when used for slicing:

```python
>>>
>>> word[4:42]
'on'
>>> word[42:]
''
```

Python strings cannot be changed — they are **immutable**. Therefore, assigning to an indexed position in the string results in an error.

### 3.1.3 Lists

All slice operations return a new list containing the requested elements. This means that the following slice returns a new (shallow) copy of the list:

```python
>>> squares[:]
[1, 4, 9, 16, 25]
```

Unlike strings, which are **immutable**, lists are a **mutable** type.

## 3.2 First Steps Towards Programming
