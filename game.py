import board
import pieces
from constants import *

class Game:
    def __init__(self, firstPlayer, board, gameType):
        self.gameType = gameType
        self.player = firstPlayer
        self.board = board
    
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

        whiteState = self.board.whitePlayer.pieceState
        whiteColor = self.board.whitePlayer.playerColor
        print(whiteState)
        print(whiteColor)


if __name__ == "__main__":
    game = ClassicGame()