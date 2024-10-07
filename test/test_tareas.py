from tareas import ListaDeTareas


def test_agregar_tarea():
    lista_de_tareas = ListaDeTareas()

    descripcion1 = "Comprar leche"
    descripcion2 = "Hacer ejercicio"
    descripcion3 = "Leer un libro"

    lista_de_tareas.agregar_tarea(descripcion1)
    lista_de_tareas.agregar_tarea(descripcion2)
    lista_de_tareas.agregar_tarea(descripcion3)

    tareas = lista_de_tareas.obtener_tareas()

    assert len(tareas) == 3

    assert tareas[0].descripcion() == descripcion1
    assert not tareas[0].esta_completada()

    assert tareas[1].descripcion() == descripcion2
    assert not tareas[1].esta_completada()

    assert tareas[2].descripcion() == descripcion3
    assert not tareas[2].esta_completada()


def test_obtener_tarea():
    lista_de_tareas = ListaDeTareas()
    lista_de_tareas.agregar_tarea("Comprar leche")
    tarea = lista_de_tareas.obtener_tareas()[0]
    tarea_obtenida = lista_de_tareas.obtener_tarea(tarea.descripcion())
    assert tarea_obtenida is not None
    assert tarea_obtenida.descripcion() == "Comprar leche"


def test_marcar_tarea_como_completada():
    lista_de_tareas = ListaDeTareas()
    lista_de_tareas.agregar_tarea("Comprar leche")
    tarea = lista_de_tareas.obtener_tareas()[0]
    lista_de_tareas.completada(tarea.descripcion())
    assert tarea.esta_completada()


def test_eliminar_todas_las_tareas_completadas():
    lista_de_tareas = ListaDeTareas()
    lista_de_tareas.agregar_tarea("Comprar leche")
    lista_de_tareas.agregar_tarea("Hacer ejercicio")
    lista_de_tareas.agregar_tarea("Leer un libro")

    lista_de_tareas.completada("Comprar leche")
    lista_de_tareas.completada("Hacer ejercicio")

    lista_de_tareas.eliminar_tareas_completadas()
    tareas = lista_de_tareas.obtener_tareas()

    assert len(tareas) == 1
    assert tareas[0].descripcion() == "Leer un libro"


def test_no_eliminar_tareas_si_no_hay_completadas():
    lista_de_tareas = ListaDeTareas()
    lista_de_tareas.agregar_tarea("Comprar leche")
    lista_de_tareas.agregar_tarea("Hacer ejercicio")

    lista_de_tareas.eliminar_tareas_completadas()
    tareas = lista_de_tareas.obtener_tareas()

    assert len(tareas) == 2
    assert tareas[0].descripcion() == "Comprar leche"
    assert tareas[1].descripcion() == "Hacer ejercicio"




