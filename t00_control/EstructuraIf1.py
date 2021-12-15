def prueba(valor_prueba, referente):
    if valor_prueba > referente:
        return 1
    elif valor_prueba < referente:
        return -1
    else:
        return 0


print(prueba(10, 5))
print(prueba(5, 10))
print(prueba(5, 5))
