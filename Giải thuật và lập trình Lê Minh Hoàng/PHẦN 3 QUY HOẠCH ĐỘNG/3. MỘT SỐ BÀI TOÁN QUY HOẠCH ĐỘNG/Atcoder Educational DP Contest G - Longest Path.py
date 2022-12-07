#N: đỉnh, M: cạnh

N,M=list(map(int,input().split()))

thanhpho=[]
for i in range(0,N+1):
    thanhpho.append([])

for i in range(0,M):
    a,b=list(map(int,input().split()))
    thanhpho[b].append(a)

dp=[]
for i in range(0,N+1):
    dp.append([])
    for j in range(0,N+1):
        dp[i].append(0)

#dp[i][j]: Độ dài đường đi dài nhất đến thành phố j sử dụng từ thành phố [1...i]
res=0
"""
#include <bits/stdc++.h>

using namespace std;

vector<int> dp(100001);
vector<vector<int>> adj(100001);

int dfs(int x) {
	if (dp[x]) return dp[x];
	for (auto e : adj[x]){
			dp[e] = dfs(e);
			dp[x] = max(dp[e] + 1, dp[x]);
	}
	return dp[x];
}

int main(){
	int n,m;
	cin >> n >> m;

	for(int i = 0; i < m; ++i) {
		int a, b;
		cin >> a >> b;
		a--; b--;
		adj[a].push_back(b);
	}

	for (int i = 0; i < n; ++i) {
		dfs(i);
	}

	int ans = 0;

	for (int i = 0;i < n; ++i) {
		ans = max(dp[i], ans);
	}

	cout << ans;
}
"""