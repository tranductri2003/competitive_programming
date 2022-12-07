#include <bits/stdc++.h>

using namespace std;

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

int n, m;
vector<vector<int>> c;
vector<vector<char>> trace;
vector<int> mx = {0, 1, -1, 0}, my = {-1, 0, 0, 1};
vector<char> mm = {'R', 'U', 'D', 'L'};

int charToInt(char mc) {
    if (mc == '.')
        return 0;
    if (mc == 'E')
        return 1;
    if (mc == 'X')
        return 2;
    return 3;
}

bool canGo(int x, int y) {
    if (x < 0 || x >= n || y < 0 || y >= m)
        return false;
    return c[x][y] < 2;
}

void bfs(int x, int y) {
    queue<pair<int, int>> q;
    //cout << corToString(x, y) << endl;
    trace[x][y] = 'E';
    q.push({x, y});
    while (!q.empty()) {
        pair<int, int> u = q.front(); q.pop();
        for (int i = 0; i < 4; i++) {
            pair<int, int> v = u;
            v.first += mx[i], v.second += my[i];
            //cout << v.first << ' ' << v.second << endl;
            if (!canGo(v.first, v.second) || trace[v.first][v.second] != '?')
                continue;
            q.push(v);
            trace[v.first][v.second] = mm[i];
        }
    }
}

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int x, y, q;
    string s;
    cin >> n >> m;
    cin.ignore();
    c.assign(n, vector<int>(m));
    trace.assign(n, vector<char>(m, '?'));
    for (int i = 0; i < n; i++) {
        getline(cin, s);
        for (int j = 0; j < m; j++) {
            c[i][j] = charToInt(s[j]);
            if (s[j] == 'E')
                x = i, y = j;
        }
    }
    //cout << x << ' ' << y << endl;
    bfs(x, y);

    cin >> q;
    while (q--) {
        cin >> x >> y;
        x--, y--;
        if (!canGo(x, y)) {
            if (c[x][y] == 2)
                cout << "X" << endl;
            else
                cout << "W" << endl;
        } else
            cout << trace[x][y] << endl;
    }

    return 0;
}
