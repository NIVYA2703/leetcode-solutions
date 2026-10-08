# LeetCode #1021 - Remove Outermost Parentheses
# Difficulty: Easy
#
# Approach:
# Track the nesting depth of parentheses.
# Skip '(' when it starts a primitive and skip ')'
# when it closes a primitive.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def removeOuterParentheses(self, s):
        
        result = []
        depth = 0
        
        for ch in s:
            
            if ch == '(':
                # If depth > 0, this is not the outermost '('
                if depth > 0:
                    result.append(ch)
                
                depth += 1
            
            else:
                depth -= 1
                
                # If depth > 0, this is not the outermost ')'
                if depth > 0:
                    result.append(ch)
        
        return ''.join(result)
