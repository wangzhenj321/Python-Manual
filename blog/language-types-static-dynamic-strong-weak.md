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
