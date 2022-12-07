#include<iostream>
#include<vector>
using namespace std;
const long long maxwei = 1e11;
int n,limit, wei,val,sumval;
int main(){
    cin >> n >> limit;
 
    vector<long long> Max(100001, maxwei);
    Max[0] = 0;
    for (int i = 0; i < n; ++i){
        cin >> wei >> val;
        sumval+=val;
        for (int j = sumval; j >= val; --j)
            Max[j]= min(Max[j], Max[j - val] + wei);
    }
	for(val= sumval; val>0; --val){
    	if(Max[val]<=limit)
            return cout<<val, 0;
	}
}