import matplotlib.pyplot as plt

def turbo_climb_test(base_n, damper_pattern, count):
    # Формуємо число: (патерн * count) + база
    binary_n = (damper_pattern * count) + bin(base_n)[2:]
    n = int(binary_n, 2)
    
    curr = n
    history = [n]
    steps = 0
    
    # Ліміт кроків 10 000 для глибокого аналізу
    while curr != 1 and steps < 10000:
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = 3 * curr + 1
        history.append(curr)
        steps += 1
        
    return steps, history

# Параметри експерименту
base = 27
blocks = 100

steps_10, hist_10 = turbo_climb_test(base, "10", blocks)
steps_110, hist_110 = turbo_climb_test(base, "110", blocks)

print(f"Результат '10'  (100 блоків): {steps_10} кроків")
print(f"Результат '110' (100 блоків): {steps_110} кроків")

# Візуалізація порівняння
plt.figure(figsize=(15, 8))
plt.plot(hist_10, color='blue', alpha=0.5, label=f"Демпфер '10' ({steps_10} кр.)")
plt.plot(hist_110, color='green', linewidth=1, label=f"Демпфер '110' ({steps_110} кр.)")
plt.yscale('log')
plt.title(f"Порівняння паливних структур для числа {base}", fontsize=14)
plt.xlabel("Крок (час)")
plt.ylabel("Значення (log)")
plt.legend()
plt.grid(True, which="both", alpha=0.2)
plt.show()