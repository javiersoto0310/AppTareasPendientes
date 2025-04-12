from PySide6.QtWidgets import  QWidget, QListWidgetItem, QMessageBox
from vista.pantalla_tareas import AppTareasPendientes
from modelo.lista_de_tareas import ListaDeTareas

class VentanaPrincipal(QWidget, AppTareasPendientes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lista = ListaDeTareas()

        self.boton_agregar_tarea.clicked.connect(self.agregar_tarea)
        self.boton_tarea_completada.clicked.connect(self.alternar_completada)
        self.boton_eliminar_tarea.clicked.connect(self.eliminar_tarea_completada)

    def agregar_tarea(self):
        ingreso_de_tarea = self.input_tareas.text()
        if ingreso_de_tarea:
            self.lista.agregar_tarea(ingreso_de_tarea)
            item = QListWidgetItem(ingreso_de_tarea)
            item.setData(1, ingreso_de_tarea)
            self.lista_de_tareas.addItem(item)
            self.input_tareas.clear()

    def alternar_completada(self):
        item_de_tarea = self.lista_de_tareas.currentItem()
        if item_de_tarea:
            descripcion = item_de_tarea.data(1)
            tarea = self.lista.obtener_tarea(descripcion)
            if tarea:
                if tarea["marcada"]:
                    self.lista.desmarcar_como_completada(descripcion)
                    item_de_tarea.setText(descripcion)
                else:
                    self.lista.marcar_como_completada(descripcion)
                    item_de_tarea.setText(f"{descripcion} ✅")

    def eliminar_tarea_completada(self):
        item = self.lista_de_tareas.currentItem()
        if item:
            descripcion = item.data(1)
            tarea = self.lista.obtener_tarea(descripcion)
            if tarea and tarea["marcada"]:
                self.lista.eliminar_tarea(descripcion)
                self.lista_de_tareas.takeItem(self.lista_de_tareas.row(item))
            else:
                QMessageBox.warning(self, "Advertencia", "Solo se pueden eliminar tareas marcadas.")

