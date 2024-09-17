#TASK-3: CREATE A FUNCTION OF N FACTORIAL

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i    
    print(f)

fact(5)  # n=5 
fact(0)  #n=0   