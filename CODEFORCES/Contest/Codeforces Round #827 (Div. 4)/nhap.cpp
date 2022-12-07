#include <bits/stdc++.h>
using namespace std;
int main()
{
    int var_x = 3;
    int *ptr = &var_x;
    cout << ptr << " " << *ptr << endl;
    *(++ptr) = 2;
    cout << *ptr;
}