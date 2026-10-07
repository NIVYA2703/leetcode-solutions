# LeetCode #60 - Permutation Sequence
# Difficulty: Hard
#
# Approach:
# Use factorial groups to directly determine each digit
# of the kth permutation instead of generating all permutations.
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def getPermutation(self, n, k):
        
        numbers = [str(i) for i in range(1, n + 1)]
        result = ""
        
        # Convert k to 0-based indexing
        k -= 1
        
        for i in range(n, 0, -1):
            
            # Number of permutations for each group
            factorial = 1
            for j in range(1, i):
                factorial *= j
            
            # Find which group k belongs to
            index = k // factorial
            
            result += numbers[index]
            numbers.pop(index)
            
            k %= factorial
        
        return result
        
