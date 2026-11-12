import random 

class Tragamonedas :
    def __init__(self,nombre,credito ,simbolos):
        self.nombre= nombre
        self._credito= credito
        self.simbolos=simbolos
        self._total_apostado=0
        self._ganancias_total=0
        self._numero_apuestas=0

    def mostrar(self):
        return f"{self.nombre} con {self._credito} creditos "


    def girar(self):
        lista=[]
        for i in range(3):
            elejido= random.choice(self.simbolos)
            lista.append(elejido)

        print(f"[ {lista[0]}  {lista[1]}  {lista[2] } ]")


        return lista

    def jugar(self):

        self._total_apostado=0
        self._ganancias_total=0 
        self._numero_apuestas=0

        apuesta=int(input("¿Cuánto apuesta? (0 para salir): "))
        
        while apuesta !=0 : 
            
            if apuesta>self._credito:
                print(f"No tienes sufientes saldo: {self._credito} ")
                return

            self._credito-=apuesta

            self._total_apostado+=apuesta
            self._numero_apuestas+=1
            

            resultado=self.girar()

            premio=0
            if resultado[0]==resultado[1]==resultado[2]:
                premio=apuesta*10
                print(f"jackpot ganastes {premio}")
                self._credito+=premio
                
            elif resultado[0]==resultado[1] or resultado[1]==resultado[2] or resultado[0]==resultado[2]:
                premio=apuesta*2
                print(f"¡Dos iguales! Ganastes  {premio}")
                self._credito+=premio
            else:               
                print(f"perdistes {apuesta}")
                
            apuesta=int(input("¿Cuánto apuesta? (0 para salir): "))
            self._ganancias_total+=premio   
 
 



    def estadistica(self):
        print(f"Saliste con $/{self._credito}. ¡Vuelve pronto!")
        print(f"Apostantes {self._numero_apuestas} veces ")
        print(f"Apostantes en total {self._total_apostado} soles ")
        print(f"Ganastes en total {self._ganancias_total} soles")
        

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
                print(f"te queda {self._credito}")
                break

            if apuesta> self._credito:
                print(f"apuesta es mayor al {self._credito}")
                return 

            self._numero_apuestas+=1
            self._total_apostado+=self._credito
            


            self._credito-=apuesta

            girar= self.girar()

            premio=0
            if girar[0]==girar[1]==girar[2]:
                premio=apuesta*15
                self._credito+=premio
                print(f"JACKPOT ,ganastes {premio}")
                
            elif girar[0]==girar[1] or girar[1]==girar[2] or girar[0]==girar[2]:
                premio= apuesta*10
                self._credito+=premio
                print(f"¡Dos iguales! Ganastes {premio}")
                
            else:
                print(f"perdistes {apuesta}")

            apuesta=int(input("¿Cuanto apuestas? (0 para salir):")) 
            self._ganancias_total+=premio

    def estadistica(self):
        print(f"Saliste con $/{self._credito}. ¡Vuelve pronto!")
        print(f"Apostantes {self._numero_apuestas} veces ")
        print(f"Apostantes en total {self._total_apostado} soles ")
        print(f"Ganastes en total {self._ganancias_total} soles")  
        
        

