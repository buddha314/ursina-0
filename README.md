# The Sequel to "Ursina Minus One"

## Virtual Environments

You can use either a python virtual environment or the docker image I included. The Docker image takes a bit more work, so start with the Python environment.

First, get [Python 3+](https://www.python.org/downloads/windows/) on your windows machine.  Then you'll need to [install Pip](https://pip.pypa.io/en/stable/installation/) as well.

Now create a virtual environment. From a terminal, do into the directory where you checked out the code.  Then try

```
python -m venv .env
```

You only need to do this the first time. You will re-use the virtual environment.

This will take a second, but it will create a directory called `.env` right there.  I something use `.wenv` when I'm going to use a Windows environment.  Now you need to activate that environment with

```
.\.env\Scripts\activate
```
on Windows.

Okay, in the new venv, you need to install the requirements. It's customary to put these in a file called `requirements.txt`.  So just do

```
pip install -r requirements.txt
```

and it will download several packages.  You only need to run this again when the requirements file has been updated.

## Crafting System

I'm only to the point where I'm bulding out the resources.  Most of the system is in the `crafting` package.  To see where we are, try out

```
python crafting_main.py
```