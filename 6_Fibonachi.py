nterms = int(input("How many terms? "))
# first two terms
n1, n2 = 0, 1
count = 0
Fibo_series=[]

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    Fibo_series=[n1]
    print("Fibonacci sequence upto",nterms,":")
    print(Fibo_series)
else:
    while count < nterms:
        
        nth = n1 + n2
        Fibo_series.append(n1)
        # update values
        n1 = n2
        n2 = nth
        count += 1
    print(Fibo_series[:])