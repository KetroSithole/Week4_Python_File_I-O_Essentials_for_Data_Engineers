# 📂 Reading the first 5 lines of the file
with open('data.txt', 'r') as file:
    for _ in range(8):  # Loop to read the first 5 lines
        line = file.readline().strip()  # Read one line at a time
        if line:  # Check if there's still content
            print(line)
        else:
            break  # Exit if there are fewer than 5 lines
