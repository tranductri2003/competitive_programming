#include <bits/stdc++.h>
#define FORn(i, n) for (int i = 1; i <= (n); i++)
using namespace std;
float n, k, a[100005], l = 1, r = 0;
bool kt(int x)
{
    int dem = 0;
    FORn(i, n) dem += a[i] / x;
    return dem >= k;
}
int main()
{
    cin >> n >> k;
    FORn(i, n)
    {
        cin >> a[i];
        r = max(r, a[i]);
    }
    while (l <= r)
    {
        int mid = (l + r) / 2;
        if (kt(mid))
            l = mid + 1;
        else
            r = mid - 1;
    }
    printf("%.2f", l - 1);
}