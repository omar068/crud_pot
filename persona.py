class Persona():
    name: str
    cc: str
    age: int
    email:str
    address: str
    personas: dict = {}
    def __init__(self, name:str, cc:str, age:int, email:str, address:str):
        self.name   =   name
        self.cc     =   cc
        self.age    =   age
        self.email  =   email
        self.address=   address
        Persona.personas[cc] = self
    
    @classmethod
    def ToString(cls):
        for persona in cls.personas.keys():
            print(f"""
Nombre: {persona.name}
Edad: {persona.age}
Direción: {persona.address}
E-mail: {persona.email}
                        """)

    