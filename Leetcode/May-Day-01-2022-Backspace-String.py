# 844. Backspace String Compare
# Easy

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".

# Example 2:
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".

# Example 3:
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
 
# Constraints:
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            ans = []
            for c in s:
                if c!= '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s) == build(t)
    
    def backspaceCompare1(self,s:str,t:str) -> bool:
        def getNextChar(string,pointer):
            num_of_backspaces = 0
            while pointer >= 0 and (num_of_backspaces>0 or string[pointer]=="#"):
                if string[pointer]=="#":
                    num_of_backspaces+=1
                else:
                    num_of_backspaces-=1
                pointer-=1
            return (string[pointer],pointer) if pointer>=0 else ("",-1)

        sptr,tptr = len(s)-1,len(t)-1
        while sptr>=0 or tptr>=0:
            schar,sptr = getNextChar(s,sptr)
            tchar,tptr = getNextChar(t,tptr)
            if schar != tchar:
                return False
            sptr -= 1
            tptr -= 1
        return True

S = Solution()
print(S.backspaceCompare("ab#qwertyu","ad#qwertyu"))
print(S.backspaceCompare1("ab#qwertyu","ad#qwertyu"))