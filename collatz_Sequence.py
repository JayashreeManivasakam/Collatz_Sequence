num=int(input())
print(num,end=" ")
while(num>1):
    if(num%2==0):
        num=int(num/2)
    else:
        num=int((3*num)+1)
    print(num,end=" ")
