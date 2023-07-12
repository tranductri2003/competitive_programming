#include <iostream>
#include <vector>

using namespace std;
int modulo;
struct Node
{
    int topLeft;
    int topRight;
    int bottomLeft;
    int bottomRight;

    Node(int tl = 0, int tr = 0, int bl = 0, int br = 0)
    {
        topLeft = tl;
        topRight = tr;
        bottomLeft = bl;
        bottomRight = br;
    }
};

class SegmentTree
{
private:
    int n;
    int size;
    vector<Node> a;
    Node baseMatrix;
    vector<Node> tree;

public:
    SegmentTree(int n, vector<Node> &a)
    {
        this->n = n;
        this->size = n * 4;
        this->a = a;
        this->baseMatrix = Node(1, 0, 0, 1);
        this->tree.resize(this->size, this->baseMatrix);
    }

    Node merge(const Node &nodeA, const Node &nodeB)
    {
        int topLeft = nodeA.topLeft * nodeB.topLeft % modulo + nodeA.topRight * nodeB.bottomLeft % modulo;
        int topRight = nodeA.topLeft * nodeB.topRight % modulo + nodeA.topRight * nodeB.bottomRight % modulo;
        int bottomLeft = nodeA.bottomLeft * nodeB.topLeft % modulo + nodeA.bottomRight * nodeB.bottomLeft % modulo;
        int bottomRight = nodeA.bottomLeft * nodeB.topRight % modulo + nodeA.bottomRight * nodeB.bottomRight % modulo;
        return Node(topLeft % modulo, topRight % modulo, bottomLeft % modulo, bottomRight % modulo);
    }

    void build(int id, int l, int r)
    {
        if (l == r)
        {
            tree[id] = a[l];
        }
        else
        {
            int mid = (l + r) / 2;
            build(2 * id + 1, l, mid);
            build(2 * id + 2, mid + 1, r);
            tree[id] = merge(tree[2 * id + 1], tree[2 * id + 2]);
        }
    }

    Node getValue(int id, int l, int r, int u, int v)
    {
        if (v < l || u > r)
        {
            return baseMatrix;
        }
        if (u <= l && r <= v)
        {
            return tree[id];
        }
        else
        {
            int mid = (l + r) / 2;
            Node leftNode = getValue(2 * id + 1, l, mid, u, v);
            Node rightNode = getValue(2 * id + 2, mid + 1, r, u, v);
            return merge(leftNode, rightNode);
        }
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n, m;
    cin >> modulo >> n >> m;

    vector<Node> a(n);
    for (int i = 0; i < n; i++)
    {
        int topLeft, topRight, bottomLeft, bottomRight;
        cin >> topLeft >> topRight;
        cin >> bottomLeft >> bottomRight;
        string space;
        getline(cin, space); // Read the remaining newline character
        a[i] = Node(topLeft, topRight, bottomLeft, bottomRight);
    }

    SegmentTree st(n, a);
    st.build(0, 0, n - 1);

    for (int i = 0; i < m; i++)
    {
        int l, r;
        cin >> l >> r;
        l--;
        r--;
        Node temp = st.getValue(0, 0, n - 1, l, r);
        cout << temp.topLeft %
                    modulo
             << " " << temp.topRight % modulo << '\n';
        cout << temp.bottomLeft % modulo << " " << temp.bottomRight % modulo << '\n';
        cout << '\n';
    }

    return 0;
}
