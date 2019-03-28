# Static and Dynamic

> Python is a dynamically-typed language. Java is a statically-typed language.

## Static

In a **statically typed language**, every variable name is bound both to a type (at compile time, by means of a data declaration)
to an object. The binding to an object is optional — if a name is not bound to an object, the name is said to be null.

Once a variable name has been bound to a type (that is, declared) it can be bound (via an assignment statement) only to objects of that type; it cannot ever be bound to an object of a different type. An attempt to bind the name to an object of the wrong type will raise a type exception.

## Dynamic

In a **dynamically typed language**, every variable name is (unless it is null) bound only to an object. Names are bound to objects at execution time by means of assignment statements, and it is possible to bind a name to objects of different types during the execution of the program.

## Examples

In a statically-typed language, the following sequence of statements (which binds an integer object, then a string object, to the name `employeeName`) is illegal. If `employeeName` had been declared to be an int, then the second statement would be illegal; if it had been declared to be a String, then the first statement would be illegal. But in a dynamically-typed language this sequence of statements is perfectly fine.

```
employeeName = 9
employeeName = "Steve Ferg"
```

# Strong and Weak

> Both Java and Python are strongly typed languages. Examples of weakly typed languages are Perl and Rexx.

## Strong

In a **strongly typed language**, on the other hand, the last two statements would raise type exceptions. To avoid these exceptions, some kind of explicit type conversion would be necessary, like this.

```
a  = 9
b = "9"
c = concatenate(  str(a),  b)
d = add(a,  int(b)  )
```

## Weak

In a **weakly typed language**, variables can be implicitly coerced to unrelated types, whereas in a strongly typed language they cannot, and an explicit conversion is required. (Note that I said unrelated types. Most languages will allow implicit coercions between related types — for example, the addition of an integer and a float. By unrelated types I mean things like numbers and strings.) In a typical weakly typed language, the number 9 and the string "9" are interchangeable, and the following sequence of statements is legal.

```
a  = 9
b = "9"
c = concatenate(a, b)  // produces "99"
d = add(a, b)          // produces 18
```

# Compiled and Interpreted

## Compiled

**Compiled languages** are written in a code that can be executed directly on a computer's processor. A compiler is a special program that processes statements written in a particular programming language and turns them into machine language or "code" that a computer's processor uses.

## Interpreted

An **Interpreted language** is any programming language that isn't already in "machine code" prior to runtime. Unlike compiled languages , an interpreted language's translation doesn't happen beforehand. Translation occurs at the same time as the program is being executed.

> Python as a programming language has no saying about if it's an compiled or interpreted programming language, only the implementation of it. The terms interpreted or compiled is not a property of the language but a property of the implementation. Python program runs directly from the source code. So Python will fall under byte code interpreted. The `.py` source code is first compiled to byte code as `.pyc`. This byte code can be interpreted (official CPython), or JIT compiled (PyPy). Python source code (.py) can be compiled to different byte code also like IronPython (.Net) or Jython (JVM). There are multiple implementations of Python language. The official one is a byte code interpreted one. There are byte code JIT compiled implementations too.
> 
> **As concluding remarks, Python(Cpython) is neither a true compiled time nor pure interpreted language but it is called interpreted language.**
