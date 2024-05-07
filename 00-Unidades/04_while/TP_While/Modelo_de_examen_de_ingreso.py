import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

Nombre
Importe ganado (mayor o igual $1000)
Género (“Femenino”, “Masculino”, “Otro”)
Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

1) Nombre y género de la persona que más ganó.
2) Promedio de dinero ganado en Ruleta.
3) Porcentaje de personas que jugaron en el Tragamonedas.
4) Cuál es el juego menos elegido por los ganadores.
5) Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000
6) Porcentaje de dinero en función de cada juego
7) Nombre del jugador que más dinero ganó jugando poker

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        max_ganado = 0
        bandera_maximo = False
        contador_ruleta = 0
        acumulador_ruleta = 0
        contador_poker = 0
        contador_tragamonedas = 0
        contador_no_poker = 0
        acumulador_no_poker = 0
        acumulador_poker = 0
        acumulador_tragamonedas= 0
        max_ganado_poker = 0
        bandera_maximo_poker = False

        seguir = True

        while seguir == True:
            nombre = prompt("", "Ingrese su nombre: ")
            
            importe_ganado = prompt("", "Ingrese el importe ganado: (mayor o igual $1000)")
            importe_ganado = float(importe_ganado)
            while importe_ganado < 1000:
                importe_ganado = prompt("", "Reingrese el importe ganado: (mayor o igual $1000)")
                importe_ganado = float(importe_ganado)
            
            genero = prompt("", "Ingrese su género: (Masculino, Femenino, Otro)") 
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("", "Reingrese su género: (Masculino, Femenino, Otro)")

            juego = prompt("", "Ingrese su juego: (Ruleta, Poker, Tragamonedas)")
            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = prompt("", "Reingrese su juego: (Ruleta, Poker, Tragamonedas)")

            if importe_ganado > max_ganado or bandera_maximo == False:
                max_ganado = importe_ganado
                nombre_persona_que_mas_gano = nombre
                genero_persona_que_mas_gano = genero
                bandera_maximo = True
            
            match juego:
                case "Ruleta":
                    contador_ruleta += 1
                    acumulador_ruleta += importe_ganado
                
                case "Poker":
                    contador_poker += 1
                    acumulador_poker += importe_ganado
                    if importe_ganado > max_ganado_poker or bandera_maximo_poker == False:
                        max_ganado_poker = importe_ganado
                        nombre_persona_que_mas_gano_poker = nombre
                        bandera_maximo_poker = True
                case "Tragamonedas":
                    contador_tragamonedas += 1
                    acumulador_tragamonedas += importe_ganado
            
            if juego != "Poker" and importe_ganado > 15000:
                contador_no_poker += 1
                acumulador_no_poker += importe_ganado

            seguir = question("", "Desea continuar?")
            

        if contador_ruleta  > 0:
            promedio_dinero_ganado_ruleta = acumulador_ruleta / contador_ruleta
        else:
            promedio_dinero_ganado_ruleta = "Ningun ganador jugó Ruleta"
        
        contador_total = contador_ruleta + contador_poker + contador_tragamonedas
        porcentaje_tragamonedas_del_total = (contador_tragamonedas * 100) / contador_total
        
        
        acumulador_total = acumulador_poker + acumulador_tragamonedas + acumulador_ruleta
        porcentaje_tragamonedas_importe_del_total = (acumulador_tragamonedas * 100) / acumulador_total
        porcentaje_ruleta_importe_del_total = (acumulador_ruleta * 100) / acumulador_total
        porcentaje_poker_importe_del_total = (acumulador_poker * 100) / acumulador_total
        
        if contador_ruleta < contador_poker and contador_ruleta < contador_tragamonedas:
            menos_jugado = "El juego menos jugado por los ganadores es Ruleta"
        elif contador_poker < contador_tragamonedas:
            menos_jugado = "El juego menos jugado por los ganadores es Poker"
        else:
            menos_jugado = "El juego menos jugado por los ganadores es Tragamonedas"
        
        if contador_no_poker > 0:
            promedio_no_poker = acumulador_no_poker / contador_no_poker
        else:
            promedio_no_poker = "No hay ningun ganador que no haya jugado Poker y/o supere los 15000$"
        
        
        alert("", f"1) El nombre de la persona que mas gano es: {nombre_persona_que_mas_gano} y su genero es: {genero_persona_que_mas_gano}")
        alert("", f"2) El promedio de dinero ganado en Ruleta: {promedio_dinero_ganado_ruleta}")
        alert("", f"3) El porcentaje de personas que jugaron en el Tragamonedas es: {porcentaje_tragamonedas_del_total}%")
        alert("", f"4) {menos_jugado}")
        alert("", f"5) El promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000, es: {promedio_no_poker}")
        alert("", f"6) El porcentaje de dinero ganado con respecto del total es: Ruleta: {porcentaje_ruleta_importe_del_total}%, Poker: {porcentaje_poker_importe_del_total}%, Tragamonedas; {porcentaje_tragamonedas_importe_del_total}%")
        alert("", f"7) El nombre de la persona que más dinero ganó jugando Poker es: {nombre_persona_que_mas_gano_poker}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
