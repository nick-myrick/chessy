import numpy as np
import time
from bitstring import Bits, BitArray, BitStream, pack

from constants import *

class Board:
    def __init__(self, width, height, whitePieces, blackPieces):
        # Board fundamental requirements: has n rows, m columns, and at least two players
        board_width = width
        board_height = height
        self.whitePlayer = whitePieces
        self.blackPlayer = blackPieces
        self.bitBoards = self.generateBitBoards()

    def generateBitBoards(self):
        start = time.time()
        whitePawnBoards, blackPawnBoards = [],[]
        rookBoards, knightBoards, bishopBoards, queenBoards, kingBoards = [],[],[],[],[]

        for i in range(64):
            whitePawn, blackPawn, rook, knight, bishop, queen, king = "0" * 64,"0" * 64,"0" * 64,"0" * 64,"0" * 64,"0" * 64,"0" * 64,

            # TODO: make extensible to any n x m board
            # Pawns
            if i > 7 and i < 55:
                # White
                if ((i + 7) % 8) < (i % 8):
                    whitePawn = whitePawn[:i + 7] + '1' + whitePawn[i + 7 + 1:]
                if ((i + 9) % 8) > (i % 8):
                    whitePawn = whitePawn[:i + 9] + '1' + whitePawn[i + 9 + 1:]
                if i + 8 < 64:
                    whitePawn = whitePawn[:i + 8] + '1' + whitePawn[i + 8 + 1:]
                if i < 16:
                    whitePawn = whitePawn[:i + 16] + '1' + whitePawn[i + 16 + 1:]
            if i < 56 and i > 7:
                # Black
                if ((i - 7) % 8) > (i % 8):
                    blackPawn = blackPawn[:i - 7] + '1' + blackPawn[i - 7 + 1:]
                if ((i - 9) % 8) < (i % 8):
                    blackPawn = blackPawn[:i - 9] + '1' + blackPawn[i - 9 + 1:]
                if i - 8 >= 0:
                    blackPawn = blackPawn[:i - 8] + '1' + blackPawn[i - 8 + 1:]
                if i > 47:
                    blackPawn = blackPawn[:i - 16] + '1' + blackPawn[i - 16 + 1:]

            # Knights
            if ((i + 6) % 8) < (i % 8) and (i + 6) < 64:
                knight = knight[:i + 6] + '1' + knight[i + 6 + 1:]
            if ((i - 6) % 8) > (i % 8) and (i - 6) >= 0:
                knight = knight[:i - 6] + '1' + knight[i - 6 + 1:]

            if ((i + 10) % 8) > (i % 8) and (i + 10) < 64:
                knight = knight[:i + 10] + '1' + knight[i + 10 + 1:]
            if ((i - 10) % 8) < (i % 8) and (i - 10) >= 0:
                knight = knight[:i - 10] + '1' + knight[i - 10 + 1:]

            if ((i + 15) % 8) < (i % 8) and (i + 15) < 64:
                knight = knight[:i + 15] + '1' + knight[i + 15 + 1:]
            if ((i - 15) % 8) > (i % 8) and (i - 15) >= 0:
                knight = knight[:i - 15] + '1' + knight[i - 15 + 1:]

            if ((i + 17) % 8) > (i % 8) and (i + 17) < 64:
                knight = knight[:i + 17] + '1' + knight[i + 17 + 1:]
            if ((i - 17) % 8) < (i % 8) and (i - 17) >= 0:
                knight = knight[:i - 17] + '1' + knight[i - 17 + 1:]

            # King
            if ((i + 1) % 8) > (i % 8) and (i + 1) < 64:
                king = king[:i + 1] + '1' + king[i + 1 + 1:]
            if ((i - 1) % 8) < (i % 8) and (i - 1) >= 0:
                king = king[:i - 1] + '1' + king[i - 1 + 1:]
            if (i + 8) < 64 and (i + 8) < 64:
                king = king[:i + 8] + '1' + king[i + 8 + 1:]
            if (i - 8) >= 0 and (i - 8) >= 0:
                king = king[:i - 8] + '1' + king[i - 8 + 1:]
            if ((i + 7) % 8) < (i % 8) and (i + 7) < 64:
                king = king[:i + 7] + '1' + king[i + 7 + 1:]
            if ((i - 7) % 8) > (i % 8) and (i - 7) >= 0:
                king = king[:i - 7] + '1' + king[i - 7 + 1:]
            if ((i + 9) % 8) > (i % 8) and (i + 9) < 64:
                king = king[:i + 9] + '1' + king[i + 9 + 1:]
            if ((i - 9) % 8) < (i % 8) and (i - 9) >= 0:
                king = king[:i - 9] + '1' + king[i - 9 + 1:]

            # Sliders
            for j in range(1, 9):
                if ((i + j) % 8) > (i % 8) and (i + j) < 64:
                    rook = rook[:i + j] + '1' + rook[i + j + 1:]
                    queen = queen[:i + j] + '1' + queen[i + j + 1:]
                if ((i - j) % 8) < (i % 8) and (i - j) >= 0:
                    rook = rook[:i - j] + '1' + rook[i - j + 1:]
                    queen = queen[:i - j] + '1' + queen[i - j + 1:]
                if (i + j * 8) < 64:
                    rook = rook[:i + j * 8] + '1' + rook[i + j * 8 + 1:]
                    queen = queen[:i + j * 8] + '1' + queen[i + j * 8 + 1:]
                if (i - j * 8) >= 0:
                    rook = rook[:i - j * 8] + '1' + rook[i - j * 8 + 1:]
                    queen = queen[:i - j * 8] + '1' + queen[i - j * 8 + 1:]

                if ((i + j * 7) % 8) < (i % 8) and (i + j * 7) < 64:
                    bishop = bishop[:i + j * 7] + '1' + bishop[i + j * 7 + 1:]
                    queen = queen[:i + j * 7] + '1' + queen[i + j * 7 + 1:]
                if ((i + j * 9) % 8) > (i % 8) and (i + j * 9) < 64:
                    bishop = bishop[:i + j * 9] + '1' + bishop[i + j * 9 + 1:]
                    queen = queen[:i + j * 9] + '1' + queen[i + j * 9 + 1:]
                if ((i - j * 7) % 8) > (i % 8) and (i - j * 7) >= 0:
                    bishop = bishop[:i - j * 7] + '1' + bishop[i - j * 7 + 1:]
                    queen = queen[:i - j * 7] + '1' + queen[i - j * 7 + 1:]
                if ((i - j * 9) % 8) < (i % 8) and (i - j * 9) >= 0:
                    bishop = bishop[:i - j * 9] + '1' + bishop[i - j * 9 + 1:]
                    queen = queen[:i - j * 9] + '1' + queen[i - j * 9 + 1:]

            if whitePawn != ("0" * 64):
                whitePawnBoards.append(Bits(bin=whitePawn))
            if blackPawn != ("0" * 64):
                blackPawnBoards.append(Bits(bin=blackPawn))

            rookBoards.append(BitArray(bin=rook))
            knightBoards.append(Bits(bin=knight))
            bishopBoards.append(Bits(bin=bishop))
            queenBoards.append(Bits(bin=queen))
            kingBoards.append(Bits(bin=king))

            for j in range(64):
                print(int(queenBoards[i][j]), end=" ")
                if (j + 1) % 8 == 0:
                    print(" ")
            print(" ")

        end = time.time()
        print("Time to generate BitBoards: ", end - start)

        return [whitePawnBoards, blackPawnBoards, rookBoards, knightBoards, bishopBoards, queenBoards, kingBoards]

    # Returns a composite bitboard which holds the state of every unspecified piece belonging to each player
    def getTotalCompositeBoard(self):
        whitePieces = self.whitePlayer.pieceState
        blackPieces = self.blackPlayer.pieceState
        mask = (
                whitePieces[PAWN]   |
                whitePieces[ROOK]   |
                whitePieces[KNIGHT] | 
                whitePieces[BISHOP] | 
                whitePieces[QUEEN]  |
                whitePieces[KING]   |
                blackPieces[PAWN]   |
                blackPieces[ROOK]   |
                blackPieces[KNIGHT] | 
                blackPieces[BISHOP] | 
                blackPieces[QUEEN]  |
                blackPieces[KING]
        )
        return mask

    def getPlayerCompositeBoard(self, player):
        if player is WHITE:
            pieces = self.whitePlayer.pieceState
        elif player is BLACK:
            pieces = self.blackPlayer.pieceState
        mask = (
                pieces[PAWN]   |
                pieces[ROOK]   |
                pieces[KNIGHT] | 
                pieces[BISHOP] | 
                pieces[QUEEN]  |
                pieces[KING]
        )
    
    def getLegalMoves(self, player):
        pawns, rooks, knights, bishops = {},{},{},{}
        queen, king = [],[]

        if player == WHITE:
            playerState = self.whitePlayer.pieceState
            playerCompBoard = self.getCompositeBoard(WHITE)
            enemyCompBoard = self.getCompositeBoard(BLACK)
        elif player == BLACK:
            playerState = self.blackPlayer.pieceState
            playerCompBoard = self.getCompositeBoard(BLACK)
            enemyCompBoard = self.getCompositeBoard(WHITE)


        emptySquares = (BitArray(bin="1"*64) | enemyCompBoard) ^ playerState

        return [pawns, rooks, knights, bishops, queen, king]
        
'''
Classic 8x8 board configuration for White and Black piece sets
'''
class ClassicBoard(Board):
    def __init__(self, whitePieces, blackPieces):
        board_width = 8
        board_height = 8
        super().__init__(board_width, board_height, whitePieces, blackPieces)
    
    #def displayBoardState(self):

    
