
from collections import deque


class Solution:
    def removeInvalidParentheses(self, s):
        result = []
        queue = deque([s])
        visited = {s}

        found = False

        while queue:
            current = queue.popleft()

            # If the current string is valid, it has
            # the minimum number of removals.
            if self.isValid(current):
                result.append(current)
                found = True

            # Once valid strings are found, don't remove
            # any more characters.
            if found:
                continue

            # Generate the next level by removing one parenthesis.
            for i in range(len(current)):

                # Remove only parentheses, not letters.
                if current[i] != '(' and current[i] != ')':
                    continue

                next_string = current[:i] + current[i + 1:]

                if next_string not in visited:
                    visited.add(next_string)
                    queue.append(next_string)

        return result

    def isValid(self, s):
        count = 0

        for ch in s:

            if ch == '(':
                count += 1

            elif ch == ')':
                count -= 1

                # More closing parentheses than opening ones.
                if count < 0:
                    return False

        # Valid only when all parentheses are balanced.
        return count == 0

