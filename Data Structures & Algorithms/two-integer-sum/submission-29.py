class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i, j in enumerate(nums):
            hash_map[j] = i  

        for i, j in enumerate(nums):
            diff = target - j

            if diff in hash_map and i != hash_map[diff]:
                return [i, hash_map[diff]]

            hash_map[diff] = i

