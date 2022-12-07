#include <bits/stdc++.h>
using namespace std;
#define mp make_pair
long long a[1000001];
bool check[1000001];
vector<long long> d[1000001];
void dfs(long long u)
{
	queue<int> q;
	check[u] = false;
	q.push(u);
	while (q.empty() == false)
	{
		int dinh = q.front();
		q.pop();
		for (int i = 0; i < d[dinh].size(); i++)
		{
			if (check[d[dinh][i]])
			{
				check[d[dinh][i]] = false;
				q.push(d[dinh][i]);
			}
		}
	}
}

int main()
{
	int n, k;
	cin >> n >> k;
	int u, v;
	for (int i = 1; i <= n; i++)
		check[i] = true;
	for (int i = 1; i <= k; i++)
	{
		cin >> u >> v;
		d[u].push_back(v);
		d[v].push_back(u);
	}
	int sothanhphanlienthong = 0;
	for (int i = 1; i <= n; i++)
		if (check[i])
		{
			sothanhphanlienthong++;
			dfs(i);
		}
	if (sothanhphanlienthong == 1)
		cout << "-" << (k - (n - 1)) << endl;
	else
		cout << "+" << sothanhphanlienthong - 1 << endl;
}