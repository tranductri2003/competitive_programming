class Solution(object):
    def countOdds(self, low, high):
        start = low+(low+1) % 2
        finish = high-(high+1) % 2
        return (finish-start)//2+1
