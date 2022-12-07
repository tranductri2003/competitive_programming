#include<bits/stdc++.h>
using namespace std;


int N;
vector<int> mang[1001];


int main()
{
    ios::sync_with_stdio(0); cin.tie(NULL); cout.tie(NULL);
	while(true)
    {

        scanf("%d",&N);
        if(N == 0)break;
        int a,b;

        queue<int> Q;

        for(int i = 0; i < N; i++)
        {

            scanf("%d %d",&a,&b);
            if(a == b)continue;

            if(a > b)
            {
                swap(a,b);
            }

            mang[i].push_back(a);
            mang[i].push_back(b);
            Q.push(i);
        }

        int res = 0;

        while(!Q.empty())
        {

            int now = Q.front();
            Q.pop();

            int next = Q.front();

            mang[next].push_back(mang[now][0]);
            mang[now].erase(mang[now].begin());

            res++;

            if(mang[now].size() > 0)
            {
                Q.push(now);
            }

            sort(mang[next].begin(),mang[next].end());
            if(mang[next].size() == 2)
            {

                if(mang[next][0] == mang[next][1])
                {
                    mang[next].clear(); 
                    Q.pop();
                }

            }
            else
            { 

                if(mang[next][0] == mang[next][1])
                {

                    int tmp = mang[next][2];
                    mang[next].clear();
                    mang[next].push_back(tmp);

                }
                else if(mang[next][1] == mang[next][2])
                {

                    int tmp = mang[next][0];
                    mang[next].clear();
                    mang[next].push_back(tmp);

                }
            }
        }

        printf("%d\n",res);


    }
}



