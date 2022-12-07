#include<stdio.h>
void gen(int a[],int n)
{
	int i=n-1;
	int stop=0;
	while (a[i]>a[i+1])
	{
        i--;
	}
	if (i==0) stop=1;
	else
	{
        int k=n;
        while (a[k]<a[i])
        {
            k--;
        }
        int t=a[i];
        a[i]=a[k];
        a[k]=t;
        int l=i+1,r=n;
        while (l<r)
        {
            int temp=a[l];
            a[l]=a[r];
            a[r]=temp;
            l++;
            r--;	
        }
    }
}

void init(int a[],int n)
{
	for (int i=1;i<=n;i++)
	{
		a[i]=i;
	}
}
void out(int a[],int n)
{
	for (int i=1;i<=n;i++)
	printf("%d",a[i]);
	printf("\n");
}
int inlast(int a[],int n)
{
	int i=n-1;
	while (a[i]>a[i+1])
	{
        i--;
	    if (i==-1) break;
	}
	if (i==-1) return 1;
    else return 0;
}

void method(int a[],int n)
{
	  init(a,n);
	  out(a,n);

      while(inlast(a,n)==0)
      {
      	gen(a,n);
      	out(a,n);
	  }
}

int main()
{
     int n;
	 scanf("%d",&n);
	 int a[n+1];
	 method(a,n);	
}
