count=0
print("Enter your number, To Sumup write down Exit" )


while True:
    n=input()
    count+=1
    
    if n=="Exit":
        break
    elif count==1:
        n_Sum =int(n) 
    elif count> 1 :
        n1 = n_Sum
        n_Sum = int(n1)+int(n)
print ("Numbers Sumup:", n_Sum)


    
    