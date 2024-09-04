# tareasPendinetes.py
from PySide6.QtWidgets import QApplication, QWidget, QListWidgetItem, QMessageBox
from pantallaAppTareasPendientes import Ui_AppTareasPendientes

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

class MainWindow(QWidget, Ui_AppTareasPendientes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lista = ListaDeTareas()

        self.boton_agregar_tarea.clicked.connect(self.agregar_tarea)
        self.boton_tarea_completada.clicked.connect(self.marcar_como_completada)
        self.boton_eliminar_tarea.clicked.connect(self.eliminar_tarea_completada)

    def agregar_tarea(self):
        ingreso_de_tarea = self.input_tareas.text()
        if ingreso_de_tarea:
            self.lista.agregar_tarea(ingreso_de_tarea)
            item = QListWidgetItem(ingreso_de_tarea)
            item.setData(1, ingreso_de_tarea)
            self.lista_de_tareas.addItem(item)
            self.input_tareas.clear()

    def marcar_como_completada(self):
        item_de_tarea = self.lista_de_tareas.currentItem()
        if item_de_tarea:
            descripcion = item_de_tarea.data(1)
            self.lista.marcar_como_completada(descripcion)
            item_de_tarea.setText(f"{descripcion} (Completada)")

    def eliminar_tarea_completada(self):
        item = self.lista_de_tareas.currentItem()
        if item:
            descripcion = item.data(1)
            tarea = self.lista.obtener_tarea(descripcion)
            if tarea and tarea["completada"]:
                self.lista.eliminar_tarea(descripcion)
                self.lista_de_tareas.takeItem(self.lista_de_tareas.row(item))
            else:
                QMessageBox.warning(self, "Advertencia", "Solo se pueden eliminar tareas completadas.")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
