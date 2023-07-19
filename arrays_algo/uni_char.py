def uni_char(st: str) -> bool:
    return len(set(st)) == len(st)


def uni_char2(st: str) -> bool:
    sett = set()
    for ch in st:
        if ch in sett:
            return False
        else:
            sett.add(ch)
    return True

print(uni_char2("abcdee"))