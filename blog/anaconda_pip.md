# Anaconda

## What's Anaconda?

Anaconda is a package manager, an environment manager, a Python/R data science distribution, and a collection of over 1,500+ open source packages.

## Anaconda Navigator or conda?

After you install Anaconda or Miniconda, if you prefer a desktop graphical user interface (GUI) then use **Navigator**. If you prefer to use Anaconda prompt (or Terminal on Linux or macOS), then use that and **conda**. You can also switch between them.

## Uninstalling Anaconda

1. Option A. Use simple remove to uninstall Anaconda:

    Open the terminal application, and then remove your entire Anaconda directory, which has a name such as anaconda2 or anaconda3, by entering `rm -rf ~/anaconda3`.

2. Option B. Full uninstall using Anaconda-Clean and simple remove.

    > Anaconda-Clean must be run before simple remove.
    
    ```
    conda install anaconda-clean
    anaconda-clean
    ```
    
    After using Anaconda-Clean, follow the instructions above in Option A to uninstall Anaconda.

# conda

## Conda directory structure

- `ROOT_DIR`

    The directory that Anaconda or Miniconda was installed into.

- `/pkgs`

    Also referred to as `PKGS_DIR`. **This directory contains decompressed packages, ready to be linked in conda environments.** Each package resides in a subdirectory corresponding to its canonical name.
    
    Example: `matplotlib`
    
    - the `matplotlib` package in `/pkgs`
        - `pkgs/matplotlib-3.1.0-py37h54f8f79_0.tar.bz2`
        - `pkgs/matplotlib-3.1.0-py37h54f8f79_0`
    
    - the decompressed `matplotlib` package in `/pkgs`
        - `pkgs/matplotlib-3.1.0-py37h54f8f79_0/lib/python3.7/site-packages/matplotlib`
    
    - the linked `matplotlib` package in conda environments
        - `envs/dummy/lib/python3.7/site-packages/matplotlib`

- `/envs`

    The system location for additional conda environments to be created.

---

The following subdirectories comprise the default Anaconda environment. Other conda environments usually contain the same subdirectories as the default environment.

- `/bin`
- `/include`
- `/lib`
- `/share`

## Error of `conda activate` on Windows

The usage of `conda activate python36` on Windows results in the following error:

```
CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
```

The solution to this error is to run the following two commands on terminal. It's better to write them into `.bash_profile` or `.bashrc` file.

```
source activate
source deactivate
```

## conda or pip?

> Having been involved in the python world for so long, we are all aware of pip, easy_install, and virtualenv, but these tools did not meet all of our specific requirements. The main problem is that they are focused around Python, neglecting non-Python library dependencies, such as HDF5, MKL, LLVM, etc., which do not have a setup.py in their source code and also do not install files into Python’s site-packages directory.

So Conda is a packaging tool and installer that aims to do more than what pip does; handle library dependencies outside of the Python packages as well as the Python packages themselves. Conda also creates a virtual environment, like `virtualenv` does.

Because Conda introduces a new packaging format, you cannot use pip and Conda interchangeably; pip cannot install the Conda package format. **You can use the two tools side by side (by installing pip with conda install pip) but they do not interoperate either.**

# pip

## Basic commands

### List of basic commands

| Commands | Description |
| --- | --- |
| `install` | Install packages |
| `uninstall` | Uninstall packages |
| `freeze` | Output installed packages in requirements format |
| `list` | List installed packages |
| `show` | Show information about installed packages |
| `search` | Search PyPI for packages |

### Common usage of basic commands

- `install`
    - `pip install SomePackage            # latest version`
    - `pip install SomePackage==1.0.4     # specific version`
    - `pip install 'SomePackage>=1.0.4'   # minimum version`
    - `pip install --upgrade SomePackage`
    - `pip install -r <requirements file>`

- `uninstall`
    - `pip uninstall simplejson`

- `freeze`
    - `pip freeze > requirements.txt`

- `list`
    - `pip list -v`
    - `pip list --outdated`

- `show`
    - `pip show sphinx`

- `search`
    - `pip search peppercorn`
