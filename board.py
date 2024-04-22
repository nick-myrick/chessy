import numpy as np
from bitstring import Bits, BitArray, BitStream, pack

from constants import *

class Board:
    def __init__(self, width, height):
        # Board fundamentals: has a n x m 
        board_width = width
        board_height = height

'''
Classic 8x8 board configuration for White and Black piece sets
'''
class ClassicBoard(Board):
    def __init__(self, whitePieces, blackPieces):

        self.whitePlayer = whitePieces
        self.blackPlayer = blackPieces
        board_width = 8
        board_height = 8
        super().__init__(board_width, board_height)
    
    def whiteState(self):
        return whiteState

    #def displayBoardState(self):

    def getLegalMoves(self, player):
        legalMoves = {
            "pawns":   [],
            "rooks":   [],
            "knights": [],
            "bishops": [],
            "queen":   [],
            "king":    []
        }

        # Pawns
        if player == WHITE:
            pawnState = self.whiteState["pawns"]
        elif player == BLACK:
            pawnState = self.blackState["pawns"]
