class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict()
        for num in nums :
            if num in result :
                result[num]+=1
            else :
                result[num] = 1

        ans = (sorted(result, key=result.get, reverse=True))

        return ans[:k]