class persona:
    
    def __init__(self,nombre,altura,peso,nacionalidad,color_de_ojos):
        self.nombre: str = nombre
        self.altura : float= altura
        self.peso : float = peso
        self.nacionalidad : str = nacionalidad
        self.color_de_ojos : str = color_de_ojos
        
    def __str__(self):
       return f"Nombre: {self.nombre}. Altura: {self.altura} CM. Peso: {self.peso} Kg. Nacionalidad: {self.nacionalidad}. Color de Ojos: {self.color_de_ojos}."

    def __repr__ (self):
        return self.__str__()
    
def pedirtexto(mensaje):
        
    while True:
        texto = input(mensaje).strip()
        if not texto.replace(" ","").isalpha():
            print("solo se permiten letras en este espacio")
            continue
        return texto  
       
def pedirint(num):
    try:
        return int(input(num))
    except ValueError as e:
        print("Este espacio solo acepta numeros", e)

def pedirfloat(decimal):
    try:
        return float(input(decimal))
    except ValueError as e:
        print("Este espacio solo acepta numeros con decimales", e)
        
personas = []
def mostrar_personas():
    if personas == []:
        return print("no hay personas en la lista")
    else:
        for i, j in enumerate(personas, start=1):
            return (f"{i}. {j}")    
def main():
    indice = "a"
    
    while (indice != 0):
        try:
            indice : int = int(input("----------\nMENÚ\n1. Agregar nueva persona\n2. Mostrar personas\n3. Eliminar personas\n4. editar persona\n>>>" ))
        except ValueError as e:
            print(f"ERROR debe ingresar un número válido, {e} ")
        match indice:
            case 1:
                nombre = pedirtexto("ingrese su nombre: ")

                altura = pedirfloat ("ingrese su altura en formato: M.cm: ")
                peso : float = float(input("ingrese su peso en kg:"))
                nacionalidad : str = input("ingrese su nacionalidad:")
                color_de_ojos : str = input("ingrese su color de ojos:")
                p1 = persona(nombre,altura,peso,nacionalidad,color_de_ojos)
                personas.append(p1)
            case 2:
                print(mostrar_personas())
                        
            case 3:
                
                option: int  = int(input(f"seleccione el numero de la persona que quiere eliminar\n{mostrar_personas()}\n>>>"))
                personas.remove(personas[option-1])
                
            case 4:

                option: int  = int(input(f"seleccione el numero de la persona que quiere editar\n{mostrar_personas()}\n>>>"))
                option2: int = int(input(f"seleccione el numero del atributo a editar\n1.Nombre\n2.Altura\n3.peso\n4.nacionalidad\n5.color de ojos\n>>>"))
                match option2:
                    case 1:
                        personas[option-1].nombre = input("ingrese el nuevo nombre: ")
                    case 2:
                        personas[option-1].altura = input("ingrese la nueva altura: ")
                    case 3:
                        personas[option-1].peso = input("ingrese el nuevo peso: ")
                    case 4:
                        personas[option-1].nacionalidad = input("ingrese la nuevo nacionalidad: ")
                    case 5:
                        personas[option-1].color_de_ojos = input("ingrese el nuevo color de ojos: ")
                    
main()
#"a"