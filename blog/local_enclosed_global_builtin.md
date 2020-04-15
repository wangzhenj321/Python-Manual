# Part 1

- **namespaces**

    Roughly speaking, namespaces are just containers for mapping names to objects. As you might have already heard, everything in Python is an object. Such a "name-to-object" mapping allows us to access an object by a name that we’ve assigned to it. We can picture a namespace as a Python dictionary structure, where the dictionary keys represent the names and the dictionary values the object itself.

- **scope**

    We have learned that namespaces can exist independently from each other and that they are structured in a certain hierarchy, which brings us to the concept of "scope". The "scope" in Python defines the "hierarchy level" in which we search namespaces for certain "name-to-object" mappings.

    - **Local** can be inside a function or class method, for example.
    - **Enclosed** can be its enclosing function, e.g., if a function is wrapped inside another function.
    - **Global** refers to the uppermost level of the executing script itself, and
    - **Built-in** are special names that Python reserves for itself.

## Example 1: Local and Global scopes

- **Case 1**

    ```python
    i = 1

    def foo():
        i = 5
        print(i, 'in foo()')

    print(i, 'global')

    foo()
    ```

- **Case 2**

    ```python
    a_var = 'global variable'

    def a_func():
        print(a_var, '[ a_var inside a_func() ]')

    a_func()
    print(a_var, '[ a_var outside a_func() ]')
    ```

## Example 2: `global`

```python
a_var = 'global value'

def a_func():
    global a_var
    a_var = 'local value'
    print(a_var, '[ a_var inside a_func() ]')

print(a_var, '[ a_var outside a_func() ]')
a_func()
print(a_var, '[ a_var outside a_func() ]')
```

## Example 3: `nonlocal`

```python
a_var = 'global value'

def outer():
    a_var = 'local value'
    print('outer before:', a_var)
    def inner():
        nonlocal a_var
        a_var = 'inner value'
        print('in inner():', a_var)
    inner()
    print('outer after:', a_var)

outer()
```

## Example 4: UnboundLocalError

- **Case 1**

    ```python
    a_var = 1

    def a_func():
        a_var = a_var + 1
        print(a_var, '[ a_var inside a_func() ]')

    print(a_var, '[ a_var outside a_func() ]')
    a_func()
    ```

- **Case 2**

    ```python
    global_var = 'foo'

    def ex1():
        local_var = 'bar'
        print('locals(): ', locals())
        print(global_var)
        print(local_var)
        global_var = 'foo2'

    ex1()
    ```

## Example 5: free variable

> A **free variable** is not defined in the current environment, i. e. collection of local variables, and is also not a global variable!

```python
def bar():
    x = 1
    def foo():
        print(x)
        print(locals())
    foo()
```

# References

1. [A Beginner's Guide to Python's Namespaces, Scope Resolution, and the LEGB Rule](https://sebastianraschka.com/Articles/2014_python_scope_and_namespaces.html)
2. [How to define free-variable in python?](https://stackoverflow.com/questions/12919278/how-to-define-free-variable-in-python)
3. [python学习笔记 - local, global and free variable](https://www.jianshu.com/p/e1fd4f14136a)
