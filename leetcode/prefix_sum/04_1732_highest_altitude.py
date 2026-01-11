class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest = 0
        highest = max(highest, gain[0])
        for i in range(1,len(gain)):
            gain[i] = gain[i-1] + gain[i]
            highest = max(highest, gain[i])
        return highest