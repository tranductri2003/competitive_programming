class Solution:
    def totalFruit(self, fruits):

        count, streak, basket1, basket2 = 0, 0, 0, 0

        for i, f in enumerate(fruits):
            if f != fruits[basket1] and f != fruits[basket2]:
                basket1 = streak
                basket2 = i
            if f != fruits[streak]:
                streak = i

            count = max(count, i-basket1+1)

        return count
