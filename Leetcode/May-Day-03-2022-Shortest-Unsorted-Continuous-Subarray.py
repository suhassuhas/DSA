# 581. Shortest Unsorted Continuous Subarray

# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

# Return the shortest such subarray and output its length.

 

# Example 1:

# Input: nums = [2,6,4,8,10,9,15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 0
# Example 3:

# Input: nums = [1]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# -105 <= nums[i] <= 105


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        s,e = 0,n-1
        liop,siop=0,0
        prev = nums[0]
        for i in range(n):
            if nums[i] < prev:
                liop = i
            else:
                prev = nums[i]
        
        #reverse
        nex = nums[n-1]
        for i in range(n-1,-1,-1):
            if nums[i] > nex:
                siop = i
            else:
                nex = nums[i]
        if liop != 0:
            return liop - siop + 1
        return 0
        