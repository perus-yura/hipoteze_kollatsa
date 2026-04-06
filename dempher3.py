import matplotlib.pyplot as plt

def ultra_climb_test(base_n, damper_count):
    # Створюємо Гіпер-Магната: (10 * count) + 27
    binary_n = ("10" * damper_count) + bin(base_n)[2:]
    n = int(binary_n, 2)
    
    curr = n
    history = [n]
    steps = 0
    
    # Збільшуємо ліміт до 10 000 кроків для 100 блоків
    while curr != 1 and steps < 10000:
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = 3 * curr + 1
        history.append(curr)
        steps += 1
        
    print(f"Політ завершено! Кількість кроків: {steps}")
    print(f"Кількість розрядів у піковому значенні: {len(str(max(history)))}")

    # Графік польоту
    plt.figure(figsize=(15, 7))
    plt.plot(history, color='darkred', linewidth=0.8)
    plt.yscale('log')
    plt.title(f"Резонансний підйом: 27 + {damper_count} блоків '10'\nШлях: {steps} кроків", fontsize=14)
    plt.xlabel("Час (кроки)", fontsize=12)
    plt.ylabel("Значення (Log scale)", fontsize=12)
    plt.grid(True, which="both", alpha=0.3)
    plt.show()

# Запускаємо межу системи
ultra_climb_test(27, 100)