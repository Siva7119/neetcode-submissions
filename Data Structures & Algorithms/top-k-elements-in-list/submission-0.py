class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #from collections import defaultdict
        rept = dict()
        res = []
        for i in nums:
            if i in rept:
                rept[i]+=1
            else:
                rept[i] = 1

        rep = list(sorted(rept.items(), key =lambda item : item[1], reverse = True))
        res = [item[0] for item in rep]

        return(res[:k])
            



        