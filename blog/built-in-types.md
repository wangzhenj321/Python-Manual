## `list`

### List Comprehensions

List comprehensions provide a concise way to create lists. A list comprehension consists of brackets containing an expression followed by a `for` clause, then zero or more `for` or `if` clauses. The result will be a new list resulting from evaluating the expression in the context of the `for` and `if` clauses which follow it.

For example, assume we want to create a list of squares, like:

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

> Note that this creates (or overwrites) a variable named `x` that still exists after the loop completes. 

We can calculate the list of squares without any side effects using:

```python
squares = [x**2 for x in range(10)]
```

or, equivalently:

```python
squares = list(map(lambda x: x**2, range(10)))
```

> If the expression is a tuple (e.g. the `(x, y)` in the previous example), it must be parenthesized.
> 
> ```python
> >>> # create a list of 2-tuples like (number, square)
> >>> [(x, x**2) for x in range(6)]
> [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
> >>> # the tuple must be parenthesized, otherwise an error is raised
> >>> [x, x**2 for x in range(6)]
>   File "<stdin>", line 1, in <module>
>     [x, x**2 for x in range(6)]
>                ^
> SyntaxError: invalid syntax
> ```

### Nested List Comprehensions

The initial expression in a list comprehension can be any arbitrary expression, **including another list comprehension**.

Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4:

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

The following list comprehension will transpose rows and columns:

```python
>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

> Be careful of the order of evaluating the inner and outer `for`s.

## `str`



## `dict`

It is best to think of a dictionary as a set of *key: value* pairs, with the requirement that **the keys are unique (within one dictionary)**.

> 1. Key can be any immutable type.
> 
> 2. A pair of braces creates an empty dictionary: `{}`.

There are few ways to create a dictionary shown as follows:

1. `>>> b = {'one': 1, 'two': 2, 'three': 3}`

2. `class dict(**kwarg)`

    - `>>> a = dict(one=1, two=2, three=3)`
    
    - `>>> e = dict({'three': 3, 'one': 1, 'two': 2})`

3. `class dict(mapping, **kwarg)`

    - `>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))`

4. `class dict(iterable, **kwarg)`

    - `>>> d = dict([('two', 2), ('one', 1), ('three', 3)])`

5. dict comprehensions

    ```python
    >>> {x: x**2 for x in (2, 4, 6)}
    {2: 4, 4: 16, 6: 36}
    ```

### Operations

1. `len(d)`

2. `d[key]` :vs: `get(key[, default])`

3. `d[key] = value` :vs: `setdefault(key[, default])` :vs: `update([other])`

4. `del d[key]`

5. `key in d` :vs: `key not in d`

6. `iter(d)`

7. `clear()`

8. `copy()`

9. `items()` :vs: `keys()` :vs: `values()`

10. `pop(key[, default])` :vs: `popitem()`

### References

1. [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

2. [Mapping Types — `dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
