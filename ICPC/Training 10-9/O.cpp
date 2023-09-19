#include <bits/stdc++.h>
using namespace std;
char s[11][11];
int ship[11][11];
map<int, int> mp;
int main()
{
    for (int i = 1; i <= 10; i++)
    {
        for (int j = 1; j <= 10; j++)
        {
            cin >> s[i][j];
        }
    }
    bool ship4 = false;
    for (int i = 1; i <= 10; i++)
    {
        for (int j = 1; j <= 10; j++)
        {
            if (s[i][j] == '#' && !ship[i][j])
            {
                int cnt = 1;
                for (int k = j + 1; k <= j + 3; k++)
                {
                    if (s[i][k] == '#' && !ship[i][k])
                        cnt++;
                }
                if (cnt == 4)
                {
                    ship4 = true;
                    for (int k = j; k <= j + 3; k++)
                    {
                        ship[i][k] = 1;
                        mp[1] = 4;
                    }
                }
            }
            if (ship4 == true)
                break;
        }
        if (ship4 == true)
            break;
    }
    if (!ship4)
    {
        for (int i = 1; i <= 10; i++)
        {
            for (int j = 1; j <= 10; j++)
            {
                if (s[i][j] == '#' && !ship[i][j])
                {
                    int cnt = 1;
                    for (int k = i + 1; k <= i + 3; k++)
                    {
                        if (s[k][j] == '#' && !ship[k][j])
                            cnt++;
                    }
                    if (cnt == 4)
                    {
                        for (int k = i; k <= i + 3; k++)
                        {
                            ship[k][j] = 1;
                            mp[1] = 4;
                        }
                    }
                }
                if (ship4 == true)
                    break;
            }
            if (ship4 == true)
                break;
        }
    }
    int ship3 = 0;
    for (int i = 1; i <= 10; i++)
    {
        for (int j = 1; j <= 10; j++)
        {
            if (s[i][j] == '#' && !ship[i][j])
            {
                int cnt = 1;
                for (int k = j + 1; k <= j + 2; k++)
                {
                    if (s[i][k] == '#' && !ship[i][k])
                        cnt++;
                }
                if (cnt == 3)
                {
                    ship3++;
                    for (int k = j; k <= j + 2; k++)
                    {
                        ship[i][k] = ship3 + 1;
                        mp[ship3 + 1] = 3;
                    }
                }
            }
            if (ship3 == 2)
                break;
        }
        if (ship3 == 2)
            break;
    }
    if (ship3 < 2)
    {
        for (int i = 1; i <= 10; i++)
        {
            for (int j = 1; j <= 10; j++)
            {
                if (s[i][j] == '#' && !ship[i][j])
                {
                    int cnt = 1;
                    for (int k = i + 1; k <= i + 2; k++)
                    {
                        if (s[k][j] == '#' && !ship[k][j])
                            cnt++;
                    }
                    if (cnt == 3)
                    {
                        ship3++;
                        for (int k = i; k <= i + 2; k++)
                        {
                            ship[k][j] = ship3 + 1;
                            mp[ship3 + 1] = 3;
                        }
                    }
                }
                if (ship3 == 2)
                    break;
            }
            if (ship3 == 2)
                break;
        }
    }
    int ship2 = 0;
    for (int i = 1; i <= 10; i++)
    {
        for (int j = 1; j <= 10; j++)
        {
            if (s[i][j] == '#' && s[i][j + 1] == '#' && !ship[i][j] && !ship[i][j + 1])
            {
                ship2++;
                ship[i][j] = ship2 + 3;
                ship[i][j + 1] = ship2 + 3;
                mp[ship2 + 3] = 2;
            }
            if (ship2 == 3)
                break;
        }
        if (ship2 == 3)
            break;
    }
    if (ship2 < 3)
    {
        for (int i = 1; i <= 10; i++)
        {
            for (int j = 1; j <= 10; j++)
            {
                if (s[i][j] == '#' && s[i + 1][j] == '#' && !ship[i][j] && !ship[i + 1][j])
                {
                    ship2++;
                    ship[i][j] = ship2 + 3;
                    ship[i + 1][j] = ship2 + 3;
                    mp[ship2 + 3] = 2;
                }
                if (ship2 == 3)
                    break;
            }
            if (ship2 == 3)
                break;
        }
    }
    int ship1 = 0;
    for (int i = 1; i <= 10; i++)
    {
        for (int j = 1; j <= 10; j++)
        {
            if (s[i][j] == '#' && !ship[i][j])
            {
                ship1++;
                ship[i][j] = ship1 + 6;
                mp[ship1 + 6] = 1;
            }
        }
    }

    int q;
    cin >> q;
    int un = 10, hit = 0, sunk = 0;
    for (int j = 1; j <= q; j++)
    {
        string str;
        int x, y;
        cin >> str >> x >> y;
        cout << str << x << y;
        if (str == "SHOW")
        {
            cout << un << " " << hit << " " << sunk << '\n';
        }
        else
        {
            if (s[x][y] == '#')
            {
                int tau = ship[x][y];
                mp[tau]--;
                if (mp[tau] <= 0)
                    sunk++;
                else
                    hit++;
            }
        }
    }
}