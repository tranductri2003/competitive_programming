#include <bits/stdc++.h>
using namespace std;

inline void debugLocal()
{
    if (!fopen("input.txt", "r"))
        return;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
}

vector<vector<int>> nextPos;

int jumpNext(int pos, char c)
{
    if (nextPos[c].size() == 0 || nextPos[c][0] <= pos)
        return 1e9;
    int l = 0, r = nextPos[c].size() - 1, m;
    while (l < r)
    {
        m = (l + r + 1) / 2;
        if (nextPos[c][m] > pos)
            l = m;
        else
            r = m - 1;
    }
    return nextPos[c][l];
}

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    debugLocal();

    int t;
    string s1, s2;
    cin >> t;
    while (t--)
    {
        cin >> s1 >> s2;
        nextPos.clear();
        nextPos.resize(303);
        for (int i = 0; i < s1.length(); i++)
            nextPos[s1[i]].push_back(i);
        for (int i = 0; i < 303; i++)
            reverse(nextPos[i].begin(), nextPos[i].end());
        int lans = 0, rans = s1.length() - 1;
        for (int i = 0; i < s1.length(); i++)
        {
            nextPos[s1[i]].pop_back();
            if (s1[i] != s2[0])
                continue;
            int curPos = i;
            bool iok = true;
            for (int j = 1; j < s2.size(); j++)
            {
                curPos = jumpNext(curPos, s2[j]);
                if (curPos >= s1.length())
                {
                    iok = false;
                    break;
                }
            }
            // cout << pos[i] << "->" << curPos << endl;
            if (!iok)
                break;
            if ((rans - lans) > (curPos - i))
                rans = curPos, lans = i;
        }
        // cout << lans << ' ' << rans << endl;
        cout << s1.substr(lans, rans - lans + 1) << endl;
    }

    return 0;
}
