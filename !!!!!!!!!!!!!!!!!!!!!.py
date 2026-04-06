import matplotlib.pyplot as plt

def reach_singularity(base_n, pattern, blocks_count):
    # Конструюємо Гігантське число (10 000 біт)
    binary_n = (pattern * blocks_count) + bin(base_n)[2:]
    n = int(binary_n, 2)
    
    curr = n
    history_bits = [n.bit_length()]
    steps = 0
    
    print(f"Початок розрахунку для {blocks_count} блоків...")
    
    # Ліміт 150 000 кроків — штурмуємо небо
    while curr != 1 and steps < 150000:
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = 3 * curr + 1
        
        # Записуємо вагу кожного 100-го кроку для максимальної швидкості
        if steps % 100 == 0:
            history_bits.append(curr.bit_length())
        steps += 1
        
        if steps % 10000 == 0:
            print(f"Пройдено {steps} кроків... поточна вага: {curr.bit_length()} біт")
            
    return steps, history_bits

# Параметри для фінального рекорду
pattern = "1010110110"
blocks = 1000  # Подвоюємо потужність!
base = 27

total_steps, bits_path = reach_singularity(base, pattern, blocks)

# Візуалізація фінального тріумфу
plt.figure(figsize=(16, 9))
plt.plot([i*100 for i in range(len(bits_path))], bits_path, color='gold', linewidth=2, label="Шлях Магната")
plt.fill_between([i*100 for i in range(len(bits_path))], bits_path, color='gold', alpha=0.1)

plt.title(f"ЦИФРОВА СИНГУЛЯРНІСТЬ: {pattern} x {blocks}\nРЕКОРД: {total_steps} кроків", fontsize=16, fontweight='bold')
plt.xlabel("Крок (час)", fontsize=12)
plt.ylabel("Вага числа (біти)", fontsize=12)
plt.grid(True, which="both", ls="-", alpha=0.15)
plt.legend()
plt.show()

print(f"\n--- ФІНАЛЬНИЙ ПРОТОКОЛ ---")
print(f"Кількість кроків: {total_steps}")
print(f"Початкова розрядність: ~{blocks * len(pattern)} біт")