class Person:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return (f'Información:\n'
                f'Nombre: {self.first_name}\n'
                f'Apellido: {self.last_name}')


class Student(Person):
    def __init__(self, fname: str, lname: str, grade: str) -> None:
        super().__init__(fname, lname)
        self.grade = grade

    def __str__(self) -> str:
        return (f'Info del estudiante:\n'
                f'Nombre: {self.full_name()}\n'
                f'Curso: {self.grade}')
    
    def welcome(self) -> str:
        return f'Bienvenido {self.full_name()} a el grado {self.grade}'


# Ejemplo
student = Student('Pepito', 'Perez', '11-1')
print(student.welcome())
print(student)

#Inheritance Class Polymorphism
'''
Polimorfismo es un concepto de programación que permite que diferentes clases sean tratadas como si fueran la misma clase a través de una interfaz común. 
Esto significa que puedes definir un método en una clase base y luego implementar ese mismo método de manera diferente en las clases derivadas.
'''

class Animal:
    def hacer_ruido():
        pass

class Perro(Animal):
    def hacer_ruido(s) -> str:
        return 'Guau!'
    
class Gato(Animal):
    def hacer_ruido(s) -> str:
        return 'Miau!'
    
class Vaca(Animal):
    def hacer_ruido(s) ->str:
        return 'Muuuuuuu!'

class Loro(Animal):
    def hacer_ruido(self) ->str:
        return 'silbido'
    
    
def sonido_del_animal(animal: Animal):
    print(animal.hacer_ruido())

kiara = Perro()
maca = Gato()
mi_vaca = Vaca()
tommy = Loro()

sonido_del_animal(kiara)
sonido_del_animal(maca)
sonido_del_animal(mi_vaca)
sonido_del_animal(tommy)


class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand
    
    def move(s) ->str:
        return "Mover!"

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(s) -> str:
        return 'Navegar'

class Plane(Vehicle):
    def move(s) -> str:
        return 'Volar'
    
carro = Car('Mustang')
bote = Boat('Ibiza')
avion = Plane('Jet')

for vehicle in (carro, bote, avion):
    print(vehicle.brand)
    print(vehicle.move())


'''
Parsear es el proceso de analizar una cadena de texto (como un código, un archivo o un mensaje) para extraer su estructura y significado.

La palabra "parsear" proviene del inglés "parse", que a su vez se deriva del latín "pars", que significa "parte". 
Originalmente, se refería al acto de dividir un texto en partes más pequeñas para analizar su gramática y estructura.

Resumen
En resumen, parsear es un proceso que implica:

Analizar un texto o dato.
Extraer información relevante.
Organizar esa información en una forma que sea más fácil de manejar.


Proceso de analisis para extracion de estrucutra y significado con el fin de organizarlo en una forma mas facil de manejar
'''


try:
    print(No_definida)
except:
    print('Algo paso')