class Numeros:
    def __init__(self, numero1, numero2, numero3):
        self.__numero1 = numero1
        self.__numero2 = numero2
        self.__numero3 = numero3
    
    def sumar(self):
        suma = self.__numero1 + self.__numero2 + self.__numero3
        return f"suma: {suma}"
    
    def mayor(self):
        if self.__numero1 > self.__numero2 and self.__numero1 > self.__numero3:
            return f"El numero {self.__numero1} es mayor"
        elif self.__numero2 > self.__numero1 and self.__numero2 > self.__numero3:
            return f"El numero {self.__numero2} es mayor"
        elif self.__numero3 > self.__numero1 and self.__numero3 > self.__numero2:
            return f"El numero {self.__numero3} es mayor"
            
    def menor(self):
        if self.__numero1 < self.__numero2 and self.__numero1 < self.__numero3:
            return f"El numero {self.__numero1} es menor" 
        elif self.__numero2 < self.__numero1 and self.__numero2 < self.__numero3:
            return f"El numero {self.__numero2} es menor"
        elif self.__numero3 < self.__numero1 and self.__numero3 < self.__numero2:
            return f"El numero {self.__numero3} es menor"
            
    def iguales(self):
        igual1y2 = self.__numero1 == self.__numero2
        igual1y3 = self.__numero1 == self.__numero3
        igual2y3 = self.__numero2 == self.__numero3
        todoigual = self.__numero1 == self.__numero2 == self.__numero3
        
        return f"Numero 1 y 2 son iguales: {igual1y2}, Numero 1 y 3 son iguales: {igual1y3}, Numero 2 y 3 son iguales: {igual2y3}, Todos son iguales: {todoigual}"
    
    def concatenar(self):
        resultado = str(self.__numero1) + str(self.__numero2) + str(self.__numero3)
        return resultado
    
# Prueba de clase
    
numeros1 = Numeros(33, 50, 1)
print("numeros: 33, 50, 1")
print(numeros1.sumar())
print(numeros1.mayor())
print(numeros1.menor())
print(numeros1.concatenar())

print("---------------------------")
print("numeros: 11, 11, 10")
numeros2 = Numeros(11, 11, 10)
print(numeros2.iguales())
