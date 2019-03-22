## What's Anaconda?

Anaconda is a package manager, an environment manager, a Python/R data science distribution, and a collection of over 1,500+ open source packages.

## Anaconda Navigator or conda?

After you install Anaconda or Miniconda, if you prefer a desktop graphical user interface (GUI) then use **Navigator**. If you prefer to use Anaconda prompt (or Terminal on Linux or macOS), then use that and **conda**. You can also switch between them.

## Packages available in Anaconda

- Over 200 packages are automatically installed with Anaconda.

- Over 2000 additional open source packages (including R) can be individually installed from the Anaconda repository with the `conda install` command.

- Thousands of other packages are available from **Anaconda Cloud**.

- You can download other packages using the `pip install` command that is installed with Anaconda. **Pip packages** provide many of the features of **conda packages** and in some cases they can work together. However, the preference should be to install the conda package if it is available.

- You can also make your own custom packages using the `conda build` command, and you can share them with others by uploading them to Anaconda Cloud, PyPi or other repositories.

## Updating from older versions

```
conda update conda
conda update anaconda
```

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
