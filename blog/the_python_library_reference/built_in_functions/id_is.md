## [`id(object)`](https://docs.python.org/3/library/functions.html?highlight=staticmethod#id)

Return the "identity" of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same `id()` value.

> CPython implementation detail: This is the address of the object in memory.

- **Example 1: Immutable**

    ```python
    >>> x = 'wang'
    >>> y = 'wang'
    >>> id(x)
    4397491288
    >>> id(y)
    4397491288  # id of x and y is same
    >>> x = 'wang' + 'zhen'
    >>> id(x)
    4395952752  # change x and also change its id
    ```

- **Example 2: Mutable**

    ```python
    >>> x = ['wang', 'xu']
    >>> y = ['wang', 'xu']
    >>> id(x)
    4346196232
    >>> id(y)
    4347167112  # id of x and y is not same
    >>> y = x
    >>> id(y)
    4346196232
    >>> x.append('liu')
    >>> x
    ['wang', 'xu', 'liu']
    >>> id(x)
    4346196232  # change x but not change its id
    >>> id(y)
    4346196232
    ```

## [Identity comparisons](https://docs.python.org/3/reference/expressions.html#is-not)

The operators `is` and `is not` test for an object’s identity: `x is y` is true if and only if x and y are the same object. An Object’s identity is determined using the `id()` function. `x is not y` yields the inverse truth value.
