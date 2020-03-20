# Objects, values and types

# The standard type hierarchy

# Special method names

A class can implement certain operations that are invoked by special syntax (such as arithmetic operations or subscripting and slicing) by defining methods with special names. This is Python's approach to *operator overloading*, allowing classes to define their own behavior with respect to language operators.

## Basic customization

- `object.__new__(cls[, ...])`
- `object.__init__(self[, ...])`
- `object.__del__(self)`

---

- `object.__repr__(self)`
- `object.__str__(self)`
- `object.__bytes__(self)`
- `object.__format__(self, format_spec)`

---

- `object.__lt__(self, other)`
- `object.__le__(self, other)`
- `object.__eq__(self, other)`
- `object.__ne__(self, other)`
- `object.__gt__(self, other)`
- `object.__ge__(self, other)`

---

- `object.__hash__(self)`

---

- `object.__bool__(self)`

## Customizing attribute access

The following methods can be defined to customize the meaning of attribute access (use of, assignment to, or deletion of `x.name`) for class instances.

- `object.__getattr__(self, name)`
- `object.__getattribute__(self, name)` (Refer to [Special method lookup](special_method_lookup.md))
- `object.__setattr__(self, name, value)`
- `object.__delattr__(self, name)`
- `object.__dir__(self)`

### Customizing module attribute access

Special names `__getattr__` and `__dir__` can be also used to customize access to module attributes.

For a more fine grained customization of the module behavior (setting attributes, properties, etc.), one can set the `__class__` attribute of a module object to a subclass of `types.ModuleType`.

### Implementing Descriptors

- `object.__get__(self, instance, owner)`
- `object.__set__(self, instance, value)`
- `object.__delete__(self, instance)`
- `object.__set_name__(self, owner, name)`

### Invoking Descriptors

### __slots__

## Special method lookup

Refer to []()
