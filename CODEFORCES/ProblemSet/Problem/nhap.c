#include <stdio.h>
#include <math.h>
#define e 0.001

float g(float x)
{
    float res=0;
    res=pow(x+1.0,1.0/3);
    return res;
}

float lap(int *p)
{
    int n=0;

    float x0;
    scanf("%f",&x0);
    float temp;

    temp=g(x0);

    int count=0;
    while (fabs(temp-x0)>=e && count<1000)
    {
        x0=temp;
        temp=g(temp);
        count++;
    }
    if (fabs(temp-x0)>e)    
    {
        *p=0;
        return 0;
    }
    
    *p=1;
    return x0;
}

int main()
{
    int p=0;
    float res=lap(&p);
    if (p==0) 
    {
        printf("Phan ky");
    }
    else
    {
        printf("%f",res);
    }
}