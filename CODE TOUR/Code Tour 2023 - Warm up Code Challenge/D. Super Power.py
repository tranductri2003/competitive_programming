N, Q = map(int, input().split())
team = list(map(int, input().split()))

initial_strength = sum(abs(x) for x in team)
print(initial_strength)

for _ in range(Q):
    action, value = input().split()
    value = int(value)

    if action == 'D':
        for i in range(N):
            team[i] -= value
    elif action == 'B':
        for i in range(N):
            team[i] += value

    current_strength = sum(abs(x) for x in team)
    print(current_strength)
