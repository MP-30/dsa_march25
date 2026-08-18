def longestCommonPrefix(A):
    result = ""
    first = A[0]
    
    for i in range(len(first)):
        ch = first[i]
        for s in A:
            if i >=len(s) or s[i] != ch:
                return result
        result +=ch
    return result
            
A = ["abcdefgh", "aefghijk", "abcefgh"]

# print(longestCommonPrefix(A))

a = 'uire'
a += 'b'
print(a)