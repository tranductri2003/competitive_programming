from collections import Counter, defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    count = Counter(s)
    countDaSort = sorted(list(count.values()), reverse=True)
    if len(set(countDaSort)) == 1:
        print(0)
        print(s)
    else:
        soNhomKyTu = []
        soKyTuCanDoi = defaultdict(lambda: 0)
        for i in range(1, 27):
            if n % i == 0:
                temp = []
                soNhomKyTu.append(i)
                soKyTuMoiNhom = n//i

                for cha in count:
                    temp.append((cha, abs(soKyTuMoiNhom-count[cha])))
                temp = sorted(temp, key=lambda x: x[1])
                changes = 0
                for j in range(min(len(count), i)):
                    changes += temp[j][1]
                soKyTuCanDoi[i] = changes

        soNhomRes = 0
        res = 10**9
        for num in soKyTuCanDoi:
            if soKyTuCanDoi[num] <= res:
                res = soKyTuCanDoi[num]
                soNhomRes = num
        soKyTuMoiNhom = n//soNhomRes

        need = defaultdict(lambda: 0)
        temp = []
        for cha in count:
            temp.append((cha, (count[cha]-soKyTuMoiNhom)))
        temp = sorted(temp, key=lambda x: abs(x[1]))

        # cacKyTuGiuNguyen = []
        # for i in range(min(len(count), soNhomRes)):
        #     cacKyTuGiuNguyen.append(temp[i][0])
        # print(cacKyTuGiuNguyen)
        # count = dict(count)
        # print(count)
        if soKyTuMoiNhom == 1:
            unusedCha = []
            for cha in "abcdefghijklmnopqrstuvwxyz":
                if cha not in s:
                    unusedCha.append(cha)
            i = 0
            j = 0
            s = list(s)
            count = defaultdict(lambda: 0)
            while i < n:
                count[s[i]] += 1
                if count[s[i]] == 2:
                    count[s[i]] -= 1
                    s[i] = unusedCha[j]
                    j += 1
                i += 1
            print(res)
            print("".join(s))
        else:
            s = list(s)
            change = defaultdict(lambda: defaultdict(lambda: 0))
            i = 0
            j = soNhomRes
            while i < soNhomRes and j < len(temp):
                if temp[i][1] == 0:
                    i += 1
                elif temp[i][1] < 0:  # Thieu
                    benKiaCo = soKyTuMoiNhom-abs(temp[j][1])
                    if benKiaCo > abs(temp[i][1]):
                        change[temp[j][0]][temp[i][0]] = abs(temp[i][1])
                        temp[j][1] += abs(temp[i][1])
                        i += 1
                    elif benKiaCo < abs(temp[i][1]):
                        change[temp[j][0]][temp[i][0]] = abs(temp[j][1])
                        temp[i][1] += abs(temp[j][1])
                        j += 1
                    else:
                        j += 1
                else:  # du
                    benKiaCo = soKyTuMoiNhom-abs(temp[j][1])
                    if benKiaCo > abs(temp[i][1]):
                        change[temp[i][0]][temp[j][0]] = abs(temp[i][1])
                        temp[j][1] -= abs(temp[i][1])
                        i += 1
                    elif benKiaCo < abs(temp[i][1]):
                        change[temp[i][0]][temp[j][0]] = abs(temp[j][1])
                        temp[j][1] -= abs(temp[j][1])
                        j += 1
                    else:
                        j += 1
                if temp[i][1] == 0:
                    i += 1

            for i in range(n):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if change[s[i]][j] > 0:
                        s[i] = j
                        change[s[i]][j] -= 1
                        break
            print(res)
            print("".join(s))
