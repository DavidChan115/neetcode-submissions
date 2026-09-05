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
        # i = 0, j = 3  
        # i = 1, j = 4

        for i, j in enumerate(nums):
            
            diff = target - j # diff = 7 - 3 = 4

            if diff in hash_map:
                return [hash_map[diff], i]

            # hash_map冇diff呢個數就加入去, key係list嘅value, value係list嘅index
            hash_map[j] = i

            # 呢句唔可以放喺check diff喺唔喺hash map之前，因為





