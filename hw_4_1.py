from pathlib import Path

def total_salary(path):
    """
    This function calculates the total and avarage salary of all employees in a given directory.

    Args:
        path (str): The path to the directory containing the employee data.

    Returns:
        tuple: (total_salary, avarage_salary) if successful, othrwise None.
    """
    try:
        file_path = Path(path)
        if not file_path.is_file():
            raise FileNotFoundError(f"Error: File '{path}' not found.")
        
        total = 0
        count = 0
        
        with file_path.open('r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skipping blank lines
                
                try:
                    name, salary = line.rsplit(',', 1)  # Divide only by the last comma.
                    salary = int(salary) # Ensure salary is an integer
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Error in line: '{line}' - incorrect format.")
        
        if count == 0:
            raise ValueError("The file does not contain correct salary records.")
        
        average = total / count
        return total, average
    
    except Exception as e:
        print(f"Unknown error: {e}")

    return None

# Test case
total, average = total_salary("salary.txt")
print(f"Total salary: {total}, Average salary: {average}")
