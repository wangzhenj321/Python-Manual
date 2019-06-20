## Samples of class variables

<table>
<!-- 1st row: header -->
<tr>
<th rowspan="2">
<b>Types of class variables</b>
</th>
<th colspan="2">
<b>Outside of class</b>
</th>
<th rowspan="2">
<b>Inside of class functions</b>
</th>
</tr>
<!-- 2nd row: header -->
<tr>
<td>
<b>By instance</b>
</td>
<td>
:star::star:<b>By class</b>:star::star:
</td>
</tr>
<!-- 3nd row: immutable -->
<tr>
<td>
Immutable
</td>
<td>
<pre lang="python">
>>> class A():
...     i = 10
...
>>> a = A()
>>> a.i is A.i
True
>>> a.i = 10
>>> a.i is A.i
True
>>> a.i = 20
>>> a.i is A.i
False
</pre>
</td>
<td>
<pre lang="python">
>>> class A():
...     i = 10
...
>>> a = A()
>>> A.i = 20
>>> a.i is A.i
True
</pre>
</td>
<td rowspan="2">
:star::star:<b>Without <code>self</code></b>:star::star:
<pre lang="python">
>>> class A():
...     i = 10
...
...     def print_i(self):
...         print(i)
...
>>> a = A()
>>> a.print_i()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in print_i
NameError: name 'i' is not defined
</pre>
<b>With <code>self</code></b>
<pre lang="python">
>>> class A():
...     i = 10
...
...     def set_i(self, new_i):
...         self.i = new_i
...
>>> a1 = A()
>>> a2 = A()
>>> a1.set_i(10)
>>> a1.i is A.i
True
>>> a1.set_i(20)
>>> a1.i is A.i
False
>>> a2.i is A.i
True
</pre>
</td>
</tr>
<!-- 4th row: mutable -->
<tr>
<td>
Mutable
</td>
<td>
<pre lang="python">
>>> class A():
...     i = [10, 20]
...
>>> a = A()
>>> a.i is A.i
True
>>> a.i.append(30)
>>> a.i is A.i
True
>>> a.i = [10, 20]
>>> a.i is A.i
False
</pre>
</td>
<td>
<pre lang="python">
>>> class A():
...     i = [10, 20]
...
>>> a = A()
>>> A.i = [20, 30]
>>> a.i is A.i
True
</pre>
</td>
</tr>
</table>
