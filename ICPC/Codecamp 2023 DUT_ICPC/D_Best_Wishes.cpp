#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>

const int MAX = 1000000; // Maximum value of D can be 10^6

int main()
{
    int t;
    std::cin >> t;

    std::vector<int> dp(MAX + 1, std::numeric_limits<int>::max());

    dp[1] = 1;

    for (int i = 2; i <= MAX; i++)
    {
        if (i % 2 == 0)
        {
            dp[i] = std::min(dp[i], dp[i / 2] + 1);
        }
        if (i % 3 == 0)
        {
            dp[i] = std::min(dp[i], dp[i / 3] + 1);
        }
        if (i - 1 >= 1)
        {
            dp[i] = std::min(dp[i], dp[i - 1] + 1);
        }
    }

    while (t--)
    {
        int n;
        std::cin >> n;

        std::cout << dp[n] << '\n';

        std::vector<int> seq;

        int i = n;
        while (i > 1)
        {
            seq.push_back(i);
            if (i - 1 >= 1 && dp[i] == 1 + dp[i - 1])
            {
                i = i - 1;
            }
            else if (i % 2 == 0 && dp[i] == 1 + dp[i / 2])
            {
                i = i / 2;
            }
            else if (i % 3 == 0 && dp[i] == 1 + dp[i / 3])
            {
                i = i / 3;
            }
        }

        seq.push_back(1);

        std::reverse(seq.begin(), seq.end());

        for (int i = 0; i < seq.size(); i++)
        {
            std::cout << seq[i] << ' ';
        }
        std::cout << '\n';
    }

    return 0;
}
