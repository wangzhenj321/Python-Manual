# :star::star::star: **Everything in Python is an object.** :star::star::star:

## `id(object)` and Identity comparisons

- [`id(object)`](https://docs.python.org/3/library/functions.html?highlight=staticmethod#id)

    Return the "identity" of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same `id()` value.

    > CPython implementation detail: This is the address of the object in memory.

- [Identity comparisons](https://docs.python.org/3/reference/expressions.html#is-not)

    The operators `is` and `is not` test for an object’s identity: `x is y` is true if and only if x and y are the same object. An Object’s identity is determined using the `id()` function. `x is not y` yields the inverse truth value.

## Immutable and mutable types

| **immutable** | **mutable** |
| --- | --- |
| <ul><li>bool</li><li>int</li><li>float</li><li>tuple</li><li>str</li><li>frozenset</li><ul> | <ul><li>list</li><li>set</li><li>dict</li><li>custom classes</li><ul> |

## Samples of immutable and mutable

> The immutable type in Python is not same as the primitive type in Java. Please refer the case of "Assignment"-"Immutable" in the following table. The address of `x` and `y` in memory is same, but it's not possible in Java. In Java, the different memory will be allocated.

<table align="center">
<!-- 1st row: header -->
<tr>
<td>
<b>Operation</b>
</td>
<td>
<b>Immutable</b>
</td>
<td>
<b>Mutable</b>
</td>
</tr>
<!-- 2nd row: assignment -->
<tr>
<td>
Assignment
</td>
<td>
:star::star::star::star::star:
<pre lang="python">
>>> x = 10
>>> y = 10
>>> x is y
True
</pre>
</td>
<td>
<pre lang="python">
>>> x = [10, 20]
>>> y = [10, 20]
>>> x is y
False
</pre>
</td>
</tr>
<!-- 3rd row: partially change -->
<tr>
<td>
Partially change
</td>
<td>
<pre lang="python">
Not supported!
</pre>
</td>
<td>
<pre lang="python">
>>> x = [10, 20]
>>> y = x
>>> x is y
True
>>> y.append(30)
>>> x is y
True
</pre>
</td>
</tr>
<!-- 4th row: totally change -->
<tr>
<td>
Totally change
</td>
<td>
<pre lang="python">
>>> x = 10
>>> y = x
>>> x is y
True
>>> y = 20
>>> x is y
False
</pre>
</td>
<td>
<pre lang="python">
>>> x = [10, 20]
>>> y = x
>>> x is y
True
>>> y = [10, 20]
>>> x is y
False
</pre>
</td>
</tr>
</table>
