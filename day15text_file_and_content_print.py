# Write a Python program to read a text file and print its contents.

with open("filename.txt",'r')as file:
    content=file.read()

print("you write the content in notepad:",content)


