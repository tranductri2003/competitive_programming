#include <iostream>
#include <queue>
#include <cstring>
#include <cstdio>
#include <queue>
#include <algorithm>
#include <stack>
#include <vector>

using namespace std;
const int N = 500010;
int cnt[N];//记录个数
int num[N];//记录编号

int main()
{
    int n,k,m;
    scanf("%d %d %d",&n,&k,&m);
    while(m--)
    {
        int a,b;
        cin>>a>>b;
    }
    int key;
    for(int i=1;i<=n*k;i++)
    {
        cin>>key;
        cnt[key]++;
        if(i==n*k)
        {
            cout<<cnt[key];
        }
        else
        {
            cout<<cnt[key]<<" ";
        }
    }
    return 0;
}