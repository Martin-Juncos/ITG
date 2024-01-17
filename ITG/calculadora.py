# Calculadora

# i = 0

# while i < 5:
#     i += 1
#     print(i)

# for i in range(1,6):
#     print(i)


def seleccionar_palabra(params):
    palabras = ['comunicacion', 'picaporte', 'mate']
    return palabras[params]
    # for palabra in palabras:
    #     print(palabra)

palabra_seleccionada = seleccionar_palabra(0)

# for i in range(len(palabra_seleccionada)):
#     print(palabra_seleccionada[i])
#     if palabra_seleccionada[i] == 't':
#         print('encontrada la letra "t"')
#         break


i = 0
while i != len(palabra_seleccionada):
    print(palabra_seleccionada[i])
    if palabra_seleccionada[i] == 't':
        print('encontrada la letra "t"')
        break
    i += 1


# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# numeros_pares = [numero for numero in lista if numero % 2 != 0]
# print(type(numeros_pares), numeros_pares)
    
