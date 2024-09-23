import tkinter as tk
from tkinter import ttk

# Funciones de MIA
def buenos_dias():
    print("Ejecutando: Buenos días")

def reproducir_musica():
    print("Ejecutando: Reproducir música")

def obtener_ip():
    print("Ejecutando: Obtener IP")

def mostrar_hora():
    print("Ejecutando: Mostrar Hora")

def apagar():
    print("Ejecutando: Apagar")

def abre():
    print("Ejecutando: Abrir")

def recordatorio():
    print("Ejecutando: Recordatorio")

def pregunta():
    print("Ejecutando: Pregunta")

def captura_pantalla():
    print("Ejecutando: Captura de pantalla")

def bloquear_pantalla():
    print("Ejecutando: Bloquear pantalla")

def que_hay_para_hoy():
    print("Ejecutando: Qué hay para hoy")

def anota():
    print("Ejecutando: Anotar")

def quien_soy():
    print("Ejecutando: Quién soy")

def guardar_codigo():
    print("Ejecutando: Guardar código")

def envia_mensaje():
    print("Ejecutando: Enviar mensaje")

def modo_estudio():
    print("Ejecutando: Modo estudio")

# Funciones del navegador
def nueva_ventana():
    print("Ejecutando: Nueva ventana")

def cierra_ventana():
    print("Ejecutando: Cierra ventana")

def acerca():
    print("Ejecutando: Acercar")

def aleja():
    print("Ejecutando: Alejar")

def cambia_ventana():
    print("Ejecutando: Cambiar ventana")

def recarga():
    print("Ejecutando: Recargar")

def ve_al_historial():
    print("Ejecutando: Ir al historial")

def ve_atras():
    print("Ejecutando: Ir atrás")

def inspeccionar():
    print("Ejecutando: Inspeccionar")

def pantalla_completa():
    print("Ejecutando: Pantalla completa")

def ventana_privada():
    print("Ejecutando: Ventana privada")

def desliza():
    print("Ejecutando: Desliza")

def bajar():
    print("Ejecutando: Bajar")

def principio():
    print("Ejecutando: Principio")

def final():
    print("Ejecutando: Final")

root = tk.Tk()
root.title("MIA - Asistente Virtual")
root.geometry("550x600")
root.configure(bg="#2e2e2e")

contenedor = tk.Frame(root)
contenedor.pack(fill="both", expand=True)

canvas = tk.Canvas(contenedor, bg="#2e2e2e")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

menu_frame = tk.Frame(canvas, bg="#2e2e2e")
canvas.create_window((0, 0), window=menu_frame, anchor="nw")

# Estilos de los botones
button_style = {
    "bg": "#4CAF50", 
    "fg": "white", 
    "font": ("Helvetica", 12),
    "width": 20,
    "height": 2,
    "relief": tk.RAISED
}
tk.Label(menu_frame, text="Funciones de MIA", font=("Helvetica", 16), bg="#2e2e2e", fg="white").grid(row=0, column=0, pady=10)
tk.Button(menu_frame, text="Buenos días", command=buenos_dias, **button_style).grid(row=1, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Reproducir música", command=reproducir_musica, **button_style).grid(row=2, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Obtener IP", command=obtener_ip, **button_style).grid(row=3, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Mostrar Hora", command=mostrar_hora, **button_style).grid(row=4, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Apagar", command=apagar, **button_style).grid(row=5, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Abrir", command=abre, **button_style).grid(row=6, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Recordatorio", command=recordatorio, **button_style).grid(row=7, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Pregunta", command=pregunta, **button_style).grid(row=8, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Captura de pantalla", command=captura_pantalla, **button_style).grid(row=9, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Bloquear pantalla", command=bloquear_pantalla, **button_style).grid(row=10, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Qué hay para hoy", command=que_hay_para_hoy, **button_style).grid(row=11, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Anotar", command=anota, **button_style).grid(row=12, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Quién soy", command=quien_soy, **button_style).grid(row=13, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Guardar código", command=guardar_codigo, **button_style).grid(row=14, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Enviar mensaje", command=envia_mensaje, **button_style).grid(row=15, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Modo estudio", command=modo_estudio, **button_style).grid(row=16, column=0, padx=10, pady=5)
tk.Label(menu_frame, text="Interacción con el navegador", font=("Helvetica", 16), bg="#2e2e2e", fg="white").grid(row=0, column=1, pady=10)
tk.Button(menu_frame, text="Nueva ventana", command=nueva_ventana, **button_style).grid(row=1, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Cierra ventana", command=cierra_ventana, **button_style).grid(row=2, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Acerca", command=acerca, **button_style).grid(row=3, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Aleja", command=aleja, **button_style).grid(row=4, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Cambiar ventana", command=cambia_ventana, **button_style).grid(row=5, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Recargar", command=recarga, **button_style).grid(row=6, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Ver historial", command=ve_al_historial, **button_style).grid(row=7, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Ir atrás", command=ve_atras, **button_style).grid(row=8, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Inspeccionar", command=inspeccionar, **button_style).grid(row=9, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Pantalla completa", command=pantalla_completa, **button_style).grid(row=10, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Ventana privada", command=ventana_privada, **button_style).grid(row=11, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Desliza", command=desliza, **button_style).grid(row=12, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Bajar", command=bajar, **button_style).grid(row=13, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Principio", command=principio, **button_style).grid(row=14, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Final", command=final, **button_style).grid(row=15, column=1, padx=10, pady=5)

root.mainloop()
