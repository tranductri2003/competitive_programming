#include<cstdio>
#include<algorithm>
#include<cstdlib>
using namespace std;
typedef long long ll;
const int N=1000010,M=2000010;
int T,C,n,m,root,x,y,i,g[N],v[N<<1],nxt[N<<1],ed;
int st[N],en[N],size[N],dfn;
int son[N],top[N],d[N],f[N];
inline void add(int x,int y){
  v[++ed]=y;nxt[ed]=g[x];g[x]=ed;
}
void dfs(int x){
  size[x]=1;
  for(int i=g[x];i;i=nxt[i])if(v[i]!=f[x]){
    f[v[i]]=x,d[v[i]]=d[x]+1;
    dfs(v[i]);
    size[x]+=size[v[i]];
    if(size[v[i]]>size[son[x]])son[x]=v[i];
  }
}
void dfs2(int x,int y){
  st[x]=++dfn;top[x]=y;
  if(son[x])dfs2(son[x],y);
  for(int i=g[x];i;i=nxt[i])if(v[i]!=son[x]&&v[i]!=f[x])dfs2(v[i],v[i]);
  en[x]=dfn;
}
inline int lca2(int x,int y){
  int t;
  while(top[x]!=top[y])t=top[y],y=f[top[y]];
  return x==y?t:son[x];
}
inline int ask(int x){
  if(root==x)return n;
  if(st[x]>st[root]||en[x]<en[root])return size[x];
  return n-size[lca2(x,root)];
}
void check(int x){
  if(x<1||x>n)exit(0);
}
int main(){
  scanf("%d",&T);
  for(C=1;C<=T;C++){
    printf("Case #%d:\n",C);
    scanf("%d%d%d",&n,&m,&root);
    check(root);
    for(ed=dfn=0,i=1;i<=n;i++)g[i]=0;
    for(i=1;i<=n;i++)size[i]=son[i]=top[i]=f[i]=d[i]=0;
    for(i=1;i<n;i++){
      //x=i+1;y=rand()%i
      scanf("%d%d",&x,&y);
      check(x);
      check(y);
      add(x,y),add(y,x);
    }
    dfs(1);
    dfs2(1,1);
    while(m--){
      scanf("%d%d",&x,&y);
      check(y);
      if(x==0)root=y;
      else{
        printf("%d\n",ask(y));
      }
    }
  }
}