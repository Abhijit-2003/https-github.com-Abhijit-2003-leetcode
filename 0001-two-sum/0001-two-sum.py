class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for index, num in enumerate(nums) :
            complaints = target - num
            if complaints in map :
                return list([map[complaints], index])
            else :
                map[num] = index

        return list()