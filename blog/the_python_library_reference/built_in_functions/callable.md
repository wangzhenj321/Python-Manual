## [`callable(object)`](https://docs.python.org/3/library/functions.html#callable)

Return `True` if the object argument appears callable, `False` if not. If this returns true, it is still possible that a call fails, but if it is false, calling object will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a `__call__()` method.

> A callable is anything that can be called.

## Examples

```python
>>> callable(0)
False
>>> callable("mystring")
False
>>> def add(a, b):
…     return a + b
…
>>> callable(add)
True
>>> class A:
…      def method(self):
…         return 0
…
>>> callable(A)
True
>>> a = A()
>>> callable(a)
False
>>> class B:
…     def __call__(self):
…         return 0
…
>>> callable(B)
True
>>> b = B()
>>> callable(b)
True
```

## References

1. [What is a "callable"?](https://stackoverflow.com/questions/111234/what-is-a-callable)
