def is_power_of(a, b):
    i = a
    while i <= b:
        if i == b:
            return True
        i *= a
    return False


n = int(input())

array_a = [0] + list(map(int, input().split()))
array_b = [0] + list(map(int, input().split()))
visited = [0] * (n + 1)
ans1 = 0

for i in range(1, n + 1):
    ans1 += array_a[i]

for i in range(2, n + 1):
    max_sum = 0
    current_sum = 0

    if not visited[i]:
        multiples = []
        j = i
        while j <= n:
            multiples.append(j)
            visited[j] = 1
            j *= i

        total_combinations = 1 << len(multiples)

        for combination in range(total_combinations):
            current_sum = 0
            selected_elements = []

            for l in range(len(multiples)):
                if combination & (1 << l):
                    current_sum += array_a[multiples[l]]
                    selected_elements.append(multiples[l])

            for x in range(len(selected_elements)):
                for y in range(len(selected_elements)):
                    if selected_elements[x] > selected_elements[y] and is_power_of(selected_elements[y], selected_elements[x]):
                        current_sum -= array_b[selected_elements[x]]

            max_sum = max(max_sum, current_sum)

        ans1 += max_sum

print(ans1)
