class Game:
    def __init__(self, i):
        print("Game initialization: ", i)

    def start(self):
        print("Starting game")


class BoardGame(Game):
    def __init__(self, i):
        super().__init__(i)
        print("BoardGame initialization")


class Chess(BoardGame):
    def __init__(self):
        super().__init__(11)
        print("Chess initialization")


Chess().start()
