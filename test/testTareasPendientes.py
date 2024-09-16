from src.tareasPendinetes import ListaDeTareas

def test_agregar_tarea():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    tareas = lista.obtener_tareas()
    assert len(tareas) == 1
    assert tareas[0]["descripcion"] == "Comprar leche"
    assert not tareas[0]["completada"]

def test_marcar_como_completada():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.marcar_como_completada("Comprar leche")
    tareas = lista.obtener_tareas()
    assert tareas[0]["completada"] is True


def test_eliminar_tarea():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.agregar_tarea("Comprar pan")

    lista.marcar_como_completada("Comprar leche")

    lista.eliminar_tarea("Comprar leche")

    tareas = lista.obtener_tareas()

    assert len(tareas) == 1
    assert tareas[0]["descripcion"] == "Comprar pan"

def test_eliminar_tarea_no_completada():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.eliminar_tarea("Comprar leche")
    tareas = lista.obtener_tareas()
    assert len(tareas) == 1

def test_eliminar_tarea_completada():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.marcar_como_completada("Comprar leche")
    lista.eliminar_tarea("Comprar leche")
    tareas = lista.obtener_tareas()
    assert len(tareas) == 0


