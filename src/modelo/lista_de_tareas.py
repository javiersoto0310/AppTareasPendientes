class ListaDeTareas:
    def __init__(self):
        self._tareas = []

    def agregar_tarea(self, descripcion):
        tarea = {"descripcion": descripcion, "marcada": False}
        self._tareas.append(tarea)

    def obtener_tarea(self, descripcion):
        for tarea in self._tareas:
            if tarea["descripcion"] == descripcion:
                return tarea

    def marcar_como_completada(self, descripcion):
        tarea = self.obtener_tarea(descripcion)
        if tarea:
            tarea["marcada"] = True

    def desmarcar_como_completada(self, descripcion):
        tarea = self.obtener_tarea(descripcion)
        if tarea:
            tarea["marcada"] = False

    def eliminar_tarea(self, descripcion):
        self._tareas = [tarea for tarea in self._tareas if tarea["descripcion"] != descripcion or not tarea["marcada"]]

    def obtener_tareas(self):
        return self._tareas
