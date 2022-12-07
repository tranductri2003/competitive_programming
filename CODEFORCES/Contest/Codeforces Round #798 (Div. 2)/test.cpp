#include<stdio.h>
void out(int s[],int n, int k)
{
	for (int i=1;i<=k;i++)
	{
		printf("%d",s[i]);
	}
	printf("\n");
}
void hv(int i,int s[],int n,int check[], int k)
{
	for (int j=1;j<=n;j++)
	{
		if (check[j]==1)
		{
			s[i]=j;
			check[j]=0;
			if (i==k) 
			{
				out(s,n,k);
			}
			else
			{
				 hv(i+1,s,n,check,k);
			}
			check[j]=1;
		}
}
}
int main()
{
	int n,k;
	scanf("%d %d",&n,&k);
	int s[n+1],check[n+1];
	for (int i=1;i<=n;i++) check[i]=1;
	hv(1,s,n,check,k);
}
