#include <bits/stdc++.h>
using namespace std;

inline void debugLocal()
{
    if (!fopen("input.txt", "r"))
        return;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
}

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    debugLocal();

    int n, m, cur_time = 1;
    cin >> n >> m;
    map<string, string> server_dns, client_dns;
    map<int, string> client_cache_time;

    bool hacked = false;
    while (n--)
    {
        cur_time++;
        int type;
        cin >> type;
        if (type == 1)
        {
            string name, ip;
            cin >> name >> ip;
            server_dns[name] = ip;
        }
        else
        {
            string name;
            cin >> name;
            if (server_dns.find(name) == server_dns.end())
                continue;
            if (hacked)
                continue;
            if (client_dns.find(name) != client_dns.end())
            {
                string pre = client_dns[name];
                if (pre != server_dns[name])
                    hacked = true;
            }
            else
            {
                if (client_dns.size() >= m)
                {
                    pair<int, string> far = *client_cache_time.begin();
                    client_cache_time.erase(client_cache_time.begin());
                    client_dns.erase(client_dns.find(far.second));
                }
                client_dns.insert({name, server_dns[name]});
                client_cache_time.insert({cur_time, name});
            }
        }
    }

    cout << (hacked ? "Warning: Possible DNS Poisoning detected!" : "Everything looks ok!") << endl;

    return 0;
}