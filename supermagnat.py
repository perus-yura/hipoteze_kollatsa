import matplotlib.pyplot as plt

def search_ultimate_magnate(base_n, pattern, blocks_count):
    # Конструюємо Гігантське число
    binary_n = (pattern * blocks_count) + bin(base_n)[2:]
    n = int(binary_n, 2)
    
    curr = n
    history_bits = [n.bit_length()]
    steps = 0
    
    # Ліміт 50 000 кроків для справжнього виклику
    while curr != 1 and steps < 50000:
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = 3 * curr + 1
        
        # Записуємо вагу кожного 10-го кроку для економії пам'яті
        if steps % 10 == 0:
            history_bits.append(curr.bit_length())
        steps += 1
        
    return steps, history_bits

# Параметри для супер-тесту
pattern = "1010110110"
blocks = 500  # Максимальна потужність
base = 27

print(f"Запуск симуляції для {blocks} блоків патерна {pattern}...")
total_steps, bits_path = search_ultimate_magnate(base, pattern, blocks)

# Візуалізація
plt.figure(figsize=(15, 8))
plt.plot([i*10 for i in range(len(bits_path))], bits_path, color='purple', linewidth=1.5)
plt.title(f"Абсолютний Магнат: {pattern} x {blocks}\nШлях: {total_steps} кроків", fontsize=14)
plt.xlabel("Крок (час)")
plt.ylabel("Вага числа (кількість бітів)")
plt.grid(True, alpha=0.2)
plt.show()

print(f"ФІНІШ! Ми досягли позначки у {total_steps} кроків.")