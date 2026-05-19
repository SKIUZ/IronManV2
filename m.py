valores = [3, 5, 7, 9]

resultado = 1

contador = 0

 

for valor in valores:

    if contador % 2 == 0:

        resultado = resultado * valor

    else:

        resultado = resultado +  valor

    contador = contador + 1

 

print(resultado)