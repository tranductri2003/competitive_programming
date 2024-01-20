#include <iostream>
#include <vector>
#include <limits.h>

using namespace std;

struct Node
{
    int value;
    Node *left;
    Node *right;
    Node(int val) : value(val), left(nullptr), right(nullptr) {}
};

Node *buildSegmentTree(vector<int> &array, int start, int end)
{
    if (start == end)
    {
        return new Node(array[start]);
    }

    int mid = start + (end - start) / 2;
    Node *leftNode = buildSegmentTree(array, start, mid);
    Node *rightNode = buildSegmentTree(array, mid + 1, end);

    Node *node = new Node(leftNode->value & rightNode->value);
    node->left = leftNode;
    node->right = rightNode;

    return node;
}

int queryRange(Node *node, int start, int end, int l, int queryEnd)
{
    if (!node || l > end || queryEnd < start)
    {
        return INT_MAX;
    }
    if (l <= start && queryEnd >= end)
    {
        return node->value;
    }

    int mid = start + (end - start) / 2;
    int leftResult = queryRange(node->left, start, mid, l, queryEnd);
    int rightResult = queryRange(node->right, mid + 1, end, l, queryEnd);

    return leftResult & rightResult;
}

void solve()
{
    int n, q;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> a[i];
    }
    cin >> q;

    Node *root = buildSegmentTree(a, 0, n - 1);

    while (q--)
    {
        int l, k;
        cin >> l >> k;
        l--;

        int low = l;
        int high = n - 1;
        int result = -1;

        while (low <= high)
        {
            int mid = low + (high - low) / 2;
            int res = queryRange(root, 0, n - 1, l, mid);

            if (res >= k)
            {
                low = mid + 1;
                result = mid;
            }
            else
            {
                high = mid - 1;
            }
        }

        if (result >= 0)
        {
            result += 1;
        }

        cout << result << " ";
    }
    cout << "\n";

    delete root;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
