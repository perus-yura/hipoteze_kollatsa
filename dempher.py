def analyze_climb_stamina(base_n, max_blocks):
    print(f"{'Блоків 10':<10} | {'Число (Дес.)':<15} | {'Кроків росту':<12} | {'Пікове значення'}")
    print("-" * 65)
    
    for i in range(1, max_blocks + 1):
        # Конструюємо демпфер: блоки "10" перед числом
        damper = "10" * i
        binary_n = damper + bin(base_n)[2:]
        n = int(binary_n, 2)
        
        # Рахуємо кроки, поки число росте або не впаде суттєво
        curr = n
        steps = 0
        peak = n
        while curr > 1 and steps < 1000:
            if curr % 2 == 0:
                curr //= 2
            else:
                curr = 3 * curr + 1
            if curr > peak:
                peak = curr
            steps += 1
            if curr < n // 2: # Зупиняємось, якщо почалося серйозне падіння
                break
        
        print(f"{i:<10} | {n:<15} | {steps:<12} | {peak}")

# Проаналізуємо 27 з демпферами від 1 до 15 блоків
analyze_climb_stamina(27, 15)