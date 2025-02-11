from pathlib import Path

def total_salary(path):
    try:
        file_path = Path(path)
        if not file_path.is_file():
            raise FileNotFoundError(f"Файл '{path}' не знайдено.")
        
        total = 0
        count = 0
        
        with file_path.open('r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки
                
                try:
                    name, salary = line.rsplit(',', 1)  # Розділяємо тільки по останній комі
                    salary = int(salary)
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Помилка у рядку: '{line}' - некоректний формат.")
        
        if count == 0:
            raise ValueError("Файл не містить коректних записів про зарплати.")
        
        average = total / count
        return total, average
    
    except Exception as e:
        print(f"Помилка: {e}")
        return None


total, average = total_salary("salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
