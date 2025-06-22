arr1 = [3, 6, 0, 6, 3]
arr2 = [1, 2, 3, 4, 5]

def palindrome(arr):
    for i in range(0, (len(arr)//2)+1):
        if arr[i] == arr[-(i+1)]:
            pass
        else:
            return False
    return True

print(palindrome(arr2))