from tkinter import * # tkinter sirve para crear interfaces gráficas de usuario

# funcionalidad de la calculadora
operador = ""

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ""

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set("0")
        x += 1


    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_comida[x].set("0")
        x += 1


    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_comida[x].set("0")
        x += 1

# iniciar la ventana
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry("1224x756")

# evitar maximizar la ventana
# aplicacion.resizable(0,0) # 0,0 = no se puede maximizar

# título de la ventana
aplicacion.title("Stefan futuro experto en python")

# color de fondo de la ventana
aplicacion.config(bg="burlywood")

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT )
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Stefan python", fg="azure4",
                        font=("Dosis", 58), bg="burlywood", width=27)

etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4", padx=50)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comida", font=("Dosis", 19, "bold"),
                                                                 bd=1, relief=FLAT, fg="azure4")
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas", font=("Dosis", 19, "bold"),
                                                                 bd=1, relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres", font=("Dosis", 19, "bold"),
                                                                 bd=1, relief=FLAT, fg="azure4")
panel_postres.pack(side=LEFT)

# panel derecho
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg="burlywood")
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg="burlywood")
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg="burlywood")
panel_botones.pack()

# lista de productos
lista_comidas = ["Pizza", "Hamburguesa", "Papas fritas", "Hot dog", "Tacos", "Burritos", "Pollo frito", "Alitas"]
lista_bebidas = ["Agua", "Refresco", "Cerveza", "Vino", "Tequila", "Whisky", "Vodka", "Ron"]
lista_postres = ["Helado", "Pastel", "Galletas", "Tiramisu", "Flan", "Mousse", "Brownie", "Crepe"]

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    # crear checkbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=("Dosis", 12, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set("0")
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:

    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=("Dosis", 12, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set("0")
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items postres
variables_postre = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:

    # crear checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=("Dosis", 12, "bold"),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set("0")
    cuadros_postres[contador] = Entry(panel_postres,
                                     font=("Dosis", 18, "bold"),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                  column=1)

    contador += 1


# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiqueta de panel costo y campos de entrada

# comida
etiqueta_costo_comida = Label(panel_costos,
                            text="Costo comida:",
                            font=("Dosis", 12, "bold"),
                            bg="azure4",
                            fg="white")
etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=("Dosis", 12, "bold"),
                           bd=1,
                           width=10,
                           state="readonly",
                           textvariable = var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# bebida
etiqueta_costo_bebida = Label(panel_costos,
                            text="Costo bebida:",
                            font=("Dosis", 12, "bold"),
                            bg="azure4",
                            fg="white")
etiqueta_costo_bebida.grid(row=1, column=0)

texto_costo_bebida = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable = var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# postre
etiqueta_costo_postre = Label(panel_costos,
                            text="Costo postre:",
                            font=("Dosis", 12, "bold"),
                            bg="azure4",
                            fg="white")
etiqueta_costo_postre.grid(row=2, column=0)

texto_costo_postre = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable = var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# subtotal
etiqueta_subtotal = Label(panel_costos,
                            text="Subtotal:",
                            font=("Dosis", 12, "bold"),
                            bg="azure4",
                            fg="white")
etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable = var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# impuesto
etiqueta_impuesto = Label(panel_costos,
                            text="Impuesto:",
                            font=("Dosis", 12, "bold"),
                            bg="azure4",
                            fg="white")
etiqueta_impuesto.grid(row=1, column=2)

texto_impuesto = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable = var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

# total
etiqueta_total = Label(panel_costos,
                            text="Total:",
                            font=("Dosis", 12, "bold"),
                            bg="azure4",
                            fg="white")
etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                            font=("Dosis", 12, "bold"),
                            bd=1,
                            width=10,
                            state="readonly",
                            textvariable = var_total)
texto_total.grid(row=2, column=3, padx=41)

# botones
botones = ["total", "recibo", "guardar", "reset"]
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=("Dosis", 14, "bold"),
                   fg="white",
                   bg="azure4",
                   bd=1,
                   width=9)
    boton.grid(row=0,
               column=columnas)
    columnas += 1

# area de recibo
texto_recibo = Text(panel_recibo,
                    font=("Dosis", 12, "bold"),
                    bd=1,
                    width=42,
                    height=10)

texto_recibo.grid(row=0,
                  column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=("Dosis", 16, "bold"),
                          bd=1,
                          width=32)

visor_calculadora.grid(row=0,
                          column=0,
                          columnspan=4)

# botones calculadora
botones_calculadora = ["7", "8", "9", "+",
                       "4", "5", "6", "-",
                       "1", "2", "3", "x",
                       "R", "B", "0", "/"]

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                     text=boton.title(),
                     font=("Dosis", 16, "bold"),
                     fg="white",
                     bg="azure4",
                     bd=1,
                     width=8)

    botones_guardados.append(boton)

    boton.grid(row=fila,
                column=columna)

    if columna == 3:
        fila += 1

    columna += 1
    if columna == 4:
        columna = 0

botones_guardados[0].configure(command=lambda: click_boton("7"))
botones_guardados[1].configure(command=lambda: click_boton("8"))
botones_guardados[2].configure(command=lambda: click_boton("9"))
botones_guardados[3].configure(command=lambda: click_boton("+"))
botones_guardados[4].configure(command=lambda: click_boton("4"))
botones_guardados[5].configure(command=lambda: click_boton("5"))
botones_guardados[6].configure(command=lambda: click_boton("6"))
botones_guardados[7].configure(command=lambda: click_boton("-"))
botones_guardados[8].configure(command=lambda: click_boton("1"))
botones_guardados[9].configure(command=lambda: click_boton("2"))
botones_guardados[10].configure(command=lambda: click_boton("3"))
botones_guardados[11].configure(command=lambda: click_boton("*"))
botones_guardados[12].configure(command=obtener_resultado)
botones_guardados[13].configure(command=borrar)
botones_guardados[14].configure(command=lambda: click_boton("0"))
botones_guardados[15].configure(command=lambda: click_boton("/"))

# evitar que la talla se cierre
aplicacion.mainloop()
