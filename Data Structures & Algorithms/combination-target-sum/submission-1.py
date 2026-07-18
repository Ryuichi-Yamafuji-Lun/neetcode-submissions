class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []
        def bt(total:int, idx:int):
            if total == target:
                ans.append(subset.copy())
                return
            if total > target or idx >= len(nums):
                return
            subset.append(nums[idx])
            bt(total + nums[idx], idx)
            subset.pop()
            bt(total, idx + 1)
            return
        bt(0,0)
        return ans