hands = []

from collections import Counter

from utils.filereaders import Linereader

faces = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2",
         "J"]
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
        if "J" not in self.cards:
            for item in self.cardset.values():
                score += item**2
            return score
        if self.cards == list("JJJJJ"):
            for item in self.cardset.values():
                score += item**2
            return score
        kopie = self.cardset.copy()
        jokers = kopie.pop("J")
        highest_values = [kv for kv in kopie.items() if kv[1] == max(
            kopie.values())]
        hoogste_set = max(highest_values, key=lambda x: CARDVALS[x[0]])[0]
        kopie[hoogste_set] += jokers
        for item in kopie.values():
            score += item ** 2
        return score

    def __repr__(self):
        return "".join(self.cards)

    def __lt__(self, other):
        if self.hand_score == other.hand_score:
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                else:
                    # print(self.cards[i], CARDVALS[self.cards[i]], CARDVALS[
                    #     other.cards[i]], other.cards[i])
                    return CARDVALS[self.cards[i]] < CARDVALS[other.cards[i]]
        return self.hand_score < other.hand_score


data = Linereader("inputs/day7.txt").parse()
data = [line.split(" ") for line in data]
hands = []
for line in data:
    hands.append(Hand(line[0], line[1]))

# scores for 1 2 3 4 or 5 of a kind [1, 4, 9, 16, 25]
hands.sort()
winnings = 0
rank = 1
for hand in hands:
    winnings += hand.bet * rank
    rank += 1
print(winnings)
