class Numeros:
    def __init__(self, numero1, numero2, numero3):
        self.__numero1 = numero1
        self.__numero2 = numero2
        self.__numero3 = numero3
    
    def sumar(self):
        suma = self.__numero1 + self.__numero2 + self.__numero3
        return f"suma: {suma}"
    
    def mayor(self):
        if self.numero1 > self.numero2 and self.numero1 > self.numero3:
            print(f"El numero {self.numero1} es mayor")
        elif self.numero2 > self.numero1 and self.numero2 > self.numero3:
            print(f"El numero {self.numero2} es mayor")
        elif self.numero3 > self.numero1 and self.numero3 > self.numero2:
            print(f"El numero {self.numero3} es mayor")
    

        