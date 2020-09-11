import re
from collections import defaultdict


def get_new_dictionary(input_dict_name, output_dict_name):
    resultLines = []
    file1 = open(input_dict_name, "r")
    file2 = open(output_dict_name, "w")
    resultDic = defaultdict(list)
    for line in file1.readlines()[1:]:
        line = line.strip()
        words = re.split(r"[, -]", line)
        words = list(filter(lambda x: x != '', words))
        key = words[0]
        for w in words[1:]:
            resultDic[w].append(key)
    for k in sorted(resultDic.keys()):
        translations = ", ".join(sorted(resultDic[k]))
        line = f"{k} - {translations}"
        resultLines.append(line)
    resultLines.insert(0, f'{len(resultLines)}')
    file2.writelines(map(lambda x: x + "\n", resultLines))
    file2.close()
    file1.close()
