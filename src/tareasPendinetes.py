class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea = {"descripcion": descripcion, "completada": False}
        self.tareas.append(tarea)