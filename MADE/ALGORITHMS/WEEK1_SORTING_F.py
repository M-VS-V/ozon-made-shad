
def convertRomanToInteger(romeNumber):
    if len(romeNumber) == 0:
        return 0

    romanLetterDict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
        
    romanPairsLettersDict = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }

    prevLetter = None
    result = 0
    for letter in romeNumber:
        if prevLetter is None:
            prevLetter = letter
        else:
            romanPairs = prevLetter + letter
            if romanPairs in romanPairsLettersDict:
                prevLetter = None
                result += romanPairsLettersDict[romanPairs] 
            else:
                result += romanLetterDict[prevLetter]
                prevLetter = letter
    if prevLetter is not None:
        result += romanLetterDict[prevLetter]
    return result


def solveProblem():
    n = int(input())
    kings = []
    for _ in range(n):
        kingName, romanNumber = input().split()
        kings.append((kingName, romanNumber))
    kings.sort(key = lambda x: (x[0], convertRomanToInteger(x[1])))
    [print(f'{king[0]} {king[1]}') for king in kings]

solveProblem()