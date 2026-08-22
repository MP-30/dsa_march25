bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
Output = [10,55,45,25,25]


# bookings = [[1,2,10],[2,2,15]]
# n = 2
# Output = [10,25]


def corpFlightBookings(bookings, n: int):
    result = [0] * n
    for i in bookings:
        result[i[0]-1] += i[2]
        if i[1] < n:
            result[i[1]] -= i[2]
    for j in range(1,len(result)):
        result[j] += result[j-1]
    return result

# def corpFlightBookings1(bookings, n: int):
#     result = [0] * n
#     for i in bookings:
#         for j in range(i[0]-1, i[1]):
#             result[j] += i[2]
#     return result

print(corpFlightBookings(bookings,n))

