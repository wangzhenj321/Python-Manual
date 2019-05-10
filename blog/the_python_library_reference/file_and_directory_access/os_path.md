> The [`pathlib`](./pathlib.md) module offers high-level path objects.

> All of these functions accept either only bytes or only string objects as their parameters. The result is an object of the same type, if a path or file name is returned.

> The `os.path` module is always the path module suitable for the operating system Python is running on, and therefore usable for local paths. However, you can also import and use the individual modules if you want to manipulate a path that is always in one of the different formats. They all have the same interface:
> 
> - `posixpath` for UNIX-style paths
> - `ntpath` for Windows paths
> - `macpath` for old-style MacOS paths

## Attributes

- `os.path.abspath(path)`
- `os.path.basename(path)`
- `os.path.dirname(path)`
- `os.path.expanduser(path)`

    On Unix and Windows, return the argument with an initial component of `~` or `~user` replaced by that user’s home directory.
    
    > If the expansion fails or if the path does not begin with a tilde, the path is returned unchanged.

- `os.path.expandvars(path)`
- `os.path.getsize(path)`
- `os.path.normcase(path)`
- `os.path.normpath(path)`
- `os.path.realpath(path)`
- `os.path.relpath(path, start=os.curdir)`

---

- `os.path.commonpath(paths)`
- `os.path.commonprefix(list)`
- `os.path.samefile(path1, path2)`
- `os.path.sameopenfile(fp1, fp2)`
- `os.path.samestat(stat1, stat2)`

---

- `os.path.getatime(path)`
- `os.path.getmtime(path)`
- `os.path.getctime(path)`

- **is_exist**

    - [`os.path.exists(path)`](https://docs.python.org/3/library/os.path.html#os.path.exists)
    - [`os.path.isabs(path)`](https://docs.python.org/3/library/os.path.html#os.path.isabs)
    - [`os.path.isfile(path)`](https://docs.python.org/3/library/os.path.html#os.path.isfile)
    - [`os.path.isdir(path)`](https://docs.python.org/3/library/os.path.html#os.path.isdir)
    - [`os.path.islink(path)`](https://docs.python.org/3/library/os.path.html#os.path.islink)
    - [`os.path.ismount(path)`](https://docs.python.org/3/library/os.path.html#os.path.ismount)

- **join or split**

    - [`os.path.join(path, *paths)`](https://docs.python.org/3/library/os.path.html#os.path.join)
    - [`os.path.splitext(path)`](https://docs.python.org/3/library/os.path.html#os.path.splitext)
