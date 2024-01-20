#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <ctime>

using namespace std;

#include <bits/stdc++.h>

using namespace std;

struct Node
{
    int val, lazy;
    Node(int dat, int lzy)
    {
        val = dat;
        lazy = lzy;
    }
};

struct SegTree
{

    Node SKIP_VALUE = Node(0, 0);
    int ts;
    vector<Node> ST;

    SegTree(int tsize)
    {
        ts = 1;
        while (ts < tsize)
            ts *= 2;
        ST.assign(2 * ts + 2, SKIP_VALUE);
    }

    Node mergeN(Node n1, Node n2)
    {
        return Node(max(n1.val, n2.val), 0);
    }

    void pushDown(int id)
    {
        int lz = ST[id].lazy;
        ST[id * 2].val += lz;
        ST[id * 2].lazy += lz;
        ST[id * 2 + 1].val += lz;
        ST[id * 2 + 1].lazy += lz;
        ST[id].lazy = 0;
    }

    void build(int id, int l, int r, vector<int> &a, int n)
    {
        if (l >= n)
        {
            ST[id] = SKIP_VALUE;
            return;
        }
        if (l == r)
        {
            ST[id] = Node(a[l], 0);
            return;
        }
        int mid = (l + r) / 2;
        build(id * 2, l, mid, a, n);
        build(id * 2 + 1, mid + 1, r, a, n);
        ST[id] = mergeN(ST[id * 2], ST[id * 2 + 1]);
    }

    void build(vector<int> &a, int n)
    {
        build(1, 0, ts, a, n);
    }

    void update(int id, int l, int r, int u, int v, int val)
    {
        if (v < l || r < u)
        {
            return;
        }
        if (u <= l && r <= v)
        {
            ST[id].val += val;
            ST[id].lazy += val;
            return;
        }
        pushDown(id);
        int mid = (l + r) / 2;
        update(id * 2, l, mid, u, v, val);
        update(id * 2 + 1, mid + 1, r, u, v, val);
        ST[id] = mergeN(ST[id * 2], ST[id * 2 + 1]);
    }

    void update(int l, int r, int val)
    {
        update(1, 0, ts, l, r, val);
    }

    Node get(int id, int l, int r, int u, int v)
    {
        if (v < l || r < u)
        {
            return SKIP_VALUE;
        }
        if (u <= l && r <= v)
        {
            return ST[id];
        }
        pushDown(id);
        int mid = (l + r) / 2;
        return mergeN(get(id * 2, l, mid, u, v), get(id * 2 + 1, mid + 1, r, u, v));
    }

    int get(int l, int r)
    {
        Node rs = get(1, 0, ts, l, r);
        return rs.val;
    }
};

// Note: LazySegTree index 0

struct TreapNode
{
    TreapNode *left;
    TreapNode *right;
    int priority;
    int size;
    char value;
    bool flip;

    TreapNode(char x)
    {
        left = right = nullptr;
        priority = rand();
        size = 1;
        value = x;
        flip = false;
    }
};

int treapSize(TreapNode *treap)
{
    return treap ? treap->size : 0;
}

void treapPush(TreapNode *treap)
{
    if (treap && treap->flip)
    {
        treap->flip = false;
        swap(treap->left, treap->right);
        if (treap->left)
            treap->left->flip ^= 1;
        if (treap->right)
            treap->right->flip ^= 1;
    }
}

void treapSplit(TreapNode *treap, TreapNode *&left, TreapNode *&right, int k)
{
    if (!treap)
        left = right = nullptr;
    else
    {
        treapPush(treap);
        if (treapSize(treap->left) < k)
        {
            treapSplit(treap->right, treap->right, right, k - treapSize(treap->left) - 1);
            left = treap;
        }
        else
        {
            treapSplit(treap->left, left, treap->left, k);
            right = treap;
        }
        treap->size = treapSize(treap->left) + treapSize(treap->right) + 1;
    }
}

void treapMerge(TreapNode *&treap, TreapNode *left, TreapNode *right)
{
    if (!left)
        treap = right;
    else if (!right)
        treap = left;
    else
    {
        treapPush(left);
        treapPush(right);
        if (left->priority < right->priority)
        {
            treapMerge(left->right, left->right, right);
            treap = left;
        }
        else
        {
            treapMerge(right->left, left, right->left);
            treap = right;
        }
        treap->size = treapSize(treap->left) + treapSize(treap->right) + 1;
    }
}

void treapPrint(TreapNode *treap)
{
    if (!treap)
        return;
    treapPush(treap);
    treapPrint(treap->left);
    cout << treap->value;
    treapPrint(treap->right);
}

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n, k;
        cin >> n >> k;

        TreapNode *treap = nullptr;

        string s;
        cin >> s;

        for (char c : s)
        {
            treapMerge(treap, treap, new TreapNode(c));
        }

        vector<int> leftBounds(k), rightBounds(k);

        for (int i = 0; i < k; i++)
        {
            cin >> leftBounds[i];
        }

        for (int i = 0; i < k; i++)
        {
            cin >> rightBounds[i];
        }

        int q;
        cin >> q;
        vector<int> queries(q);

        for (int i = 0; i < q; i++)
        {
            cin >> queries[i];
        }

        for (int i = 0; i < q; i++)
        {
            int val = queries[i];
            int index = upper_bound(leftBounds.begin(), leftBounds.end(), val) - leftBounds.begin() - 1;

            int left = min(val, rightBounds[index] + leftBounds[index] - val);
            int right = max(val, rightBounds[index] + leftBounds[index] - val);

            TreapNode *A, *B, *C;
            treapSplit(treap, A, B, left - 1);
            treapSplit(B, B, C, right - left + 1);
            B->flip ^= 1;
            treapMerge(treap, A, B);
            treapMerge(treap, treap, C);
        }

        treapPrint(treap);
        cout << endl;
    }

    return 0;
}
