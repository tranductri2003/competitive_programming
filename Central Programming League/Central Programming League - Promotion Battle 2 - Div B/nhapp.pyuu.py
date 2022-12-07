T = 8
ns = [1, 2, 3, 4, 5, 6, 7, 10]

legal_moves = [2, 3, 5]

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def next_move(n):
    next_ns = map(lambda x: n - x, legal_moves)
    next_ns = filter(lambda x: x >= 0, next_ns)
    next_n_rewards = map(which_player_wins, next_ns)  # Reward for opponent
    if any(map(lambda x: x == "Second", next_n_rewards)):  # Opponent enters a losing position
        return "First"
    else:
        return "Second"

def which_player_wins(n):
    if n <= 1:
        return "Second"               # First player loses
    elif n in legal_moves:
        return "First"                # First player wins immediately
    else:
        return next_move(n)

for n in ns:
    print (which_player_wins(n))