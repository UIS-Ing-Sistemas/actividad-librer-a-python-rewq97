import numpy as np

# cantidad de estudiantes y candidatos a representantes
estudiantes= 5000
candidatos= 30

# se le asigna 0 votos a cada candidato
votos = np.zeros(candidatos, dtype=int)

# le da la misma probabilidad a acada candidato de sacar una cantidad de votos (1/30)
votos = np.random.multinomial(estudiantes,[1/candidatos] *  candidatos)

# se crea un arreglo de la cantidad de candidatos
candidatos = np.arange(1, candidatos + 1)

# se asigna a cada candidato sus votos y se organizan de mayor a menor(reverse=True), despues se muestra en pantalla
totalvotos = list(zip(candidatos, votos))
totalvotos.sort(key=lambda x: x[1], reverse=True)
print("los resultados de votos por candidatos del mayor a menor son :")
for candidato, votos in totalvotos:
    print(f"Candidato {candidato}: {votos} votos")
#se usa f para que no se imprima lo escrito si o en forma de formato y lo que tiene dentro
