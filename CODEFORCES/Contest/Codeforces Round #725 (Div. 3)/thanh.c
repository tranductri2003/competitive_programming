#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int compare (const void* x, const void* y)
{
    const int* a=(int*) x;
    const int* b=(int*) y;
    if ( *a> *b)
    {
        return 1;
    }
    else if (*a<*b)
    {
        return -1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    unsigned long long P,Q;
    scanf("%llu %llu",&P,&Q);

    unsigned long long mang[Q+2];
    mang[0]=1;
    for (int i = 1; i <=Q; i++)
    {
        scanf("%llu",&mang[i]);
    }
    mang[Q+1]=P+1;
    
    qsort(mang,Q+2,sizeof(unsigned long long),compare);


    unsigned long long res=0;
    for (int i =2; i<Q+2; i++)
    {
        res+=mang[i]-2;
    }
    printf("%llu",res);
    
    
    
    
}