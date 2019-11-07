# Text Sequence Type — `str`

## Strings

1. single quotes or double quotes
2. raw strings `r`
3. triple-quotes
4. concatenate
5. a character is simply a string of size one
6. immutable

## `str`

```python
class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
```

## String Methods

1. `count(sub[, start[, end]])`
2. `encode(encoding="utf-8", errors="strict")`
3. `format(*args, **kwargs)`
4. `join(iterable)`
5. `split(sep=None, maxsplit=-1)`
6. `strip([chars])`
7. `upper()`

### `str.format(*args, **kwargs)`

1. **Basic formatting**

    Simple positional formatting is probably the most common use-case. Use it if the order of your arguments is not likely to change and you only have very few elements you want to concatenate.

    ```python
    >>> '{} {}'.format('one', 'two')
    'one two'
    >>> '{} {}'.format(1, 2)
    '1 2'
    >>> '{1} {0}'.format('one', 'two')
    'two one'
    ```

2. **Value conversion**

    The new-style simple formatter calls by default the `__format__()` method of an object for its representation. If you just want to render the output of `str(...)` or `repr(...)` you can use the `!s` or `!r` conversion flags.
    
    ```python
    >>> class Data(object):
    ...     def __str__(self):
    ...         return 'str'
    ...     def __repr__(self):
    ...         return 'repr'
    ...
    >>> '{0!s} {0!r}'.format(Data())
    'str repr'
    ```

3. Padding and aligning strings

    ```python
    >>> '{:>10}'.format('test')
    '      test'
    >>> '{:10}'.format('test')
    'test      '
    >>> '{:_<10}'.format('test')
    'test______'
    >>> '{:^6}'.format('zip')
    ' zip  '
    ```

## printf-style String Formatting

## References

1. [Strings](https://docs.python.org/3.7/tutorial/introduction.html#strings)
2. [PyFormat](https://pyformat.info/)
3. [Text Sequence Type](https://docs.python.org/3.7/library/stdtypes.html#text-sequence-type-str)

# Binary Sequence Types — `bytes`, `bytearray`, `memoryview`

## Bytes Objects

## Bytearray Objects

## Bytes and Bytearray Operations

## printf-style Bytes Formatting

## Memory Views

## References

1. [Binary Sequence Types](https://docs.python.org/3.7/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview)
