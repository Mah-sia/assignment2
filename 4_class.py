n = int(input('Enter the number of students: '))
Scores=[]
R = 0
i=0 
for i in range(0,n):
    item=int(input())
    Scores.append(item)

for i in range(0,n):
    sum=Scores[i]+R
    R=sum
Av=sum/n
print("average is",Av)
for i in range(0,n-2):
    if Scores[i]>=Scores[i+1]:
        maxItem=Scores[i]
        min=Scores[i+1]
    elif Scores[i]<Scores[i+1]:       
        maxItem=Scores[i+1]
        min=Scores[i]
print("Maximom is:",maxItem,"Minimum is",min)
