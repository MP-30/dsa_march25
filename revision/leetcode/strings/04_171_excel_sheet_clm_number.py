strr = 'ABCDEFGHIJKLMNONQRSTUVWXYZ'

columnTitle = "N"
def excel(columnTitle):
    dictt = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
        'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
        'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
    }
    new_column = columnTitle[::-1]
    summ = 0
    for a,b in enumerate(new_column):
        n = (dictt[b])
        print(n)
        m = a
        print(f"m is {m}")
        sum1 = n * (26**m)
        summ += sum1
    print(summ)
excel(columnTitle)