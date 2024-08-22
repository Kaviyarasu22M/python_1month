#Write a Python program to write some data to a text file.

m=input("what you write in text file enter:")
with open("filename.txt",'w')as file:
    content=file.write(m)
print("your new writed content here:",m)

