#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	std::ios::sync_with_stdio(false);
	//ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int n, q, x;
	cin >> n >> q;
	n++;
	//int temp[n];
	int ans[n];
	ans[0] = 0;
	for(int i=1;i<n;i++){
	    cin >> x;
	    //temp[i] = x;
	    ans[i] = ans[i-1]^x;
	}
	//int temp[n];

    for (int i=0;i<n;i++){cout << ans[i] << endl;}
	while(q--){
	    cin >> x;
	    cout << ans[x%(n)] << endl;
	}
	
}
