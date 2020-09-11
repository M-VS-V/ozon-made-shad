def find_max_substring_occurrence(input_string):
    if len(input_string) == 0:
        return 0
    else:
        repeatLengthCandidate = 1
        while repeatLengthCandidate < len(input_string):
            if len(input_string) % repeatLengthCandidate == 0:
                k = len(input_string) // repeatLengthCandidate
                if input_string[0:repeatLengthCandidate] * k == input_string:
                    return k
            repeatLengthCandidate += 1

    return 1
