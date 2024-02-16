# Вводим общую стоимость часов
total_cost = int(input("Введите общую стоимость часов: "))

# Стоимость серебряных часов
silver_cost = 48

# Количество серебряных часов
silver_count = 96

# Количество золотых часов
gold_count = silver_count / 16

# Стоимость золотых часов
gold_cost = (total_cost - silver_count * silver_cost) / gold_count

# Выводим стоимость золотых часов
print("Стоимость золотых часов:", gold_cost)