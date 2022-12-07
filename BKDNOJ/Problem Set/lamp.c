/*https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=FC51_LAMP */

#include<stdio.h>

int main()
{
    int N,q,l,r;
    scanf("%d %d",&N,&q);
    int lamp[N+1];

    for (int i=1;i<=N;i++)
    {
        lamp[i]=-1;
    }

    for (int i=1;i<=q;i++)
    {
        scanf("%d %d",&l,&r);
        for (int j=l;j<=r;j++)
        {
            lamp[j]=lamp[j]*-1;
        }
    }
    
    for (int i=1;i<=N;i++)
    {
        if (lamp[i]==-1)
        {
            printf("0 ");
        }
        else
        {
            printf("1 ");
        }
    }
}
