def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # return sorted(s1) == sorted(s2)

    if len(s1) != len(s2):
        return False

    count = dict()

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            return False
    
    
    return True


print(anagram('car', 'arcc'))
print(anagram('clint eastwood', 'old west action'))