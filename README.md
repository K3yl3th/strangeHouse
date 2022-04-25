# strangeHouse

Strange House is a puzzle game designed for the command line.
You are stuck in your house, and your goal is to escape by interacting with your environment. To do so, you different commands to perform different actions.

## Dependecies

- [Python 3](https://www.python.org/)
- [Matplotlib](https://matplotlib.org/) (can be installed with pip by using the command `pip install matplotlib`)

## Installation

1. Clone the repository to your local machine, or copy the content of the [strangeHouse.py](https://github.com/MarianneDery/strangeHouse/blob/master/strangeHouse.py) file to a local file with the same name.
2. Open the terminal at the location of the file.
3. Run it with the command `python strangeHouse.py`
4. Enjoy!

## Commands

The commands available in the game are:

- **instructions** : Present this menu
- **go \[direction\]** : Move from one room to another
- **examine \[object\]** : Get more information on an object present in the room <br/> 
**tip**: You could get clues!
- **interact \[object\]** : Interact with an object in the room
- **access \[object\]** : Acces an object within your inventory
- **status**: Tells you which room you are in as well as what your inventory contains
- **description** : Short description of the room you are in
- **leave**: While doing a puzzle, allows you to leave the puzzle and return to the room you were in
- **exit**: Exit the game

**P.S.** The game can't be saved. All progress will be lost if you quit.
