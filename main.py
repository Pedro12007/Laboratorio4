import tkinter as tk
from abc import ABC, abstractmethod

class Participante(ABC):
    def __init__(self, nombre, institucion):
        self.nombre = nombre
        self.institucion = institucion

    @abstractmethod
    def mostrar_info(self):
        pass

class BandaEscolar(Participante):
    def __init__(self, nombre, institucion, categoria):
        super().__init__(nombre, institucion)
        self._categoria = categoria
        self._puntajes = {'Ritmo': 0, 'Uniformidad': 0, 'Coreografía': 0, 'Alineación': 0, 'Puntualidad': 0}

    def set_categoria(self, nueva_categoria):
        self._categoria = nueva_categoria

    def registrar_puntajes(self, criterio, puntaje):
        if criterio in self._puntajes:
            return 'Criterio ya registrado. No se ha podido guardar.'
        else:
            self._puntajes[criterio] = puntaje

    def mostrar_info(self):
        return f'|Nombre: {self.nombre}| Institución: {self.institucion}| Categoria: {self._categoria}|\n     |Puntaje total: {self.total}| Promedio: {round(self.promedio, 2)}|'

    @property
    def total(self):
        return sum(self._puntajes.values())

    @property
    def promedio(self):
        return self.total / 5

class Concurso:
    def __init__(self):
        self.bandas = {'Liceo': BandaEscolar('Liceo Guatemala', 'Liceo Guatemala', 'Básico'), 'Patria': BandaEscolar('Colors', 'La Patria', 'Básico')}

    def inscribir_banda(self, nombre, banda):
        if nombre in self.bandas:
            print('Banda ya existente. No se ha podido guardar')
        else:
            self.bandas[nombre] = banda

    def registrar_evaluacion(self, nombre_banda, puntajes):
        if nombre_banda in self.bandas:
            banda = self.bandas[nombre_banda]
            for criterio, valor in puntajes.items():
                banda.registrar_puntajes(criterio, valor)
            return f"Evaluación registrada para {nombre_banda}."
        else:
            return "Banda no encontrada."

    def listar_bandas(self):
        if self.bandas:
            listado = ''
            for i, banda in enumerate(self.bandas.values(), 1):
                listado += f'{i}. {banda.mostrar_info()}\n'
            return listado
        else:
            return 'No hay bandas registradas.'

    def ranking(self):
        pass

concurso = Concurso()

class ConcursoBandasApp:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Concurso de Bandas - Quetzaltenango")
        self.ventana.geometry("700x500")

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
        ventana_inscribir.geometry("700x500")

        tk.Label(ventana_inscribir, text="Ingresar el nombre de la banda:").pack(pady=3)
        ent_nombre = tk.Entry(ventana_inscribir)
        ent_nombre.pack(pady=3)

        tk.Label(ventana_inscribir, text="Ingresar el nombre de la institución:").pack(pady=3)
        ent_inst = tk.Entry(ventana_inscribir)
        ent_inst.pack(pady=3)

        tk.Label(ventana_inscribir, text="Ingresar la categoría de la banda:").pack(pady=3)

        categorias_validas = ["Primaria", "Básico", "Diversificado"]

        categoria_seleccionada = tk.StringVar(ventana_inscribir)
        categoria_seleccionada.set("Seleccione una categoría")  # Valor por defecto

        menu_cat = tk.OptionMenu(ventana_inscribir, categoria_seleccionada, *categorias_validas)
        menu_cat.pack(pady=3)

        registrar = tk.Label(ventana_inscribir, text="")
        registrar.pack(pady=10)

        def registrar_banda():
            nombre_b = ent_nombre.get()
            nombre_i = ent_inst.get()
            cat = categoria_seleccionada.get()
            if len(nombre_b.replace(' ', '')) and len(nombre_i.replace(' ', '')) and cat != "Seleccione una categoría":
                if nombre_b not in concurso.bandas.keys():
                    concurso.inscribir_banda(nombre_b, BandaEscolar(nombre_b, nombre_i, cat))
                    registrar.config(text=f"Se registró la banda:\n{nombre_b}\nInstitución:\n{nombre_i}\nCategoría:\n {cat}")
                else:
                    registrar.config(text='Banda ya registrada. Ingrese otro nombre.')
            else:
                registrar.config(text='Campos sin llenar. Verifique sus datos.')

        tk.Button(ventana_inscribir, text="Registrar", command=registrar_banda).pack(pady=5)

    def registrar_evaluacion(self):
        print("Registrar Evaluación")
        ventana_eval = tk.Toplevel(self.ventana)
        ventana_eval.title("Registrar Evaluación")
        ventana_eval.geometry("700x500")

    def listar_bandas(self):
        print("Se abrió la ventana: Listado de Bandas")
        ventana_listado = tk.Toplevel(self.ventana)
        ventana_listado.title("Listado de Bandas")
        ventana_listado.geometry("700x500")

        tk.Label(
            ventana_listado,
            text="Listado de bandas\n",
            font=("Arial", 12, "bold"),
            justify="center"
        ).pack(pady=50)

        tk.Label(ventana_listado, text=concurso.listar_bandas(), justify='left').pack(pady=5)

    def ver_ranking(self):
        print("Se abrió la ventana: Ranking Final")
        ventana_ranking = tk.Toplevel(self.ventana)
        ventana_ranking.title("Ranking Final")
        ventana_ranking.geometry("700x500")


if __name__ == "__main__":
    ConcursoBandasApp()
