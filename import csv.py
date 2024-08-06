import csv

def read_csv(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        raise
    except csv.Error as e:
        print(f"CSV Error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected Error: {e}")
        raise

def process_data(data, column_name):
    try:
        total = 0
        count = 0
        for row in data:
            if column_name not in row:
                raise KeyError(f"Column '{column_name}' does not exist.")
            try:
                value = float(row[column_name])
                total += value
                count += 1
            except ValueError:
                print(f"Warning: Non-numeric value found in column '{column_name}'. Skipping row.")
                continue
        
        if count == 0:
            raise ValueError(f"No numeric values found in column '{column_name}'.")
        
        average = total / count
        
        for row in data:
            row['average'] = average
        
        return data
    except KeyError as e:
        print(f"Key Error: {e}")
        raise
    except ValueError as e:
        print(f"Value Error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected Error: {e}")
        raise

def write_csv(file_path, data):
    try:
        if not data:
            raise ValueError("Data is empty. No data to write.")
        
        fieldnames = data[0].keys()
        
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    except PermissionError:
        print(f"Error: Permission denied for writing to '{file_path}'.")
        raise
    except csv.Error as e:
        print(f"CSV Error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected Error: {e}")
        raise

if __name__ == "__main__":
    input_file = 'KIRAN.txt'
    output_file = 'KIRAN.txt'
    column_to_average = 'Age'
    
    try:
        data = read_csv(input_file)
        processed_data = process_data(data, column_to_average)
        write_csv(output_file, processed_data)
        print("Data processing and writing complete.")
    except Exception as e:
        print(f"An error occurred: {e}")
