"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x= 0
    num_o= 0

    for row in range(3):       

        for column in range(3):

            if board[row][column] != EMPTY:

                if board[row][column] == X:
                    num_x +=1

                else:
                    num_o +=1

    if num_x > num_o:
        return O

    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_list= []

    for row in range(3):       

        for column in range(3):

            if board[row][column] == EMPTY:
                
                actions_list.append((row, column))

    return actions_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultant_board= copy.deepcopy(board)
    resultant_board[action[0]][action[1]]= player(board)
    
    return resultant_board
   

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner= None

    x_conseq= 0
    o_conseq= 0

    #scans rows
    for row in range(3):

        #check 3 in a row
        if x_conseq == 3:
            winner = X
        if o_conseq == 3:
            winner = O

        for column in range(3):
            if board[row][column]== X:
                x_conseq +=1
                o_conseq =0
            elif board[row][column]== O: 
                x_conseq =0
                o_conseq +=1
            else:
                x_conseq= 0
                o_conseq= 0
    
    #check 3 in a row
    if x_conseq == 3:
        winner = X
    if o_conseq == 3:
        winner = O

    x_conseq= 0
    o_conseq= 0

    #scans columns
    if winner == None:

        for column in range(3):

            if x_conseq == 3:
                winner = X
            if o_conseq == 3:
                winner = O

            for row in range(3):
                if board[row][column]== X:
                    x_conseq +=1
                    o_conseq =0
                elif board[row][column]== O: 
                    x_conseq =0
                    o_conseq +=1
                else:
                    x_conseq= 0
                    o_conseq= 0

    if x_conseq == 3:
        winner = X
    if o_conseq == 3:
        winner = O

    x_conseq= 0
    o_conseq= 0

    #scans diagonals
    if winner == None:
        for row_column in range(3):
            if board[row_column][row_column]== X:
                x_conseq +=1
                o_conseq =0

            elif board[row_column][row_column]== O: 
                x_conseq =0
                o_conseq +=1
            else:
                x_conseq= 0
                o_conseq= 0

    if x_conseq == 3:
        winner = X
    if o_conseq == 3:
        winner = O

    x_conseq= 0
    o_conseq= 0

    if winner == None:
        column= 2
        for row in range(3):
            if board[row][column]== X:
                x_conseq +=1
                o_conseq =0
            elif board[row][column]== O: 
                x_conseq =0
                o_conseq +=1
            else:
                x_conseq= 0
                o_conseq= 0
            column+=-1

    if x_conseq == 3:
        winner = X
    if o_conseq == 3:
        winner = O
    
    return winner


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    game_over= False

    if winner(board) != None:
        game_over= True
    
    if actions(board) == []:
        game_over= True

    return game_over

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win= winner(board)
    if win == X:
        utility= 1
    elif win == O:
        utility= -1
    else:
        utility= 0

    return utility

class Node():
    def __init__(self, board, action):

        self.player= player(board)
        self.action= action

        #tests if this node is terminal or not and assigns utility value given who won/tied
        if terminal(board) == True:
            if winner(board) == X:
                self.utility= 1
            elif winner(board) == O:
                self.utility= -1
            else:
                self.utility= 0

        else:
            #finds the actions and all results of the board possible after the opponent's turn after this node
            self.results=[]
            self.result_actions= actions(board)
            for result_action in self.result_actions:

                result_instance= result(board, result_action)
                self.results.append(result_instance)
               
            #finds the utility of these resultant
            self.result_utilities=[]
            for result_instance in self.results:
  
                utility_instance= utility(result_instance)
                self.result_utilities.append(utility_instance)

            #assigns utility to this node given the worst case scenario of the resultant boards
            if self.player == O:
                if -1 in self.result_utilities:
                    self.utility= -1
                else:
                    self.utility= 0

            else:
                if 1 in self.result_utilities:
                    self.utility= 1
                else:
                    self.utility= 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    frontier= []
    
    player_turn= player(board)
    actions_list= actions(board)

    #create a list of possible moves/nodes
    for action in actions_list:

        possible_board= result(board, action)
        node= Node(possible_board, action)
        frontier.append(node)
    
    #sorts the frontier in order of utility and returns the optimal action
    if player(board)== X:
        frontier.sort(key=lambda x:x.utility, reverse=True )

    else:
        frontier.sort(key=lambda x:x.utility)

    return frontier[0].action

