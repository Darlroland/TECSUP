import random 

class Tragamonedas :
    def __init__(self,nombre,credito ):
        self.nombre= nombre,
        self.credito= credito

    def mostrar(self):
        return f"{self.nombre} con {self.credito} creditos "

    def aleatorio(self):
        
        lista=[]
        for i in range(3):
            numero=random.randint(1,10) 
            lista.append(numero)

        print(lista)

    def girar(self):
        simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]
        
        lista=[]
        for i in range(3):
            elejido= random.choice(simbolos)
            lista.append(elejido)

        print(f"[ {lista[0]}  {lista[1]}  {lista[2] } ]")
        return lista

    def jugar(self,apuesta):
        if apuesta>self.credito:
            print(f"No tienes sufientes saldo: {self.credito} ")
            return
        
        self.credito-=apuesta;

        girar=self.girar()

        if girar[0]==girar[1]==girar[2]:
            premio=apuesta*10
            print(f"jackpot ganastes {premio}")
            self.credito+=premio
            
        elif girar[0]==girar[1] or girar[1]==girar[2] or girar[0]==girar[2]:
            premio=apuesta*2
            print(f"premio chico {premio}")
            self.credito+=premio
        else:
            print(f"perdistes {apuesta}")

    

maquina1= Tragamonedas("La siete", 100)
maquina1.aleatorio()
print(maquina1.girar())
maquina1.jugar(100)

print("-----------------------------------------")
print("-----------------------------------------")


maquina2= Tragamonedas("La Frutal", 250)
maquina3= Tragamonedas("Jackpot City", 500)
print(maquina1.mostrar())
print(maquina2.mostrar())
print(maquina3.mostrar())



