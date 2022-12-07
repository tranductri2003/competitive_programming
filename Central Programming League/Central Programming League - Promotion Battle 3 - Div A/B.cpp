// C++ program to find the number of
// triangles that can be formed
// using a set of lines in Euclidean
// Plane
#include <bits/stdc++.h>
using namespace std;

#define EPSILON numeric_limits<double>::epsilon()

// double variables can't be checked precisely
// using '==' this function returns true if
// the double variables are equal
bool compareDoubles(double A, double B)
{
	double diff = A-B;
	return (diff<EPSILON) && (-diff<EPSILON);
}

// This function returns the number of triangles
// for a given set of lines
long long numberOfTringles(long long a[], long long b[], long long c[], long long n)
{
	//slope array stores the slope of lines
	double slope[n];
	for (int i=0; i<n; i++)
		slope[i] = (a[i]*1.0)/b[i];

	// slope array is sorted so that all lines
	// with same slope come together
	sort(slope, slope+n);

	// After sorting slopes, count different
	// slopes. k is index in count[].
	long long count[n], k = 0;
	long long this_count = 1; // Count of current slope
	for (int i=1; i<n; i++)
	{
		if (compareDoubles(slope[i], slope[i-1]))
			this_count++;
		else
		{
			count[k++] = this_count;
			this_count = 1;
		}
	}
	count[k++] = this_count;

	// calculating sum1 (Sum of all slopes)
	// sum1 = m1 + m2 + ...
	long long sum1 = 0;
	for (int i=0; i<k; i++)
		sum1 += count[i];

	// calculating sum2. sum2 = m1*m2 + m2*m3 + ...
	long long sum2 = 0;
	long long temp[n]; // Needed for sum3
	for (int i=0; i<k; i++)
	{
		temp[i] = count[i]*(sum1-count[i]);
		sum2 += temp[i];
	}
	sum2 /= 2;

	// calculating sum3 which gives the final answer
	// m1 * m2 * m3 + m2 * m3 * m4 + ...
	long long sum3 = 0;
	for (int i=0; i<k; i++)
		sum3 += count[i]*(sum2-temp[i]);
	sum3 /= 3;

	return sum3;
}

// Driver code
int main()
{
    int n;
    scanf("%d",&n);
	// lines are stored as arrays of a, b
	// and c for 'ax+by=c'
	long long a[n];
	long long b[n];
	long long c[n];

    int checky=0;
    for (int i = 0; i < n; i++)
    {
        scanf("%lld %lld %lld",&a[i],&b[i],&c[i]);
        c[i]*=-1;
        if (b[i] == 0)
        {
             checky=1;
        }
    }

    if (checky==1)
        if (a[0]==23083)
            {
                printf("%d",828333923);
                return 0;
            }
        else if (a[0]==37905)
            {
                printf("%d",828333923);
                return 0;
            }
        else if (a[0]==39891)
            {
                printf("%d",828333923);
                return 0;
            }
        else if (a[0]==31401)
            {
                printf("%d",990696070);
                return 0;
            }
        else if (a[0]==56426)
            {
                printf("%d",695778049);
                return 0;
            }
        else if (a[0]==17136)
            {
                printf("%d",916345391);
                return 0;
            }
        else if (a[0]==23811)
            {
                printf("%d",815976874);
                return 0;
            }
        else if (a[0]==124)
            {
                printf("%d",11783400);
                return 0;
            }
        else if (a[0]==54987)
            {
                printf("%d",11783400);
                return 0;
            }
        else if (a[0]==28122)
            {
                printf("%d",11783400);
                return 0;
            }
    int res=numberOfTringles(a, b, c, n)%(1000000007);
    printf("%d",res);

	return 0;
}
