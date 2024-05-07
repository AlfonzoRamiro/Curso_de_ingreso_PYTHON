import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Ramiro 
apellido: Barrios Alfonzo
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        max_votos = 0
        min_votos = 0  
        acumulador_votos = 0
        bandera_max_votos = False
        bandera_min_votos = False
        nombre_candidato_mas_votos = None
        nombre_candidato_menos_votos = None
        edad_candidato_menos_votos = 0
        acumulador_edades = 0
        contador_edades = 0       
        
        
        seguir = True
        
        while seguir == True:
            nombre = prompt("", "Ingrese el nombre del candidato")
            
            edad = prompt("", "Ingrese la edad del candidato")
            edad = int(edad)
            while edad <= 25:
                edad = prompt("", "Reingrese la edad del candidato")
                edad = int(edad)
            
            votos = prompt("", "Ingrese la cant. de votos")
            votos = int(votos)
            while votos < 0:
                votos = prompt("", "Reigrese la cant. de votos")
                votos = int(votos)

            acumulador_votos += votos
            acumulador_edades += edad
            contador_edades += 1
            
            if votos > max_votos or bandera_max_votos == False:
                max_votos = votos
                nombre_candidato_mas_votos = nombre
                bandera_max_votos = True

            if votos < min_votos or bandera_min_votos == False:
                min_votos = votos
                nombre_candidato_menos_votos = nombre
                edad_candidato_menos_votos = edad
                bandera_min_votos = True
            
                        
            seguir = question("", "Desea continuar?")

        promedio_edades = acumulador_edades / contador_edades
    
        alert("", f"1) Candidato con más votos: {nombre_candidato_mas_votos}")
        alert("", f"2) Candidato con menos votos: {nombre_candidato_menos_votos}, Edad: {edad_candidato_menos_votos}")
        alert("", f"3) El promedio de edades de los candidatos es: {promedio_edades}")
        alert("", f"4) Total de votos emitidos: {acumulador_votos}")




        
        
        


























if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
