## Difference between `@staticmethod` and `@classmethod` 

Maybe a bit of example code will help: Notice the difference in the call signatures of `foo`, `class_foo` and `static_foo`:

```python
class A(object):
    def foo(self, x):
        print "executing foo(%s, %s)" % (self, x)

    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s, %s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x    

a = A()
```

Below is the usual way an object instance calls a method. The object instance, `a`, is implicitly passed as the first argument.

```python
a.foo(1)
# executing foo(<__main__.A object at 0xb7dbef0c>,1)
```

---

**With classmethods**, the class of the object instance is implicitly passed as the first argument instead of `self`.

```python
a.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)
```

You can also call `class_foo` using the class. In fact, if you define something to be a classmethod, it is probably because you intend to call it from the class rather than from a class instance. `A.foo(1)` would have raised a `TypeError`, but `A.class_foo(1)` works just fine:

```
A.class_foo(1)
# executing class_foo(<class '__main__.A'>,1)
```

One use people have found for class methods is to create **inheritable alternative constructors**.

> ```python
> >>> class y(object):
> ...   def __init__(self, astring):
> ...     self.s = astring
> ...   @classmethod
> ...   def fromlist(cls, alist):
> ...     x = cls('')
> ...     x.s = ','.join(str(s) for s in alist)
> ...     return x
> ...   def __repr__(self):
> ...     return 'y(%r)' % self.s
> ...
> >>> y1 = y('xx')
> >>> y1
> y('xx')
> >>> y2 = y.fromlist(range(3))
> >>> y2
> y('0,1,2')
> ```

---

**With staticmethods**, neither `self` (the object instance) nor `cls` (the class) is implicitly passed as the first argument. They behave like plain functions except that you can call them from an instance or the class:

```python
a.static_foo(1)
# executing static_foo(1)

A.static_foo('hi')
# executing static_foo(hi)
```

Staticmethods are used to group functions which have some logical connection with a class to the class.

---

`foo` is just a function, but when you call `a.foo` you don't just get the function, you get a "partially applied" version of the function with the object instance `a` bound as the first argument to the function. `foo` expects 2 arguments, while `a.foo` only expects 1 argument.

`a` is bound to `foo`. That is what is meant by the term "bound" below:

```python
print(a.foo)
# <bound method A.foo of <__main__.A object at 0xb7d52f0c>>
```

With `a.class_foo`, `a` is not bound to `class_foo`, rather the class `A` is bound to `class_foo`.

```python
print(a.class_foo)
# <bound method type.class_foo of <class '__main__.A'>>
```

Here, with a staticmethod, even though it is a method, `a.static_foo` just returns a good'ole function with no arguments bound. `static_foo` expects 1 argument, and `a.static_foo` expects 1 argument too.

```python
print(a.static_foo)
# <function static_foo at 0xb7d479cc>
```

And of course the same thing happens when you call `static_foo` with the class `A` instead.

```python
print(A.static_foo)
# <function static_foo at 0xb7d479cc>
```

## Call static methods within the same class

假设我们有一个`class Test`，有一个`@staticmethod foo`：

```python
class Test:
    @staticmethod
    def foo():
        print("foo")
```

那么对于下面三种情况：

1. `class Test`有一个`member method`要`call foo`
2. `class Test`有一个`@classmethod`要`call foo`
3. `class Test`有一个`@staticmethod`要`call foo`

我们应该怎么写代码？

1. When a member method calls @staticmethod foo

    用`self.foo()`、`self.__class__.foo()`或者class全称`Test.foo()`都可以：

    ```python
    class Test:
        @staticmethod
        def foo():
            print("foo")

        def bar(self):
            self.foo()

        def baz(self):
            self.__class__.foo()

        def qux(self):
            Test.foo()

    t = Test()
    t.bar()  # Output: foo
    t.baz()  # Output: foo
    t.qux()  # Output: foo
    ```

2. When a @classmethod calls @staticmethod foo

    依葫芦画瓢，此时用`cls.foo()`或者class全称调用都行：

    ```python
    class Test:
        @staticmethod
        def foo():
            print("foo")

        @classmethod
        def bar(cls):
            cls.foo()

        @classmethod
        def baz(cls):
            Test.foo()

    Test.bar()  # Output: foo
    Test.baz()  # Output: foo
    ```

3. When another @staticmethod calls @staticmethod foo

    这种情况下，你既没有`self`也没有`cls`，所以你此时只能用class全称去调用。不用前缀直接调用是非法的：

    ```python
    class Test:
        @staticmethod
        def foo():
            print("foo")

        @staticmethod
        def bar():
            foo()  # WRONG 

        @staticmethod
        def baz():
            Test.foo()  # OK

    Test.bar()  # NameError: name 'foo' is not defined
    Test.baz()  # Output: foo
    ```

总结一下就是：

- 有 handle (self 或 cls) 就用 handle
- 没有 handle 就用 class 全称

## References

1. [What is the difference between @staticmethod and @classmethod?](https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod)

2. [Python: calling static methods within the same class / recursive static methods](http://yaoyao.codes/python/2020/03/23/python-calling-static-methods-within-the-same-class)
