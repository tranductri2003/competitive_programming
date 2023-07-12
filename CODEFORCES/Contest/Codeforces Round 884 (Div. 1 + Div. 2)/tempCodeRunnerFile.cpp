#include <bits/stdc++.h>
using namespace std;

bool is_prime(int x)
{
    if (x <= 1)
    {
        return false;
    }
    for (int i = 2; i * i <= x; i++)
    {
        if (x % i == 0)
        {
            return false;
        }
    }
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> nums(n);
        for (int i = 0; i < n; i++)
        {
            nums[i] = i + 1;
        }
        sort(begin(nums), end(nums), [](int a, int b)
             { return !is_prime(a) && is_prime(b); });

        for (int i = 0; i < n; i++)
        {
            cout << nums[i] << " ";
        }
        cout << endl;
    }
}