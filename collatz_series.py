n = int(input("enter  a number"))
t = n
while(n != 1):
    if(t%2 == 0):
        t= t//2
    if(t==1):
        break
    print(t)
    if(t%2 == 1):
        t = ((3*t)+1)
        print(t)
    n = t
print(1)
