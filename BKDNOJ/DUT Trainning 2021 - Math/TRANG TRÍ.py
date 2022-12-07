
testcase=int(input())
M=10**6+3
giaithua=[0]*(M+100)

a=1

for i in range(1,M+1):
    a=(a*i)%(M)
    giaithua[i]=a

for test in range(0,testcase):
    N,X=list(map(int,input().split()))

    res=X%M
    if N>=M:
        res=0
    else:
        res=((res*giaithua[N]))%M
    print(res)
"""
#include<bits/stdc++.h>

using namespace std;

const long long M=1e6+3;

long long d, x,y;

void extendedEuclid(long long a, long long b){// sau ham nay sẽ trả về d là gcd, x, y trong ax+by=d;
    if (b==0){
        d=a;
        x=1;
        y=0;
    }
    else {
        extendedEuclid(b,a%b);
        int temp =x;
        x=y;
        y=temp-(a/b)*y;
    }
}

long long pow(long long a, long long b){
    if (b==0){
        return 1;
    }
    else if (b%2==1){
        return (pow((a*a)%M,b/2)*a)%M;
    }
    else if (b%2==0){
        return pow((a*a)%M,b/2)%M;
    }
    return 1;
}

long long gcd(long long a,long long b){
    extendedEuclid(a,b);
    return d;
}

long long modInv(long long a, long long m){
    extendedEuclid(a,m);
    return(x%m+m)%m;
}

long long N,X;
long long arr[M+100];
int main(){
    int t;
    long long resu=1;
    for (int i=1;i<M+1;i++){
        resu=(resu*i)%M;
        arr[i]=resu;
    }
    cin>>t;
    for (int i =0;i<t; i++){
        cin>>N>>X;
        long long res=1;
        res=X%M;
        if(N>=M) res=0;
        else {
            res=(res*arr[N])%M;
        } 
        cout<<res<<endl;
    }
    return 0; 
}
"""