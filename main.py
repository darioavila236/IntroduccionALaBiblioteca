lista = []
lista.append(input("Que pais deseas agregar?: "))
lista = list(set(lista))
print(lista)