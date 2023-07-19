def strComp(string: str)-> str:
    l = len(string)
    r = ""

    if l == 0:
        return ""
    if l == 1:
        return string[0] + str(1)
    
    cnt = 1
    i = 1

    while i < l:
        if string[i] == string[i-1]:
            cnt += 1
        else:
            r = r + string[i-1] + str(cnt)
            cnt = 1
        i += 1
    r = r + string[i-1] + str(cnt)

    return r

print(strComp("AABBbbaa"))