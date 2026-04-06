import matplotlib.pyplot as plt

def battle_of_patterns(base_n, patterns, count):
    results = {}
    
    for pattern in patterns:
        binary_n = (pattern * count) + bin(base_n)[2:]
        n = int(binary_n, 2)
        
        curr = n
        history = [n]
        steps = 0
        
        while curr != 1 and steps < 15000: # Збільшуємо ліміт для наддовгих шляхів
            curr = curr // 2 if curr % 2 == 0 else 3 * curr + 1
            history.append(curr)
            steps += 1
        
        results[pattern] = (steps, history)
    
    return results

# Тестуємо три різні стратегії
base = 27
blocks = 100
patterns_to_test = ["110", "1110", "10110"]

results = battle_of_patterns(base, patterns_to_test, blocks)

# Візуалізація
plt.figure(figsize=(16, 9))
colors = ['green', 'red', 'purple']

for i, (pattern, (steps, hist)) in enumerate(results.items()):
    plt.plot(hist, label=f"Патерн '{pattern}' ({steps} кр.)", color=colors[i], alpha=0.8, linewidth=1)

plt.yscale('log')
plt.title(f"Порівняння енергетичних структур (27 + {blocks} блоків)", fontsize=16)
plt.xlabel("Крок (Час)", fontsize=12)
plt.ylabel("Значення (log10)", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, which="both", alpha=0.2)
plt.show()

for pattern, (steps, _) in results.items():
    print(f"Структура '{pattern}': {steps} кроків.")