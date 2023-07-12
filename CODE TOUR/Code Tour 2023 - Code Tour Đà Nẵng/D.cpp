#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int find_max_value(vector<int> &a, int w1, int w2)
{
    int n = a.size();
    int max_sum = numeric_limits<int>::min();

    for (int i1 = 0; i1 < n - 4; ++i1)
    {
        for (int i2 = i1 + 1; i2 < n - 3; ++i2)
        {
            for (int i3 = i2 + 1; i3 < n - 2; ++i3)
            {
                for (int i4 = i3 + 1; i4 < n - 1; ++i4)
                {
                    for (int i5 = i4 + 1; i5 < n; ++i5)
                    {
                        int current_sum = w1 * (a[i1] + a[i5]) +
                                          w2 * (a[i2] + a[i4]) + a[i3];
                        if (current_sum > max_sum)
                        {
                            max_sum = current_sum;
                        }
                    }
                }
            }
        }
    }

    return max_sum;
}

int find_max_value(vector<int> &a, int w1)
{
    int n = a.size();
    int max_value = numeric_limits<int>::min();

    for (int i1 = 0; i1 < n - 2; ++i1)
    {
        for (int i2 = i1; i2 < n - 1; ++i2)
        {
            for (int i3 = i2 + 1; i3 < n; ++i3)
            {
                int current_value = (a[i1] + a[i3]) * w1 + a[i2];
                if (current_value > max_value)
                {
                    max_value = current_value;
                }
            }
        }
    }

    return max_value;
}

int main()
{
    int n, w1, w2;
    cin >> n >> w1 >> w2;

    vector<int> a(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }

    cout << find_max_value(a, w1, w2) << endl;

    return 0;
}
