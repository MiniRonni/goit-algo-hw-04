from pathlib import Path

def get_cats_info(path):
    try:
        file_path = Path(path)
        if not file_path.is_file():
            raise FileNotFoundError(f"Файл '{path}' не знайдено.")
        
        cats_info = []
        
        with file_path.open('r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Пропускаємо порожні рядки
                
                try:
                    cat_id, name, age = line.split(',')
                    cats_info.append({"id": cat_id.strip(), "name": name.strip(), "age": age.strip()})
                except ValueError:
                    print(f"Помилка у рядку: '{line}' - некоректний формат.")
        
        return cats_info
    
    except Exception as e:
        print(f"Помилка: {e}")
        return None

# Приклад використання:
cats_info = get_cats_info("cats.txt")
if cats_info is not None:
    for cat in cats_info:
        print(f"{{'id': '{cat['id']}', 'name': '{cat['name']}', 'age': '{cat['age']}'}},")