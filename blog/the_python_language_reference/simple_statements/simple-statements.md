## `global`

The `global` statement is a declaration which holds for the entire current code block. It means that the listed identifiers are to be interpreted as globals. It would be impossible to assign to a global variable without `global`, although **free variables** may refer to globals without being declared global.

> 1. Names listed in a `global` statement must not be used in the same code block textually preceding that `global` statement.
> 
> 2. Names listed in a `global` statement must not be defined as formal parameters or in a `for` loop control target, class definition, function definition, import statement, or variable annotation.

## `nonlocal`

The `nonlocal` statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals. This is important because the default behavior for binding is to search the local namespace first. The statement allows encapsulated code to rebind variables outside of the local scope besides the global (module) scope.

> 1. Names listed in a `nonlocal` statement, unlike those listed in a `global` statement, must refer to pre-existing bindings in an enclosing scope.
> 
> 2. Names listed in a `nonlocal` statement must not collide with pre-existing bindings in the local scope.
