def singleNumber(nums):
    start = 0
    for i in nums:
        start = start ^ i
    return start

nums = [4,1,2,1,2]
print(singleNumber(nums))