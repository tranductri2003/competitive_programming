#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <map>
using namespace std;
const long long mod = 1e9 + 7;
struct Matrix
{
    long long data[35][35];
    int col, row;
    Matrix() {}
    Matrix(int _row, int _col)
    {
        row = _row;
        col = _col;
        memset(data, 0, sizeof(data));
    }
    const long long * operator [] (int row) const         //жидиЯТБъдЫЫуЗћ
    {
        return data[row];
    }
    long long * operator [] (int row)
    {
        return data[row];
    }
};
Matrix operator * (const Matrix &m1, const Matrix &m2)
{
    Matrix ans_met(m1.row, m2.col);
    int i, j, k;
    for (i = 0; i < m1.row; i++)
    {
        for (j = 0; j < m2.col; j++)
        {
            for (k = 0; k < m1.col; k++)
            {
                ans_met[i][j] = (ans_met[i][j] + (m1[i][k] * m2[k][j]) % mod) % mod;
            }
        }
    }
    return ans_met;
}
Matrix operator ^(const Matrix &mm, long long q)
{
    Matrix ans_met(mm.row, mm.col);
    Matrix ret(mm.row, mm.col);
    int i, j;
    for (i = 0; i < ans_met.row; i++)
    {
        for (j = 0; j < ans_met.col; j++) ret[i][j] = mm[i][j];
        ans_met[i][i] = 1;
    }
    while (q > 0)
    {
        if (q % 2 == 1) ans_met = ans_met * ret;
        ret = ret * ret;
        q /= 2;
    }
    return ans_met;
}
Matrix operator + (const Matrix &m1, const Matrix &m2)
{
    Matrix ans_met(m1.row, m2.col);
    int i, j;
    for (i = 0; i < m1.row; i++)
    {
        for (j = 0; j < m1.col; j++)
        {
            ans_met[i][j] = (m1[i][j] + m2[i][j]) % mod;
        }
    }
    return ans_met;
}

Matrix fab(2, 2), mat(3, 3);

long long solve(long long q)
{
    q++;              //注意要移位
    Matrix tmp(3, 3);
    tmp = mat ^ q;
    return tmp[0][2]-1;
}

int main()
{
    int i, j;
    int t;
    scanf("%d", &t);
    int cases = 1;
    while (t--)
    {
        long long l, r, k;
        scanf("%lld%lld%lld", &l, &r, &k);
        if (l%k != 0) l += k - (l%k);      //处理余数
        if (r%k != 0) r -= r % k;
        fab[0][0] = 1;
        fab[0][1] = 1;
        fab[1][0] = 1;
        fab[1][1] = 0;
        fab = fab ^ k;

        mat[0][0] = fab[0][0];         //构造求和矩阵
        mat[0][1] = fab[0][1];
        mat[1][0] = fab[1][0];
        mat[1][1] = fab[1][1];
        mat[0][2] = 1;
        mat[1][2] = 1;
        mat[2][0] = 0;
        mat[2][1] = 0;
        mat[2][2] = 1;
        long long le = solve(l / k - 1), ri = solve(r / k);
        long long ans = ((ri - le) % mod + mod) % mod;
        printf("Case %d: ", cases++);
        printf("%d\n", ans);
    }
    return 0;
}