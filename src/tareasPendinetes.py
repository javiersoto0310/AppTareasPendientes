class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = {"descripcion": descripcion, "completada": False}
        self.tareas.append(tarea)

    def obtener_tarea(self, descripcion):
        for tarea in self.tareas:
            if tarea["descripcion"] == descripcion:
                return tarea

    def marcar_como_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea["descripcion"] == descripcion:
                tarea["completada"] = True

    def eliminar_tarea(self, descripcion):
        self.tareas = [tarea for tarea in self.tareas if tarea["descripcion"] != descripcion]
