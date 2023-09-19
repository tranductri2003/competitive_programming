def find_modular_inverses(num, modulo):
    inverses = []
    for x in range(modulo):
        if (num * x) % modulo == 1:
            inverses.append(x)
    return inverses

# Sử dụng hàm để tìm tất cả modulo nghịch đảo của số 7 trong modulo 10
num = 6
modulo = 8
result = find_modular_inverses(num, modulo)
print("Tất cả modulo nghịch đảo của", num, "trong modulo", modulo, "là:", result)
