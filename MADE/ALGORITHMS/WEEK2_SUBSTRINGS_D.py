from collections import Counter

def naturalSum(n):
    return n * (n + 1) // 2
import random
string1 = ''.join(random.choice("abcd") for _ in range(10))
string2 = ''.join(random.choice("abc") for _ in range(4))

def solveProblem(grishaString, cardString):
    cardLettersFrequencies = Counter(cardString)
    leftIndex = 0
    rightIndex = -1
    total = 0

    while rightIndex < len(grishaString):
        rightIndex += 1
        if rightIndex == len(grishaString):
            total += naturalSum(rightIndex - leftIndex) 
        else:
            letter = grishaString[rightIndex]
            if letter not in cardLettersFrequencies:
                cardLettersFrequencies[letter] = 0
            cardLettersFrequencies[letter] -= 1
            while cardLettersFrequencies[letter] < 0:
                total += rightIndex - leftIndex
                cardLettersFrequencies[grishaString[leftIndex]] += 1
                leftIndex += 1
             

    return total

print(string1)
print(string2)
print(solveProblem(string1, string2))
