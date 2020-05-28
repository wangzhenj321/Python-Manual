This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

- `sys.argv`

- `sys.path`

    A list of strings that specifies the search path for modules. **Initialized from the environment variable `PYTHONPATH`, plus an installation-dependent default.**
    
    > As initialized upon program startup, the first item of this list, `path[0]`, is the directory containing the script that was used to invoke the Python interpreter. If the script directory is not available (e.g. if the interpreter is invoked interactively or if the script is read from standard input), `path[0]` is the empty string, which directs Python to search modules in the current directory first. Notice that the script directory is inserted before the entries inserted as a result of `PYTHONPATH`.
    
    A program is free to modify this list for its own purposes. Only strings and bytes should be added to `sys.path`; all other data types are ignored during import.
    
    - **Interactive mode on Windows with the direct installation of Python 3.7**
    
        ```
        >>> print('\n'.join(sys.path))

        C:\Users\wangzhenj321\AppData\Local\Programs\Python\Python37\python37.zip
        C:\Users\wangzhenj321\AppData\Local\Programs\Python\Python37\DLLs
        C:\Users\wangzhenj321\AppData\Local\Programs\Python\Python37\lib
        C:\Users\wangzhenj321\AppData\Local\Programs\Python\Python37
        C:\Users\wangzhenj321\AppData\Roaming\Python\Python37\site-packages
        C:\Users\wangzhenj321\AppData\Local\Programs\Python\Python37\lib\site-packages
        C:\Users\wangzhenj321\AppData\Local\Programs\Python\Python37\lib\site-packages\win32
        C:\Users\wangzhenj321\AppData\Local\Programs\Python\Python37\lib\site-packages\win32\lib
        C:\Users\wangzhenj321\AppData\Local\Programs\Python\Python37\lib\site-packages\Pythonwin
        ```
    
    - **Interactive mode on Ubuntu with the installation of Miniconda**
    
        ```
        >>> print('\n'.join(sys.path))

        /home/wang/miniconda3/lib/python37.zip
        /home/wang/miniconda3/lib/python3.7
        /home/wang/miniconda3/lib/python3.7/lib-dynload
        /home/wang/miniconda3/lib/python3.7/site-packages
        ```

- `sys.platform`
