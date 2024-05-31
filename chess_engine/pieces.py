from bitstring import Bits, BitArray, BitStream, pack

from constants import *

class Pieces:
    def __init__(self, playerColor, pieceState):
        self.playerColor = playerColor
        self.pieceState = pieceState

'''
Classic piece configuration for white and black players
'''
class ClassicPieces(Pieces):
    def __init__(self, playerColor):
        if playerColor == WHITE:
            pieceState = {
                PAWN: BitArray(bin="""00000000
                                      11111111
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000"""),
                
                ROOK: BitArray(bin="""10000001
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000"""),

                KNIGHT: BitArray(bin="""01000010
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000"""),

                BISHOP: BitArray(bin="""00100100
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000"""),

                QUEEN: BitArray(bin="""00010000
                                       00000000
                                       00000000
                                       00000000
                                       00000000
                                       00000000
                                       00000000
                                       00000000"""),

                KING: BitArray(bin="""00001000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000"""),
            }

        elif playerColor == BLACK:
            pieceState = {
                PAWN: BitArray(bin="""00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      11111111
                                      00000000"""),
                
                ROOK: BitArray(bin="""
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      10000001"""),

                KNIGHT: BitArray(bin="""00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        01000010"""),

                BISHOP: BitArray(bin="""00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        00000000
                                        00100100"""),

                QUEEN: BitArray(bin="""00000000
                                       00000000
                                       00000000
                                       00000000
                                       00000000
                                       00000000
                                       00000000
                                       00010000"""),

                KING: BitArray(bin="""00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00000000
                                      00001000"""),

            }
        super().__init__(playerColor, pieceState)
