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

        print(f"{self.nombre} - Creditos:  {apuesta} ")
        

        while apuesta !=0 : 
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
                print(f"¡Dos iguales! Ganastes  {premio}")
                self.credito+=premio
            else:               
                print(f"perdistes {apuesta}")
                
            
            apuesta=int(input("¿Cuánto apuestas? (0 para salir): "))
        else:
            print(f"Saliste con $/{self.credito}. ¡Vuelve pronto!")


    


maquina1=Tragamonedas("La Siete",100 )
apuesta=int(input("¿Cuánto apuesta? (0 para salir): "))
maquina1.jugar(apuesta)