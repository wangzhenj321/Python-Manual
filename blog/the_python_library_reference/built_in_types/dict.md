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

## Operations

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

## References

1. [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

2. [Mapping Types — `dict`](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
