import collections


class Solution(object):
    def maxDistance(self, grid):
        n = len(grid)
        queue = collections.deque()
        visited = collections.defaultdict(lambda: False)
        res = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j, 0))
                    visited[(i, j)] = True

        res = -1
        while queue:
            i, j, d = queue.popleft()
            if grid[i][j] == 0:
                res = max(res, d)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x = i+dx
                y = j+dy
                if 0 <= x < n and 0 <= y < n and visited[(x, y)] == False:
                    queue.append((x, y, d+1))
                    visited[(x, y)] = True
                    # As soon as we assign d-smallest distance to the nearest land,
                    # we have to mark it as visited because if we don't do that,
                    # this place will be revisited later with bigger d!!!

        return res


t = Solution()
print(t.maxDistance([[0, 0, 0], [0, 0, 0], [1, 1, 1]]))
