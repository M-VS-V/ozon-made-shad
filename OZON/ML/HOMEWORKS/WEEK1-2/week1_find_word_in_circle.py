def check(input, index, pattern):
    patternIndex = 0
    inputIndex = index
    result = -1
    isRightPossible = True
    isLeftPossible = True
    while patternIndex < len(pattern):
        if inputIndex == len(input):
            inputIndex = 0
        if input[inputIndex] == pattern[patternIndex]:
            patternIndex += 1
            inputIndex += 1
        else:
            isRightPossible = False
            break
    if isRightPossible:
        return (index, 1)

    patternIndex = 0
    inputIndex = index
    while patternIndex < len(pattern):
        if inputIndex == -1:
            inputIndex = len(input) - 1
        if input[inputIndex] == pattern[patternIndex]:
            patternIndex += 1
            inputIndex -= 1
        else:
            isLeftPossible = False
            break

    if isLeftPossible:
        return (index, -1)
    return -1


def find_word_in_circle(input, pattern):
    if pattern == "" or input == pattern:
        return (0, 1)

    patternIndex = 0
    for i in range(len(input)):
        result = check(input, i, pattern)
        if result != -1:
            return result
    return -1
