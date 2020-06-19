import tictactoe as ttt
import tictactoe

X = "X"
O = "O"
EMPTY = None

board= [[O, EMPTY, EMPTY],
        [X, X, EMPTY],
        [O, EMPTY, EMPTY]]

action= (2,0)

cog= ttt.Node(board, action)