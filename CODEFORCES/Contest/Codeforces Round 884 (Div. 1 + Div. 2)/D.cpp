#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <string>

std::vector<int> getDivisors(int n)
{
    std::vector<int> divisors;
    int i = 1;
    while (i * i <= n)
    {
        if (i * i == n)
        {
            divisors.push_back(i);
        }
        else
        {
            if (n % i == 0)
            {
                divisors.push_back(i);
                divisors.push_back(n / i);
            }
        }
        i++;
    }
    return divisors;
}

std::string generateString(int n)
{
    std::vector<int> divisors = getDivisors(n);
    std::sort(divisors.begin(), divisors.end());

    std::unordered_map<int, bool> check;
    for (int num : divisors)
    {
        check[num] = true;
    }

    int temp = 0;
    for (int i = 1; i <= n; i++)
    {
        if (!check[i])
        {
            temp = i;
            break;
        }
    }
    if (temp == 0)
    {
        temp = n + 1;
    }

    std::string res = "";
    for (int i = 0; i < n; i++)
    {
        res += 'a' + (i % temp);
    }

    return res;
}

int main()
{
    int t;
    std::cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n;
        std::cin >> n;

        std::string result = generateString(n);
        std::cout << result << std::endl;
    }

    return 0;
}
