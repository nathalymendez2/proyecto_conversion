import tkinter as tk
from tkinter import messagebox

def validar(valor):
    try:
        return float(valor)
    except ValueError:
        messagebox.showerror("Porfavor, ingrese otro número.")
        return None
    
