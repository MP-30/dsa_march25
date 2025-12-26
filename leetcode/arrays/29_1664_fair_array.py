def fair_array(nums):
    right_even_sum = 0
    right_odd_sum = 0
    result = 0
    
    for i in range(0,len(nums)):
        if i % 2 == 0:
            right_even_sum += nums[i]
        else:
            right_odd_sum += nums[i]
    
    # print(even_sum, odd_sum)
    left_even_sum = 0
    left_odd_sum = 0
    
    for i in range(0,len(nums)):
        if i % 2 == 0:
            right_even_sum = right_even_sum - nums[i]
    
        else :
            right_odd_sum = right_odd_sum - nums[i]
            
        new_even = left_even_sum + right_odd_sum
        new_odd = left_odd_sum + right_even_sum
        if new_even == new_odd:
            result +=1
        
        if i % 2 == 0:
            left_even_sum = left_even_sum + nums[i]
    
        else :
            left_odd_sum = left_odd_sum + nums[i]
        
    return result
'''

    def waysToMakeFair(self, nums):
        total_even = 0
        total_odd = 0
        
        for i in range(len(nums)):
            if i % 2 == 0:
                total_even += nums[i]
            else:
                total_odd += nums[i]

        left_even = 0
        left_odd = 0
        count = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                total_even -= nums[i]
            else:
                total_odd -= nums[i]

            # after removal, right part parity flips
            if left_even + total_odd == left_odd + total_even:
                count += 1

            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i]

        return count


'''


nums = [2,1,6,4]
# 2 6 4
# nums = [1,1,1]
print(fair_array(nums))