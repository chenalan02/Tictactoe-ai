# Tictactoe-ai
Tictactoe algorithm that picks the most optimal move by analyzing all possible boards 2 moves in the future. Compile Runner.py to run the game

## Logic
Tictactoe can be interpreted as a search problem where we must consider all possible future board positions/nodes to chose an optimal tile to play. This is achieved through the Node class, which is created for all possibles moves that the ai can play. Upon initializing, creates a list of results possible the move after the Node class. The Node class is given a utility score. Each player is given a minimax assigned score of either 1 or -1. The utility score will be 0 unless there is a move in the list of results in which the opponent wins. In this case, the utility score will be the opposite of the minimax assigned score. This node is undesirable and will not likely be chosen(unless it is the only choice or all other nodes will result in a loss as well). If the Code itself is a direct win for the ai, the utility score will be the minimax assigned score and will be chosen by the ai.

## Template
This was an assignment in which I built upon a template from the Harvard CS50 online course.It can be found at https://cs50.harvard.edu/ai/2020/projects/0/tictactoe/

![tictactoe ai](https://github.com/chenalan02/Tictactoe-ai-Harvard-cs50ai/blob/master/tictactoe%20ai.JPG)
