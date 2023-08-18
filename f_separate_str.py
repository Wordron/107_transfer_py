def separate_str(str, delim):
    separated_str = []
    temp = str.partition(delim)
    while 1:
        if len(temp[0]) != 0:
            separated_str.append(temp[0])
            if len(temp[2]) == 0:
                return separated_str
        temp = temp[2].partition(delim)
    return separated_str
