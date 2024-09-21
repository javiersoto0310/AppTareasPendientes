from PySide6.QtWidgets import QApplication, QWidget, QListWidgetItem, QMessageBox
from ui.pantalla import Ui_AppTareasPendientes

class Tarea:
    def __init__(self, id: int, descripcion):
        self.__id = id
        self.__descripcion = descripcion
        self.__completada = False

    def marcar_como_completada(self):
        self.__completada = True

    def obtener_id(self):
        return self.__id

    def obtener_descripcion(self):
        return self.__descripcion

    def esta_completada(self):
        return self.__completada


class ListaDeTareas:
    def __init__(self):
        self.__tareas = []
        self.__contador_id = 0

    def agregar_tarea(self, descripcion):
        if not descripcion:
            raise ValueError("Debe ingresar una tarea.")
        self.__contador_id += 1
        tarea = Tarea(self.__contador_id, descripcion)
        self.__tareas.append(tarea)

    def obtener_tarea_por_id(self, id: int):
        return next((tarea for tarea in self.__tareas if tarea.obtener_id() == id), None)

    def marcar_como_completada(self, id: int):
        tarea = self.obtener_tarea_por_id(id)
        if tarea:
            tarea.marcar_como_completada()

    def eliminar_tarea(self, id: int):
        self.__tareas = [tarea for tarea in self.__tareas if tarea.obtener_id() != id or not tarea.esta_completada()]

    def obtener_tareas(self):
        return self.__tareas


class VentanaPrincipal(QWidget, Ui_AppTareasPendientes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__lista = ListaDeTareas()

        self.boton_agregar_tarea.clicked.connect(self.__agregar_tarea)
        self.boton_tarea_completada.clicked.connect(self.__marcar_como_completada)
        self.boton_eliminar_tarea.clicked.connect(self.__eliminar_tarea_completada)

    def __agregar_tarea(self):
        descripcion = self.input_tareas.text().strip().capitalize()
        if descripcion:
            self.__lista.agregar_tarea(descripcion)
            tarea = self.__lista.obtener_tareas()[-1]

            item_text = f"N°: {tarea.obtener_id()} - {tarea.obtener_descripcion()}"

            item = QListWidgetItem(item_text)
            item.setData(1, tarea.obtener_id())
            self.lista_de_tareas.addItem(item)
            self.input_tareas.clear()
        else:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una tarea.")

    def __marcar_como_completada(self):
        item_de_tarea = self.lista_de_tareas.currentItem()
        if item_de_tarea:
            tarea_id = item_de_tarea.data(1)
            self.__lista.marcar_como_completada(tarea_id)
            item_de_tarea.setText(f"{item_de_tarea.text()} (Completada)")
        else:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar una tarea.")

    def __eliminar_tarea_completada(self):
        item = self.lista_de_tareas.currentItem()
        if item:
            tarea_id = item.data(1)
            tarea = self.__lista.obtener_tarea_por_id(tarea_id)
            if tarea and tarea.esta_completada():
                self.__lista.eliminar_tarea(tarea_id)
                self.lista_de_tareas.takeItem(self.lista_de_tareas.row(item))
            else:
                QMessageBox.warning(self, "Advertencia", "Solo se pueden eliminar tareas completadas.")
        else:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar una tarea para eliminar.")


if __name__ == "__main__":
    app = QApplication([])
    window = VentanaPrincipal()
    window.show()
    app.exec()



