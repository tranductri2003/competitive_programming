s = input()
res = []

so0 = s.count('0')
so1 = s.count('1')

if so0 > so1:
    res = '1'*len(s)
if so1 > so0:
    res = '0'*len(s)
if so1 == so0:
    if s[0] == '0':
        res = '1'+(len(s)-1)*'0'
    else:
        res = '0'+(len(s)-1)*'1'

print(res)
