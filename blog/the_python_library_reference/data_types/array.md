## `array`: Efficient arrays of numeric values

This module defines an object type which can compactly represent an array of basic values: characters, integers, floating point numbers. Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained. The type is specified at object creation time by using a type code, which is a single character. The following type codes are defined:

| Type code | C Type | Python Type | Minimum size in bytes |
| --- | --- | --- | --- |
| `'b'` | signed char | int | 1 |
| `'B'` | unsigned char | int | 1 |
| `'u'` | Py_UNICODE | Unicode character | 2 |
| `'h'` | signed short | int | 2 |
| `'H'` | unsigned short | int | 2 |
| `'i'` | signed int | int | 2 |
| `'I'` | unsigned int | int | 2 |
| `'l'` | signed long | int | 4 |
| `'L'` | unsigned long | int | 4 |
| `'q'` | signed long long | int | 8 |
| `'Q'` | unsigned long long | int | 8 |
| `'f'` | float | float | 4 |
| `'d'` | double | float | 8 |

The actual representation of values is determined by the machine architecture (strictly speaking, by the C implementation).

The module defines the following type: `class array.array(typecode[, initializer])`

## References

1. [array — Efficient arrays of numeric values](https://docs.python.org/3.7/library/array.html)
