class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = {"descripcion": descripcion, "completada": False}
        self.tareas.append(tarea)

    def marcar_como_completada(self, descripcion):
        for tarea in self.tareas:
            if tarea["descripcion"] == descripcion:
                tarea["completada"] = True