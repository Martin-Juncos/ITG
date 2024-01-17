palabra = 'info'

intentos_restantes = 6

letras_acertadas = [] 

while intentos_restantes > 0 :
    
      letra = input('inghrese letra: ')

      if letra in palabra:
            letras_acertadas.append(letra)
            print(letras_acertadas)
            if len(palabra) == len(letras_acertadas):
                  print('Ha ganado!')
                  break
      else:
            intentos_restantes = intentos_restantes - 1
            print(intentos_restantes)
            if intentos_restantes == 0:
                  print('Looseeeerr!')
                  break

print('Juego terminado')