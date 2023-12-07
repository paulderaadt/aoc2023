from utils.filereaders import Linereader

data = Linereader("inputs/day2a.txt").parse()

class Game():
    def __init__(self, gameid, info):
        self.id = gameid
        self.blue = 0
        self.green = 0
        self.red = 0
        self.info = info

    @property
    def blue(self):
        return self._blue

    @blue.setter
    def blue(self, new):
        self._blue = new

    @property
    def red(self):
        return self._red

    @red.setter
    def red(self, new):
        self._red = new

    @property
    def green(self):
        return self._green

    @green.setter
    def green(self, new):
        self._green = new

    def __repr__(self):
        return f'Game: {self.id} green: {self.green} red: {self.red} blue: ' \
               f'{self.blue}'
def day2a(data):
    valid_games = []
    for i, line in enumerate(data):
        gameid, game = line.split(":")
        gameid = int(gameid.strip("Game "))
        game = game.strip().split(";")
        hands = [hand.split(",") for hand in game]
        valid = True
        game_obj = Game(gameid, game)
        for draws in hands:
            for pair in draws:
                pair = pair.strip()
                amount, color = pair.split(" ")
                amount = int(amount)
                color = color.strip()
                if color == "red" and amount > 12:
                    valid = False
                if color == "green" and amount > 13:
                    valid = False
                if color == "blue" and amount > 14:
                    valid = False
        if valid:
            valid_games.append(game_obj)
    return valid_games

day2a_games = day2a(data)

print(sum([game.id for game in day2a_games]))

def day2b(games):
    for draws in games:
        for draw in draws.info:
            draw = draw.strip()
            draw = draw.split(",")
            for pair in draw:
                pair = pair.strip()
                amount, color = pair.split(" ")
                amount = int(amount)
                color = color.strip()
                if color == "red":
                    draws.red = max(draws.red, amount)
                if color == "green":
                    draws.green = max(draws.green, amount)
                if color == "blue":
                    draws.blue = max(draws.blue, amount)

    total = 0
    for game in games:
        gamepower = game.red * game.green * game.blue
        total += gamepower
        print(game, gamepower)
    print(total)

allgames = []
for i, line in enumerate(data):
    gameid, game = line.split(":")
    gameid = int(gameid.strip("Game "))
    game = game.strip().split(";")
    hands = [hand.split(",") for hand in game]
    valid = True
    allgames.append(Game(gameid, game))

day2b(allgames)
