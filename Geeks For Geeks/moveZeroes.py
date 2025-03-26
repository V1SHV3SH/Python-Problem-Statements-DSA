# Move All Zeroes to End
# Difficulty: Easy Accuracy: 45.51%
# Submissions: 287K+ Points: 2Average Time: 15m
# You are given an array arr[] of non-negative integers.
#  Your task is to move all the zeros in the array
#  to the right end while maintaining the relative order of
#  the non-zero elements. The operation must be performed in place,
#   meaning you should not use extra space for another array.
#
# Examples:
#
# Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
# Output: [1, 2, 4, 3, 5, 0, 0, 0]
# Explanation: There are three 0s that are moved to the end.
# Input: arr[] = [10, 20, 30]
# Output: [10, 20, 30]
# Explanation: No change in array as there are no 0s.
# Input: arr[] = [0, 0]
# Output: [0, 0]
# Explanation: No change in array as there are all 0s.
# Constraints:
# 1 ≤ arr.size() ≤ 105
# 0 ≤ arr[i] ≤ 105

#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	i=0
    	while 0 in arr:
    	    arr.remove(0)
    	    i+=1
    	arr.extend(0 for j in range(i))


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
        print("~")
# } Driver Code Ends

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	for num in arr:
			if num == 0:
				arr.remove(num)
				arr.append(num)
		return arr

ssdfjlksf
 ksjfkja
  aksfkjs
   as'dfj k
   a alsf
    vishveshesar
	 hiremath
	 vishveshesar
	 vishveshesar # WARNING:  vish
	 
