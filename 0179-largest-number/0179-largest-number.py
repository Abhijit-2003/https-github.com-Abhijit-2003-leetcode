class Solution:
    def compare(self, a, b):
            if (a + b) > (b + a):
                return -1  
            elif (a + b) < (b + a):
                return 1  
            else:
                return 0

    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]

        nums_str.sort(key = cmp_to_key(self.compare))

        result =  "".join(nums_str)

        return "0" if result[0] == "0" else result