def calculate_token_number(numbers):
    xor_result = 0
    for num in numbers:
        xor_result ^= num
    return xor_result


# Đọc số lượng câu hỏi
q = int(input())

token_numbers = []
results = []

# Xử lý các câu hỏi
for _ in range(q):
    p, n = map(int, input().split())
    if p == 1:
        token_numbers.append(n)
    elif p == 2:
        token_number = calculate_token_number(token_numbers)
        sorted_tokens = sorted(token_numbers)
        results.append(sorted_tokens[n - 1])

# In kết quả
for result in results:
    print(result)
