class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ind = {}
        res = []
        for n,i in enumerate(strs):
            sorted_i = "".join(sorted(i))
            if sorted_i in ind:
                ind[sorted_i].append(n)
            else:
                ind[sorted_i] = [n]
        
        for count, (key,value) in enumerate(ind.items()):
            res.append([])
            for i in value:
                res[count].append(strs[i])

        return res    

        