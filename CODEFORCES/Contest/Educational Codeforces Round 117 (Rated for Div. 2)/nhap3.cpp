#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t--)
	{
	   long long int k,q,x,p,y;
	   double n;
	   cin>>k>>x;
	   p=k*(k+1);
	   p=p/2;
	   if(x<=p)
	   {
	       n=(sqrt(1+8*x)-1)/2;
	       if(n!=(int)n)
	       q=n+1;
	       else
	       q=n;
	       cout<<q<<"\n";
	   }
	   else
	   {
	       x=x-p;
	       y=(k-1)*k;
	       y=y/2;
	       y=y-x;
	       if(y<=0)
	       cout<<(2*k-1)<<"\n";
	       else
	       {
	           n=(sqrt(1+8*y)-1)/2;
	           p=n;
	           p=k-1-p;
	           cout<<(k+p)<<"\n";
	       }
	   }
	}
}