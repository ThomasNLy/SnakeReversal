# SnakeReversal
 The classic snake game but with time travelling
## Introduction
This project was something I made for fun as I wanted to test my knowledge of Data Structures such as Linked Lists and 
Stacks. It's a recreation of the classic snake game but with additional features added on such as lives and the ability
to reverse time.

[![Static Badge](https://img.shields.io/badge/python-3.10%2B-blue?link=https%3A%2F%2Fwww.python.org%2Fdownloads%2Frelease%2Fpython-3107%2F)](https://www.python.org/downloads/release/python-3107)
[![dependency - pygame](https://img.shields.io/badge/dependency-pygame-blue?logo=pygame&logoColor=white)](https://pypi.org/project/pygame)

- [How to run the game/project](#how-to-run-the-gameproject)
- [How to play the Game](#how-to-play-the-game)
  - [Controls](#controls)
  - [Lives and Game Over](#lives-and-game-over)
  - [Rewinding Time](#rewinding-time)
  - [Collecting Apples](#collecting-apples)


## How to run the game/project
1. Download the Zip file and extract all files or clone the repository using Git Bash Command Line and type the following command 
`git clone https://github.com/ThomasNLy/SnakeReversal.git`
2. Download and install python and follow the instructions of the installation wizard: 
[Python download link](https://www.python.org/downloads/)

3. Along with that download and install a code editor capable of opening python files(.py extensions)
- VS Code [Link to download](https://code.visualstudio.com/download)
- PyCharm [Link to download](https://www.jetbrains.com/pycharm/download/?section=windows)

4. After you will want to open up the project in the code editor of your choice and set up pygame library along with a virtual environment
### PyCharm
create a virtual environment in pycharm by navigating to settings -> project -> python interpreter and 
selecting Add Interpreter -> local Interpreter
in the next window select virtualenv Environment then click ok.
Official Instructions from PyCharm are linked here: [Set up Virtual Env Instructions](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#python_create_virtual_env)

After that you will want to set up the project to include the pygame library to run it
by navigating back to settings -> project -> python interpreter from there follow the instructions on PyCharm's website to install packages under **Manage packages in Python interpreter settings** 

[Package Installation Instructions](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html#interpreter-settings)
 
### VS Code
make sure for VS code you have the python extension installed into the editor to have the editor support python. After you will want to create a virtual environment in the project by 
following the instructions listed on VS Codes Web page.

[VS Code Creating a Virtual Environment](https://code.visualstudio.com/docs/python/environments)

After you will want to setup and install the pygame library to the virtual environment by opening the terminal in VS Code and typing 
`pip install pygame`.

5. Run the `main.py` file and you can start playing the game

## How to play the Game
### Controls
To control the snake use the **WASD** to move the snake in the respective directions and collect apples to gain points and have the snake grow.

### Lives and Game Over
Lives are indicated by the number of hearts, whenever the snake's head crosses over it's own body the player will
lose 1 life along with the snake reducing in size. Along with that the player will gain a 5 point reduction as a penalty.

![life bar.png](https://github.com/ThomasNLy/SnakeReversal/blob/main/Doc%20Imgs/life%20bar.png)

A **Game Over** state can occur if the player were to lose all their lives or if the head of the snake were to touch any of the
four walls in the level.


![walls.png](https://github.com/ThomasNLy/SnakeReversal/blob/main/Doc%20Imgs/walls.png)
### Restarting the Game after a Game Over
pressing the **ENTER/RETURN** key on the keyboard will restart the game.
### Rewinding Time
The player can rewind time up to the 5 most recent moments by pressing the **SPACE BAR** on the keyboard. The number of 
moments the player can rewind time is indicated by the dots in the UI, each dot represents the number of moments recorded
so far the player can rewind too.
The number of times the player can rewind is indicated by the **REWIND counter** in the UI. A rewind points is consumed
when the player decides a moment in time to continue from by moving the snake using the **WASD** keys

![Moments recorded.png](https://github.com/ThomasNLy/SnakeReversal/blob/main/Doc%20Imgs/rewind%20time%20moment%20recorded.png)

This feature can be helpful if the player almost run straight into any of the walls avoiding an instant game over. It can also be
used to have the player revert to an earlier time before any point penalties were to occur. The number of **lives** however 
are not affected when rewinding time.

### Collecting apples
The objective of the game is for the player to collect the apple that will randomly spawn in different locations in the level.
Whenever the player collides with the apple, the snake will grow longer and the player will gain a point in doing so.
![colelcting apples.gif](https://github.com/ThomasNLy/SnakeReversal/blob/main/Doc%20Imgs/collecting%20apples.gif)




