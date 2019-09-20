## Command line

When invoking Python, you may specify any of these options:

```
python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]
```

### Interface options

The interpreter interface resembles that of the UNIX shell, but provides some additional methods of invocation:

1. When called with standard input connected to a tty device (`-` or no interface option), it prompts for commands and executes them until an EOF (an end-of-file character, you can produce that with `Ctrl-D` on UNIX or `Ctrl-Z, Enter` on Windows) is read.

2. When called with a file name argument (`script`) or with a file as standard input (`-`), it reads and executes a script from that file.

3. When called with a directory name argument (`script`), it reads and executes an appropriately named script from that directory.

4. When called with `-c` command, it executes the Python statement(s) given as command. Here command may contain multiple statements separated by newlines. Leading whitespace is significant in Python statements!

5. When called with `-m` module-name, the given module is located on the Python module path and executed as a script.

> Also refer to [Top-level components](../the_python_language_reference/toplevel_components/toplevel-components.md).
