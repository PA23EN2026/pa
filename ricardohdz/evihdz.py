class Trabajo:
    def __init__(self, nombre, salario, Hextras, bonos, puesto):
        self.__nombre = nombre 
        self.__salario = salario 
        self.__Hextras = Hextras
        self.__bonos = bonos 
        self.__puesto = puesto
    
    def salario_total(self):
        Hextras = self.__Hextras * 100  
        total = self.__salario + Hextras + self.__bonos
        return total
    
    def horas_extra(self, horas):
        if horas > 0:
            self.__Hextras += horas
            print("Horas extra agregadas")
        else:
            print("sin horas extras")

    def info(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Puesto: {self.__puesto}")
        print(f"Salario base: ${self.__salario}")
        print(f"Horas extra: {self.__Hextras}")
        print(f"Bono: ${self.__bonos}")
        print(f"Salario total: ${self.salario_total()}")

    # GETTERS
    def get_nombre(self):
        return self.__nombre

    def get_puesto(self):
        return self.__puesto

    def get_salario_base(self):
        return self.__salario

    def get_horas_extra(self):
        return self.__Hextras

    def get_bono(self):
        return self.__bonos

    # SETTERS
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_puesto(self, puesto):
        self.__puesto = puesto

    def set_salario_base(self, salario):
        if salario > 0:
            self.__salario = salario
        else:
            print("Error en salario")

    def set_horas_extra(self, horas):
        if horas >= 0:
            self.__Hextras = horas
        else:
            print("Horas inválidas")

    def set_bonos(self, bonos):
        if bonos >= 0:
            self.__bonos = bonos
        else:
            print("Bono inválido")


# PRUEBA
empleado = Trabajo("Ricardo", 8000, 5, 1000, "cajero")
empleado.info()

empleado.horas_extra(3)
print("Nuevo salario total:", empleado.salario_total())

empleado.set_bonos(1500)

print("\n--- Información ---")
empleado.info()