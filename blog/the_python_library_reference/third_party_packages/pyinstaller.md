## Installation

```
pip install pyinstaller
```

## Using PyInstaller

The syntax of the `pyinstaller` command is:

```
pyinstaller [options] script [script …] | specfile
```

In the most simple case, set the current directory to the location of your program `myscript.py` and execute:

```
pyinstaller myscript.py
```

PyInstaller analyzes `myscript.py` and:

- Writes `myscript.spec` in the same folder as the script.
- Creates a folder `build` in the same folder as the script if it does not exist.
- Writes some log files and working files in the `build` folder.
- Creates a folder `dist` in the same folder as the script if it does not exist.
- Writes the `myscript` executable folder in the `dist` folder.

Normally you name one script on the command line. If you name more, all are analyzed and included in the output. However, the first script named supplies the name for the spec file and for the executable folder or file. Its code is the first to execute at run-time.

> **`spec` file created with `--onefile` option:**
> 
> ```
> # -*- mode: python ; coding: utf-8 -*-
> 
> block_cipher = None
> 
> 
> a = Analysis(['main.py'],
>              pathex=['C:\\Users\\wangzhenj321\\Downloads\\GluoncvUtility'],
>              binaries=[],
>              datas=[],
>              hiddenimports=[],
>              hookspath=[],
>              runtime_hooks=[],
>              excludes=[],
>              win_no_prefer_redirects=False,
>              win_private_assemblies=False,
>              cipher=block_cipher,
>              noarchive=False)
> pyz = PYZ(a.pure, a.zipped_data,
>              cipher=block_cipher)
> exe = EXE(pyz,
>           a.scripts,
>           a.binaries,
>           a.zipfiles,
>           a.datas,
>           [],
>           name='main',
>           debug=False,
>           bootloader_ignore_signals=False,
>           strip=False,
>           upx=True,
>           upx_exclude=[],
>           runtime_tmpdir=None,
>           console=True )
> ```
> 
> **`spec` file created with `--onedir` option:**
> 
> ```
> # -*- mode: python ; coding: utf-8 -*-
> 
> block_cipher = None
> 
> 
> a = Analysis(['main.py'],
>              pathex=['C:\\Users\\wangzhenj321\\Downloads\\GluoncvUtility'],
>              binaries=[],
>              datas=[],
>              hiddenimports=[],
>              hookspath=[],
>              runtime_hooks=[],
>              excludes=[],
>              win_no_prefer_redirects=False,
>              win_private_assemblies=False,
>              cipher=block_cipher,
>              noarchive=False)
> pyz = PYZ(a.pure, a.zipped_data,
>              cipher=block_cipher)
> exe = EXE(pyz,
>           a.scripts,
>           [],
>           exclude_binaries=True,
>           name='main',
>           debug=False,
>           bootloader_ignore_signals=False,
>           strip=False,
>           upx=True,
>           console=True )
> coll = COLLECT(exe,
>                a.binaries,
>                a.zipfiles,
>                a.datas,
>                strip=False,
>                upx=True,
>                upx_exclude=[],
>                name='main')
> ```

### Options

- `--clean`
    Clean PyInstaller cache and remove temporary files before building.

- `-D, --onedir`
    Create a one-folder bundle containing an executable (default)

- `-F, --onefile`
    Create a one-file bundled executable.

- `-n NAME, --name NAME`
    Name to assign to the bundled app and spec file (default: first script’s basename)

## Using Spec Files

There are four cases where it is useful to modify the spec file:

- When you want to bundle data files with the app.
- When you want to include run-time libraries (`.dll` or `.so` files) that PyInstaller does not know about from any other source.
- When you want to add Python run-time options to the executable.
- When you want to create a multiprogram bundle with merged common modules.

### Adding Data Files

```
a = Analysis(...
     datas= [ ('/mygame/sfx/*.mp3', 'sfx' ) ],
     ...
     )
```

## Q & A

1. https://stackoverflow.com/questions/9946760/add-image-to-spec-file-in-pyinstaller
2. https://stackoverflow.com/questions/44681356/reduce-pyinstaller-executable-size
3. https://stackoverflow.com/questions/48629486/how-can-i-create-the-minimum-size-executable-with-pyinstaller
4. https://stackoverflow.com/questions/43886822/pyinstaller-with-pandas-creates-over-500-mb-exe
5. https://stackoverflow.com/questions/47692213/reducing-size-of-pyinstaller-exe

## References

1. [Making a Stand Alone Executable from a Python Script using PyInstaller](https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263)
2. [PyInstaller](https://www.pyinstaller.org/)
