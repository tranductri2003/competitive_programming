#include <bits/stdc++.h>
using namespace std;

int main()
{

    int n, c, max_val = 0;
    string s;
    map<string, int> cnt;
    cin >> n >> c;
    for (int i = 0; i < n; i++)
    {
        cin >> s;
        int pos = 0;
        for (int j = 0; j < c; j++)
            if (s[j] == '*')
                pos = j;
        for (int j = 0; j < 26; j++)
        {
            s[pos] = 'a' + j;
            cnt[s]++;
            max_val = max(max_val, cnt[s]);
        }
    }
    for (auto p : cnt)
    {
        if (p.second == max_val)
        {
            cout << p.first << ' ' << p.second << endl;
            break;
        }
    }

    return 0;
}