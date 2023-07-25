def balance_check(st: str) -> bool:
    if len(st) % 2 != 0:
        return False
    
    opening = set('({[')
    matches = set([( '(', ')'), ( '{', '}'), ( '[', ']')])
    stack = []

    for paren in st:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_item = stack.pop()
            if (last_item, paren) not in matches:
                return False
            
    return len(stack) == 0

print(balance_check("[]"))
print(balance_check("[({}])"))
print(balance_check("{[([()])]}"))
