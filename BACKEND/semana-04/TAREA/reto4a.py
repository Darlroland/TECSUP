import random 

class Tragamonedas :
    def __init__(self,nombre,credito ,simbolos):
        self.nombre= nombre
        self.credito= credito
        self.simbolos=simbolos

    def mostrar(self):
        return f"{self.nombre} con {self.credito} creditos "


    def girar(self):
        lista=[]
        for i in range(3):
            elejido= random.choice(self.simbolos)
            lista.append(elejido)

        print(f"[ {lista[0]}  {lista[1]}  {lista[2] } ]")


        return lista

    def jugar(self):
        
        apuesta=int(input("¿Cuánto apuesta? (0 para salir): "))
        while apuesta !=0 : 
            
            if apuesta>self.credito:
                print(f"No tienes sufientes saldo: {self.credito} ")
                return
            
            self.credito-=apuesta;

            resultado=self.girar()

            if resultado[0]==resultado[1]==resultado[2]:
                premio=apuesta*10
                print(f"jackpot ganastes {premio}")
                self.credito+=premio
                
            elif resultado[0]==resultado[1] or resultado[1]==resultado[2] or resultado[0]==resultado[2]:
                premio=apuesta*2
                print(f"¡Dos iguales! Ganastes  {premio}")
                self.credito+=premio
            else:               
                print(f"perdistes {apuesta}")
                
            apuesta=int(input("¿Cuánto apuesta? (0 para salir): "))
            
        else:
            print(f"Saliste con $/{self.credito}. ¡Vuelve pronto!")


class TragamonedasFrutas(Tragamonedas):
    def __init__(self,nombre,credito ):
        super().__init__(nombre,credito,["🍒","🍋","🍊"])

        

        
class TragamonedasClasicas(Tragamonedas):
    def __init__(self,nombre,credito ): 
        super().__init__(nombre,credito,["7️⃣","💎", "🔔"])




class TragamonedasMundial(Tragamonedas):
    def __init__(self,nombre,credito ,simbolos=[ "🇵🇪", "🇦🇷","🇫🇷" ,"🇧🇷"]):
        super().__init__(nombre,credito ,simbolos)
    
    def jugar(self):
        
        apuesta=int(input("¿Cuanto apuestas?:")) 
        
        while True :
                
            if apuesta==0:
                print(f"te queda {self.credito}")
                break

            if apuesta> self.credito:
                print(f"apuesta es mayor al {self.creditos}")
                return 

            self.credito-=apuesta

            girar= self.girar()

            if girar[0]==girar[1]==girar[2]:
                premio=apuesta*15
                self.credito+=premio
                print(f"JACKPOT ,ganastes {premio}")
                
            elif girar[0]==girar[1] or girar[1]==girar[2] or girar[0]==girar[2]:
                premio= apuesta*10
                self.credito+=premio
                print(f"¡Dos iguales! Ganastes {premio}")
                
            else:
                print(f"perdistes {apuesta}")

            apuesta=int(input("¿Cuanto apuestas? (0 para salir):")) 

            
        
        
        

class TragamonedasAnimales(Tragamonedas):
    def __init__(self,nombre,credito ,simbolos=[ "🐶", "🐱" ,"🐼" ,"🦁" ,"🐸"]):
        super().__init__(nombre,credito ,simbolos)

    def jugar(self):
        
        

        while True :

            apuesta= int(input(f"Cuanto apostaras  (elije 0 si desea salir ): "))

            if apuesta==0:
                break
                
            if apuesta> self.credito:
                print("No tiene sufiente credido")
                continue

            self.credito-=apuesta

            animal=input(f" Si aciertas ganaras , que elijes : {self.simbolos} ")

            lista=self.girar()

            eleccion = lista.count(animal)

            
            if eleccion==3:
                premio=apuesta*15
                print(f"Felicidades ,ganastes x 15 :{premio}")
                self.credito+=premio 
            elif eleccion==2:
                premio=apuesta*5
                print(f"Que suerete adivinastes 2 , ganastes x 5 :{premio}")
                self.credito+=premio
            elif eleccion==1:
                premio=apuesta*2
                print(f"A nada , ganastes x 2: {premio}")
                self.credito+=premio    
            else:
                print("No gano nada ")    

        print(f"Gracias por su participacion tienes : {self.credito}")

        
class TragamonedasEmojis (Tragamonedas):
    def __init__(self,nombre,credito ,simbolos=[ "😂", "❤️" ,"🙏" ,"👍" ,"😎"]):
        super().__init__(nombre,credito ,simbolos)

    def jugar(self):
        pass


if __name__=="__main__":


    #maquina1=Tragamonedas("La Siete",100,["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"])
    #maquina2=TragamonedasFrutas("La Frutal",100)
    #maquina2.jugar()
    #maquina3=TragamonedasClasicas("Jackpot City",100)
    #maquina2.jugar()
    #maquina4=TragamonedasMundial("El mundial",500)
    #maquina4.jugar()
    maquina5=TragamonedasAnimales("El reino animal",100)
    maquina5.jugar()

    
