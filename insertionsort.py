def insertionsort(a):
    for i in range(1, len(a)):
        curr = a[i]
        position = i 
        while position > 0 and a[position-1] > curr:
            a[position] = a[position-1]
            position -= 1
        a[position] = curr
    return a
nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
print(insertionsort(nums))

