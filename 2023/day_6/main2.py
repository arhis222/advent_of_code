import math

# Part Two input (örnek)
T = 71530
D = 940200

# Kökleri hesapla
sqrt_val = math.isqrt(T*T - 4*D)  # int karekök
x1 = (T - sqrt_val) // 2
x2 = (T + sqrt_val) // 2

# Kazandıran x değerleri: x1 < x < x2
ways = x2 - x1 - 1  # kökler dahil değil

print(ways)