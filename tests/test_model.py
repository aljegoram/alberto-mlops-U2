from app.model import CATEGORIAS, predecir_estado_paciente


def test_modelo_retorna_enfermedad_terminal():
    resultado = predecir_estado_paciente(edad=85, presion=190, sintomas=10)
    assert resultado["estado"] == "OK"
    assert resultado["resultado"] == "ENFERMEDAD TERMINAL"


def test_modelo_retorna_todas_las_categorias():
    casos = [
        (25, 120, 0, "NO ENFERMO"),
        (30, 125, 3, "ENFERMEDAD LEVE"),
        (45, 145, 6, "ENFERMEDAD AGUDA"),
        (70, 160, 9, "ENFERMEDAD CRÓNICA"),
        (85, 190, 10, "ENFERMEDAD TERMINAL"),
    ]

    resultados = set()

    for edad, presion, sintomas, esperado in casos:
        prediccion = predecir_estado_paciente(edad, presion, sintomas)
        assert prediccion["resultado"] == esperado
        resultados.add(prediccion["resultado"])

    assert resultados == set(CATEGORIAS)


def test_modelo_valida_campos_faltantes():
    resultado = predecir_estado_paciente(edad=70, presion=160, sintomas=None)
    assert resultado["estado"] == "ERROR"
    assert "sintomas" in resultado["mensaje"]
