from src.tareasPendinetes import ListaDeTareas

def test_agregar_tarea():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    assert len(lista.tareas) == 1
    assert lista.tareas[0]["descripcion"] == "Comprar leche"
    assert not lista.tareas[0]["completada"]

def test_marcar_como_completada():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.marcar_como_completada("Comprar leche")
    assert lista.tareas[0]["completada"] is True

def test_eliminar_tarea():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.agregar_tarea("Comprar pan")
    lista.eliminar_tarea("Comprar leche")
    assert len(lista.tareas) == 1
    assert lista.tareas[0]["descripcion"] == "Comprar pan"