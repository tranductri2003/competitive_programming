#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
const int M = 1e6 + 5;

int ancestor[M];
int played[M];

int a[N], b[N];
int n, m;

int ans[N];

int find(int x)
{
    return ancestor[x] == x ? x : ancestor[x] = find(ancestor[x]);
}

void join(int x, int y)
{
    x = find(x);
    y = find(y);
    ancestor[y] = x;
}

int main()
{
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &a[i], &b[i]);
    }
    for (int i = 1; i <= m; i++)
    {
        played[i] = -1;
        ancestor[i] = i;
    }

    int temp = -1;
    for (int i = 0;; i = (i + 1) % n)
    {
        if (played[a[i]] == -1)
        {
            played[a[i]] = i;
            if (played[b[i]] == -1)
            {
                join(b[i], a[i]);
            }
        }

        else if (played[b[i]] == -1)
        {
            played[b[i]] = i;
        }
        else
        {
            temp = i;
            break;
        }
    }

    for (int i = 1; i <= m; i++)
    {
        int root = find(i);
        // if (i == 1)
        if (played[root] == -1)
        {
            ans[temp]++;
        }
        else
        {
            ans[played[root]]++;
        }
    }
    for (int i = 0; i < n; i++)
    {
        printf("%d\n", ans[i]);
    }
}