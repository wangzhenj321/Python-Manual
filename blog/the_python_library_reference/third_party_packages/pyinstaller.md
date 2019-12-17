https://stackoverflow.com/questions/9946760/add-image-to-spec-file-in-pyinstaller

## Installation

```
pip install pyinstaller
```

## Create Executable

```
pyinstaller --onefile <your_script_name>.py
```

> 1. Always pass the option `--onefile`. This option tells PyInstaller to create only one file. Without this option, the libraries will be distributed as seperate files along with the executable file, and then these libraries are necessary while invoking the executable file.
> 
> 2. After running pyinstaller, the folder "build", the folder "dist", and the file "<your_script_name>.spec" will be created, and the executable file is under the folder "dist". 
> 
> 3. "PyInstaller" can only build one python script once time.

## References

1. [Making a Stand Alone Executable from a Python Script using PyInstaller](https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263)
2. [PyInstaller](https://www.pyinstaller.org/)
