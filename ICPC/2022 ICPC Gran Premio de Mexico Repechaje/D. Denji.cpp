#include <bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;

#define ordered_set tree<pair<long long, int>, null_type, less<pair<long long, int>>, rb_tree_tag, tree_order_statistics_node_update>

int main()
{

    ordered_set os;

    long long m, t, a, b;
    vector<long long> add_op(1e5 + 1, 0);
    int rt = 0;
    cin >> m;
    while (m--)
    {
        rt++;
        cin >> t;
        if (t == 1)
        {
            cin >> a;
            os.insert({a, rt});
            add_op[rt] = a;
        }
        else if (t == 2)
        {
            cin >> b;
            os.erase(os.lower_bound({add_op[b], 1}));
        }
        else if (t == 3)
        {
            cin >> b >> a;
            os.erase(os.lower_bound({add_op[b], 1}));
            add_op[b] += a;
            os.insert({add_op[b], rt});
        }
        else
        {
            cin >> b;
            cout << os.order_of_key({add_op[b], 1}) << endl;
        }
        // cout << "Array after time = " << rt << ": ";
        // for (auto p : os)
        //     cout << p.first << ' ';
        // cout << endl;
    }

    return 0;
}