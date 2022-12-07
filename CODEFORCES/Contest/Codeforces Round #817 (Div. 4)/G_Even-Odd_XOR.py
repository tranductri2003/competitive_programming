# Commutative : A ⊕ B = B ⊕ A
# This is clear from the definition of XOR: it doesn’t matter which way round you order the two inputs.

# Associative : A ⊕ ( B ⊕ C ) = ( A ⊕ B ) ⊕ C
# This means that XOR operations can be chained together and the order doesn’t matter. If you aren’t convinced of the truth of this statement, try drawing the truth tables.

# Identity element : A ⊕ 0 = A
# This means that any value XOR’d with zero is left unchanged.

# Self-inverse : A ⊕ A = 0
# This means that any value XOR’d with itself gives zero


# Remember x⊕x=0 and a⊕b=c↔a=b⊕c (you can move an element from one side to the other side).
# Let's define your answer A. Your answer must satisfy:
# A1⊕A3⊕⋯=A2⊕A4⊕…
# ↔A1⊕A2⊕A3⊕A4⊕⋯=0
# ↔ (XOR of elements you choose) = (XOR of the remaining elements)


t = int(input())
for _ in range(t):
    n = int(input())
    res = [i for i in range(0, n-3)]

    x = 0
    for i in range(n-3):
        x = x ^ i
    x = x ^ (2**30)
    x = x ^ (2**29)
    res.append(2**30)
    res.append(2**29)
    res.append(x)
    print(*res)
