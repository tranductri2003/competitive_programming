#include <iostream>
#include <vector>
using namespace std;
const int N = 4e5 + 100;
vector <int> adj[N] , dp[N];
vector <pair<int,int>> sv[N];
int n , q , R;
int avail[N] , a[N], b[N];
void dfs(int u,int fu){
    avail[u]++;
    dp[u].push_back(1);
    for (int i = 0; i < sv[u].size(); i++)
        if (avail[sv[u][i].first] > 0) sv[u][i].second = 0;
    int k = 0;
    for (auto v : adj[u])
        if (v != fu){
            dfs(v,u);
            k++;
            for (int i = 0; i < sv[u].size(); i++)
                if (avail[sv[u][i].first] > 0 && sv[u][i].second == -1) sv[u][i].second = k;
            int s = 0;
            for (auto x : dp[v]) s = s + x;
            dp[u].push_back(s);
        }
}
void ques(){
    cin >> n >> q >> R;
    for (int i = 1; i < n; i++){
        int u ,v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    int px = R;
    for (int i = 1; i <= q; i++){
        cin >> a[i] >> b[i];
        if (a[i] == 0) px = b[i];
        else sv[b[i]].push_back({px,-1});
    }
    dfs(R,-1);
    /*for (int i = 1; i <= n; i++){
        cout << i << " : " ;
        for (auto x : dp[i]) cout << x << " ";
        cout << "\n";
        for (auto x : sv[i])
            cout << x.first << " -> " << x.second << "\n";
    }*/
    for (int w = 1; w <= q; w++)
        if (a[w] == 0) R = b[w];
        else{
            if (b[w] == R){
                cout << n << "\n";
            }
            else
            for (int i = 0; i < sv[b[w]].size(); i++)
                if (sv[b[w]][i].first == R){
                    int sum = 0;
                    if (sv[b[w]][i].second == 0){
                        for (auto x : dp[b[w]]) sum = sum + x;
                        cout << sum << "\n";
                    }
                    else
                    cout << n - dp[b[w]][sv[b[w]][i].second] << "\n";
                    break;
                }
        }
    for (int i = 1; i <= n; i++){
        adj[i].clear();
        dp[i].clear();
        sv[i].clear();
        avail[i] = 0;
    }
    return;
}
int T;
int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    cin >> T;
    int zzz = 0;
    while (T--){
        zzz++;
        cout << "Case #" << zzz << ":\n";
        ques();
    }
    return 0;
}