import os

while True:
    file_path = input("Enter the path to the file: ")

    if not os.path.exists(file_path):
        print("File not found!")
        continue

    with open(file_path, 'r') as file:
        content = file.readlines()

    
    total_lines = len(content)
    empty_lines = content.count('\n')
    lines_with_s = sum('s' in line for line in content)
    s_count = sum(line.count('s') for line in content)
    lines_with_is = sum('is' in line for line in content)

    print(f"\nFile: {file_path}")
    print(f"total lines: {total_lines}")
    print(f"empty lines: {empty_lines}")
    print(f"lines with \"s\": {lines_with_s}")
    print(f"\"s\" count: {s_count}")
    print(f"lines with \"is\": {lines_with_is}")

    answer = input("Do you want to analyze another file? (y/n): ")
    if answer.lower() != 'y':
        break
