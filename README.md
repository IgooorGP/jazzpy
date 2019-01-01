# JazzPy

This software project is a recreation of the first level (Diamondus) of the Jazz Jack Rabbit game developed by Epic MegaGames in 1994.

## Disclaimer

All the sprite sheets, fictional names, images and soundtracks used in this software project were downloaded from the internet
and are, by no means, mine. All the images, character names, stage names, other fictional names and the soundtracks belong
to Epic MegaGames (Epic Games).

## Gameplay Example

![alt-text](/docs/jazz_play.gif)

## Built with

* Python 3.7;
* Pygame 1.9.4;
* Pyinstaller 3.4 for generating the game binary file;
* Tox 3.6.1 as testing automating tool;
* Pytest 4.0.2 as the testing framework;
* Coverage 4.5.2 for testing coverage reports.

## Code Linting

The code base uses the following coding conventions:

* Pep8;
* Pyflakes.

To format the code in a standard way, Black formatter was used. Black is a python code formatter which is a great tool to standardize the code base! It enforces the coding conventions and good practices with Python. You can check more about it in:

https://github.com/ambv/black

## Generating a binary files

Python is an interpreted language and as such all Python source code requires a Python interpreter to be executed. However, in order to generate binary distributions of this software, Pyinstaller (https://pythonhosted.org/PyInstaller/operating-mode.html) was used to analyze all the modules
and packages required by the ```jazz.py``` script (bootstrap python module that runs the game) and copies all these dependencies **plus** the active Python interpreter into a single folder or single executable file.

By doing this, the end users do not need to install a specific vesion of Python. Actually, they don't need to have any Python interpreted 
installed at all.

In order to generate such binary version:

```bash
pyinstaller --onefile jazz.py
```

This will create a ```build``` folder with the build process metadata and a ```dist``` folder which will contain the executable file name
```jazz```.

To run the game using a bash terminal:

```bash
./dist/jazz  # runs the jazz binary file on the dist folder
```

### Binary file and OS version

The binary output of Pyinstaller is, naturally, specific to the OS of the user who's creating the binary and the active version of Python. Hence, to build for another OS, one needs to run Pyinstaller in that specific OS. A little note from the Pyinstaller team is as follows:

```
The output of PyInstaller is specific to the active operating system and the active version of Python. This means that to prepare a distribution for:

* a different OS
* a different version of Python
* a 32-bit or 64-bit OS
you run PyInstaller on that OS, under that version of Python. The Python interpreter that executes PyInstaller is part of the bundle, and it is specific to the OS and the word size.
```

## Getting started with local development

For local development, I highly recommend using a virtual environment for installing and managing the necessary Python packages for the
project. To create a local environment with Python 3.7 as the interpreter version, invoke the python venv as a module:

```bash
python3.7 -m venv .venv  # creates a .venv folder
```

Here, Python3.7 was used to generate a Python 3.7 environment. To install diffenrt python versions, it's recommended to use Pyenv (https://github.com/pyenv/pyenv) to manage different Python versions.

As of now, only Python 3.7 is being supported and tested but this will be expanded to older versions in the future with new tests
with tox. However, testing of older Python 3.x versions is appreciated.

After that, activate the virtual env:

```bash
source .venv/bin/activate  # (.venv) will appear in the bash prompt string indicating the venv is on
```

Now, install the dev requirements with pip:

```bash
pip install -r requirements_dev.txt
```

Finally, run the bootstrap script which uses the jazzpy package to get the main class and instantiate the game:

```bash
python jazz.py
```

## How to test

This project uses Tox (https://tox.readthedocs.io/en/latest/ for test automation and testing under different Python environments. Also,
Coverage (https://coverage.readthedocs.io/en/v4.5.x/) is used to generate reports of the overall testing coverage of the source code.

To execute the tests and get the coverage report, simply run in your virtual environment:

```bash
tox
```

As the rest of the testing process wil be handled by Tox.

## File Summary

```jazz.py```: bootstrap python module used to generate the final binary version of the game and for local development playing;

```jazzpy```: folder with Jazzpy source code;

```jazzpy/main.py```: python module with the main game class to be instantiated to run the game;

```jazzpy/camera.py```: source code of the Camera class used to compute the actual position of the objects in order to centralize the player on the screen;

```jazzpy/levels```: source code of the Level classes use to parse txt files of the stage structure, enemies, etc.

```jazzpy/music```:  folder with the game soundtrack;

```jazzpy/scenes```:  folder with the source code of the Scenes and SceneManager that is used to render the game on the screen and update it;

```jazzpy/sprites```:  folder with the source code of the sprite objects that are used in the gameplay such as Jazz, platforms, enemies, bullets, etc.

```jazzpy/spritesheets```:  folder with the spritesheets (png files download from the internet) that are used to generate the sprite images of the characters, platforms and other miscellania.