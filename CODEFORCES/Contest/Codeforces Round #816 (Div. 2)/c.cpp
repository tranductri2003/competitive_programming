#include <bits/stdc++.h>
using namespace std;


int main()
{
    a[0]=a[n+1]=1000000;
        for (int i=1;i<=n;i++)
        {
            long long f,g;
            if (a[i]!=a[i-1]) f=i;
            else f=1;
            g=n-i+1;
            res=res+f*g;
        }
        while(q--)
        {
            long long pos,x;
            cin>>pos>>x;
            if (a[pos]!=a[pos-1] && a[pos-1]==x)
            {
                res=res-(pos*(n-pos+1));
                res=res+(n-pos+1);
            }
            else if (a[pos]==a[pos-1] && a[pos-1]!=x)
            {
                res=res+(pos*(n-pos+1));
                res=res-(n-pos+1);
            }
            if (a[pos]!=a[pos+1] && a[pos+1]==x)
            {
                res=res-((pos+1)*(n-pos));
                res=res+(n-pos);
            }
            else if (a[pos]==a[pos+1] && a[pos+1]!=x)
            {
                res=res+((pos+1)*(n-pos));
                res=res-(n-pos);
            }
            a[pos]=x;
            cout<<res<<'\n';
        }
}