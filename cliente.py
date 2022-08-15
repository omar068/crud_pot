from persona import Persona

class Cliente(Persona):
    clientes: dict = {}
    cc: str
    puntos: int
    def __init__(self, name:str, age:int, email:str, address:str, cedula: str):
        super().__init__(name, age, email, address)
        self.cc = cedula
        self.puntos = 0
        Cliente.clientes[cc] = self

    
    
    @classmethod
    def ToString(cls):
        for cliente in cls.clientes.keys():
            print(f"""
Nombre: {cliente.name}
Edad: {cliente.age}
Direción: {cliente.address}
E-mail: {cliente.email}
                        """)

    @classmethod
    def update_cliente(cls, cc: int):
        for cliente in cls.clientes:
            if cliente.cc == cc:
                cliente.email = input("Ingrese el nuevo E-mail: ")
                cliente.address = input("Ingrese la nueva dirección: ")
                print(f"""
Nombre: {cliente.name}
Edad: {cliente.age}
Direción: {cliente.address}
E-mail: {cliente.email}
Datos actualizados de forma exitosa!!!""")
            break

    def update_puntos(self, puntos):
        
