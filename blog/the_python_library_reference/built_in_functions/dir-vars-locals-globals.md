## [`globals()`](https://docs.python.org/3/library/functions.html?highlight=staticmethod#globals)

Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).

## [`locals()`](https://docs.python.org/3/library/functions.html?highlight=staticmethod#locals)

**Update** and return a dictionary representing the current local symbol table. **Free variables** are returned by `locals()` when it is called in function blocks, but not in class blocks. Note that at the module level, `locals()` and `globals()` are the same dictionary.

> The contents of this dictionary should not be modified; changes may not affect the values of local and free variables used by the interpreter.

## [`vars([object])`](https://docs.python.org/3/library/functions.html?highlight=staticmethod#vars)

Return the `__dict__` attribute for a module, class, instance, or any other object with a `__dict__` attribute.

Objects such as modules and instances have an updateable `__dict__` attribute; however, other objects may have write restrictions on their `__dict__` attributes (for example, classes use a `types.MappingProxyType` to prevent direct dictionary updates).

Without an argument, `vars()` acts like `locals()`. Note, the locals dictionary is only useful for reads since updates to the locals dictionary are ignored.

## [`dir([object])`](https://docs.python.org/3/library/functions.html?highlight=staticmethod#dir)

Without arguments, return the list of names in the current local scope. With an argument, attempt to return a list of valid attributes for that object.

If the object has a method named `__dir__()`, this method will be called and must return the list of attributes. This allows objects that implement a custom `__getattr__()` or `__getattribute__()` function to customize the way `dir()` reports their attributes.

If the object does not provide `__dir__()`, the function tries its best to gather information from the object's `__dict__` attribute, if defined, and from its type object. The resulting list is not necessarily complete, and may be inaccurate when the object has a custom `__getattr__()`.

> Because `dir()` is supplied primarily as a convenience for use at an interactive prompt, **it tries to supply an interesting set of names more than it tries to supply a rigorously or consistently defined set of names**, and its detailed behavior may change across releases. For example, metaclass attributes are not in the result list when the argument is a class.
