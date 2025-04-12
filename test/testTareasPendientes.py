from src.controlador.tareas import ListaDeTareas

def test_agregar_tarea():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    tareas = lista.obtener_tareas()
    assert len(tareas) == 1
    assert tareas[0]["descripcion"] == "Comprar leche"
    assert not tareas[0]["marcada"]

def test_marcar_tarea():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.marcar_como_completada("Comprar leche")
    tareas = lista.obtener_tareas()
    assert tareas[0]["marcada"] is True

def test_eliminar_tarea():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.agregar_tarea("Comprar pan")

    lista.marcar_como_completada("Comprar leche")

    lista.eliminar_tarea("Comprar leche")

    tareas = lista.obtener_tareas()

    assert len(tareas) == 1
    assert tareas[0]["descripcion"] == "Comprar pan"

def test_eliminar_tarea_no_marcada():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.eliminar_tarea("Comprar leche")
    tareas = lista.obtener_tareas()
    assert len(tareas) == 1

def test_eliminar_tarea_marcada():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.marcar_como_completada("Comprar leche")
    lista.eliminar_tarea("Comprar leche")
    tareas = lista.obtener_tareas()
    assert len(tareas) == 0

def test_agregar_multiples_tareas():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.agregar_tarea("Comprar pan")
    tareas = lista.obtener_tareas()
    assert len(tareas) == 2
    assert tareas[0]["descripcion"] == "Comprar leche"
    assert tareas[1]["descripcion"] == "Comprar pan"

def test_desmarcar_tarea():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.marcar_como_completada("Comprar leche")
    lista.desmarcar_como_completada("Comprar leche")
    tareas = lista.obtener_tareas()
    assert not tareas[0]["marcada"]

def test_eliminar_tarea_inexistente():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    lista.eliminar_tarea("Tarea que no existe")
    tareas = lista.obtener_tareas()
    assert len(tareas) == 1
    assert tareas[0]["descripcion"] == "Comprar leche"

def test_obtener_tarea_inexistente():
    lista = ListaDeTareas()
    tarea = lista.obtener_tarea("Comprar pan")
    assert tarea is None

def test_estado_inicial():
    lista = ListaDeTareas()
    tareas = lista.obtener_tareas()
    assert len(tareas) == 0





