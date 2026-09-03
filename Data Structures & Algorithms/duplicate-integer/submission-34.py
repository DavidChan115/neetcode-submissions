class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen_set = set()

        for i in nums:     # for loop唔一定要用range的
            
            if i in seen_set:
                return True
            else:
                seen_set.add(i)

        return False
        
        