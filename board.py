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

    def getPlayerMask(self, player):

        if player == WHITE:
            pieces = self.whitePlayer.pieceState
        else:
            pieces = self.blackPlayer.pieceState

        mask = (
                pieces[PAWN]   |
                pieces[ROOK]   |
                pieces[KNIGHT] | 
                pieces[BISHOP] | 
                pieces[QUEEN]  |
                pieces[KING]
        )

        return mask

    def getLegalMoves(self, player):
        legalMoves = {
            PAWN:   {},
            ROOK:   {},
            KNIGHT: {},
            BISHOP: {},
            QUEEN:  {},
            KING:   {}
        }

        if player == WHITE:
            enemyMask = self.getPlayerMask(BLACK)
            playerMask = self.getPlayerMask(WHITE)
            playerPieceState = self.whitePlayer.pieceState

        elif player == BLACK:
            enemyMask = self.getPlayerMask(WHITE)
            playerMask = self.getPlayerMask(BLACK)
            playerPieceState = self.blackPlayer.pieceState

        for i, bit in enumerate(playerPieceState[PAWN]):
            if bit == 1:
                moves = []
                # Straight
                if enemyMask[i+8] == 0:
                    moves.append(i+8)
                if enemyMask[i+16] == 0 and i < 16:
                    moves.append(i+16)
                # Diagonal
                if enemyMask[i+7] == 1:
                    moves.append(i+7)
                if enemyMask[i+9] == 1:
                    moves.append(i+9)
                legalMoves[PAWN][i] = moves

        for i, bit in enumerate(playerPieceState[ROOK]):

            if bit == 1:
                moves = []
                rightBlocked = False
                leftBlocked = False
                upBlocked = False
                downBlocked = False

                #right
                for j in range(1, 9):

                    rightPos = i + j
                    leftPos = i - j
                    upPos = i + (8 * j)
                    downPos = i - (8 * j)
                    
                    if (not rightBlocked and
                        rightPos % 8 > i and
                        playerMask[rightPos] == 0):

                        moves.append(rightPos)
                        if enemyMask[rightPos] == 1:
                            rightBlocked = True
                    else:
                        rightBlocked = True

                    if (not leftBlocked and
                        leftPos & 8 < i and
                        playerMask[leftPos] == 0):

                        moves.append(leftPos)
                        if enemyMask[leftPos] == 1:
                            leftBlocked = True
                    else:
                        leftBlocked = True

                    if (not upBlocked and 
                        upPos < 64 and 
                        playerMask[upPos] == 0):

                        moves.append(upPos)
                        if enemyMask[upPos] == 1:
                            upBlocked = True
                    else:
                        upBlocked = True

                    if (not downBlocked and
                        downPos >= 0 and
                        playerMask[downPos] == 0):

                        moves.append(downPos)
                        if enemyMask[downPos] == 1:
                            downBlocked == True
                    else:
                        downBlocked == True

                legalMoves[ROOK][i] = moves
                

        print(legalMoves)
