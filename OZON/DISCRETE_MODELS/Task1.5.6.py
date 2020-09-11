from itertools import product, combinations

def isGood(combination):
    cardsInCombination = list(combination)
    suitCount = len(set(map(lambda card: card[1], combination)))
    aceCount = sum([1 for card in combination if card[0] == "Ace"])
    return suitCount == 4 and aceCount <= 2

values = list(map(str, range(6,11))) + ["Queen", "King", "Jack", "Ace"]
suits = ["club", "diamond", "heart", "spade"]
cards = product(values, suits)

print(sum([1 for combination in combinations(cards, 7) if isGood(combination)]))