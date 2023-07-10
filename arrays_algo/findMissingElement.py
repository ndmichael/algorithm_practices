def finderr1(arr1, arr2):
    arr1.sort()
    arr2.sort()

    ele = 0

    for num in arr1 + arr2:
        # print(ele)
        ele ^= num
    return ele


def finderr2(arr1, arr2):
    arr1.sort()
    arr2.sort()

    count = {}
    for num in arr2:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    print(count)
    for num in arr1:
        if count[num] == 0:
            return num
        else:
            count[num] -= 1
    print("count: ", count)
    return -1


print(finderr2([5,7,5,7,2], [5,7,7,2]))