from tkinter import * # tkinter sirve para crear interfaces gráficas de usuario

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
                         variable=variables_comida[contador])
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
                         variable=variables_bebida[contador])

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
                         variable=variables_bebida[contador])

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

# evitar que la talla se cierre
aplicacion.mainloop()
