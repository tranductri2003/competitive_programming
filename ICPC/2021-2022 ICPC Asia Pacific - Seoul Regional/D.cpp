#include <bits/stdc++.h>
using namespace std;

const int MAX = 1010; // maximum number of vertices
set<int> A[MAX];      // A[i] stores all the neighbours of vertex i
int C[MAX];           // this store in which "part" we save vertex i

void impossible()
{ // I just use this to print when I realize its impossible
    printf("impossible\n");
    exit(0);
}

void dfs(int x)
{
    for (int y : A[x])
    {
        if (C[y] == C[x])
            impossible(); // this means the graph is not bipartite
        if (C[y] == 0)
        {
            if (C[x] == 1)
                C[y] = 2;
            else
                C[y] = 1;
            dfs(y);
        }
    }
}

int main()
{
    int n, m;               // number of vertices and edges
    scanf("%d %d", &n, &m); // we read n and m
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i != j)
                A[i].insert(j); // we want to build the complement, so we start adding every edge
        }
    }
    for (int i = 0; i < m; i++)
    { // we read the edges in G and erase them from G^c
        int u, v;
        scanf("%d %d", &u, &v);
        A[u].erase(v);
        A[v].erase(u);
    }
    for (int i = 0; i < n; i++)
    {
        if (C[i] == 0)
        { // if i has not been explored yet we dfs from i
            C[i] = 1;
            dfs(i);
        }
    }
    printf("The set A contains:\n");
    for (int i = 0; i < n; i++)
    {
        if (C[i] == 1)
            printf("%d ", i);
    }
    printf("\nThe set B contains:\n");
    for (int i = 0; i < n; i++)
    {
        if (C[i] == 2)
            printf("%d ", i);
    }
    printf("\n");
}
