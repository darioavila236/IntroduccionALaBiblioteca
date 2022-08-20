import functools

lista = [2,4,7,9,12,13,56,77,11,1,3]

def esImpar(numero):
    return numero % 2 != 0

listaImpares = list(filter(esImpar,lista))
print(listaImpares)
print(functools.reduce(lambda a,b: a+b, listaImpares))
