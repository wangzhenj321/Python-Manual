## Creating an `Enum`

```python
>>> from enum import Enum
>>> class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3
...
```

> Member values can be anything: `int`, `str`, etc.. If the exact value is unimportant you may use `auto` instances and an appropriate value will be chosen for you. Care must be taken if you mix `auto` with other values.

Enumeration members have human readable representations:

```python
>>> print(repr(Color.RED))
<Color.RED: 1>
```

Enumerations support iteration, in definition order:

```python
>>> class Shake(Enum):
...     VANILLA = 7
...     CHOCOLATE = 4
...     COOKIES = 9
...     MINT = 3
...
>>> for shake in Shake:
...     print(shake)
...
Shake.VANILLA
Shake.CHOCOLATE
Shake.COOKIES
Shake.MINT
```

:star: Enumeration members are hashable, so they can be used in dictionaries and sets:

```python
>>> apples = {}
>>> apples[Color.RED] = 'red delicious'
>>> apples[Color.GREEN] = 'granny smith'
>>> apples == {Color.RED: 'red delicious', Color.GREEN: 'granny smith'}
True
```

## Programmatic access to enumeration members and their attributes

`Enum` allows such access:

```python
>>> Color(1)
<Color.RED: 1>
```

If you want to access enum members by *name*, use item access:

```python
>>> Color['RED']
<Color.RED: 1>
```

If you have an enum member and need its *name* or *value*:

```python
>>> member = Color.RED
>>> member.name
'RED'
>>> member.value
1
```

## Duplicating enum members and values

Having two enum members with the same name is **invalid**:

```python
>>> class Shape(Enum):
...     SQUARE = 2
...     SQUARE = 3
...
Traceback (most recent call last):
...
TypeError: Attempted to reuse key: 'SQUARE'
```

**However, two enum members are allowed to have the same value.** Given two members A and B with the same value (and A defined first), B is an alias to A. By-value lookup of the value of A and B will return A. By-name lookup of B will also return A:

```python
>>> class Shape(Enum):
...     SQUARE = 2
...     DIAMOND = 1
...     CIRCLE = 3
...     ALIAS_FOR_SQUARE = 2
...
>>> Shape.SQUARE
<Shape.SQUARE: 2>
>>> Shape.ALIAS_FOR_SQUARE
<Shape.SQUARE: 2>
>>> Shape(2)
<Shape.SQUARE: 2>
```

## Ensuring unique enumeration values

`@enum.unique`

It searches an enumeration's `__members__` gathering any aliases it finds; if any are found `ValueError` is raised with the details:

```python
>>> from enum import Enum, unique
>>> @unique
... class Mistake(Enum):
...     ONE = 1
...     TWO = 2
...     THREE = 3
...     FOUR = 3
...
Traceback (most recent call last):
...
ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE
```

## Using automatic values

If the exact value is unimportant you can use `auto`:

```python
>>> from enum import Enum, auto
>>> class Color(Enum):
...     RED = auto()
...     BLUE = auto()
...     GREEN = auto()
...
>>> list(Color)
[<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]
```

## Comparisons

Enumeration members are compared by identity:

```python
>>> Color.RED is Color.RED
True
>>> Color.RED is Color.BLUE
False
>>> Color.RED is not Color.BLUE
True
```

## References

1. [Support for enumerations](https://docs.python.org/3/library/enum.html)
