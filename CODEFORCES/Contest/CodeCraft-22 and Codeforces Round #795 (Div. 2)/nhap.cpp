// def tinh(s,n):
//     tong=0
//     for i in range(0,n-1):
//         tong+=int(s[i]+s[i+1])
//     return tong
// t=int(input())
// for _ in range(t):
//     n,k=list(map(int,input().split()))
//     s=input()
    
//     temp=list(s)
    
//     tong=0
//     tinh(s,n);
//     vitringoai=s.find('1')
//     vitritrong=s.rfind('1')

//     trai=vitringoai
//     phai=n-1-vitritrong

//     soluong1=s.count('1')
//     if soluong1==0:
//         print(0)
//     elif soluong1==1:
//         if (vitritrong==vitringoai):
//             if n-vitringoai<=k:
//                 temp[vitringoai]='0'
//                 temp[n-1]='1'
//             else:
                
        
//     else:
//         if vitringoai==n-1:
//             pass
//         else:
//             if k>=phai:
//                 temp[vitringoai],temp[n-1]=temp[n-1],temp[vitringoai]
//                 k-=phai
//         if vitritrong==0:
//             pass
//         else:
//             if k>=trai:
//                 temp[vitritrong],temp[0]=temp[0],temp[vitritrong]
//                 k-=trai
//         m="".join(temp)
//         print(tinh(m,n))
    
        


#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    long long t;
    cin>>t;
    while (t--){
        long long n,k;
        cin>>n>>k;
        string chuoi;
        cin>>chuoi;
        chuoi=" "+chuoi;
        int vitringoai=-1,vitritrong=-1;
        for (int i=1; i<=n; i++)
        if (chuoi[i]=='1') 
        {
            vitringoai=i;
            break;
        }
        for (int i=n; i>=1; i--)
        if (chuoi[i]=='1') 
        {
            vitritrong=i;
            break;
        }
        if (vitringoai==-1 && vitritrong==-1)
        {
             cout<<0;
        }
        else 
        {
            if (vitringoai==vitritrong) 
            {
                if (n-vitringoai<=k) 
                {
                    chuoi[vitringoai]='0';
                    chuoi[n]='1';
                } else 
                if (vitringoai-1<=k) 
                {
                    chuoi[vitringoai]='0';
                    chuoi[1]='1';
                }
            } else 
            {
                if (n-vitritrong<=k) 
                {
                    chuoi[vitritrong]='0';
                    chuoi[n]='1';
                    k-=(n-vitritrong);
                }
                if (vitringoai-1<=k)
                {
                    chuoi[vitringoai]='0';
                    chuoi[1]='1';
                    
                }
            }
            long long ketqua=0;
            for (int i=1; i<n; i++) 
            {
                ketqua+=(chuoi[i]-'0')*10 + (chuoi[i+1]-'0');
            }
            cout<<ketqua;
        }
        cout<<"\n";
    }
}