# Playground Express Projects

Some of my projects with the Adafruit Playground Express

## Set up

Clone the repository, create a virtual environment and install the dependencies

```bash
git clone git@github.com:mmartinortiz/playground-express-projects.git
cd playground-express-projects
python3 -m venv venv
pip install --upgrade pip
pip install -r requirements.txt
```

**Note**: On Ubuntu 20.04, if you have an error when installing PyGame, install these dependencies:

```bash
sudo apt install -y libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libportmidi-dev
```

Get the last release of [CircuitPython](https://circuitpython.org/board/circuitplayground_express/) and install it following [Adafruit's instructions](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart).

Open `mu-editor` from the command line once the Playground Express is connected to the comptuter, and copy the code of any of the projects into the `code.py` file of the Mu Editor.

- [Random led colours](./random-led-colours)
- [Coloured acceleration](./coloured-acceleration)

## Projects

- [Coloured acceleration](./coloured-acceleration/Readme.md)
- [Cool IronMan](./cool-ironman/Readme.md)
- [Random Led colours](./random-led-colours/Readme.md)
