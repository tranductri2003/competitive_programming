#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 10;
int T, n, k, cnt[26], ans;
char a[N], b[N];
int main()
{
    cin >> T;
    while (T--)
    {
        memset(cnt, 0, sizeof(cnt));
        ans = 0;
        scanf("%d%d%s%s", &n, &k, a, b);
        for (int i = 0; i < n; i++)
        {
            if (a[i] == b[i])
                ans++;
            else
                cnt[a[i] - 'a']++;
        }
        sort(cnt, cnt + 26);
        for (int i = 0; i < 26 - k; i++)
        {
            ans -= cnt[i];
        }
        printf("%d\n", ans);
    }
}
// #include <bits/stdc++.h>
// using namespace std;

// const int N = 100001;
// int t, n, m, d, p[N], a[N], res;
// int main()
// {
//     cin >> t;
//     while (t--)
//     {
//         cin >> n >> m >> d;
//         for (int i = 0; i < n; i++)
//         {
//             cin >> p[i];
//         }
//         for (int i = 0; i < m; i++)
//         {
//             cin >> a[i];
//         }
//         int res = 0, pre = -1;
//         for (int i = 0; i < m; i++)
//         {
//             int pos = -1;
//             for (int j = 0; j < n; j++)
//             {
//                 if (p[j] == a[i])
//                 {
//                     pos = j;
//                     break;
//                 }
//             }
//             if (pre != -1)
//             {
//                 if (pos <= pre)
//                 {
//                     res += (pre - pos + d) / d;
//                 }
//                 pre = pos;
//             }
//             else
//             {
//                 pre = pos;
//             }
//         }
//         cout << res << endl;
//     }
// }
