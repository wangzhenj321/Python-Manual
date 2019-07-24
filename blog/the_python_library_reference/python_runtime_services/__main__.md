## [`__main__`](https://docs.python.org/3/library/__main__.html): Top-level script environment

`'__main__'` is the name of the scope in which **top-level code** executes. A module's `__name__` is set equal to `'__main__'` when read from standard input, a script, or from an interactive prompt.

A module can discover whether or not it is running in the **main scope** by checking its own `__name__`, which allows a common idiom for conditionally executing code in a module when it is run as a script or with `python -m` but not when it is imported:

```python
if __name__ == "__main__":
    # execute only if run as a script
    main()
```

For a package, the same effect can be achieved by including a `__main__.py` module, the contents of which will be executed when the module is run with `-m`.

## [Top-level statement](https://stackoverflow.com/questions/18138166/what-is-a-top-level-statement-in-python)

### Question

In the Python Guide's chapter on project structure, the term "top-level statement" is brought up a few times. I'm not sure exactly what this refers to. My guess is it's any variable declarations that happen outside of any functions or class methods that fire as soon as a module is loaded. Is this correct? Does it also include a module's `import` statements?

### Answer

It's not just variable declarations (and there aren't any variable declarations anyway). It's pretty much anything that starts at indentation level 0.

```python
import sys         # top-level

3 + 4              # top-level

x = 0              # top-level

def f():           # top-level
    import os      # not top-level!
    return 3       # not top-level

if x:              # top-level
    print 3        # not top-level
else:
    print 4        # not top-level, but executes as part of an if statement
                   # that is top-level

class TopLevel(object): # top-level
    x = 3          # not top-level, but executes as part of the class statement
    def foo(self): # not top-level, but executes as part of the class statement
        print 5    # not top-level
```
