## 12.1 Introduction

Different applications can then use different virtual environments.

## 12.2 Creating Virtual Environments

The module used to create and manage virtual environments is called `venv`.

```python
python3 -m venv tutorial-env
```

This will create the `tutorial-env` directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter, the standard library, and various supporting files.

```
mkdir myproject
cd myproject/
virtualenv --no-site-packages venv-test1
source venv-test1/bin/activate
deactivate
```

## 12.3 Managing Packages with pip

```
pip search astronomy
pip install novas
pip install requests==2.6.0
pip install --upgrade requests
```

`pip uninstall` followed by one or more package names will remove the packages from the virtual environment.

`pip show` will display information about a particular package.

`pip list` will display all of the packages installed in the virtual environment.

`pip freeze` will produce a similar list of the installed packages, but the output uses the format that `pip install` expects. A common convention is to put this list in a `requirements.txt` file.

```
pip freeze > requirements.txt
```

Users can then install all the necessary packages with `install -r`.

```
pip install -r requirements.txt
```
