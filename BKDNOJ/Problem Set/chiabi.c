/* https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=Demo5B */


#include<stdio.h>

int main()
{
    int n,m;
    long M;
    scanf("%d %d %ld",&n,&m,&M);
    long res=0;
    long dp[n+1][m+1];
    for (int i=0;i<n+1;i++)	
    {
        for (int j=0;j<m+1;j++)
        {
            dp[i][j]=0;
        }
    }
    for (int i=1;i<n+1;i++)
    {
        for (int j=1;j<m+1;j++)
        {
            if (i>j)
            {
                dp[i][j]=(dp[i-j][j]+dp[i][j-1])%M;
            }
            else if (i==j)
            {
               dp[i][j]=(dp[i][j-1]+1)%M;
            }        
            else
            {
                dp[i][j]=(dp[i][j-1])%M;
            }
        }
    }
    res=dp[n][m]%M;
    printf("%ld\n",res);
}

