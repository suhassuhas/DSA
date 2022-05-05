# 1679. Max Number of K-Sum Pairs
# Medium

# Add to List

# Share
# You are given an integer array nums and an integer k.

# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

# Return the maximum number of operations you can perform on the array.

 

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.
 

# Constraints:

# 1 <= nums.length <= 105
# 1 <= nums[i] <= 109
# 1 <= k <= 109

from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # ctr = Counter(nums)
        # total = 0
        # for i in range(len(nums)):
        #     if nums[i] == k-nums[i]:
        #         if ctr[nums[i]]>=2:
        #             total+=1
        #             ctr[nums[i]]-=2
        #     elif ctr[nums[i]] > 0 and ctr[k-nums[i]] > 0:
        #         ctr[nums[i]]-=1
        #         ctr[k-nums[i]]-=1
        #         total+=1
        #         #print(ctr)
        # return total
    
    def maxOperations1(self,nums:List[int], k:int) -> int:
        nums.sort()
        n = len(nums)
        left,right = 0,n-1
        ans = 0
        while left < right:
            curr = nums[left] + nums[right]
            if curr == k:
                ans +=1
                left+=1
                right-=1
            elif curr < k:
                left += 1
            else:
                right -=1
        return ans