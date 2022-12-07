data = []
for i in range(1, 100):
    for j in range(1, i):
        # data.append((f"({i}-{j})*({i}+{j})", i**2-j**2))
        data.append(i**2-j**2)

data = list(set(data))
# data.sort(key=lambda x: x[1])
data.sort()
for i in range(len(data)):
    # print("so thu", i+1, ":", data[i][0], data[i][1])
    print("so thu", i+1, ":", data[i])


# for i in range(3, max(data)):
#     if i not in data:
#         print(i)
