import tkinter as tk

class Participante:
    def __init__(self, nombre, institucion):
        self.nombre = nombre
        self.institucion = institucion

    def mostrar_info(self):
        pass

class BandaEscolar(Participante):
    def __init__(self, nombre, institucion, categoria):
        super().__init__(nombre, institucion)
        self._categoria = categoria
        self._puntajes = {'ritmo': 0, 'uniformidad': 0, 'coreografia': 0, 'alineacion': 0, 'puntualidad': 0}

    def set_categoria(self, nueva_categoria):
        self._categoria = nueva_categoria

    def registrar_puntajes(self, criterio, puntaje):
        if criterio in self._puntajes:
            return 'Criterio ya registrado. No se ha podido guardar.'
        else:
            self._puntajes[criterio] = puntaje

    def mostrar_info(self):
        pass

class Concurso:
    def __init__(self):
        self.bandas = {}

    def inscribir_banda(self, nombre, banda):
        if nombre in self.bandas:
            return 'Banda ya existente. No se ha podido guardar'
        else:
            self.bandas[nombre] = banda

    def registrar_evaluacion(self, nombre_banda, puntajes):
        pass

    def listar_bandas(self):
        if self.bandas:
            for banda in self.bandas.values():
                banda.mostrar_info()



    def ranking(self):
        pass



class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("500x300")

        self.menu()

        tk.Label(
            self.ventana,
            text="Sistema de Inscripción y Evaluación de Bandas Escolares\nConcurso 14 de Septiembre - Quetzaltenango",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        self.ventana.mainloop()

    def menu(self):
        barra = tk.Menu(self.ventana)
        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Inscribir Banda", command=self.inscribir_banda)
        opciones.add_command(label="Registrar Evaluación", command=self.registrar_evaluacion)
        opciones.add_command(label="Listar Bandas", command=self.listar_bandas)
        opciones.add_command(label="Ver Ranking", command=self.ver_ranking)
        opciones.add_separator()
        opciones.add_command(label="Salir", command=self.ventana.quit)
        barra.add_cascade(label="Opciones", menu=opciones)
        self.ventana.config(menu=barra)

    def inscribir_banda(self):
        print("Se abrió la ventana: Inscribir Banda")
        ventana_inscribir = tk.Toplevel(self.ventana)
        ventana_inscribir.title("Inscribir Banda")
        ventana_inscribir.geometry("400x300")

        tk.Label(ventana_inscribir, text="Ingresar el nombre de la banda:").pack(pady=3)
        ent_nombre = tk.Entry(ventana_inscribir)
        ent_nombre.pack(pady=3)

        tk.Label(ventana_inscribir, text="Ingresar la categoría de la banda:").pack(pady=3)
        ent_cat = tk.Entry(ventana_inscribir)
        ent_cat.pack(pady=3)

        registrar = tk.Label(ventana_inscribir, text="")
        registrar.pack(pady=10)

        def registrar_banda():
            nombre_b = ent_nombre.get()
            cat = ent_cat.get()
            registrar.config(text=f"Se registró la banda:\n{nombre_b}\nCategoría:\n {cat}")

        tk.Button(ventana_inscribir, text="Registrar", command=registrar_banda).pack(pady=5)

    def registrar_evaluacion(self):
        print("Se abrió la ventana: Registrar Evaluación")
        ventana_eval = tk.Toplevel(self.ventana)
        ventana_eval.title("Registrar Evaluación")
        ventana_eval.geometry("400x300")

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        ventana_listado = tk.Toplevel(self.ventana)
        ventana_listado.title("Listado de Bandas")
        ventana_listado.geometry("400x300")

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        ventana_ranking = tk.Toplevel(self.ventana)
        ventana_ranking.title("Ranking Final")
        ventana_ranking.geometry("400x300")


if __name__ == "__main__":
    ConcursoBandasApp()
