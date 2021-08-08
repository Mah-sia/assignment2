import random
print("Press Enter to Dice")
x=input()
y=random.randint(1,6)
print("your dice is:", y)
if y==6:
    y=random.randint(1,6)
    print("you have Award,your second dice is:",y)

