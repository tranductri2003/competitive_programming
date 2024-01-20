def count_A_around_B(s):
    n = len(s)
    left_A_count = [0] * n
    right_A_count = [0] * n

    # Tính số lượng chữ 'A' liên tiếp bên trái và bên phải của mỗi chữ 'B'
    for i in range(n):
        if s[i] == 'B':
            left_A_count[i] = 0
            consecutive_A_left = 0
        else:
            consecutive_A_left += 1
            left_A_count[i] = consecutive_A_left

    consecutive_A_right = 0
    for i in range(n - 1, -1, -1):
        if s[i] == 'B':
            right_A_count[i] = 0
            consecutive_A_right = 0
        else:
            consecutive_A_right += 1
            right_A_count[i] = consecutive_A_right

    return left_A_count, right_A_count

t = int(input("Nhập số lượng test cases: "))

for _ in range(t):
    s = input("Nhập chuỗi: ")
    left_A, right_A = count_A_around_B(s)

    print("Số lượng chữ A liên tiếp bên trái của mỗi chữ B:", left_A)
    print("Số lượng chữ A liên tiếp bên phải của mỗi chữ B:", right_A)
