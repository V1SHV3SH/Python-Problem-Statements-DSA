maxcount=0
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c=''
        count=0
        for ind, char in enumerate(s):
            for j in c:
                if j==char:
                    if maxcount<count:
                        maxcount = count
                    d= s.pop(0)
                    if len(s)== 0:
                        return maxcount
                    else:
                        lengthOfLongestSubstring(s)
                else:
                    c=char
                    count+=1

st = 'abcabcbb'
obj = Solution()
b = obj.lengthOfLongestSubstring(st)
print(b)
