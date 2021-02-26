x = input("Ingrese la altura del triángulo:")
x = int(x)
sim = "*"
i=0
j=0
for i in range(x+1):
    for j in range(i):
        print(sim,end="")
    print()
