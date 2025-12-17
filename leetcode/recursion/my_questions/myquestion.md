

# ⭐ **20 Beginner-Level Recursion Problems**

(Simple → Slightly harder, but all pure recursion)

---

## ✅ **LEVEL 1 — Very Easy (Base Case Practice)**

### 1. Print numbers from 1 to N

Use recursion to print `1 2 3 ... N`.

### 2. Print numbers from N to 1

Print in reverse: `N N-1 ... 1`.

### 3. Sum of first N numbers

Compute:

```
1 + 2 + 3 + ... + N
```

### 4. Factorial of N

Classic:

```
n! = n × (n-1)!
```

### 5. Print characters of a string one by one

Recursively print each character:

```
"abc" → a b c
```

### 6. Count digits of a number

Example:

```
input 456 → output 3
```

### 7. Sum of digits of a number

Example:

```
input 432 → output 4+3+2 = 9
```

### 8. Reverse digits of a number

Convert `432 → 234`.

---

## ✅ **LEVEL 2 — Medium Beginner (Return Values Practice)**

### 9. Power function

Compute `a^b` using recursion.

### 10. Fibonacci simple recursive

`fib(n) = fib(n-1) + fib(n-2)`.

### 11. Check if a string is palindrome

Example:

```
madam → True
hello → False
```

### 12. Count occurrences of a character in a string

Example:

```
("banana", 'a') → 3
```

### 13. Print sum of array elements (recursively)

Use recursion to sum all values in a list.

### 14. Minimum in an array

Find the smallest element using recursion.

### 15. Check if array is sorted (increasing)

Return `True` or `False`.

---

## ✅ **LEVEL 3 — Slight Thinking (Pattern Recursion)**

### 16. Print a number N times

Example, N = 4 →

```
4 4 4 4
```

### 17. Print a string in reverse

Example:

```
"abc" → c b a
```

### 18. Product of digits of a number

Example:

```
input 234 → output 2×3×4 = 24
```

### 19. Count zeros in a number

Example:

```
input 102030 → output = 3
```

### 20. Convert integer to binary using recursion

Example:

```
5 → 101
```

class Solution:
    # @param A : string
    # @return an integer



stack = []
        
        for ch in A:
            if stack and stack[-1] == ch:
                stack.pop()        # remove the pair
            else:
                stack.append(ch)   # add new char
        
        return "".join(stack)

