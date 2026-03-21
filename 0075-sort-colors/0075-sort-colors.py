class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        current = 0

        while current <= right:
            if nums[current] == 0:
                # Swap with element at left boundary and expand 0s region
                nums[current], nums[left] = nums[left], nums[current]
                left += 1
                current += 1
            elif nums[current] == 2:
                # Swap with element at right boundary and shrink unprocessed region
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
                # Do not increment current as the swapped element needs to be examined
            else:
                # Found a 1: already in correct position, just move forward
                current += 1
        