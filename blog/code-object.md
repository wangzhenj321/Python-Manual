## code object

A **code object** is CPython's internal representation of a piece of runnable Python code, such as a function, a module, a class body, or a generator expression. When you run a piece of code, it is parsed and compiled into a code object, which is then run by the CPython virtual machine (VM). The code object contains a list of instructions that operate directly on the VM's internal state, like "add the two objects at the top of the stack together, pop them off, and put the result on the stack instead".

This is similar to how languages like C work: you write code as human-readable text, this code is converted into a binary format by a compiler, and the binary code (machine code for C and so-called bytecode for Python) is run directly, either by the CPU (for C) or by the virtual CPU of the CPython VM.

## References

1. [What is a code object in Python?](https://www.quora.com/What-is-a-code-object-in-Python)
