import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.attributes("-topmost", True)
        self.configure(bg="#202020")
        self.title("La Calculadora!")
        self.iconbitmap("1200px-Circle-icons-calculator.svg.ico")
        
        self.resultado = tk.StringVar()
        self.resultado.set("")
        
        self.entrada = tk.Label(width=20, height=2, justify="right", font=("Arial", 20), padx=5, anchor="e", text=1)
        self.entrada.grid(row=0, column=0, columnspan=4)
        self.entrada.config(textvariable=self.resultado)
        
        self.texto_actual = 1
        
        self.operacion_realizada = False # indicando que es falso que se ha realizado la operacion
        
        self.frame = tk.Frame(self, bg="#202020", height=2)
        self.frame.grid(row=1, column=0)
        self.crear_botones()
        
    def crear_botones(self):
        botones = [
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3),
            ("0", 5, 0), ("C", 5, 2), ("=", 5, 3)
        ]

        for (texto, fila, columna) in botones:
            if texto == "0":  # Verifica si el texto es "0" para ajustar el columnspan
                boton = tk.Button(self, text=texto, width=22, height=2, pady=5, command=lambda t=texto: self.insertar_valores(t))
                boton.grid(row=fila, column=columna, columnspan=2, padx=2, pady=2)
            else:
                boton = tk.Button(self, text=texto, width=10, height=2, pady=5, command=lambda t=texto: self.insertar_valores(t))
                boton.grid(row=fila, column=columna, padx=2, pady=2)
    
    def insertar_valores(self, valor):
        if valor == "C":
            self.resultado.set("")
        elif valor == "=":
            try:
                resultado = eval(self.resultado.get())
                self.resultado.set(resultado)
                self.operacion_realizada = True
            except Exception as e:
                self.resultado.set("Valor no numerico")
                self.operacion_realizada = True
        else:
            if self.operacion_realizada:  # Si se ha realizado una operación, borrar texto anterior
                self.resultado.set("")
                self.operacion_realizada = False
                self.resultado.set(self.resultado.get() + valor)
            else:
                self.resultado.set(self.resultado.get() + valor)
calculadora = Calculadora()
calculadora.mainloop()