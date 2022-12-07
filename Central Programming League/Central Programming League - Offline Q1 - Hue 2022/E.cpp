#include<bits/stdc++.h>
using namespace std;


const int N = 1e5 + 7;

int a[N];

int main(){

    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);

    freopen("inp.txt", "r", stdin);

    int n,m; cin>>n>>m;

    for(int i=0;i<n;i++) cin>>a[i];

    vector<int> v;

    for (int i = 0;i<n;++i)
    {
        int cnt = 0;

        for (int j = 2; j*j<=a[i];++j){
            if (a[i] % j == 0) { 
                ++cnt; 
                v.push_back(j); 
                v.push_back(a[i]/j);
            }
        }

        if (cnt == 0) v.push_back(a[i]);
    }



    bool D[N] = {0};

    for (auto x:v){
        D[x] = true;
    }

    vector<int> vs;

    for (int i = 2;i<N;++i) if (D[i]) vs.push_back(i);

    bool DS[N] = {0};

    for (auto x:vs){

        for (int i = x; i < N; i += x) DS[i] = true;

    }

    vector<int> res;

    for (int i = 1;i<=m;++i)
        if (DS[i]==0) res.push_back(i);
    
    cout << res.size() << endl;

    for (auto x:res) cout << x << endl;

} 
