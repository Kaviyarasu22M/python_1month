m=input("enter the file path:")
try:
    with open(m,'r')as file:
        content=file.readlines()
        no_of_lines=len(content)
        print(f"this is the textfile line:{no_of_lines}")
except FileNotFoundError:
    print(f"in this file is {'no_of_lines'} is not found")