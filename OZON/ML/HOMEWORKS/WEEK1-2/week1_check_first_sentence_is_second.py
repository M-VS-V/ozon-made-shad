from collections import defaultdict


def check_first_sentence_is_second(firstSentence, secondSentence):
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    for x in firstSentence.split():
        dic1[x] += 1

    for x in secondSentence.split():
        dic2[x] += 1

    for k, v in dic2.items():
        if k not in dic1 or dic1[k] < dic2[k]:
            return False
    return True
