num=int(input())
s=0
prod=1
while(num>0):
    b=num%10
    s=s+b
    prod=prod*b
    num=num//10
if(s==prod):
    print('Spy Number')
else:
    print('Not Spy Number')