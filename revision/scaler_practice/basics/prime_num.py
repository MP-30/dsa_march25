def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for j in range(2,N+1):
        for i in range(2,int(j **0.5)+1):
            if j % i == 0:
                break
        else: print(j)

if __name__ == '__main__':
    main()
# def main():
#     N = int(input())
#     for j in range(2, N + 1):  # numbers from 2 to N
#         for i in range(2, int(j**0.5) + 1):  # check divisibility up to sqrt(j)
#             if j % i == 0:
#                 break
#         else:
#             print(j)


# if __name__ == '__main__':
#     main()   # no need to print(main())
# lower = 900
# upper = 1000

# def number(lower,upper):
#     for num in range(lower, upper + 1):
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 print(num)