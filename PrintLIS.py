class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #num =10
        #res = [()10]
        self.sol =[]
        N = len(nums)
        def f(i,prev,res):
            if i>=N:
                if res not in self.sol:
                    self.sol.append(res[:])
                return
            if  prev ==-1 or nums[i] > nums[prev]:
                res.append((i,nums[i]))
                f(i+1,i,res)
            if (i,nums[i]) in res:
                res.remove((i,nums[i]))
            f(i+1,prev,res)
        
        f(0,-1,[])
        mp = map(len,self.sol)
        i = mp.index(max(mp))
        print [each[1] for each in self.sol[i]]
        return max(mp)
