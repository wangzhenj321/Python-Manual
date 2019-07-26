- [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path)

    A list of strings that specifies the search path for modules. Initialized from the environment variable `PYTHONPATH`, plus an installation-dependent default.
    
    As initialized upon program startup, the first item of this list, `path[0]`, is the directory containing the script that was used to invoke the Python interpreter. If the script directory is not available (e.g. if the interpreter is invoked interactively or if the script is read from standard input), `path[0]` is the empty string, which directs Python to search modules in the current directory first. Notice that the script directory is inserted before the entries inserted as a result of `PYTHONPATH`.
    
    A program is free to modify this list for its own purposes. Only strings and bytes should be added to sys.path; all other data types are ignored during import.
