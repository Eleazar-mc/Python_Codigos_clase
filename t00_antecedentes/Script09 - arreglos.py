lista = [458,'python',-9.47,False]
print(lista)
print('Longitud de la lista:', len(lista))
print('Tercer elemento de la lista:', lista[2])

lista.append('anaconda')
lista.append('jupyter')
print(lista)
lista.pop()
print(lista)
lista.pop(3)
print(lista)

print('anaconda' in lista)
print(458 in lista)
