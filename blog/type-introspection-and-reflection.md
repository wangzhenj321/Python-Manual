## Definitions from wikipedia

- **Type introspection:** is the ability of a program to examine the type or properties of an object at runtime.

    > Introspection should not be confused with reflection, which goes a step further and is the ability for a program to manipulate the values, meta-data, properties and/or functions of an object at runtime. Some programming languages - e.g. Java, Python and Go - also possess that capability.

- **Reflection:** is the ability of a process to examine, *introspect*, and modify its own structure and behavior.

## Type Introspection

Type introspection is the ability of a program to examine the type or properties of an object at runtime. The types of questions you might want to ask are what type is this object, or is it an instance of a certain class. Some languages even allow you to traverse the inheritance hierarchy to see if your object is derived from an inherited base class. Several languages have the type introspection capability, such as Ruby, Java, PHP, Python, C++, and more. Overall, type introspection is a very simple concept to understand – and you can really write powerful logic when you can query some of the metadata about your objects. Below are some examples of type introspection in the wild:

```java
// Java
 
if(obj instanceof Person){
   Person p = (Person)obj;
   p.walk();
}
```

```python
# Python
 
class foo(object):
  def __init__(self, val):
    self.x = val
  def bar(self):
    return self.x
 
...
 
dir(foo(5))
=> ['__class__', '__delattr__', '__dict__', '__doc__', '__getattribute__', '__hash__', '__init__', '__module__',
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__str__', '__weakref__', 'bar', 'x']
```

## Reflection

If type introspection allows you to inspect an object’s attributes at runtime, then reflection is what allows you to manipulate those attributes at runtime. As a concrete definition, reflection is the ability of a computer program to examine and modify the structure and behavior (specifically the values, meta-data, properties and functions) of a program at runtime. **In layman’s terms, what this allows you to do is invoke a method on an object, instantiate a new object, or modify an attribute of an object – all without knowing the names of the interfaces, fields, methods at compile time.** Because of the runtime-specific nature of reflection, it’s more difficult to implement reflection in a statically-typed language compared to a dynamically-typed language because type checking occurs at compile time in a statically-typed language instead of at runtime (you can read more about that in my post). However it is by no means impossible, as Java, C#, and other modern statically-typed languages allow for both type introspection and reflection (but not C++, which allows only type introspection and not reflection).

Just as reflection is easier to implement in dynamically-typed languages as compared to statically-typed languages, it’s also easier to implement in interpreted language implementations compared to compiled language implementations. This is because as functions, objects, and other data structures are created and invoked at runtime, some sort of runtime system must exist to allocate memory properly. In an interpreted language implementation, this is simple because the interpreter by default usually provides the runtime system, but compiled language implementations must provide an additional compiler and interpreter that watches program execution throughout its runtime to allow reflection to occur (this can often be done through program transformation as well).

```java
// Java
 
// without reflection
Foo foo = new Foo();
foo.hello();
 
// with reflection
Object foo = Class.forName("complete.classpath.and.Foo").newInstance();
// Alternatively: Object foo = Foo.class.newInstance();
Method m = foo.getClass().getDeclaredMethod("hello", new Class<?>[0]);
m.invoke(foo);
```

```python
# Python
 
# without reflection
obj = Foo()
obj.hello()
 
# with reflection
class_name = "Foo"
method = "hello"
obj = globals()[class_name]()
getattr(obj, method)()
 
# with eval
eval("Foo().hello()")
```

Reflection is a very powerful concept which allows you to write some very powerful code, and it is considered a metaprogramming practice. Beware though, reflection can easily lead you down a rabbit hole of poor coding practices if you let it. While it has obvious benefits, code that uses reflection is much more difficult to read than non-reflective code, it may make documentation-searching and debugging more difficult, and it opens the doors for really bad things such as code-injection via eval statements.

## Examples

```python
def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.
    
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])

if __name__ == "__main__":
    print info.__doc__
```

```python
>>> from apihelper import info
>>> li = []
>>> info(li)
append     L.append(object) -- append object to end
count      L.count(value) -> integer -- return number of occurrences of value
extend     L.extend(list) -- extend list by appending list elements
index      L.index(value) -> integer -- return index of first occurrence of value
insert     L.insert(index, object) -- insert object before index
pop        L.pop([index]) -> item -- remove and return item at index (default last)
remove     L.remove(value) -- remove first occurrence of value
reverse    L.reverse() -- reverse *IN PLACE*
sort       L.sort([cmpfunc]) -- sort *IN PLACE*; if given, cmpfunc(x, y) -> -1, 0, 1
```

## References

1. [Type introspection](https://en.wikipedia.org/wiki/Type_introspection)
2. [Reflection](https://en.wikipedia.org/wiki/Reflection_(computer_programming))
3. [Programming Concepts: Type Introspection and Reflection](https://thecodeboss.dev/2016/02/programming-concepts-type-introspection-and-reflection/)
4. [The Power Of Introspection](https://linux.die.net/diveintopython/html/power_of_introspection/index.html)
