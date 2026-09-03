class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        nums.sort() # sort the list = xx.sort()  (xx is a list)

        for i in range(1, len(nums)): # 個list skip index 0, 由 index 1 開始, 唔由index 1開始, 下面i - 1會out of range
            if nums[i] == nums[i - 1]: # if index 1 == index 0, if index 2 == index 1
                return True
        return False


# Python built-in sorting complexity:
# time: Best = O(n), Average/Worst = O(n log n) 
# space: Best/Average/Worst = O(n)

# so the time complexity must be O(n log n) (bottleneck) rather than O(n) even though there is only 1 loop

                
        
        