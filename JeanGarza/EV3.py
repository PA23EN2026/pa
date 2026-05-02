class Mi_Clase:
    def __init__(self,num1,num2,num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3
    
    def sumar(self):
        resultado = self.__num1 + self.__num2 + self.__num3
        print(f"El resultado de la suma de esos tres numero es: {resultado}")
     

    def mayor(self):
        if self.__num1 > self.__num2 and self.__num1 > self.__num3:
            print(f"El numero mayor es: {self.__num1}")
        
        elif self.__num2 > self.__num3:
            print(f"El numero mayor es: {self.__num2}")
        
        else:
            print(f"El numero mayor es: {self.__num3}")
    
    
    def menor(self):
        if self.__num1 < self.__num2 and self.__num1 < self.__num3:
            print(f"El numero menor es: {self.__num1}")

        elif self.__num2 < self.__num3:
            print(f"El numero menor es: {self.__num2}")
        
        else:
            print(f"El numero menor es: {self.__num3}")
    

    def iguales(self):
        igual = False
        if self.__num1 == self.__num2 and self.__num1 == self.__num3:
            igual = True
            print(f"Son iguales: {igual}")
        else:
            print(f"Son iguales: {igual}")


    @property
    def num1 (self):
        return self.__num1
    
    @num1.setter
    def num1(self,nuevonum):
        return self.__num1 == nuevonum
    
    


objetosuma = Mi_Clase(1,2,3)
objetosuma.sumar()
print(objetosuma.num1)

objetomayor_menor = Mi_Clase(1,10,100)
objetomayor_menor.mayor()
objetomayor_menor.menor()

objeto_igual_T = Mi_Clase(1,1,1)
objeto_igual_F = Mi_Clase(1,2,3)

objeto_igual_T.iguales()
objeto_igual_F.iguales()

