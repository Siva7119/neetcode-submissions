class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        suf = [1]
        res = []
        j = len(nums) - 1
        for i,n in enumerate(nums):
            if i > 0:
                prod = nums[i-1] * pre[i-1]
                pre.append(prod)
            k = j - i
            if k < j:
                prod1 = nums[k+1] * suf[i-1]
                suf.append(prod1)
        suf.reverse()
        #print(suf) 
        res = [x * y for x,y in zip(pre,suf)]

        return res   


        