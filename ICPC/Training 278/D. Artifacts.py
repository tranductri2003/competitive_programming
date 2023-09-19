# from collections import defaultdict

# data = defaultdict(lambda:0)
# for _ in range(25):
#     s=input()
#     posCong = s.find('+')
#     type = s[:posCong]
#     value = s[posCong+1:]
    
    
#     if "%" in value:
#         value = value[:-1]
#         value = float(value)/100
        
#     data[type] = float(value)

# if data['Crit Rate']>1:
#     data['Crit Rate'] = 1


# data['Crit Rate']+=0.05
# data['Crit DMG Rate']+=0.5


# data['ATK']=1500*(1+data["ATK Rate"])+data['ATK']



# res = data['ATK'] * (1 - (data['Crit Rate'])) + data['ATK'] *(1 + (data['Crit DMG Rate'])) * (data['Crit Rate'])


# print(res)

atk = 0
atkrate = 0
critdmg = 50
critrate = 5
e = 0

for _ in range(25):
    s = input().strip()
    n = len(s)
    tmp = 0
    base = 0.1
    flag = False

    for j in range(n):
        if '0' <= s[j] <= '9':
            if not flag:
                tmp = tmp * 10 + int(s[j])
            else:
                tmp += base * int(s[j])
                base *= 0.1
        elif s[j] == '.':
            flag = True

    if s[0:3] == 'ATK':
        if s[3] == ' ':
            atkrate += tmp
        else:
            atk += tmp
    if s[0:4] == 'Crit':
        if s[5] == 'R':
            critrate += tmp
        else:
            critdmg += tmp

atk = 1500 * (1 + atkrate * 0.01) + atk
critrate *= 0.01
critdmg *= 0.01

if critrate > 1:
    critrate = 1

e = atk * (1 - critrate) + atk * (1 + critdmg) * critrate
print("{:.6f}".format(e))