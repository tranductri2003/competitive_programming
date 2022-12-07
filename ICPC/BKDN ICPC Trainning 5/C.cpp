#include <bits/stdc++.h>
using namespace std;

long long n, k, i;
char s[200007];

bool check(long long left, long long right, int pos)
{
    if (left == right)
        return true;
    if (s[pos] == '=')
        return false;

    if (s[pos] == '<')
    {
        long long mid = (left + right + 1) / 2;
        return check(left, mid - 1, pos + 1);
    }
    if (s[pos] == '>')
    {
        long long mid = (left + right - 1) / 2;
        return check(mid + 1, right, pos + 1);
    }
}

void solve(long long left, long long right, int pos)
{
    if (s[pos] == '=')
    {
        assert(left == right);
        printf("%lld\n", left);
        return;
    }

    if (s[pos] == '<' && check(left, right - 1, pos + 1))
    {
        printf("%lld ", right);
        solve(left, right - 1, pos + 1);
        return;
    }
    if (s[pos] == '>' && check(left + 1, right, pos + 1))
    {
        printf("%lld ", left);
        solve(left + 1, right, pos + 1);
        return;
    }

    if (s[pos] == '<')
    {
        long long mid = (left + right + 1) / 2;
        printf("%lld ", mid);
        solve(left, mid - 1, pos + 1);
        return;
    }
    if (s[pos] == '>')
    {
        long long mid = (left + right - 1) / 2;
        printf("%lld ", mid);
        solve(mid + 1, right, pos + 1);
        return;
    }
}

int main()
{
    scanf("%lld%lld", &n, &k);
    scanf("%s", s);
    int length = strlen(s);

    if (s[length - 1] == '=' && length > n)
    {
        printf("-1\n");
        return 0;
    }
    if (s[length - 1] != '=' && length >= n)
    {
        printf("-1\n");
        return 0;
    }

    if (s[length - 1] != '=')
    {
        long long left = 1;
        long long right = n;
        for (i = 0; i < length; i++)
        {
            if (s[i] == '<')
                printf("%lld ", right--);
            if (s[i] == '>')
                printf("%lld ", left++);
        }
        return 0;
    }

    if (!check(1, n, 0))
    {
        printf("-1\n");
        return 0;
    }
    solve(1, n, 0);
}