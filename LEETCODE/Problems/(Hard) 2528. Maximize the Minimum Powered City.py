class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)

        def isGood(minPowerRequired, additionalStations):
            # init windowPower to store power of 0th city (minus stations[r])
            windowPower = sum(stations[:r])
            additions = [0] * n
            for i in range(n):
                # now, windowPower stores sum of power stations from [i-r..i+r], it also means it's the power of city `ith`
                if i + r < n:
                    windowPower += stations[i + r] + additions[i + r]

                if windowPower < minPowerRequired:
                    needed = minPowerRequired - windowPower
                    if needed > additionalStations:  # Not enough additional stations to plant
                        return False
                    # Plant the additional stations on the farthest city in the range to cover as many cities as possible
                    additions[min(n - 1, i + r)] += needed
                    windowPower = minPowerRequired
                    additionalStations -= needed

                if i - r >= 0:  # out of window range
                    windowPower -= stations[i - r] + additions[i - r]

            return True

        left = 0
        # The answer = `right`, when `r = n`, all value of stations are the same!
        right = sum(stations) + k
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if isGood(mid, k):
                ans = mid  # This is the maximum possible minimum power so far
                left = mid + 1  # Search for a larger value in the right side
            else:
                right = mid - 1  # Decrease minPowerRequired to need fewer additional power stations
        return ans
