#include <bits/stdc++.h>
using namespace std;
const long long INF = 2000000000000000000LL;
struct Edge{
    int v;
    long long w;
};
struct Node{
    int u;
    long long Dist_u;
};
struct cmp{
    bool operator() (Node a, Node b) {
        return a.Dist_u > b.Dist_u;
    }
};
void dijkstraSparse(int n, int s, vector<vector<Edge>> &E, vector<long long> &D) {
    D.resize(n, INF);
    vector<bool> P(n, 0);
    
    D[s] = 0;
    priority_queue<Node, vector<Node>, cmp> h; 
    h.push({s, D[s]});
    
    while(!h.empty()) {
        Node x = h.top();
        h.pop();
        
        int u = x.u;
        if(P[u] == true) 
            continue;
            
        P[u] = true; 
        for(auto e : E[u]) {
            int v = e.v;
            long long w = e.w; 
            
            if(D[v] > D[u] + w) {
                D[v] = D[u] + w;
                h.push({v, D[v]});
            }
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long n,m,l,u;
    cin>>n>>m>>l>>u;
    vector<vector<Edge>> E(n);
    vector<long long> D;
    for (int i=1; i<=m; i++){
        int x,y,len;
        cin>>x>>y>>len;
        E[x].push_back({y,len});
        E[y].push_back({x,len});
    }
    dijkstraSparse(n,0,E,D);
    map< pair<int,int> ,bool> ma;
    long long res=0;
    for (int i=0; i<n; i++)
    if (D[i]*2<u) {
        for (auto x:E[i]) {
            int t1=i;
            int t2=x.v;
            if (t1>t2) swap(t1,t2);
            if (ma[{t1,t2}]==false) {
                ma[{t1,t2}]=true;
                res++;
            }
        }
    }
    cout<<res;
}