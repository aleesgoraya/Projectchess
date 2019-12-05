## Chess
The two player board game recreated using pygame and python

## Index
- [Installation](https://github.com/aleesgoraya/Projectchess#installation)
- [Why our Chess Game is Unique](https://github.com/aleesgoraya/Projectchess#why-our-chess-game-is-unique)
- [How To Play](https://github.com/aleesgoraya/Projectchess#how-to-play)
- [Extending our Game](https://github.com/aleesgoraya/Projectchess#extending-our-game)
- [Documentation](https://github.com/aleesgoraya/Projectchess#documentation)
- [Developers](https://github.com/aleesgoraya/Projectchess#developers)
- [Contibutions](https://github.com/aleesgoraya/Projectchess#contributions)
- [License Information](https://github.com/aleesgoraya/Projectchess#license-information)



## Installation
To Download and install our Chess Game follow these steps:

1.) Open the CMD and change into the directory that you would like to download our chess game in 
and execute the command: "git clone https://github.com/aleesgoraya/Projectchess.git"

<img src="https://raw.githubusercontent.com/aleesgoraya/Projectchess/master/images/install1.PNG"/>

2.) You will now have a copy of the repo. Now executed the command:
"pip install pyinstaller". This will give you the required installer 
to create a .exe file for our Chess game. 

<img src="https://raw.githubusercontent.com/aleesgoraya/Projectchess/master/images/insta.png"/>

3.) Change Directories to the class containing the View.py folder which should be in  
Source/View and execute the command: "pyinstaller --onefile View.py". this will create 
the View.exe file required to play our game.

<img src="https://raw.githubusercontent.com/aleesgoraya/Projectchess/master/images/install2.PNG"/>

4.) Open a file exploerer and go to the Source/View directory, you will see a couple of 
files have been created. Go into the dist folder and your View.exe file will be in there. 
<img src="https://raw.githubusercontent.com/aleesgoraya/Projectchess/master/images/install3.PNG"/>

<img src="https://raw.githubusercontent.com/aleesgoraya/Projectchess/master/images/install4.PNG"/>

## Why our Chess Game is Unique
<img src="https://raw.githubusercontent.com/aleesgoraya/Projectchess/master/images/chessboard.PNG" width="350" height="350"/> <img src="https://raw.githubusercontent.com/aleesgoraya/Projectchess/master/images/compchess.png" width="350" height="350"/>
- Colorful randomized chessboard.
- New rules! If a player makes a move that is not possible, e.g attempts to move a rook diagnolly;  The player loses the game.

## How To Play
<img src="https://raw.githubusercontent.com/aleesgoraya/Projectchess/master/images/chessboard.PNG" width="350" height="350"/>

We have simplified the interface for you

1.) Press restart to reset the board and play a new game.

2.) Press quit to close the application

This is not your traditional chess game.

The controls are simple.

1.) Use your mouse to click on the piece you want to move.

2.) After selecting your piece, click on the square you want to move to. Simple right!

However, if you make and invalid move(click on a square where a move cannot be made) you lose!


## Extending our Game

To ensure our game follows the path wanted by the community, we decided to make our game easily extendable. To do this, our entire repository is public. This will allow you to copy any files and make the desired modifications. We hope with the help of the community, we can make our chess game a unique and fun spinoff of the classic chess game. 


## Documentation

* The `Chess` class contains the game logic
  * The `move` method will move the pieces to `row`, `col`
  * The `has_check` checks if the player is in check or not
  * The `change_turn` will switch the turn to the player who moves next
  * The `is_game_over` checks if the game is over by checking if any player is in checkmate
  * The `get_piece` returns the chess piece at the given position
  * The `get_current_turn` returns the current turn of the chess game
  * The `get_winner` returns the winner of the chess game

* The `ChessPiece` class contains methods for all the chess pieces
  * The `move` method changes the `self._position` to the given position
  * The `get_color` returns the color of the piece (either black or white)
  * The `get_position` returns the position of the piece
  * The `get_valid_coordinates` is an **_abstract_** method that will be implemented differently by different chess pieces; it returns a list of valid moves of the piece
  * The `check_move` returns true if and only if there is another piece on the way that this piece is going

* The `Chessboard` class contains methods for moving pieces, checking turns, and checking winners etc.
  * The `move` returns true if and only if the move is successfully made.
  * The `has_check` returns true if and only if the `player`'s king is in check
  * The `get` returns the chess piece with given `row` and `col`
  
 * The `View` class contains methods for initializing the GUI
   * The `create_board` creates a board and two buttons as a GUI for players
   * The `add_pieces` adds all the chess pieces with corresponding pictures to the screen 
   * The `main` runs the pygame application
   * The `next_color` returns 3 random integers that are used for generating colors
  
## Contributions

I, Alees Ahmad Goraya, worked on four classes. The classes are Rook, Knight, Bishop, and View class. I helped my fellow group members and wrote how to play section in readme file.

I, Michael Wong, worked on the Chess class as well as the Chessboard class and wrote the Installation section of the README.md file. I also assisted my members with planning.

## License Information
GNU GENERAL PUBLIC LICENSE
      Version 3, 29 June 2007
     Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
