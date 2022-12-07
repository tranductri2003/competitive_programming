#include <bits/stdc++.h>
using namespace std;

vector<int> prefix_function(string s)
{
    int n = s.length();
    vector<int> pi(n);
    for (int i = 1; i < n; i++)
    {
        int j = pi[i - 1];
        while (j > 0 && s[i] != s[j])
            j = pi[j - 1];
        if (s[i] == s[j])
            j++;
        pi[i] = j;
    }
    return pi;
}

int main()
{

    string s1, s2, tmp;
    cin >> s1;
    cin >> s2;
    int ans = 0;
    for (int i = s1.length() - 1; i >= 0; i--)
    {
        tmp = s1[i] + tmp;
        string tt = tmp + '#' + s2;
        vector<int> ttt = prefix_function(tt);
        for (int j = tmp.length(); j < ttt.size(); j++)
            ans = max(ans, ttt[j]);
    }
    cout << ans << endl;

    return 0;
}