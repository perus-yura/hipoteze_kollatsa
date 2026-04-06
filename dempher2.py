def find_resonance(base_n, limit=50):
    print(f"{'Демпфер':<15} | {'Число':<20} | {'Кроків':<10} | {'Макс. висота'}")
    print("-" * 75)
    
    max_steps = 0
    best_damper = 0
    
    for i in range(1, limit + 1):
        # Будуємо число: блоки "10" + база
        binary_n = ("10" * i) + bin(base_n)[2:]
        n = int(binary_n, 2)
        
        # Рахуємо кроки до 1
        curr = n
        steps = 0
        peak = n
        while curr != 1 and steps < 5000: # Захист від нескінченності
            curr = curr // 2 if curr % 2 == 0 else 3 * curr + 1
            if curr > peak: peak = curr
            steps += 1
            
        if steps > max_steps:
            max_steps = steps
            best_damper = i
            
        # Виводимо результати для кожного 5-го кроку, щоб не забивати термінал
        if i % 5 == 0 or i == 1:
            print(f"10 * {i:<8} | {n:<20} | {steps:<10} | {peak}")

    print("-" * 75)
    print(f"РЕЗОНАНС ЗНАЙДЕНО: Блок '10' повторений {best_damper} разів дає {max_steps} кроків!")

# Шукаємо резонанс для 27
find_resonance(27, 50)