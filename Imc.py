peso = input("¿Cuál es tu peso?")
estatura = input("¿Cuál es tu estatura?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu imc es:"+str(imc))