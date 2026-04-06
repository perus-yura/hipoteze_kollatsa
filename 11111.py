import math
import matplotlib.pyplot as plt

def safe_super_climb_test(base_n, patterns, blocks):
    results = {}
    
    for pattern in patterns:
        binary_n = (pattern * blocks) + bin(base_n)[2:]
        n = int(binary_n, 2)
        
        curr = n
        # Записуємо не саме число, а його логарифм (порядок величини)
        # Якщо число занадто велике для math.log, використовуємо довжину рядка
        history_log = [n.bit_length()] 
        steps = 0
        
        while curr != 1 and steps < 25000:
            curr = curr // 2 if curr % 2 == 0 else 3 * curr + 1
            # n.bit_length() — це безпечний спосіб дізнатися "вагу" числа
            history_log.append(curr.bit_length())
            steps += 1
            
        results[pattern] = (steps, history_log)
    
    return results

# Тестуємо складні структури
base = 27
blocks_count = 150
new_patterns = ["10110", "10110110", "110110110", "1010110110"]

final_results = safe_super_climb_test(base, new_patterns, blocks_count)

# Побудова графіка "Ваги числа"
plt.figure(figsize=(16, 10))
for pattern, (steps, hist_bits) in final_results.items():
    plt.plot(hist_bits, label=f"'{pattern}' | {steps} кроків", alpha=0.8)

plt.title("Динаміка ваги (в бітах) Гіпер-Магнатов\nШтурм 5000 кроків без перевантаження", fontsize=14)
plt.xlabel("Час (кроки)")
plt.ylabel("Кількість бітів (розрядність)")
plt.legend()
plt.grid(True, alpha=0.2)
plt.show()