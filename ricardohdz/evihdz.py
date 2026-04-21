class Trabajo:
    def __init__(self,nombre,salario,extras,bonos,puesto):
        self.__nombre = nombre 
        self.__salario = salario 
        self.__extras = extras
        self.__bonos = bonos 
        self.__puesto = puesto
    
    def salario_total(self):
        extras = self.__extra * 100  
        total = self.__salario + extras + self.__bono
        return total
    