def encode_rle(x):
    prevElement = None
    result = ([], [])
    currentCount = 0
    for element in x:
        if prevElement is None:
            currentCount = 1
        elif element == prevElement:
            currentCount += 1
        else:
            result[0].append(prevElement)
            result[1].append(currentCount)
            currentCount = 1
        prevElement = element
    result[0].append(prevElement)
    result[1].append(currentCount)
    return result



