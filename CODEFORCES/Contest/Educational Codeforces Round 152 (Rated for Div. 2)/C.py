def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    result = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, max_val + 1):
        count[i] += count[i - 1]

    for num in reversed(arr):
        result[count[num] - 1] = num
        count[num] -= 1

    return result


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = input()

    # Create an array to store the initial string
    original_string = [int(c) for c in s]

    copies = []
    for _ in range(m):
        l, r = map(int, input().split())
        copies.extend(original_string[l - 1:r])

    # Apply counting sort on the copies
    sorted_copies = counting_sort(copies)

    # Find unique elements in sorted_copies
    unique_strings = set()
    for i in range(len(sorted_copies)):
        if i == 0 or sorted_copies[i] != sorted_copies[i - 1]:
            unique_strings.add(sorted_copies[i])
        print(unique_strings)
    print(len(unique_strings))
