# 1641. Count Sorted Vowel Strings
# Medium

# 2758

# 62

# Add to List

# Share
# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

# Example 1:

# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
# Example 2:

# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
# Example 3:

# Input: n = 33
# Output: 66045
 

# Constraints:

# 1 <= n <= 50 


class Solution:
    def countVowelStrings1(self, n: int) -> int:
        a=1
        e=1
        i=1
        o=1
        u=1
        def increment():
            nonlocal a,e,i,o,u
            a = a+e+i+o+u
            e = e+i+o+u
            i = i+o+u
            o = o+u
        for _ in range(1,n):
            increment()
        return a+e+i+o+u
        
    def countVowelStrings2(self, n: int) -> int:
        
        dp = [[0]*5 for _ in range(n)]
        for i in range(5):
            dp[0][i] = 1
        for i in range(1,n):
            for j in range(4,-1,-1):
                if j == 4:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j+1]
        return sum(dp[n-1])
            
    def countVowelStrings3(self, n: int) -> int:
        
        dp = [1]*5
        for i in range(1,n):
            for j in range(3,-1,-1):
                dp[j] = dp[j] + dp[j+1]
        return sum(dp)