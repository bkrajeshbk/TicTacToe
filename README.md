# Information :
This project is implement in python and showcases OOPS concept namely abstraction, encapsulation, inheritznce and exception handling. 

# Direction of Use:
- python -m tictactoe <absolute_path_to_filename>. Please refer #RULES for more details.

# To run Tests:
- python -m unittest discover -s "./tests" <absolute_path_to_tests_folder> -p "test_*.py"

# NOTE: 
Use "py" in place of "python" in above commands for venv 3.10.

# RULES:
Minimum 2 players are required to play a game.
There are 9 slots in a 3X3 format, available to be filled.
The Player1 starts the game and each player will get the chance alternatively.
These slots can be filled vertically, horizontally or diagonally and in any order.
The game ends when:
    1. A player fills 3 consecutive slots with his Symbol, hence with a decisive result : Win/Lose.
    2. There are no more slots to be filled, hence a Draw.

# Problem Statement
Part A: Write a program that lets two players play tic-tac-toe with each other.
Board: The program starts with the empty grid. 
Players: Player one chooses the symbol (options: X and O) she likes to play with. Player two is automatically assigned the other symbol. 
Turn: A player’s turn is completed when she chooses the right slot on the grid. On an invalid input, ask the user to re-enter the correct slot. 
The game ends when there is no more move to make or a player has scored a sequence (3 slots in a row, column or a diagonal). 
Consider this as version v1.0 for your program.

Part B: Modify the program that allows players to play against a computer.
The Player will always go first and the computer will play second. 

Before submitting the code
Think about the following things:
How does your program handle invalid inputs? Are there any memory leaks? Does your program crash?
Have you made any assumptions in the code? Are they documented?
Is your documentation and communication about your code complete?
Can the next developer pick your code and start working with it?
Do you have enough tests? Do they cover your core logic or the whole program?
Do you have git history? Or a changelog?

Note: The problem statement may not define every little thing the program should do. We want you to make reasonable assumptions and be able to discuss those assumptions.
