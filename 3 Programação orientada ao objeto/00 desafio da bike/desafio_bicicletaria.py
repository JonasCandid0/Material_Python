class Bicicleta:
    def __init__( self , cor , modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor 

    def buzinar(self):
        print("Plin plin...")

    def parar (self):
        print("Parando a bicicleta")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrunmm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}= {valor}' for chave,valor in self.__dict__.items()])}"

#Os atributos são acessados diretamente da 
# instância usando a sintaxe objeto.atributo
# ex: b1.cor

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
#Os métodos são chamados 
#usando a sintaxe objeto.método()
#ex: b1.buzinar

b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2= Bicicleta ("verde", "monark", "2000", "189")
print(b2)
b2.correr()