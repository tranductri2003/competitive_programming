class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        check = []
        for i in range(len(rooms)+1):
            check.append([])
        for i in range(len(rooms)):
            for num in rooms[i]:
                if num != i:
                    check[num].append(i)
        print(check)
        for i in range(1, len(rooms)):
            if check[i] == []:
                return False
        else:
            return True


t = Solution()
t.canVisitAllRooms([[4], [3], [], [2, 5, 7], [1], [], [8, 9], [], [], [6]])
