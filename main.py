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
        self._puntajes = {}

    def set_categoria(self, nueva_categoria):
        self._categoria = nueva_categoria

    def registrar_puntajes(self, rango):
        pass

    def mostrar_info(self):
        pass

class Concurso:
    def inscribir_banda(self, banda):
        pass

    def registrar_evaluacion(self, nombre_banda, puntajes):
        pass

    def listar_bandas(self):
        pass

    def ranking(self):
        pass






def inscribir_banda():
    print("Se abrió la ventana: Inscribir Banda")
    ventana_inscribir = tk.Toplevel(ventana)
    ventana_inscribir.title("Inscribir Banda")
    ventana_inscribir.geometry("400x300")

    nombre_banda = tk.Label(ventana_inscribir, text="Ingresar el nombre de la banda: ")
    nombre_banda.pack(pady=3)
    ent_nombre = tk.Entry(ventana_inscribir)
    ent_nombre.pack(pady=3)

    categoria_banda = tk.Label(ventana_inscribir, text="Ingresar la categoría de la banda: ")
    categoria_banda.pack(pady=3)
    ent_cat = tk.Entry(ventana_inscribir)
    ent_cat.pack(pady=3)

    registrar = tk.Label(ventana, text="Registro ")
    registrar.pack(pady=10)

    nombre_b = str(ent_nombre.get())
    cat = str(ent_cat.get())
    registrar.config(text=f"Se registró la banda: {nombre_b}\n" f"Categoría: {cat}")

    boton_inscribir = tk.Button(ventana_inscribir, text="Registrar", command=inscribir_banda)
    boton_inscribir.pack(pady=5)

def registrar_evaluacion():
    print("Registrar Evaluación")
    ventana_eval = tk.Toplevel(ventana)
    ventana_eval.title("Registrar Evaluación")
    ventana_eval.geometry("400x300")

    puntaje = tk.Label(ventana_eval, text="Ingresar puntaje:")
    puntaje.pack(pady=3)
    ent = tk.Entry(ventana_eval)
    ent.pack(pady=3)

def listar_bandas():
    print("Se abrió la ventana: Listado de Bandas")
    ventana_listado = tk.Toplevel(ventana)
    ventana_listado.title("Listado de Bandas")
    ventana_listado.geometry("400x300")

def ver_ranking():
    print("Se abrió la ventana: Ranking Final")
    ventana_ranking = tk.Toplevel(ventana)
    ventana_ranking.title("Ranking Final")
    ventana_ranking.geometry("400x300")

def salir():
    print("Aplicación cerrada")
    ventana.quit()



ventana = tk.Tk()
ventana.title("Concurso de Bandas - Quetzaltenango")
ventana.geometry("500x300")

barra_menu = tk.Menu(ventana)

menu_opciones = tk.Menu(barra_menu, tearoff=0)
menu_opciones.add_command(label="Inscribir Banda", command=inscribir_banda)
menu_opciones.add_command(label="Registrar Evaluación", command=registrar_evaluacion)
menu_opciones.add_command(label="Listar Bandas", command=listar_bandas)
menu_opciones.add_command(label="Ver Ranking", command=ver_ranking)
menu_opciones.add_separator()
menu_opciones.add_command(label="Salir", command=salir)

barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

ventana.config(menu=barra_menu)

etiqueta = tk.Label(
    ventana,
    text="Sistema de Inscripción y Evaluación de Bandas Escolares\nDesfile 15 de Septiembre - Quetzaltenango",
    font=("Arial", 12, "bold"),
    justify="center"
)
etiqueta.pack(pady=50)

ventana.mainloop()
