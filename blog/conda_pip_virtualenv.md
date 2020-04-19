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

## Create venv with `conda` and `virtualenv`

```
$ conda create -n dummy python==3.7.3
$ conda list
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
ca-certificates           2020.1.1                      0  
certifi                   2020.4.5.1               py37_0  
libedit                   3.1.20181209         hc058e9b_0  
libffi                    3.2.1                hd88cf55_4  
libgcc-ng                 9.1.0                hdf63c60_0  
libstdcxx-ng              9.1.0                hdf63c60_0  
ncurses                   6.2                  he6710b0_0  
openssl                   1.1.1f               h7b6447c_0  
pip                       20.0.2                   py37_1  
python                    3.7.3                h0371630_0  
readline                  7.0                  h7b6447c_5  
setuptools                46.1.3                   py37_0  
sqlite                    3.31.1               h7b6447c_0  
tk                        8.6.8                hbc83047_0  
wheel                     0.34.2                   py37_0  
xz                        5.2.5                h7b6447c_0  
zlib                      1.2.11               h7b6447c_3  
```

The `dummy` venv created with `conda` seems including too many packages, but almost all of them are dependencies of `python==3.7.3`. In fact, there are only four packages as follows:

```
python                    3.7.3                h0371630_0  
pip                       20.0.2                   py37_1  
setuptools                46.1.3                   py37_0  
wheel                     0.34.2                   py37_0  
```

These default installed packages are same as those installed in the venv created with `virtualenv`.

## Basic commands

### List of basic commands

| Commands | Description |
| --- | --- |
| `create` | Create a new conda environment from a list of specified packages |
| `info` | Display information about current conda install |
| `install` | Installs a list of packages into a specified conda environment |
| `remove` | Remove a list of packages from a specified conda environment |
| `uninstall` | Alias for conda remove |
| `list` | List linked packages in a conda environment |
| `search` | Search for packages and display associated information |
| `update` | Updates conda packages to the latest compatible version |
| `upgrade` | Alias for conda update |
| `env` | - |

### Common usage of basic commands

- `create`
    - `conda create -n dummy python==3.7.3`
    - `conda create -n myenv --file package-list.txt`

- `install`
    - `conda install --file package-list.txt`

- `list`
    - `conda list`
    - `conda list --export > package-list.txt`

- `search`
    - `conda search numpy=1.10.4=py27_1 --info`

- `env`
    - `conda env list`
    - `conda env remove -n FOO`

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
    - `pip install SomePackage`
    - `pip install SomePackage==1.0.4`
    - `pip install 'SomePackage>=1.0.4'`
    - `pip install --upgrade SomePackage`
    - `pip install -r <requirements file>`
    - `pip install --user SomePackage`

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

> `pip` defaults to installing Python packages to a system directory (such as `/usr/local/lib/python3.4`). This requires root access. `--user` makes `pip` install packages in your home directory instead, which doesn't require any special privileges. Typically `~/.local/`, or `%APPDATA%\Python` on Windows.
