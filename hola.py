import tkinter as tk
from tkinter import messagebox

def validar(valor):
    try:
        return float(valor)
    except ValueError:
        messagebox.showerror("Porfavor, ingrese otro número.")
        return None
    
def longitudes(tipo, entrada, resultado):
    valor = validar(entrada.get())
    if valor is None:
        return
    
    if tipo == "metro_kilometro":
        resultadoo = valor /1000
        resultado.config(text=f"{valor} pulgadas = {resultado} km")
    
    elif tipo == "pulgada_metro":
        resultadoo = valor * 0.02
        resultado.config(text=f"{valor} pulgadas = {resultado} metros")

def masa(tipo, entrada, resultado):
    valor = validar(entrada.get())
    if valor is None:
        return
    
    if tipo == "kilogramo_gramo":
        resultadoo = valor*1000
        resultado.config(text=f"{valor} kg = {resultado} g")
    
    elif tipo == "libra_kilogramo":
        resultadoo = valor*0.4
        resultado.config(text=f"{valor} lb = {resultado} kg")

def tiempo(tipo, entrada, resultado):
    valor = validar(entrada.get())
    if valor is None:
        return
    
    if tipo == "segundo_minuto":
        resultadoo = valor/60
        resultado.config(text=f"{valor} segundos = {resultado} minutos")

    elif tipo == "hora_dia":
        resultadoo = valor/24
        resultado.config(text=f"{valor} horas = {resultado} días")

    def formulario(titulo, opciones, conversion):
        ventana = tk.Toplevel()
        ventana.title(titulo)
        ventana.geometry("400x400")

        tk.Label(ventana, text="Valor a convertir:").pack(pady=5)
        entrada = tk.Entry(ventana)
        entrada.pack(pady=5)

        for nombre, tipo in opciones:
            frame =tk.Frame(ventana)
            frame.pack(pady=2)
            boton = tk.Button(frame, text=nombre, command=lambda t=tipo: conversion(t, entrada, resultado))
            boton.pack()

        resultado = tk.Label(ventana, text="", fg= "pink")
        resultado.pack(pady=10)

    principal = tk.Tk()
    principal.title("Menú de Conversiones")
    principal.geometry("400x400")

    menu = tk.Menu(principal)
    principal.config(menu=menu)

    menu_conversion = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Conversión", menu=menu_conversion)

    menu_conversion.add_command(label="Longitud", command=lambda: formulario(
        "Conversión de longitudes",
        [("Metros a kilometros", "metros_kilometros"), ("Pulgadas a Metros", "pulgadas_metros")],
        longitudes))
    
    menu_conversion.add_command(label="Masa", command=lambda: formulario(
        "Conversión de Masa",
        [("Kilogramos a gramos", "kilogramo_gramo"), ("Libras a kilogramos", "libra_kilogramo")],
        masa))
    
    menu_conversion.add_command(label="Tiempo", command=lambda: formulario(
        "Conversión de tiempo",
        [("Segundos a minutos", "segundo_minuto"), ("Horas a días", "hora_dia")],
        tiempo))
    
    principal.mainloop()


