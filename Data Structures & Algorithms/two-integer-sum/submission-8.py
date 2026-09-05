class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # enumerate(iterable, start=0)

        # fruits = ["apple", "banana", "cherry"]

        # for index, fruit in enumerate(fruits):
        #      print(f"Index {index}: {fruit}")

        # Index 0: apple
        # Index 1: banana

        # fruit會根據前面loop緊嘅index去轉內容 


        hash_map = {}

        # nums = [3,4,5,6], target = 7
        # i = 0, j = 3  i = 1, j = 4

        for i, j in enumerate(nums):
            

            difference = target - j

            if difference in hash_map:
                return [hash_map[difference], i]
            hash_map[j] = i





