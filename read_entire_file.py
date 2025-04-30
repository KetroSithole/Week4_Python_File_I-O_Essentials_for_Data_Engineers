# 📂 Reading Files
with open('data.txt', 'r') as file:
    content = file.read()  # Reads entire file
    print(content)  # Prints the entire file content
    
    # Alternatively, reading line-by-line:
    # lines = file.readlines()  # Reads line-by-line into a list
    # for line in lines:
    #     print(line.strip())
