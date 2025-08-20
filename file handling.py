
# 1. Create & Write to a file
file = open("sample.txt", "w")   # "w" = write mode 
file.write("Hello, My name is Sandhyarani.\n")
file.write("This is the second line.\n")
file.close()
print("File created and data written successfully.")

# 2. Append data to the file
file = open("sample.txt", "a")   # "a" = append mode
file.write("This line is appended to the file.\n")
file.close()
print("Data appended successfully.")

# 3. Read the entire file
file = open("sample.txt", "r")   # "r" = read mode
print("\nReading full file content:")
print(file.read())
file.close()

# 4. Read line by line
file = open("sample.txt", "r")
print("\nReading file line by line:")
for line in file:
 print(line.strip())  # strip() removes \n
file.close()

# 5. Using 'with' (automatic close)
print("\nUsing 'with' keyword to read:")
with open("sample.txt", "r") as file:
    data = file.readlines()
    print(data)

# 6. Check file pointer position
with open("sample.txt", "r") as file:
    print("\nCurrent file pointer:", file.tell())  # tell() shows current position

    print(file.readline())  # read one line

    print("File pointer after reading:", file.tell())

    file.seek(2)  #  seek() move pointer to beginning
    print("File pointer reset:", file.tell())
    print(file.readline())
