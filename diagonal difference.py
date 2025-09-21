def diagonal_difference(arr):
    s1 = 0
    s2 = 0
    n = len(arr)
    for i in range(n):  # Using single loop
        s1 += arr[i][i]
        s2 += arr[n-i-1][i]
    return abs(s1-s2)

arr=[list(map(int,input().split())) for x in range(3)]
print(diagonal_difference(arr))