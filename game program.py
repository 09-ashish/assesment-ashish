import random
import itertools
sys_gen=[]
def ran_num():
    for i in range(4):
        sys_gen.append(random.randint(0,9))
    return sys_gen
def guess_num():
    no=input("\nguess a number:")
    guess_no=[int(no[0]),int(no[1]),int(no[2]),int(no[3])]
    return guess_no



def evaluate():
    for (x,y) in zip(n2,n1):
        if x==y:
            print ("R",end='')
        if x not in n1:
            print("B",end='')
        elif x!=y:
            print("Y",end='')


      
n=10
n1=ran_num()
while (n>0):
    n2=guess_num()
    n=n-1
    if(n1==n2):
        print("\n congratulation!! you guessed it correctly")
        break
    evaluate()
else:
    print("\nyou are out of chance")
            
