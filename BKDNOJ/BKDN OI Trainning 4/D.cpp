#include <bits/stdc++.h>
using namespace std;
int check(long s)
{
    for (int i = 1; i * i <= s; i++)
    {
        if ((s - i) % (2 * i + 1) == 0)
        {
            return 1;
        }
    }
    return 0;
}

int main()
{
    int n;
    scanf("%d", &n);
    int res = 0;
    for (int i = 0; i < n; i++)
    {
        int s = 0;
        scanf("%d", &s);
        if (check(s) == 0)
        {
            res += 1;
        }
    }
    printf("%d\n", res);
}