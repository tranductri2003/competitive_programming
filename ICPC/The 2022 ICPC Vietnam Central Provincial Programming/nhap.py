s = "AAA"
for i in range(0, len(s)-len("AA")+1):
    if s[i:i+len("AA")] == "AA":
        print('a')
