inicio = 1
fim = 20
numero_a_pular = 13
for numero in range(inicio, fim + 1):
    if numero == numero_a_pular:
        continue 
    print(numero)


numero = 1
while numero <= 20:
        if numero != 13:
      
            print(numero)
   
        numero += 1



#DESAFIO
lista = []

numero = 20

while len(lista) < 20:
    if numero != 13:
        lista.append(numero)
    numero -= 1

print(lista)