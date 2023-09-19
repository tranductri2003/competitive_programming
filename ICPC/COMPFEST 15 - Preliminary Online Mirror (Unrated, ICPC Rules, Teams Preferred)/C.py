MOD = 998244353

def dfs(node, a, dp, vst):
    vst[node] = 1
    for v, w in a[node]:
        if not vst[v]:
            dfs(v, a, dp, vst)

    topo.append(node)
def main():
    global topo
    global MOD
    n = int(input())
    a = [[] for _ in range(n)]
    dp = [(0, (0, 0))] * (n + 1)

    for i in range(1, n + 1):
        m = int(input())
        for j in range(1, m + 1):
            v, w = map(int, input().split())
            a[i].append((v, w))

    vst = [0] * (n + 1)
    topo = []
    dfs(1, a, dp, vst)



    for x in topo:
        if len(a[x]) == 0:
            dp[x] = (0, (0, 0))
            continue

        curr0, curr1, currVal = 0, 0, 0

        for y, w in a[x]:
            if w == 0:
                curr0 += 1
                currVal += curr1
                currVal %= MOD
            else:
                curr1 += 1
                currVal %= MOD

            currVal += dp[y][0]
            currVal += curr1 * dp[y][1][0]
            currVal %= MOD

            curr0 += dp[y][1][0]
            curr1 += dp[y][1][1]

        dp[x] = (currVal, (curr0, curr1))

    print(dp[1][0])

if __name__ == "__main__":
    main()
