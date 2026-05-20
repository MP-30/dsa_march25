# my solution
def solve(ranges, left, right):
    completed = set()
    for i in range(left,right+1):
        for j in ranges:
            if i in range(j[0], j[1]+1):
                completed.add(i)
         
    print(completed)       
    if len(completed) == right -left+1:
        return True
    else:
        return False
    
#  chatGPT solution
class Solution:
    def isCovered(self, ranges, left, right):
        diff = [0] * 52

        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1

        active = 0
        for i in range(1, 51):
            active += diff[i]
            if left <= i <= right and active == 0:
                return False

        return True

    ...
    
# ranges = [[1,2],[3,4],[5,6]]
# left = 2
# right = 5

# ranges = [[1,10],[10,20]]
# left = 21
# right = 21

ranges = [[25,42],[7,14],[2,32],[25,28],[39,49],[1,50],[29,45],[18,47]]
left = 15
right = 38
print(solve(ranges, left, right))