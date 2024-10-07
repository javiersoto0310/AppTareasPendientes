from PySide6.QtWidgets import QApplication, QWidget, QListWidgetItem, QMessageBox
from ui.pantalla import Ui_AppTareasPendientes


class Tarea:
    def __init__(self, descripcion):
        self.__descripcion = descripcion
        self.__completada = False

    def completada(self):
        self.__completada = True

    def descripcion(self):
        return self.__descripcion

    def esta_completada(self):
        return self.__completada


class ListaDeTareas:
    def __init__(self):
        self.__tareas = []

    def agregar_tarea(self, descripcion):
        tarea = Tarea(descripcion)
        self.__tareas.append(tarea)

    def obtener_tarea(self, descripcion):
        return next((tarea for tarea in self.__tareas if tarea.descripcion() == descripcion))

    def completada(self, descripcion):
        tarea = self.obtener_tarea(descripcion)
        if tarea:
            tarea.completada()

    def eliminar_tareas_completadas(self):
        self.__tareas = [tarea for tarea in self.__tareas if not tarea.esta_completada()]

    def obtener_tareas(self):
        return self.__tareas


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_AppTareasPendientes()
        self.ui.setupUi(self)

        self.__lista = ListaDeTareas()

        self.ui.boton_agregar_tarea.clicked.connect(self.__agregar_tarea)
        self.ui.boton_tarea_completada.clicked.connect(self.__completar_tarea)
        self.ui.boton_eliminar_tarea.clicked.connect(self.__eliminar_tareas_completadas)

    def __agregar_tarea(self):
        descripcion = self.ui.input_tareas.text().strip().capitalize()
        if descripcion:
            self.__lista.agregar_tarea(descripcion)
            tarea = self.__lista.obtener_tareas()[-1]

            item_text = f"Tarea: {tarea.descripcion()}"
            item = QListWidgetItem(item_text)
            item.setData(1, tarea.descripcion())
            self.ui.lista_de_tareas.addItem(item)
            self.ui.input_tareas.clear()
        else:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una tarea.")

    def __completar_tarea(self):
        item_de_tarea = self.ui.lista_de_tareas.currentItem()
        if item_de_tarea:
            descripcion = item_de_tarea.data(1)
            self.__lista.completada(descripcion)
            item_de_tarea.setText(f"{item_de_tarea.text()} (Completada)")
        else:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar una tarea.")

    def __eliminar_tareas_completadas(self):
        tareas_completadas = [self.ui.lista_de_tareas.item(i) for i in range(self.ui.lista_de_tareas.count())
                              if "Completada" in self.ui.lista_de_tareas.item(i).text()]

        if tareas_completadas:
            self.__lista.eliminar_tareas_completadas()
            for tarea in tareas_completadas:
                self.ui.lista_de_tareas.takeItem(self.ui.lista_de_tareas.row(tarea))
        else:
            QMessageBox.warning(self, "Advertencia", "No hay tareas completadas para eliminar.")


if __name__ == "__main__":
    app = QApplication([])
    window = VentanaPrincipal()
    window.show()
    app.exec()












