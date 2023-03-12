class Solution:
    def countGood(self, nums, k):
        res = 0
        val = 0
        mp = {}
        n = len(nums)
        first = 0
        for i in range(n):
            if nums[i] in mp:
                val += mp[nums[i]]
            mp[nums[i]] = 1 + mp.get(nums[i], 0)

            while val >= k:
                res += n - i
                cancel = mp.get(nums[first], 0)
                val -= cancel - 1
                if cancel == 1:
                    mp[nums[first]] = 0
                else:
                    mp[nums[first]] = cancel - 1
                first += 1
        return res
