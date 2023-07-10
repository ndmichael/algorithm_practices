def pairSum(arr, k):
    if len(arr) < 2:
        return
    seen = set()
    output = set()

    for num in arr:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target, num),max(target, num)))

    print(len(output))
    return output

arr = [3,2,1,2]
print(pairSum(arr, 4))