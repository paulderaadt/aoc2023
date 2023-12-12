hands = []

from collections import Counter

from utils.filereaders import Linereader

data = Linereader("inputs/day7.txt").parse()
data = [line.split(" ") for line in data]
faces = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
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
        highest = self._highest_card()
        if self.cards == "JJJJJ":
            return 5**2
        if "J" not in self.cards:
            for item in self.cardset.values():
                score += item**2
            return score
        for item in self.cardset.values():
            if item != "J" and item == highest:
                score += (self.cardset["J"] + self.cardset[highest])**2
            else:
                score += item**2
        print(self, (self.cardset["J"] + self.cardset[highest])**2)
        return score

    def _highest_card(self):
        highest_values = [kv for kv in self.cardset.items() if kv[1] == max(
            self.cardset.values())]
        return max(highest_values, key=lambda x: CARDVALS[x[0]])[0]

    def _lowest_card(self):
        lowest_values = [kv for kv in self.cardset.items() if kv[1] == min(
            self.cardset.values()) and kv[0] != "J"]
        return min(lowest_values, key=lambda x: CARDVALS[x[0]])[0]

    def __repr__(self):
        return "".join(self.cards)

    def __gt__(self, other):
        if self.hand_score == other.hand_score:
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                else:
                    return CARDVALS[self.cards[i]] > CARDVALS[other.cards[i]]
        return self.hand_score > other.hand_score


for line in data:
    hands.append(Hand(line[0], line[1]))

hands.sort()
winnings = 0
rank = 1
for hand in hands:
    winnings += hand.bet * rank
    rank += 1
    print('score', hand, hand.hand_score)