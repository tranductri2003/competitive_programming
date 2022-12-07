#include <bits/stdc++.h>
using namespace std;
int main()
{
    char s[10000 + 5];
    gets(s);
    vector<int> data;
    int so0 = 0, so1 = 0, res = 0;

    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] == 'e' || s[i] == 'u' || s[i] == 'o' || s[i] == 'a' || s[i] == 'i')
        {
            data.push_back(1);
            so1 += 1;
        }
        else
        {
            data.push_back(0);
            so0 += 1;
        }
    }

    for (int i = 0; i < strlen(s); i++)
    {
        if (data[i] == 1)
        {
            res += so0;
            so1 -= 1;
        }
        else
        {
            res += so1;
            so0 -= 1;
        }
    }
    cout << res;
}