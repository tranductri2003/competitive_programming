#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

bool is_power_of(ll a, ll b)
{
    for (ll i = a; i <= b; i *= a)
    {
        if (i == b)
            return true;
    }
    return false;
}

int main()
{
    int n;
    cin >> n;

    vector<ll> array_a(n + 1);
    vector<ll> array_b(n + 1);
    vector<int> visited(n + 1, 0);
    ll ans1 = 0;

    for (int i = 1; i <= n; i++)
    {
        cin >> array_a[i];
    }

    for (int i = 1; i <= n; i++)
    {
        cin >> array_b[i];
    }

    ans1 = array_a[1];

    for (int i = 2; i <= n; i++)
    {
        ll max_sum = 0;
        ll current_sum = 0;

        if (!visited[i])
        {
            vector<ll> multiples;
            int k = 0;

            for (ll j = i; j <= n; j *= i)
            {
                multiples.push_back(j);
                visited[j] = 1;
            }

            int total_combinations = 1 << multiples.size();

            for (int combination = 0; combination < total_combinations; combination++)
            {
                current_sum = 0;
                vector<ll> selected_elements;

                for (int l = 0; l < multiples.size(); l++)
                {
                    if (combination & (1 << l))
                    {
                        current_sum += array_a[multiples[l]];
                        selected_elements.push_back(multiples[l]);
                    }
                }

                for (int x = 0; x < selected_elements.size(); x++)
                {
                    for (int y = 0; y < selected_elements.size(); y++)
                    {
                        if (selected_elements[x] > selected_elements[y] && is_power_of(selected_elements[y], selected_elements[x]))
                        {
                            current_sum -= array_b[selected_elements[x]];
                        }
                    }
                }

                max_sum = max(max_sum, current_sum);
            }
        }

        ans1 += max_sum;
    }

    cout << ans1;
    return 0;
}
