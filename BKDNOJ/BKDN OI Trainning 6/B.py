from dataclasses import dataclass


data = []
for i in range(28):
    data.append(int(input()))


for i in range(1, 31):
    if i not in data:
        print(i)
