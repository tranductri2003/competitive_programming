#include <iostream>
#include <vector>
#include <set>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#define ordered_set tree<pair<int, int>, null_type, less<pair<int, int>>, rb_tree_tag, tree_order_statistics_node_update>
#define endl '\n'

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        vector<int> a(n);
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }

        if (n <= 1)
        {
            cout << 0 << '\n';
        }
        else
        {
            set<int> firstTemp, remain;
            int res = 0;
            remain.insert(a[0]);

            for (int i = 1; i < n; i++)
            {
                auto firstTempIter = firstTemp.lower_bound(a[i]);
                auto remainIter = remain.lower_bound(a[i]);

                if ((firstTempIter == firstTemp.begin()) && (remainIter != remain.begin()))
                {
                    res += 1;
                    firstTemp.insert(a[i]);
                }
                remain.insert(a[i]);
            }

            cout << res << '\n';
        }
    }

    return 0;
}
