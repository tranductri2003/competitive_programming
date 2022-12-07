#include <stdio.h>
#include <math.h>

struct Matrix
{
    unsigned long long coef[35][35];
};

struct Matrix showMatrix(struct Matrix a, int n)
{
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            printf("%llu ", a.coef[i][j]);
        }
        printf("\n");
    }
}

struct Matrix initMatrix(int n)
{
    struct Matrix matran;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            scanf("%llu", &matran.coef[i][j]);
        }
    }
    return matran;
}

struct Matrix createMatrix(int n, int mod)
{
    struct Matrix A;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            A.coef[i][j] = 0;
        }
    }
    return A;
}

struct Matrix add(struct Matrix a, struct Matrix b, int n, int mod)
{
    struct Matrix res = createMatrix(n, mod);
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            res.coef[i][j] += a.coef[i][j] + b.coef[i][j];
            res.coef[i][j] %= mod;
        }
    }
    return res;
}

struct Matrix mul(struct Matrix a, struct Matrix b, int n, int mod)
{
    struct Matrix res = createMatrix(n, mod);
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            for (int k = 1; k <= n; k++)
            {
                res.coef[i][j] += a.coef[i][k] * b.coef[k][j] % mod;
                res.coef[i][j] %= mod;
            }
        }
    }
    return res;
}
struct Matrix pw(struct Matrix A, unsigned long long n, unsigned long long k, int mod)
{
    if (k == 1)
    {
        return A;
    }
    struct Matrix Q = pw(A, n, k / 2, mod);
    if (k % 2 == 0)
    {
        return mul(Q, Q, n, mod);
    }
    return mul(mul(Q, Q, n, mod), A, n, mod);
}
struct Matrix solve(struct Matrix A, struct Matrix I, int k, int n, int mod)
{
    if (k == 1)
    {
        return A;
    }
    struct Matrix Q = solve(A, I, k / 2, n, mod);
    struct Matrix P = add(pw(A, n, k / 2, mod), I, n, mod);
    Q = mul(Q, P, n, mod);

    if (k % 2 == 1)
    {
        P = pw(A, n, k, mod);
        Q = add(Q, P, n, mod);
    }
    return Q;
}
struct Matrix unitMatrix(int n, int mod)
{
    struct Matrix unit = createMatrix(n, mod);
    for (int i = 1; i <= n; i++)
    {
        unit.coef[i][i] = 1;
    }
    return unit;
}

int main()
{
    int n, k, mod;
    scanf("%d %d %d", &n, &k, &mod);

    struct Matrix Matrandau = initMatrix(n);
    struct Matrix Matrandonvi = unitMatrix(n, mod);
    struct Matrix resMatrix = solve(Matrandau, Matrandonvi, k, n, mod);

    showMatrix(resMatrix, n);
}
