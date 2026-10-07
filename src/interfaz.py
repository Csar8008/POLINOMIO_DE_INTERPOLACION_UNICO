
import tkinter as tk
from tkinter import ttk, messagebox
from interpolacion import calcular_interpolacion
from polinomio import limpiar_coeficientes, evaluar_polinomio, formatear_polinomio


class InterfazApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Polinomio de Interpolación Único")
        self.root.geometry("640x720")
        self.root.resizable(False, False)

        self.entradas_x = []
        self.entradas_y = []
        self.coeficientes_actuales = None

        self._crear_componentes()

    def _crear_componentes(self):
        lbl_titulo = tk.Label(
            self.root, 
            text="POLINOMIO DE INTERPOLACIÓN ÚNICO", 
            font=("Arial", 12, "bold"),
            pady=10
        )
        lbl_titulo.pack()

        frame_puntos = tk.Frame(self.root)
        frame_puntos.pack(pady=5)

        tk.Label(frame_puntos, text="Número de puntos:").grid(row=0, column=0, padx=5)
        self.ent_num_puntos = tk.Entry(frame_puntos, width=5, justify="center")
        self.ent_num_puntos.insert(0, "3")
        self.ent_num_puntos.grid(row=0, column=1, padx=5)

        btn_generar = tk.Button(
            frame_puntos, 
            text="Actualizar", 
            bg="#E91E63", 
            fg="white", 
            font=("Arial", 9, "bold"), 
            command=self._generar_tabla
        )
        btn_generar.grid(row=0, column=2, padx=5)

        btn_limpiar = tk.Button(
            frame_puntos, 
            text="Limpiar Tabla", 
            bg="#EC407A", 
            fg="white", 
            font=("Arial", 9, "bold"), 
            command=self._limpiar_tabla
        )
        btn_limpiar.grid(row=0, column=3, padx=5)

        self.frame_tabla_container = tk.Frame(self.root, bd=1, relief="sunken")
        self.frame_tabla_container.pack(pady=10, fill="x", padx=20)

        self.canvas = tk.Canvas(self.frame_tabla_container, height=95)
        self.scrollbar = ttk.Scrollbar(self.frame_tabla_container, orient="horizontal", command=self.canvas.xview)
        self.frame_tabla = tk.Frame(self.canvas)

        self.frame_tabla.bind(
            "<Configure>", 
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.frame_tabla, anchor="nw")
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="top", fill="both", expand=True)
        self.scrollbar.pack(side="bottom", fill="x")

        btn_calcular = tk.Button(
            self.root, 
            text="CALCULAR", 
            bg="#E91E63", 
            fg="white", 
            font=("Arial", 10, "bold"),
            padx=20, pady=5,
            command=self._calcular
        )
        btn_calcular.pack(pady=5)

        frame_resultados = tk.LabelFrame(self.root, text="Resultados", padx=10, pady=5)
        frame_resultados.pack(pady=5, fill="both", expand=True, padx=20)

        scroll_res = tk.Scrollbar(frame_resultados)
        scroll_res.pack(side="right", fill="y")

        self.txt_resultados = tk.Text(
            frame_resultados, 
            height=8, 
            font=("Consolas", 9), 
            yscrollcommand=scroll_res.set
        )
        self.txt_resultados.pack(fill="both", expand=True)
        scroll_res.config(command=self.txt_resultados.yview)

        frame_eval = tk.LabelFrame(
            self.root, 
            text=" EVALUACIÓN DEL POLINOMIO ", 
            font=("Arial", 11, "bold"), 
            fg="#1B5E20", 
            bg="#E8F5E9", 
            padx=15, pady=18
        )
        frame_eval.pack(pady=10, fill="x", padx=20)

        tk.Label(
            frame_eval, 
            text="Evaluar en X =", 
            font=("Arial", 11, "bold"), 
            bg="#E8F5E9"
        ).grid(row=0, column=0, padx=5)
        
        self.ent_eval_x = tk.Entry(frame_eval, width=9, justify="center", font=("Arial", 11, "bold"))
        self.ent_eval_x.grid(row=0, column=1, padx=5)
        self.ent_eval_x.bind("<Return>", lambda e: self._evaluar_x())

        btn_evaluar = tk.Button(
            frame_eval, 
            text="Evaluar P(x)", 
            bg="#4CAF50", 
            fg="white", 
            font=("Arial", 10, "bold"), 
            padx=10, pady=2,
            command=self._evaluar_x
        )
        btn_evaluar.grid(row=0, column=2, padx=12)

        self.lbl_resultado_eval = tk.Label(
            frame_eval, 
            text="P(x) = ---", 
            font=("Arial", 13, "bold"), 
            fg="#2E7D32", 
            bg="#E8F5E9"
        )
        self.lbl_resultado_eval.grid(row=0, column=3, padx=15)

        self._generar_tabla()

    def _generar_tabla(self):
        try:
            n = int(self.ent_num_puntos.get())
            if n < 2:
                raise ValueError("Mínimo 2 puntos.")
        except ValueError:
            messagebox.showerror("Error de Entrada", "Introduce un entero válido >= 2.")
            return

        valores_previos_x = [e.get() for e in self.entradas_x]
        valores_previos_y = [e.get() for e in self.entradas_y]

        for child in self.frame_tabla.winfo_children():
            child.destroy()

        self.entradas_x.clear()
        self.entradas_y.clear()

        tk.Label(self.frame_tabla, text="i", font=("Arial", 9, "bold"), width=4).grid(row=0, column=0, pady=2)
        tk.Label(self.frame_tabla, text="X", font=("Arial", 9, "bold"), width=4).grid(row=1, column=0, pady=2)
        tk.Label(self.frame_tabla, text="Y", font=("Arial", 9, "bold"), width=4).grid(row=2, column=0, pady=2)

        for col in range(n):
            tk.Label(self.frame_tabla, text=f"{col}", font=("Arial", 8, "italic")).grid(row=0, column=col + 1)

            ent_x = tk.Entry(self.frame_tabla, width=8, justify="center")
            ent_x.grid(row=1, column=col + 1, padx=3, pady=2)
            if col < len(valores_previos_x):
                ent_x.insert(0, valores_previos_x[col])
            self.entradas_x.append(ent_x)

            ent_y = tk.Entry(self.frame_tabla, width=8, justify="center")
            ent_y.grid(row=2, column=col + 1, padx=3, pady=2)
            if col < len(valores_previos_y):
                ent_y.insert(0, valores_previos_y[col])
            self.entradas_y.append(ent_y)

            ent_x.bind("<Up>", lambda e, c=col: self._mover_foco(1, c, "Up"))
            ent_x.bind("<Down>", lambda e, c=col: self._mover_foco(1, c, "Down"))
            ent_x.bind("<Left>", lambda e, c=col: self._mover_foco(1, c, "Left"))
            ent_x.bind("<Right>", lambda e, c=col: self._mover_foco(1, c, "Right"))

            ent_y.bind("<Up>", lambda e, c=col: self._mover_foco(2, c, "Up"))
            ent_y.bind("<Down>", lambda e, c=col: self._mover_foco(2, c, "Down"))
            ent_y.bind("<Left>", lambda e, c=col: self._mover_foco(2, c, "Left"))
            ent_y.bind("<Right>", lambda e, c=col: self._mover_foco(2, c, "Right"))

    def _limpiar_tabla(self):
        for ent_x in self.entradas_x:
            ent_x.delete(0, tk.END)
        for ent_y in self.entradas_y:
            ent_y.delete(0, tk.END)

    def _mover_foco(self, fila, col, direccion):
        n = len(self.entradas_x)

        if direccion == "Up" and fila == 2:
            self.entradas_x[col].focus_set()
        elif direccion == "Down" and fila == 1:
            self.entradas_y[col].focus_set()
        elif direccion == "Left" and col > 0:
            if fila == 1:
                self.entradas_x[col - 1].focus_set()
            else:
                self.entradas_y[col - 1].focus_set()
        elif direccion == "Right" and col < n - 1:
            if fila == 1:
                self.entradas_x[col + 1].focus_set()
            else:
                self.entradas_y[col + 1].focus_set()

    def _calcular(self):
        try:
            puntos_x = []
            puntos_y = []

            for i, (e_x, e_y) in enumerate(zip(self.entradas_x, self.entradas_y)):
                val_x = e_x.get().strip()
                val_y = e_y.get().strip()

                if not val_x or not val_y:
                    raise ValueError(f"El punto i={i} tiene campos vacíos.")

                puntos_x.append(float(val_x))
                puntos_y.append(float(val_y))

            coefs, matriz_aumentada = calcular_interpolacion(puntos_x, puntos_y)
            self.coeficientes_actuales = limpiar_coeficientes(coefs)

            self.txt_resultados.delete("1.0", tk.END)

            self.txt_resultados.insert(tk.END, "Matriz aumentada [A|B]:\n")
            for fila in matriz_aumentada:
                linea = "  [ " + "  ".join(f"{val:8.3f}" for val in fila[:-1]) + f" | {fila[-1]:8.3f} ]\n"
                self.txt_resultados.insert(tk.END, linea)

            self.txt_resultados.insert(tk.END, "\nCoeficientes:\n")
            for i, c in enumerate(self.coeficientes_actuales):
                self.txt_resultados.insert(tk.END, f"  a{i} = {c:.6f}\n")

            str_polinomio = formatear_polinomio(self.coeficientes_actuales)
            self.txt_resultados.insert(tk.END, f"\nPolinomio:\n  {str_polinomio}\n")

            self.lbl_resultado_eval.config(text="P(x) = ---")

        except ValueError as err:
            messagebox.showerror("Error de Entrada / Cálculo", str(err))

    def _evaluar_x(self):
        if self.coeficientes_actuales is None:
            messagebox.showwarning("Advertencia", "Primero debes calcular el polinomio.")
            return

        try:
            val_x = float(self.ent_eval_x.get().strip())
            resultado = evaluar_polinomio(self.coeficientes_actuales, val_x)
            self.lbl_resultado_eval.config(text=f"P({val_x}) = {resultado:.4f}")
        except ValueError:
            messagebox.showerror("Error", "Introduce un número válido para evaluar.")