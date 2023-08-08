from os import system


print("------------------------")
print("* Ismael Paulino #27   *")
print("* Menu de operaciones  *")
print("------------------------")


General=True
while General == True:
    lista = []
    print("--------------------------")
    print("*     Menu principal     *")
    print("--------------------------")
    print("* 1. Mayor o igual que.  *")
    print("* 2. Menor o igual que.  *")
    print("* 3. Maximo.             *")
    print("* 4. Minimo.             *")
    print("--------------------------")
    opc = input("Ingrese una opcion: ")
    
    if opc == "1":
        n1 = float(input("Primer numero: "))
        n2 = float(input("Segundo numero: "))
        if n1 == n2:
            print("Los numeros son iguales.")
        elif n1 > n2:
            print(f"El numero {n1} es mayor que {n2}.")
        else:
            print(f"El numero {n2} es mayor que {n1}.")
    
    elif opc == "2":
        n1 = float(input("Primer numero: "))
        n2 = float(input("Segundo numero: "))
        if n1 == n2:
            print("Los numeros son iguales.")
        elif n1 < n2:
            print(f"El numero {n1} es menor que {n2}.")
        else:
            print(f"El numero {n2} es menor que {n1}.")
    
    elif opc == "3":
        print("El limite de ingresar es de 5.")
        for i in range(5):
            numero = int(input("Ingrese el numero: "))
            lista.append(numero)
            
        for i in range(1, 5):
            maximo = max(lista)
        print(f"El mumero mayor de todos es: {maximo}")
    
    elif opc == "4":
        print("El limite de ingresar es de 5.")
        for i in range(5):
            numero = input("Ingrese el numero: ")
            lista.append(numero)

        for i in range(1, 5):
            minimo = min(lista)
        print(f"El mumero menor de todos es: {minimo}")
    else:
        print("La opcion es invalida.")
        continue

    salir = 0
    while salir == 0:
        print("Desea salir:")
        print("1. Si")
        print("2. No")
        op = input("Elige una opcion: ")
        
        if op == "1":
            salir += 1
            General = False
        if op == "2":
            salir += 1
            system("cls")