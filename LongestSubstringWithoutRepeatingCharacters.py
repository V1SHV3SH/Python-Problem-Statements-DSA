maxcount = 0  # Global variable (should be avoided, but keeping as is)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        global maxcount  # Use global to modify maxcount
        c = ''
        count = 0

        for ind, char in enumerate(s):
            for j in c:
                if j == char:
                    if maxcount < count:
                        maxcount = count
                    d = s[1:]  # Instead of `pop(0)`, use slicing (strings are immutable)

                    if len(d) == 0:
                        return maxcount
                    else:
                        self.lengthOfLongestSubstring(d)  # Fix: return the recursive call
                else:
                    c = char
                    count += 1

        return maxcount  # Ensure a return in all cases

# Test
st = 'abcabcbb'
obj = Solution()
b = obj.lengthOfLongestSubstring(st)
print(b)  # Expected output: 3
