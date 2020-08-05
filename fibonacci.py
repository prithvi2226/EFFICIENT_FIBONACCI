n = int(input("enter how many terms?"))

F = [i for i in range(n)]

F[0] = 0
F[1] = 1

for j in range(2, n):
    F[j] = F[j-1] + F[j-2]
print(F)

