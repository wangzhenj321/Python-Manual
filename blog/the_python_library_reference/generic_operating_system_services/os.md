## Files and Directories

> On some Unix platforms, many of these functions support one or more of these features:
> 
> - specifying a file descriptor
> - paths relative to directory descriptors
> - not following symlinks

- [`os.chdir(path)`](https://docs.python.org/3/library/os.html#os.chdir)

- [`os.getcwd()`](https://docs.python.org/3/library/os.html#os.getcwd)

- [`os.listdir(path='.')`](https://docs.python.org/3/library/os.html#os.listdir)

- **mkdir**
    - [`os.mkdir(path, mode=0o777, *, dir_fd=None)`](https://docs.python.org/3/library/os.html#os.mkdir)
    - [`os.makedirs(name, mode=0o777, exist_ok=False)`](https://docs.python.org/3/library/os.html#os.makedirs)

- **rename**
    - [`os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)`](https://docs.python.org/3/library/os.html#os.rename)
    - [`os.renames(old, new)`](https://docs.python.org/3/library/os.html#os.renames)

- **remove**
    - [`os.remove(path, *, dir_fd=None)`](https://docs.python.org/3/library/os.html#os.remove)
    - [`os.removedirs(name)`](https://docs.python.org/3/library/os.html#os.removedirs)
    - [`os.rmdir(path, *, dir_fd=None)`](https://docs.python.org/3/library/os.html#os.rmdir)

- [`os.system(command)`](https://docs.python.org/3/library/os.html#os.system)

## Miscellaneous System Information

- [`os.pardir`](https://docs.python.org/3/library/os.html#os.pardir)
