## String Methods

- `str.encode(encoding="utf-8", errors="strict")`

    Return an encoded version of the string as a bytes object.

- `str.format(*args, **kwargs)`

    Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces `{}`.

- `str.strip([chars])`

    Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or `None`, the chars argument defaults to removing whitespace. The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped.

- `str.upper()`

    Return a copy of the string with all the cased characters converted to uppercase.

## `str.format(*args, **kwargs)`

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

## References

1. [PyFormat](https://pyformat.info/)
