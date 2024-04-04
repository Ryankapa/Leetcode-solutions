#Link ref https://leetcode.com/problems/two-sum/

from typing import List

class Solution:
    def twosum(numbers: list[int], target: int) -> list[int]:
        numbers_length = len(numbers)
        for i in range(numbers_length - 1):
            for j in range(i + 1, numbers_length):
                if numbers[i] + numbers[j] == target:
                    return [i, j]
        return []


numbers = [2,7,11,15]
target = 9
test = Solution.twosum(numbers, target)
print(test)