from PySide6.QtWidgets import QApplication
from controlador.tareas import VentanaPrincipal

if __name__ == "__main__":
    app = QApplication([])

    ventana = VentanaPrincipal()
    ventana.show()

    app.exec()

