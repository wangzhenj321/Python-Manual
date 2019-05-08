## Files and Directories

> On some Unix platforms, many of these functions support one or more of these features:
> 
> - specifying a file descriptor
> - paths relative to directory descriptors
> - not following symlinks

- `os.chdir(path)`

    Change the current working directory to path.

- `os.getcwd()`

    Return a string representing the current working directory.

- `os.listdir(path='.')`

    Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order, and does not include the special entries `'.'` and `'..'` even if they are present in the directory.

- `os.mkdir(path, mode=0o777, *, dir_fd=None)`

    Create a directory named path with numeric mode mode. If the directory already exists, `FileExistsError` is raised.

- `os.makedirs(name, mode=0o777, exist_ok=False)`

    Recursive directory creation function. Like `mkdir()`, but makes all intermediate-level directories needed to contain the leaf directory.

- `os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)`

    Rename the file or directory src to dst.
