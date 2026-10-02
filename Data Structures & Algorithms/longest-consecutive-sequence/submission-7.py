class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dup = set(nums)
        result = [0]
        beg = []

        for i in dup:
            if i - 1 not in dup:
                beg.append(i)
        #print(beg)
        for n in beg:
            j = n
            res = 1
            while(j+1 in dup):
                res+=1
                j+=1
                #print("j:",j,"res:",res)
            result.append(res)
        result.sort(reverse=True)
        return result[0]


        