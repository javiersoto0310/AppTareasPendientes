# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantallaAppTareasPendientes.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QGridLayout, QLabel,
                               QLineEdit, QListWidget, QPushButton)

class Ui_AppTareasPendientes(object):
    def setupUi(self, AppTareasPendientes):
        if not AppTareasPendientes.objectName():
            AppTareasPendientes.setObjectName(u"AppTareasPendientes")
        AppTareasPendientes.resize(341, 303)
        self.gridLayout = QGridLayout(AppTareasPendientes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(AppTareasPendientes)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.input_tareas = QLineEdit(AppTareasPendientes)
        self.input_tareas.setObjectName(u"input_tareas")

        self.gridLayout.addWidget(self.input_tareas, 0, 1, 1, 2)

        self.boton_agregar_tarea = QPushButton(AppTareasPendientes)
        self.boton_agregar_tarea.setObjectName(u"boton_agregar_tarea")

        self.gridLayout.addWidget(self.boton_agregar_tarea, 1, 1, 1, 2)

        self.lista_de_tareas = QListWidget(AppTareasPendientes)
        self.lista_de_tareas.setObjectName(u"lista_de_tareas")

        self.gridLayout.addWidget(self.lista_de_tareas, 2, 0, 1, 3)

        self.boton_tarea_completada = QPushButton(AppTareasPendientes)
        self.boton_tarea_completada.setObjectName(u"boton_tarea_completada")

        self.gridLayout.addWidget(self.boton_tarea_completada, 3, 0, 1, 2)

        self.boton_eliminar_tarea = QPushButton(AppTareasPendientes)
        self.boton_eliminar_tarea.setObjectName(u"boton_eliminar_tarea")

        self.gridLayout.addWidget(self.boton_eliminar_tarea, 3, 2, 1, 1)


        self.retranslateUi(AppTareasPendientes)

        QMetaObject.connectSlotsByName(AppTareasPendientes)
    # setupUi

    def retranslateUi(self, AppTareasPendientes):
        AppTareasPendientes.setWindowTitle(QCoreApplication.translate("AppTareasPendientes", u"App Todo", None))
        self.label.setText(QCoreApplication.translate("AppTareasPendientes", u"Ingrese tarea ", None))
        self.boton_agregar_tarea.setText(QCoreApplication.translate("AppTareasPendientes", u"Agregar tarea", None))
        self.boton_tarea_completada.setText(QCoreApplication.translate("AppTareasPendientes", u"Tarea completada", None))
        self.boton_eliminar_tarea.setText(QCoreApplication.translate("AppTareasPendientes", u"Eliminar tarea completada", None))
    # retranslateUi

