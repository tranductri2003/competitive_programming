#include <bits/stdc++.h>
using namespace std;

const int MAX = 1000	;

int N,M;               
int res;            
int bando[MAX][MAX];     

bool checked[MAX][MAX];
bool Doi;           

int Row[8] = {-1,-1,-1, 0,0, 1,1,1};
int Col[8] = {-1, 0, 1,-1,1,-1,0,1};

void BFS(int row, int col)
{
	checked[row][col] = true;

	for(int i = 0; i < 8; i++)
	{
		int r = row + Row[i];
		int c = col + Col[i];

		if(r >= 0 && r < N && c >= 0 && c < M)
		{
			if(Doi && bando[r][c] > bando[row][col]) Doi = false;
			if(bando[r][c] == bando[row][col] && !checked[r][c]) BFS(r, c);
		}
	}
}

int main()
{
	cin >> N >> M;
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++)
		{
			cin >> bando[i][j];
			checked[i][j] = false;
		}
	for(int i = 0; i < N; i++)
		for(int j = 0; j < M; j++)
			if(!checked[i][j])
			{
				Doi = true;
				BFS(i, j);
				if(Doi) res++;
			}

	cout << res << endl;

	return 0;
}