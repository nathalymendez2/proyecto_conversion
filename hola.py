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
        resultado-config(text=f"{valor} lb = {resultado} kg")

