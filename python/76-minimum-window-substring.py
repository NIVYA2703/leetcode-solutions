from collections import Counter


class Solution:
    def minWindow(self, s, t):

        if not s or not t:
            return ""

        # Characters we need and their required counts
        required = Counter(t)

        # Characters currently inside our window
        window = {}

        left = 0
        formed = 0
        required_count = len(required)

        min_length = float("inf")
        min_left = 0

        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            # This character has reached its required count
            if char in required and window[char] == required[char]:
                formed += 1

            # Try shrinking the window
            while formed == required_count:

                # Update minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left

                left_char = s[left]
                window[left_char] -= 1

                # We no longer have enough of this character
                if (left_char in required and
                        window[left_char] < required[left_char]):
                    formed -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_left:min_left + min_length]
