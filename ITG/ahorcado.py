palabra = 'info'

intentos_restantes = 6

letras_acertadas = [] 

while intentos_restantes > 0 :
    
      letra = input('inghrese letra: ')

      if letra in letras_acertadas:
        print('Ya ingresaste esa letra')
        continue

      if len(letra) != 1:
        print('Por favor, ingrese solo una letra')
        continue

      if not letra.isalpha():
        print('Por favor, ingrese solo letras')
        continue

      if letra in palabra:
            letras_acertadas.append(letra)
            print('Letras acertadas: ',letras_acertadas)
            if len(palabra) == len(letras_acertadas):
                  print('Ha ganado!')
                  break
      else:
            intentos_restantes = intentos_restantes - 1
            print('Intentos restantes: ',intentos_restantes)
            if intentos_restantes == 0:
                  print('Looseeeerr!')
                  break

print('Juego terminado')