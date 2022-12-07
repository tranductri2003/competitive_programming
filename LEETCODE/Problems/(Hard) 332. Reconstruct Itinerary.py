from collections import defaultdict


class Solution(object):
    def DFS(self, airport):
        while self.adj_list[airport]:
            destination = self.adj_list[airport].pop()
            self.DFS(destination)
        self.route.append(airport)

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.adj_list = defaultdict(list)
        self.route = []
        for source, destination in tickets:
            self.adj_list[source].append(destination)
        for source in self.adj_list:
            self.adj_list[source].sort(reverse=True)

        self.DFS("JFK")
        self.route = self.route[::-1]
        return self.route


t = Solution()
print(t.findItinerary(
    [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
