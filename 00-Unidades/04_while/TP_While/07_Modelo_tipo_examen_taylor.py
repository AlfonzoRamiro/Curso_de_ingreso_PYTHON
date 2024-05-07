import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el voton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
          de crédito y su edad promedio.
3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
          pagaron con tarjeta de débito  respecto al total de personas en la lista.
4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
        los aplicados a tarjetas de crédito
5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
        tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
        edad es un número primo.
7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
        pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador_masc = 0
        contador_fem = 0
        contador_otro = 0
        contador_general_credito = 0
        edades_general_credito = 0
        contador_campo = 0
        contador_general = 0
        contador_platea = 0
        contador_platea_debito = 0 
        seguir = True
        max_precio_general = 0

        while seguir == True:
            nombre = input("Ingrese su nombre: ")
            
            edad = input("Ingrese su edad: (No menor a 16)")
            edad = int(edad)
            while edad < 16:
                edad = input("Reingrese su edad: (No menor a 16)")
                edad = int(edad)

            genero = input("Ingrese su género: (Masculino, Femenino, Otro)")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input("Reingrese su género: (Masculino, Femenino, Otro)")

            tipo_de_entrada = input("Ingrese su tipo de entrada: (General, Campo, Platea)")
            while tipo_de_entrada != "General" and tipo_de_entrada != "Campo" and tipo_de_entrada != "Platea":
                tipo_de_entrada = input("Reingrese su género: (General, Campo, Platea)")

            medio_de_pago = input("Ingrese el medio de pago: (Crédito, Efectivo, Débito)")
            while medio_de_pago != "Credito" and medio_de_pago != "Efectivo" and medio_de_pago != "Debito":
                medio_de_pago = input("Reingrese su género: (Crédito, Efectivo, Débito)")

            match tipo_de_entrada:
                case "Campo":
                    contador_campo += 1
                    match genero:
                        case "Masculino":
                            contador_masc += 1
                        case "Femenino":
                            contador_fem += 1
                        case "Otro":
                            contador_otro += 1
                
                case "General":
                    contador_general += 1
                    match medio_de_pago:
                        case "Credito":
                            contador_general_credito += 1
                            edades_general_credito += edad
                        case "Debito":
                            pass

                
                case "Platea":
                    contador_platea += 1
                    if medio_de_pago == "Debito":
                        contador_platea_debito += 1

            
            
            
            
            seguir = question("", "Desea continuar?")



        if contador_masc > contador_fem and contador_masc > contador_otro:
            mas_frecuente_campo = "Masculino"
        elif contador_fem > contador_otro:
            mas_frecuente_campo = "Femenino"
        else:
            mas_frecuente_campo = "Otro"

        if contador_general_credito > 0:
            edad_promedio_personas_general_credito = edades_general_credito / contador_general_credito
        else:
            edad_promedio_personas_general_credito = "No se encontraron personas con entrada General y abono con credito"
        
        contador_total = contador_general + contador_campo + contador_platea
        porcentaje_platea_debito = (contador_platea_debito * 100) / contador_total
        
        
        print(f"1) El género más frecuente en Campo es: {mas_frecuente_campo}")
        print(f"2) La cantidad de personas con entrada General y abono con credito es: {contador_general_credito} y su edad promedio es: {edad_promedio_personas_general_credito}")
        print(f"3) El porcentaje de personas que compraron entradas en Platea y pagaron con tarjeta de debito es: {porcentaje_platea_debito}%")

                    
  
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()