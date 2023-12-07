from utils.filereaders import Linereader

data = Linereader("inputs/day4a.txt").parse()

class Card:
    def __init__(self, card):
        self.cardid , card = card.split(":")
        self.cardid = self.cardid.split(" ")[1]
        self.cardid = int(self.cardid)
        self.winning, self.numbers = card.split("|")
        self.winning = self.winning.strip()
        self.numbers = self.numbers.strip()
        self.winning = [int(item.strip()) for item in self.winning.split(" ")]
        self.numbers = [int(item.strip()) for item in self.numbers.split(" ")]

    def __repr__(self):
        me = f'Card: {self.cardid} Winning: {self.winning}Nums:' \
             f' {self.numbers}'
        return me

    @property
    def winning_numbers(self):
        return [num for num in self.numbers if num in self.winning]

    @property
    def points(self):
        if not self.winning_numbers:
            return 0
        return 2**(len(self.winning_numbers) - 1)

# 4a
total = 0
for line in data:
    print(line)
    card = Card(line)
    total += card.points

print(total)

# 4b
total = 0
winnings = []

for i, line in enumerate(data):
    total += 1
    card = Card(line)
    won = [Card(each) for each in data[card.cardid: card.cardid + len(
        card.winning_numbers)]]
    winnings += won

while winnings:
    total += 1
    card = winnings.pop()
    won = [Card(each) for each in data[card.cardid: card.cardid + len(
        card.winning_numbers)]]
    winnings += won

print(total)