from src.tareasPendinetes import ListaDeTareas

def test_agregar_tarea():
    lista = ListaDeTareas()
    lista.agregar_tarea("Comprar leche")
    assert len(lista.tareas) == 1
    assert lista.tareas[0]["descripcion"] == "Comprar leche"
    assert not lista.tareas[0]["completada"]