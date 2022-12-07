#include <bits/stdc++.h>
using namespace std;

long long a[1000000];
bool kt = true;
long long res = 0;
void merge(int l, int key, int r)
{

    if (l != r)
    {
        if (a[key + 1] - a[key] != 1)
            res++;
        if (abs(a[l] - a[r]) != 1 && abs(a[key] - a[key + 1]) != 1)
        {
            kt = false;
        }
    }
    sort(a + l, a + r + 1);
}
void merge_sort(int l, int r)
{
    if (l < r)
    {
        merge_sort(l, (l + r) / 2);
        merge_sort((l + r) / 2 + 1, r);
        merge(l, (l + r) / 2, r);
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long t;
    cin >> t;
    while (t--)
    {
        long long n;
        cin >> n;
        kt = true;
        res = 0;
        for (int i = 1; i <= n; i++)
            cin >> a[i];
        merge_sort(1, n);
        if (!kt)
            cout << -1;
        else
            cout << res;
        cout << "\n";
    }
}