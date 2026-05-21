A = [1,4,5,2,4]
def solve(A):
    profit = 0
    min_price = float("inf")
    for i in range(len(A)):
        min_price = min(min_price, A[i])
        profit = max(profit, A[i]- min_price)
    return  profit

print(solve(A))