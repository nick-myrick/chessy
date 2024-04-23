from bitstring import Bits, BitArray, BitStream, pack

from constants import *

class Pieces:
    def __init__(self, playerColor, pieceState):
        self.playerColor = playerColor
        self.pieceState = pieceState
    
    #def getMoves(player):

'''
Classic piece configuration for white and black players
'''
class ClassicPieces(Pieces):
    def __init__(self, playerColor):
        if playerColor == WHITE:
            pieceState = {
                PAWN:   BitArray(bin="0000000011111111000000000000000000000000000000000000000000000000"),
                ROOK:   BitArray(bin="1000000100000000000000000000000000000000000000000000000000000000"),
                KNIGHT: BitArray(bin="0100001000000000000000000000000000000000000000000000000000000000"),
                BISHOP: BitArray(bin="0010010000000000000000000000000000000000000000000000000000000000"),
                QUEEN:  BitArray(bin="0001000000000000000000000000000000000000000000000000000000000000"),
                KING:   BitArray(bin="0000100000000000000000000000000000000000000000000000000000000000")
            }

        elif playerColor == BLACK:
            pieceState = {
                PAWN:   BitArray(bin="0000000000000000000000000000000000000000000000001111111100000000"),
                ROOK:   BitArray(bin="0000000000000000000000000000000000000000000000000000000010000001"),
                KNIGHT: BitArray(bin="0000000000000000000000000000000000000000000000000000000001000010"),
                BISHOP: BitArray(bin="0000000000000000000000000000000000000000000000000000000000100100"),
                QUEEN:  BitArray(bin="0000000000000000000000000000000000000000000000000000000000010000"),
                KING:   BitArray(bin="0000000000000000000000000000000000000000000000000000000000001000")
            }

        super().__init__(playerColor, pieceState)
