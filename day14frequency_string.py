def string(char):
    frequency={}
    for i in char:
        if i in char:
            frequency[i]=+1
        else:
            frequency[i]=1
    return frequency
m="hello"
n=string(m)
print(n)