class TragamonedasAnimales(Tragamonedas):
    def __init__(self,nombre,credito ,simbolos=[ "🐶", "🐱" ,"🐼" ,"🦁" ,"🐸"]):
        super().__init__(nombre,credito ,simbolos)

    def jugar(self):

        while True :

            apuesta= int(input(f"Cuanto apostaras  (elije 0 si desea salir ): "))

            if apuesta==0:
                break
                
            if apuesta> self._credito:
                print("No tiene sufiente credido")
                continue

            self._numero_apuestas+=1
            self._total_apostado+=apuesta
            
            self._credito-=apuesta

            animal=input(f" Si aciertas ganaras , que elijes : {self.simbolos} ")

            lista=self.girar()

            eleccion = lista.count(animal)

            premio=0
            if eleccion==3:
                premio=apuesta*15
                print(f"Felicidades ,ganastes x 15 :{premio}")
                self._credito+=premio 
            elif eleccion==2:
                premio=apuesta*5
                print(f"Que suerete adivinastes 2 , ganastes x 5 :{premio}")
                self._credito+=premio
            elif eleccion==1:
                premio=apuesta*2
                print(f"A nada , ganastes x 2: {premio}")
                self._credito+=premio    
            else:
                print("No gano nada ")    
            self._ganancias_total +=premio

        print(f"Gracias por su participacion tienes : {self._credito}")

    def estadistica(self):
        print(f"Saliste con $/{self._credito}. ¡Vuelve pronto!")
        print(f"Apostantes {self._numero_apuestas} veces ")
        print(f"Apostantes en total {self._total_apostado} soles ")
        print(f"Ganastes en total {self._ganancias_total} soles")   

class TragamonedasEmojis (Tragamonedas):
    def __init__(self,nombre,credito ,simbolos=[ "😂", "❤️" ,"🙏" ,"👍" ,"😎"]):
        super().__init__(nombre,credito ,simbolos)

    def jugar(self):

        while True:
            if self._credito<0:
                print(f"No tiene sufiente credito {self._credito} ")
                break

            apuesta= int(input("Cuanto vas apostar(cero si desea salir ) "))

        
            if apuesta > self._credito  or apuesta<0:
                print(f"No tienen suficente saldo ")
                return 

            if apuesta==0:
                break

            self._numero_apuestas+=1
            self._total_apostado+=apuesta

            
            self._credito-=apuesta
            
            resultado=self.girar()

            corazon=resultado.count('❤️')

            unicos= set(resultado)

            premio=0
            if len(unicos)==1 or (len(unicos)==2 and  corazon>=1):
                premio=apuesta*10
                self._credito+=premio
                print(f"Ganastes el premio mayor X10  ,premio: {premio} ")

            elif corazon==1:
                premio=apuesta
                self._credito+=premio       
                print(f"se te devuleve tu apuesta {self.apuesta} ")
            else :
                print("Perdistes puede volvera intentar ")

            self._ganancias_total+=premio
            
    def estadistica(self):
        print(f"Saliste con $/{self._credito}. ¡Vuelve pronto!")
        print(f"Apostantes {self._numero_apuestas} veces ")
        print(f"Apostantes en total {self._total_apostado} soles ")
        print(f"Ganastes en total {self._ganancias_total} soles")   

if __name__=="__main__":

    maquina1=Tragamonedas("La Siete",100,["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"])
    maquina2=TragamonedasFrutas("La Frutal",200)
    maquina3=TragamonedasClasicas("Jackpot City",300)
    maquina4=TragamonedasMundial("El mundial",500)
    maquina5=TragamonedasAnimales("El reino animal",400)
    maquina6=TragamonedasEmojis("Los Emojis",350)

    maquinas=[maquina1,maquina2,maquina3,maquina4,maquina5,maquina6]

    while True:
        opcion= int(input(f""" 
            #########🎰 CASINO ROYALE 🎰###########
            1.La Clásica
            2.La Frutal
            3.Jackpot City
            4.El mundial
            5.El reino animal
            6.Caritas
            7.MOSTRAR ESTADISTICAS DE TODAS
            8.SALIR

            ELIJE UNA OPCION : 
            """))

        
        match opcion:
            case 1:
                
                maquina1.jugar()
                
            case 2:
                
                maquina2.jugar()
            case 3:
                
                maquina3.jugar()   
            
            case 4:
                
                maquina4.jugar()         
                
            case 5:
                
                maquina5.jugar()
                
            case 6:
                
                maquina6.jugar()
            case 7: 
                print("------ESTADISTICAS DEL CASINO --------")

                for m in maquinas:
                    if m._numero_apuestas > 0:
                        print(f"################{m.nombre}####################")
                        m.estadistica()
                    else:
                        print(f"❌ {m.nombre}: Sin actividad todavía.")
            case 8:
                print("Hasta luego")
                break






    
