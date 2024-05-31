import board
import pieces
from constants import *

class Game:
    def __init__(self, firstPlayer, board, gameType):
        self.gameType = gameType
        self.player = firstPlayer
        self.board = board
        print(board for board in board.bitBoards)
    
    def startGame(self, gameType):
        print("Game Started")

class ClassicGame(Game):
    def __init__(self):
        super().__init__(
            WHITE,
            board.ClassicBoard(
                pieces.ClassicPieces(WHITE), 
                pieces.ClassicPieces(BLACK)
            ),
            CLASSIC
        )