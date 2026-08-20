class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):

                n1 = ord(num1[i]) - ord('0')
                n2 = ord(num2[j]) - ord('0')

                product = n1 * n2

                pos1 = i + j
                pos2 = i + j + 1

                total = product + result[pos2]

                result[pos2] = total % 10
                result[pos1] += total // 10

        # Convert result array to string
        start = 0

        while start < len(result) and result[start] == 0:
            start += 1

        return ''.join(map(str, result[start:]))
