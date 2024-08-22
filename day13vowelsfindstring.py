def string(n):
    count=0
    vowels="aeiouAEIOU"
    for i in n:
        if i in vowels:
            count+=1
    return count
n=input("enter the text your vowels count :")
print(string(n))