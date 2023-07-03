def lexicographically_smallest_subsequence(x, k):
    result = []
    indices = {}

    for i in range(len(x) - 1, -1, -1):
        xi = x[i]
        if xi not in indices:
            indices[xi] = i

    for i in range(1, k + 1):
        if i in indices:
            result.append(i)

    result.reverse()
    return result


# Read input
n, k = map(int, input().split())
x = []
for _ in range(n):
    x.append(int(input()))

# Find lexicographically smallest subsequence
subsequence = lexicographically_smallest_subsequence(x, k)

# Print the subsequence
print(' '.join(map(str, subsequence)))
