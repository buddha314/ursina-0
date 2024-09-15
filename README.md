# The Sequel to "Ursina Minus One"

## Ursina

I like Ursina because I know Python very well and I'm going to add a bit of AI to my games. Python is the de facto language of AI.

The [Ursina Home Page](https://www.ursinaengine.org/index.html) and [Ursina API Reference](https://www.ursinaengine.org/api_reference.html) are pretty handy.  You'll also want to check out the [Ursina Coordinate System](https://www.ursinaengine.org/coordinate_system.html)

There aren't many Python game engines, but [Panda3D](https://www.panda3d.org/) is pretty sophisticated.  I just don't need that much control right now.

Ursina has an editor, but I haven't used it yet. It's really much more about scripting and simple games than anything else. I like the punk-rock nature of it, honestly.


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

I'm starting by creating basic resources in `crafting\models.py` folder. Right now I can't control the size of the models, so I'm working that up.

## Testing

You should be able to test things with `pytest`, but right now only the crafting system has some tests.  From the room run `pytest` and watch the magic happen.