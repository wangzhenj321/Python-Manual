> The [`pathlib`](./pathlib.md) module offers high-level path objects.

> All of these functions accept either only bytes or only string objects as their parameters. The result is an object of the same type, if a path or file name is returned.

> The `os.path` module is always the path module suitable for the operating system Python is running on, and therefore usable for local paths. However, you can also import and use the individual modules if you want to manipulate a path that is always in one of the different formats. They all have the same interface:
> 
> - `posixpath` for UNIX-style paths
> - `ntpath` for Windows paths
> - `macpath` for old-style MacOS paths

## Attributes

- **part of path**
    - `os.path.basename(path)`
    - `os.path.dirname(path)`

- **normalize path**
    - [`os.path.abspath(path)`](https://docs.python.org/3/library/os.path.html#os.path.abspath)
    - `os.path.relpath(path, start=os.curdir)`
    - `os.path.normpath(path)`
    - `os.path.realpath(path)`
    - `os.path.normcase(path)`

- **expand environment variable**
    - [`os.path.expanduser(path)`](https://docs.python.org/3/library/os.path.html#os.path.expanduser)
    - [`os.path.expandvars(path)`](https://docs.python.org/3/library/os.path.html#os.path.expandvars)

- **compare two or more**
    - [`os.path.commonpath(paths)`](https://docs.python.org/3/library/os.path.html#os.path.commonpath)
    - [`os.path.commonprefix(list)`](https://docs.python.org/3/library/os.path.html#os.path.commonprefix)
    - [`os.path.samefile(path1, path2)`](https://docs.python.org/3/library/os.path.html#os.path.samefile)
    - [`os.path.sameopenfile(fp1, fp2)`](https://docs.python.org/3/library/os.path.html#os.path.sameopenfile)
    - [`os.path.samestat(stat1, stat2)`](https://docs.python.org/3/library/os.path.html#os.path.samestat)

- **size info**
    - `os.path.getsize(path)`

- **time info**
    - [`os.path.getatime(path)`](https://docs.python.org/3/library/os.path.html#os.path.getatime)
    - [`os.path.getmtime(path)`](https://docs.python.org/3/library/os.path.html#os.path.getmtime)
    - [`os.path.getctime(path)`](https://docs.python.org/3/library/os.path.html#os.path.getctime)

- **is exist**
    - [`os.path.exists(path)`](https://docs.python.org/3/library/os.path.html#os.path.exists)
    - [`os.path.isabs(path)`](https://docs.python.org/3/library/os.path.html#os.path.isabs)
    - [`os.path.isfile(path)`](https://docs.python.org/3/library/os.path.html#os.path.isfile)
    - [`os.path.isdir(path)`](https://docs.python.org/3/library/os.path.html#os.path.isdir)
    - [`os.path.islink(path)`](https://docs.python.org/3/library/os.path.html#os.path.islink)
    - [`os.path.ismount(path)`](https://docs.python.org/3/library/os.path.html#os.path.ismount)

- **join or split**
    - [`os.path.join(path, *paths)`](https://docs.python.org/3/library/os.path.html#os.path.join)
    - [`os.path.splitext(path)`](https://docs.python.org/3/library/os.path.html#os.path.splitext)
