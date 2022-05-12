47. Permutations II
Medium

5454

96

Add to List

Share
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
Accepted
635,746
Submissions
1,154,419


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(count,comb):
            if len(comb) == len(nums):
                res.append(list(comb))
                return 
            for num in count:
                if count[num]>0:
                    count[num] -=1
                    comb.append(num)
                    helper(count,comb)
                    comb.pop()
                    count[num] += 1
        helper(Counter(nums),[])
        return res
       


    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(count,comb):
            if len(comb) == len(nums):
                res.append(list(comb))
                return 
            for num in count:
                if count[num]>0:
                    count[num] -=1
                    comb.append(num)
                    helper(count,comb)
                    comb.pop()
                    count[num] += 1
        helper(Counter(nums),[])
        return res
       