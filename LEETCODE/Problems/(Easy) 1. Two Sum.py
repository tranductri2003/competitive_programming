from collections import defaultdict,Counter
class Solution(object):
    def twoSum(self, nums, target):
        res=[]
        check=defaultdict(lambda:-1)
        count=Counter(nums)
        stop=0
        for num in nums:
            check[num]=1
        for i in range(len(nums)):
            if stop==1:
                break
            if check[target-nums[i]]==1:
                if target-nums[i]!=nums[i]:
                    res.append(i)
                    res.append(nums.index(target-nums[i]))
                    break
                else:
                    if count[nums[i]]==1:
                        pass
                    else:
                        for j in range(len(nums)-1,-1,-1):
                            if nums[j]==nums[i]:
                                res.append(i)
                                res.append(j)
                                stop=1
                                break
                                
                        
        return res

        
        
        
        
