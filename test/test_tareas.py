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

    assert tareas[0].obtener_descripcion() == descripcion1
    assert not tareas[0].esta_completada()
    assert tareas[0].obtener_id() == 1

    assert tareas[1].obtener_descripcion() == descripcion2
    assert not tareas[1].esta_completada()
    assert tareas[1].obtener_id() == 2

    assert tareas[2].obtener_descripcion() == descripcion3
    assert not tareas[2].esta_completada()
    assert tareas[2].obtener_id() == 3


def test_obtener_tarea_por_id():
    lista_de_tareas = ListaDeTareas()
    lista_de_tareas.agregar_tarea("Comprar leche")
    tarea = lista_de_tareas.obtener_tareas()[0]
    tarea_obtenida = lista_de_tareas.obtener_tarea_por_id(tarea.obtener_id())
    assert tarea_obtenida is not None
    assert tarea_obtenida.obtener_descripcion() == "Comprar leche"


def test_marcar_como_completada():
    lista_de_tareas = ListaDeTareas()
    lista_de_tareas.agregar_tarea("Comprar leche")
    tarea = lista_de_tareas.obtener_tareas()[0]
    lista_de_tareas.marcar_como_completada(tarea.obtener_id())
    assert tarea.esta_completada()


def test_eliminar_tarea_completada():
    lista_de_tareas = ListaDeTareas()
    lista_de_tareas.agregar_tarea("Comprar leche")
    tarea = lista_de_tareas.obtener_tareas()[0]
    lista_de_tareas.marcar_como_completada(tarea.obtener_id())
    lista_de_tareas.eliminar_tarea(tarea.obtener_id())
    assert len(lista_de_tareas.obtener_tareas()) == 0


def test_no_eliminar_tarea_no_completada():
    lista_de_tareas = ListaDeTareas()
    lista_de_tareas.agregar_tarea("Comprar leche")
    tarea = lista_de_tareas.obtener_tareas()[0]
    lista_de_tareas.eliminar_tarea(tarea.obtener_id())
    assert len(lista_de_tareas.obtener_tareas()) == 1


def test_error_agregar_tarea_vacia():
    lista_de_tareas = ListaDeTareas()
    try:
        lista_de_tareas.agregar_tarea("")
    except ValueError as error:
        assert str(error) == "Debe ingresar una tarea."


def test_agregar_tareas_con_mismo_nombre():
    lista_de_tareas = ListaDeTareas()

    lista_de_tareas.agregar_tarea("Comprar leche")
    lista_de_tareas.agregar_tarea("Comprar leche")

    tareas = lista_de_tareas.obtener_tareas()

    assert len(tareas) == 2
    assert tareas[0].obtener_descripcion() == "Comprar leche"
    assert tareas[1].obtener_descripcion() == "Comprar leche"
    assert tareas[0].obtener_id() != tareas[1].obtener_id()

