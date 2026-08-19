class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = dict()
        for num in nums :
            if num in result :
                result[num]+=1
            else :
                result[num] = 1

        sorted_d = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

        ans = list()
        

        for num, freq in sorted_d.items() :
            ans.append(num)
            k-=1
            if k <=0 : return ans