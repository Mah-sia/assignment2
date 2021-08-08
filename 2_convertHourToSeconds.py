H,M,S=input("Enter your time:HH:MM:SS  ").split(":")
H=int(H)
M=int(M)
S=int(S)

S_Sum=int((H*3600)+(M*60)+S)
print("Your Time is",S_Sum," Seconds")


