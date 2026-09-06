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

            # 呢句唔可以放喺check diff喺唔喺hash map之前，因為你要check左佢喺唔喺hash map先，避免重覆，例子：
            # [3, 2, 4], target 6
            # 如果入曬落dict先：{3:0, 2:1, 4:2}
            # 然後計diff：i = 0, j = 3，diff = 6 - 3 = 3，
            # 3 已經in dict, return [hash_map[diff], i] = [0, 0] <- 重覆index
            # 呢到出錯因為你用左個element放入去hash map, 然後又loop呢個element去check佢喺唔喺hash map到，用左個element兩次所以錯

# time complexity: one for loop, loop through n elements in the list = O(n)
# space complexity: dictionary with n elements in the list = O(n)