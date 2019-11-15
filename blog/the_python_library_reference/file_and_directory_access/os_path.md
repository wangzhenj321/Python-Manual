> The [`pathlib`](./pathlib.md) module offers high-level path objects.

> All of these functions accept either only bytes or only string objects as their parameters. The result is an object of the same type, if a path or file name is returned.

## Attributes

- **parts of path**
    - `os.path.basename(path)` :star:
    - `os.path.dirname(path)` :star:

- **join or split**
    - `os.path.join(path, *paths)` :star:
    - `os.path.splitext(path)` :star:

- **normalize path**
    - `os.path.abspath(path)` :star:
    - `os.path.relpath(path, start=os.curdir)`
    - `os.path.normpath(path)`
    - `os.path.realpath(path)`
    - `os.path.normcase(path)`

- **expand environment variable**
    - `os.path.expanduser(path)`
    - `os.path.expandvars(path)`

- **compare two or more**
    - `os.path.commonpath(paths)`
    - `os.path.commonprefix(list)`
    - `os.path.samefile(path1, path2)`
    - `os.path.sameopenfile(fp1, fp2)`
    - `os.path.samestat(stat1, stat2)`

- **size info**
    - `os.path.getsize(path)`

- **time info**
    - `os.path.getatime(path)`
    - `os.path.getmtime(path)`
    - `os.path.getctime(path)`

- **is exist**
    - `os.path.exists(path)` :star:
    - `os.path.isabs(path)`
    - `os.path.isfile(path)`
    - `os.path.isdir(path)`
    - `os.path.islink(path)`
    - `os.path.ismount(path)`
