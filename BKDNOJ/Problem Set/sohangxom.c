/* https://bkdnoj.dut.udn.vn/public/practice_problem.php?id=Demo5A */


#include <stdio.h>
#include <math.h>

int main()


{
    int a,b,c;
    scanf("%d %d %d",&a,&b,&c);
    if (a%c==b%c)
    {
        printf("YES");
    }
    else
    {
        printf("NO");
    }
}