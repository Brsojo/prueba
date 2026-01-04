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
        indice : int = int(input("----------\nMENÚ\n1. Agregar nueva persona\n2. Mostrar personas\n3. Eliminar personas\n4. editar persona\n>>>" ))
        match indice:
            case 1:
                nombre: str = input("ingrese su nombre:")
                altura : float= float(input("ingrese su altura en formato: M.cm:"))
                peso : float = float(input("ingrese su peso en kg:"))
                nacionalidad : str = input("ingrese su nacionalidad:")
                color_de_ojos : str = input("ingrese su color de ojos:")
                p1 = persona(nombre,altura,peso,nacionalidad,color_de_ojos)
                personas.append(p1)
            case 2:
                mostrar_personas()
                        
            case 3:
                
                option: int  = int(input(f"seleccione el numero de la persona que quiere eliminar\n{mostrar_personas()}\n>>>"))
                personas.remove(personas[option-1])
                
            case 4:

                option: int  = int(input(f"seleccione el numero de la persona que quiere editar\n{mostrar_personas()}\n>>>"))
                
main()
#"a"