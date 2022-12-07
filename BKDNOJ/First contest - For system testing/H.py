def printParenthesis(str, n):
    if(n > 0):
        _printParenthesis(str, 0,
                        n, 0, 0)
    return

res=[]
def _printParenthesis(str, pos, n,
                    open, close):

    if(close == n):
        temp=[]
        for i in str:
            temp.append(i)
        temp="".join(temp)
        res.append(temp)
        return
    else:
        if(open > close):
            str[pos] = ')'
            _printParenthesis(str, pos + 1, n,
                            open, close + 1)
        if(open < n):
            str[pos] = '('
            _printParenthesis(str, pos + 1, n,
                            open + 1, close)


n,k=list(map(int,input().split()))
n=n//2
str = [""] * n*2
printParenthesis(str, n)

res.sort()
print(res[k-1])

