class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs = sorted(costs)
        res = 0
        while res < len(costs) and coins >= costs[res]:
            coins -= costs[res]
            res += 1
        return res
