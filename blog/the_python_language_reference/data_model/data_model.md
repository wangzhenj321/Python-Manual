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
- `object.__getattribute__(self, name)`
- `object.__setattr__(self, name, value)`
- `object.__delattr__(self, name)`
- `object.__dir__(self)`

### Customizing module attribute access

### Implementing Descriptors

### Invoking Descriptors

### __slots__

## Special method lookup

Refer to []()
