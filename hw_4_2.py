from pathlib import Path

def get_cats_info(path):
    """
    Reads a file containing cat information and returns a list of dictionaries.

    Args:
        path (str): Path to the file with information.

    Returns:
        list: List of dictionaries with cat data.
    """
    try:
        file_path = Path(path)
        if not file_path.is_file():
            raise FileNotFoundError(f"Error: File '{path}' not found.")
        
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
                    print(f"Error in line: '{line}' - incorrect format.")
        
        return cats_info
    
    except Exception as e:
        print(f"Error: {e}")
        return None

# Test case
cats_info = get_cats_info("cats.txt")
if cats_info is not None:
    for cat in cats_info:
        print(f"{{'id': '{cat['id']}', 'name': '{cat['name']}', 'age': '{cat['age']}'}},")