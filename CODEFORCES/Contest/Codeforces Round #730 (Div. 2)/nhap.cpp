#include <iostream>
using namespace std;

int countprimefactors(long long int n)
{
	int k = 0;
	if (n == 1)
	{
		return k;
	}
	else
	{
		long long int i = 2;
		while (n != 1)
		{
			while (n % i == 0)
			{
				n = n / i;
				if (n % i != 0)
				{
					k++;
				}
			}
			i++;
		}
		return k;
	}
}

void factorize(long long int n)
{
	if (n == 1)
	{
		return;
	}
	else
	{
		long long int i = 2;
		while (n != 1)
		{
			long long dem = 0;
			while (n % i == 0)
			{
				n = n / i;
				dem++;
			}
			if (dem >= 1)
			{
				cout << i << " " << dem << endl;
			}
			i++;
		}
	}
}
int main()
{
	long long int n;
	cin >> n;
	cout << countprimefactors(n) << endl;
	factorize(n);
	return 0;
}
