Problem 16: [Hard] Tic-Tac-Toe!

Write a Python program to implement a two-player Tic-Tac-Toe game. The game should display the Tic-Tac-Toe board, prompt players for their moves, and announce the winner or declare a tie when the game is over.

Requirements:

1- The game should be played on a 3x3 grid.
2- Players should take turns entering their moves ("X" for player 1 and "O" for player 2).
3- The program should check for valid moves and handle invalid inputs gracefully.
4- The game should announce the winner or declare a tie when there are three of the same symbol in a row, column, or diagonal.
5- Display the updated board after each move.

Example Output:
```
Welcome to Tic-Tac-Toe!

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

Player 1 (X), enter your move (1-9): 5

 1 | 2 | 3
-----------
 4 | X | 6
-----------
 7 | 8 | 9

Player 2 (O), enter your move (1-9): 2

 1 | O | 3
-----------
 4 | X | 6
-----------
 7 | 8 | 9

...

Player 1 (X), enter your move (1-9): 9

 1 | O | 3
-----------
 4 | X | 6
-----------
 7 | 8 | X

Player 1 (X) wins! Congratulations!
```