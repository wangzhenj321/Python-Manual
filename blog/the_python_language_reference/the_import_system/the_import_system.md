> **module**
> 
> An object that serves as an organizational unit of Python code. Modules have a namespace containing arbitrary Python objects. Modules are loaded into Python by the process of importing.

**invoking the import machinery**

1. `import`
    - searches for the named module
    - binds the results of that search to a name in the local scope
2. `importlib.import_module()`
3. `__import__()`

## `importlib`

## Packages

> **package**
> 
> A Python module which can contain submodules or recursively, subpackages. Technically, a package is a Python module with an `__path__` attribute.

### Regular packages

> **regular package**
> 
> A traditional package, such as a directory containing an `__init__.py` file.

```
parent/
    __init__.py
    one/
        __init__.py
    two/
        __init__.py
    three/
        __init__.py
```

### Namespace packages

> **namespace package**
> 
> Namespace packages may have no physical representation, and specifically are not like a regular package because they have no `__init__.py` file.

> **portion**
> 
> A set of files in a single directory (possibly stored in a zip file) that contribute to a namespace package

## Searching

> **qualified name**
> 
> A dotted name showing the “path” from a module’s global scope to a class, function or method defined in that module.

### The module cache

The first place checked during import search is `sys.modules`.

### Finders and loaders

If the named module is not found in `sys.modules`, then Python’s import protocol is invoked to find and load the module.

## Loading

## Package Relative Imports

Relative imports use leading dots. A single leading dot indicates a relative import, starting with the current package. Two or more leading dots indicate a relative import to the parent(s) of the current package, one level per dot after the first.

Absolute imports may use either the import <> or from <> import <> syntax, but relative imports may only use the second form.

```
package/
    __init__.py
    subpackage1/
        __init__.py
        moduleX.py
        moduleY.py
    subpackage2/
        __init__.py
        moduleZ.py
    moduleA.py
```

In either `subpackage1/moduleX.py` or `subpackage1/__init__.py`, the following are valid relative imports:

```python
from .moduleY import spam
from .moduleY import spam as ham
from . import moduleY
from ..subpackage1 import moduleY
from ..subpackage2.moduleZ import eggs
from ..moduleA import foo
```

## References

1. [The import system](https://docs.python.org/3.7/reference/import.html#)
