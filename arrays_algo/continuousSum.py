def continuousSum(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 0:
        return 0
    
    largestsum = maxsum = arr[0]
    for num in arr[1:]:
        largestsum = max(largestsum + num, num)
        maxsum = max(largestsum, maxsum)

    return maxsum


print(continuousSum([1,2,-1,10,10,7,-10,-10]))