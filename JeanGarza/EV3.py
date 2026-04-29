class Mi_Clase:
    def __init__(self,num1,num2,num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3
    
    def sumar(self):
        resultado = self.__num1 + self.__num2 + self.__num3
        print(f"El resultado de la suma de esos tres numero es: {resultado}")
     
    @property
    def num1 (self):
        return self.__num1
    


Objetosuma = Mi_Clase(2,5,10)
Objetosuma.sumar()
print(Objetosuma.num1)