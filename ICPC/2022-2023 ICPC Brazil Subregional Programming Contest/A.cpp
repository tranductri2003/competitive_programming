#include <bits/stdc++.h>
using namespace name
int main()
{
    int n;
    cin>>n;
    string s;
    cin>>s;
    long long res=0;
    int d=0;
    // s='b'+s;
    for (int i=0; i<s.size(); i++)
    if (s[i]=='a') d++; else {
        if (d>=2) res+=d;
        d=0;
    }
    cout<<res;
} // namespace name
