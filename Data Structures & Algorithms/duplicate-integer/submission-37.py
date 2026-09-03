class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums) 

# set(xx) 可以就咁將 係list嘅xx 轉做 set

# set個特性係會自動remove duplicate, 所以如果set length < list length, 等於有duplicate俾set自動remove左, 就return True

# Time complexity: O(n) because the dominant operation—building the set from the list—requires visiting each of the n elements once
# Space complexity: set = O(n)