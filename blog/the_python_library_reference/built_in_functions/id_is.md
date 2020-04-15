## [`id(object)`](https://docs.python.org/3/library/functions.html?highlight=staticmethod#id)

Return the "identity" of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same `id()` value.

> CPython implementation detail: This is the address of the object in memory.

## [Identity comparisons](https://docs.python.org/3/reference/expressions.html#is-not)

The operators `is` and `is not` test for an object’s identity: `x is y` is true if and only if x and y are the same object. An Object’s identity is determined using the `id()` function. `x is not y` yields the inverse truth value.
