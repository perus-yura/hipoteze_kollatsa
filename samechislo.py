# Конструювання числа (з вашого останнього тесту)
pattern = "1010110110"
blocks = 1000
base_n = 27

binary_string = (pattern * blocks) + bin(base_n)[2:]
ultimate_number = int(binary_string, 2)

# Збереження у файл
with open("ultimate_magnate_decimal.txt", "w") as f:
    f.write(str(ultimate_number))

print(f"Десяткове число збережено. Кількість цифр: {len(str(ultimate_number))}")