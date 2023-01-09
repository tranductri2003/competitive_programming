#include <bits/stdc++.h>
using namespace std;

int n, m;
int c[202][202], dd[202][202];
int mx[4] = {-1, 0, 0, 1}, my[4] = {0, -1, 1, 0};

void dfs(int x, int y, int t)
{
    dd[x][y] = 1;
    for (int i = 0; i < 4; i++)
    {
        int nx = x + mx[i], ny = y + my[i];
        if (nx < 1 || nx > n || ny < 1 || ny > m)
            continue;
        if (dd[nx][ny] != 1 && ((1 << c[nx][ny]) & t) > 0)
            dfs(nx, ny, t);
    }
}

int main()
{

    cin >> n >> m;
    int r1, c1, r2, c2;
    cin >> r1 >> c1 >> r2 >> c2;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            cin >> c[i][j];
            c[i][j]--;
        }
    }

    int min_ans = 11;
    for (int ans = 0; ans < (1 << 10); ans++)
    {
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= m; j++)
                dd[i][j] = 0;
        if (((1 << c[r1][c1]) & ans) > 0)
            dfs(r1, c1, ans);
        if (dd[r2][c2] == 1)
            min_ans = min(min_ans, __builtin_popcount(ans));
    }
    cout << min_ans << endl;

    return 0;
}