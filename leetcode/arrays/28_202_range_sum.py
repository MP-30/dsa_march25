class NumArray:

    def __init__(self, nums: list[int]):
        self.prefix_sum = [arr[0]]
        for i in range(1,len(arr)):
            self.prefix_sum.append(self.prefix_sum[-1] + arr[i])
            
    
    def sumRange(self, left: int, right: int) -> int:
        result = [None,]
        for i in range(1,len(nums)):
            left = nums[i][0]
            right = nums[i][1]
            result.append(self.prefix_sum[right] - self.prefix_sum[left])
        return result
        
nums = [[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]

a = NumArray(nums)
print(a.sumRange())