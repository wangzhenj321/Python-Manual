## single leading underscore

`_single_leading_underscore`: weak "internal use" indicator. E.g. `from M import *` does not import objects whose name starts with an underscore.

> Naming an attribute in your class `self._var1` indicates to the user of the class that the attribute should only be accessed by the class's internals (or perhaps those of a subclass) and that they need not directly access it and probably shouldn't modify it. **You should use leading underscores in the same places that you would use a private or protected field in Java or C#, but be aware that the language doesn't actually enforce non-access** - instead you trust your class's user to not do anything stupid, and leave them the option of accessing (or modifying) your class's private field if they're really, really sure that they know what they're doing and it makes sense.

## single trailing underscore

`single_trailing_underscore_`: used by convention to avoid conflicts with Python keyword, e.g. `Tkinter.Toplevel(master, class_='ClassName')`

## double leading underscore

`__double_leading_underscore`: when naming a class attribute, invokes **name mangling** (inside class FooBar, `__boo` becomes `_FooBar__boo`; see below).

> This one actually has syntactical significance. Referring to `self.__var1` from within the scope of your class invokes name mangling. From outside your class, the variable will appear to be at `self._YourClassName__var1` instead of `self.__var1`. Not everyone uses this - we don't at all where I work - and for simple classes it feels like a slightly absurd and irritating alternative to using a single leading underscore.
> 
> However, there is a justification for it existing; if you're using lots of inheritance, **if you only use single leading underscores then you don't have a way of indicating to somebody reading your code the difference between 'private' and 'protected' variables** - ones that aren't even meant to be accessed by subclasses, and ones that subclasses may access but that the outside world may not. Using a single trailing underscore to mean 'protected' and a double underscore to mean 'private' may therefore be a useful convention in this situation (and the name mangling will allow a subclasses to use a variable with the same name in their subclass without causing a collision).

> **You don't play around with another class's variables that look like `__foo` or `_bar`.**

> Name mangling is intended to give classes an easy way to define “private” instance variables and methods, without having to worry about instance variables defined by derived classes, or mucking with instance variables by code outside the class. **Note that the mangling rules are designed mostly to avoid accidents; it still is possible for a determined soul to access or modify a variable that is considered private.**

>> **Private name mangling:** When an identifier that textually occurs in a class definition begins with two or more underscore characters and does not end in two or more underscores, it is considered a private name of that class. Private names are transformed to a longer form before code is generated for them. The transformation inserts the class name, with leading underscores removed and a single underscore inserted, in front of the name. For example, the identifier `__spam` occurring in a class named `Ham` will be transformed to `_Ham__spam`. This transformation is independent of the syntactical context in which the identifier is used. If the transformed name is extremely long (longer than 255 characters), implementation defined truncation may happen. If the class name consists only of underscores, no transformation is done.

## double leading and trailing underscore

`__double_leading_and_trailing_underscore__`: "magic" objects or attributes that live in user-controlled namespaces. E.g. `__init__`,  `__import__` or `__file__`. **Never invent such names; only use them as documented.**

> `self.__var1__` is something you should never create as I've literally written it, because the double leading and trailing underscore naming style is meant to be used only for names that have a special meaning defined by Python, like the `__init__` or `__eq__` methods of classes. **You're free to override those to change your class's behavior (indeed, almost all classes will have a programmer-defined `__init__`), but you shouldn't make up your own names in this style like `self.__var1__`.**

## References

1. [What is the difference in python attributes with underscore in front and back ](https://stackoverflow.com/questions/14671487/what-is-the-difference-in-python-attributes-with-underscore-in-front-and-back)

2. [Does Python have “private” variables in classes?](https://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes)

3. [What is the meaning of a single and a double underscore before an object name?](https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-a-single-and-a-double-underscore-before-an-object-name)
