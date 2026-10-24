class Solution:
    def helper(self, nums, start, end, dp):
        if start >= end :
            return 0

        if dp[start] != -1 :
            return dp[start]

        take = nums[start] + self.helper(nums, start+2, end, dp)
        not_take = self.helper(nums, start+1, end, dp)

        dp[start] = max(take, not_take)

        return dp[start]

    def rob(self, nums: list[int]) -> int:
        dp = [-1]*len(nums)

        return self.helper(nums, 0, len(nums), dp)
        