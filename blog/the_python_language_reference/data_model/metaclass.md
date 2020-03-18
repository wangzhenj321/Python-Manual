## Question

In Python, what are metaclasses and what do we use them for?

## Answer

### Classes as objects

Before understanding metaclasses, you need to master classes in Python. And Python has a very peculiar idea of what classes are, borrowed from the Smalltalk language.

In most languages, classes are just pieces of code that describe how to produce an object. That's kinda true in Python too:

```python
>>> class ObjectCreator(object):
...       pass
...

>>> my_object = ObjectCreator()
>>> print(my_object)
<__main__.ObjectCreator object at 0x8974f2c>
```

But classes are more than that in Python. Classes are objects too.

Yes, objects.

As soon as you use the keyword `class`, Python executes it and creates an OBJECT. The instruction

```python
>>> class ObjectCreator(object):
...       pass
...
```

creates in memory an object with the name "ObjectCreator".

**This object (the class) is itself capable of creating objects (the instances), and this is why it's a class.**

But still, it's an object, and therefore:

- you can assign it to a variable
you can copy it
you can add attributes to it
you can pass it as a function parameter

## References

1. [What are metaclasses in Python?](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)
