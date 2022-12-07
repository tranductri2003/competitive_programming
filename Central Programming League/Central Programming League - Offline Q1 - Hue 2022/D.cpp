#include <bits/stdc++.h>
using namespace std;

int main(){

    int n, x, y; cin>>n>>mx>>mn;

    int l = 0, r = 0;

    vector<int> vx, vy;

    int a[n + 1];

    int msx = 0, msy = 0;

    for (int i = 0; i < n; i++) {
        
        cin>>a[i];

        msx = max(msx, a[i]);
        msy = min(msy, a[i]);

        if (msx > mx || msy < mn) lmn = i, lmx = i;
        
        /// L - min(lmn, lmx) + 1  


        if (a[i] == mn) lmn = i;
        if (a[i] == mx) lmx = i;

    }

}