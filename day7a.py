from collections import Counter

from utils.filereaders import Linereader

data = Linereader("inputs/day7.txt").parse()
data = [line.split(" ") for line in data]
faces = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
values = list(range(len(faces)))[::-1]
CARDVALS = dict(zip(faces, values))


class Hand:
    def __init__(self, cards, bet):
        self.cards = list(cards)
        self.cardset = Counter(cards)
        self.bet = int(bet)

    @property
    def hand_score(self):
        score = 0
        for item in self.cardset.values():
            score += item**2
        return score

    def __repr__(self):
        return "".join(self.cards)

    def __lt__(self, other):
        if self.hand_score == other.hand_score:
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                else:
                    return CARDVALS[self.cards[i]] < CARDVALS[other.cards[i]]
        return self.hand_score < other.hand_score


hands = []
for line in data:
    hands.append(Hand(line[0], line[1]))

hands.sort()
winnings = 0
rank = 1
for hand in hands:
    winnings += hand.bet * rank
    rank += 1
print(winnings)
