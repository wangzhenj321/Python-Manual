## Files and Directories

> On some Unix platforms, many of these functions support one or more of these features:
> 
> - specifying a file descriptor
> - paths relative to directory descriptors
> - not following symlinks

- `os.chdir`

    Change the current working directory to path.

- `os.getcwd`

    Return a string representing the current working directory.

- `os.listdir`

    Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order, and does not include the special entries `'.'` and `'..'` even if they are present in the directory.

- `os.rename`

    Rename the file or directory src to dst.
