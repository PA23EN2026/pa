Class Mi_Clase:
    def __init__(self, num1, num2, num3):
        self.__num1 = num1
        self.__num2 = num2
        self.__num3 = num3
        

    def sumar(self):
        return self._num1 + self.num2 + self._num3

    def mayor(self):
        return max(self._num1, self.num2, self._num3)

    def menor(self):
        return min(self._num1, self.num2, self._num3)

    def iguales(self):
        return self._num1 == self.num2 == self._num3