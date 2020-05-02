def countMachine(b):
    c=len(b)
    return {i:b.count(i) for i in range(1,c+1)}
b=[4,4,4,4]
a=countMachine(b)
print(a)


      
