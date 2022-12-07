"""
Cho một dãy A gồm N phần tử. Ban đầu, giá trị của các phần tử đều bằng 0. Có Q truy vấn,
truy vấn thứ i được mô tả bởi hai số nguyên ri và pi
, yêu cầu thực hiện pi
lần các thao tác sau:
• Chọn phần tử có giá trị nhỏ nhất trong các phần tử có vị trí từ 1 đến ri
. Nếu có nhiều phần
tử có cùng giá trị nhỏ nhất, chọn phần tử có vị trí nhỏ nhất trong số chúng.
• Tăng giá trị của phần tử được chọn thêm 1.
Hãy cho biết giá trị các phần tử trong dãy A sau khi thực hiện Q truy vấn trên.
Dữ liệu
• Dòng đầu tiên gồm hai số nguyên N, Q (1 ≤ N, Q ≤ 105
) - số phần tử của dãy A và số truy
vấn cần thực hiện.
• Q dòng tiếp theo, mỗi dòng gồm hai số nguyên ri và pi (1 ≤ ri ≤ N, 1 ≤ pi ≤ 9 ∗ 108
) - mô
tả truy vấn thứ i.
Kết quả
• In ra N số nguyên lần lượt là giá trị các phần tử trong dãy A sau khi thực hiện Q truy vấn."""