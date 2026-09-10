class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        # nums = [3,4,5,6], target = 7
        for i, j in enumerate(nums):
            hash_map[j] = i  
            # 首先入曬nums嘅element落dict, key係real value, value係index
            # 3:1, 4:2, 5:3, 6:4

        for i, j in enumerate(nums):
            diff = target - j

            if diff in hash_map and i != hash_map[diff]:
                return [i, hash_map[diff]]
            # check diff in hash_map去確保呢個diff真係有喺nums到，
            # check i != hash_map[diff]去確保冇用到同一index嘅value

            hash_map[diff] = i
            # 如果diff唔喺hash_map或者diff同hash_map入面嘅value用同一個index,
            # 將diff當一個新entry加入hash_map
