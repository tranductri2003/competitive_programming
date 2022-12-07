chuoi=str(input())
list=["u","e","o","a","i"]

for num in list:
    if chuoi[0]==num:
        print("an")
        break  # Chạy hết nó sẽ không chạy else nữa
else:
    print("a")