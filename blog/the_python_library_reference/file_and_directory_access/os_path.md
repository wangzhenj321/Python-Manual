> The [`pathlib`](./pathlib.md) module offers high-level path objects.

> All of these functions accept either only bytes or only string objects as their parameters. The result is an object of the same type, if a path or file name is returned.

## Attributes

- `os.path.abspath(path)`
- `os.path.basename(path)`
- `os.path.dirname(path)`
- `os.path.expanduser(path)`
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

---

- `os.path.exists(path)`
- `os.path.lexists(path)`
- `os.path.isabs(path)`
- `os.path.isfile(path)`
- `os.path.isdir(path)`
- `os.path.islink(path)`
- `os.path.ismount(path)`

---

- `os.path.join(path, *paths)`
- `os.path.split(path)`
- `os.path.splitdrive(path)`
- `os.path.splitext(path)`
