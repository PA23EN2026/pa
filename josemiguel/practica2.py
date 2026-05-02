class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3

    def sumar(self):
        return self.__num1 + self.__num2 + self.__num3
    
    def mayor(self):
        mayor = self.__num1
        if self.__num2 > mayor:
            mayor = self.__num2
        if self.__num3 > mayor:
            mayor = self.__num3
        return mayor

    def menor(self):
        menor = self.__num1
        if self.__num2 < menor:
            menor = self.__num2
        if self.__num3 < menor:
            menor = self.__num3
        return menor
    
    def iguales(self):
        return self.__num1 == self.__num2 == self.__num3

    def concatenar(self):
        return str(self.__num1) + str(self.__num2) + str(self.__num3)

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

obj = Mi_Clase(num1, num2, num3)

respuestas = []

while True:
    print("\n1. Sumar")
    print("2. Mayor")
    print("3. Menor")
    print("4. Iguales")
    print("5. Concatenar")
    print("6. Salir")

    opcion = input("Opcion: ")

    if opcion == "1":
        resultado = obj.sumar()
        respuestas.append("Suma: " + str(resultado))
        print("Suma:", resultado)
    elif opcion == "2":
        resultado = obj.mayor()
        respuestas.append("Mayor: " + str(resultado))
        print("Mayor:", resultado)
    elif opcion == "3":
        resultado = obj.menor()
        respuestas.append("Menor: " + str(resultado))
        print("Menor:", resultado)
    elif opcion == "4":
        resultado = obj.iguales()
        respuestas.append("Iguales: " + str(resultado))
        print("Iguales:", resultado)
    elif opcion == "5":
        resultado = obj.concatenar()
        respuestas.append("Concatenar: " + str(resultado))
        print("Concatenar:", resultado)
    elif opcion == "6":
        print("\nRespuestas:")
        for i in respuestas:
            print(i)
        break