class Cliente:
    codigo_cliente=''
    nombre_cliente=''
    fecha_cliente=''
    descripcion=''
    atencion=''
    costo=0

    def __init__(self):
        self.codigo_cliente='A-001'
        self.nombre_cliente='Juanito Perez'
        self.fecha_cliente='29/06/2023'
        self.descripcion='Pelo Corto casi pelao'
        self.atencion='Lavado de pelo'
        self.costo=20000


    def setCodigo_cliente(self,codigo):
        if codigo[0:1].isalpha() and codigo[1:2] =='-' and codigo[2:5].isdigit():
            self.codigo_cliente = codigo
            return True
        else:
            print("Codigo incorrecto")
            return False


    def setNombre_cliente(self,nombre):
        if len(nombre) > 5:
            self.nombre_cliente = nombre
            return True
        else:
            print("Largo de nombre minimo 5 ")
            return False

    def setCosto(self,costo):
        if costo >= 20000:
            self.costo = costo
            return True
        else:
            print("Costo tiene que ser mayor a 20000 pesos")
            return False
