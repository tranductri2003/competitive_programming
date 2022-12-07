#include <bits/stdc++.h>
using namespace std;
string MaxNum(string chuoi, int k)
{
    string ketqua;
    for (int i=0;i<(int)chuoi.length(); ++i)
    {
        while(ketqua.size()>0 && k>0 && chuoi[i]>ketqua.back())
        {
            ketqua.pop_back();
            k=k-1;
        }
        ketqua.push_back(chuoi[i]);
    }
    return ketqua.substr(0, ketqua.length()-k);
}
int main()
{
    string chuoi;
    int k,n;
    cin>>n>>k;
    cin >> chuoi;
    cout << MaxNum(chuoi, k);
}