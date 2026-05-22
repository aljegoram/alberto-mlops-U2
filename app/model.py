"""
Módulo de predicción simulada para el Taller 2 de MLOps.

Esta versión agrega la nueva categoría solicitada:
- ENFERMEDAD TERMINAL

IMPORTANTE:
Esta función no representa una regla médica real.
Es una simulación académica para practicar MLOps, GitHub, CI/CD y Docker.
"""


CATEGORIAS = [
    "NO ENFERMO",
    "ENFERMEDAD LEVE",
    "ENFERMEDAD AGUDA",
    "ENFERMEDAD CRÓNICA",
    "ENFERMEDAD TERMINAL",
]


def validar_entradas(edad, presion, sintomas):
    """Valida que los datos de entrada sean correctos."""

    if edad is None:
        return "El campo 'edad' es obligatorio."

    if presion is None:
        return "El campo 'presion' es obligatorio."

    if sintomas is None:
        return "El campo 'sintomas' es obligatorio."

    if not isinstance(edad, (int, float)):
        return "El campo 'edad' debe ser numérico."

    if not isinstance(presion, (int, float)):
        return "El campo 'presion' debe ser numérico."

    if not isinstance(sintomas, (int, float)):
        return "El campo 'sintomas' debe ser numérico."

    if edad < 0 or edad > 120:
        return "El campo 'edad' debe estar entre 0 y 120."

    if presion < 50 or presion > 250:
        return "El campo 'presion' debe estar entre 50 y 250."

    if sintomas < 0 or sintomas > 10:
        return "El campo 'sintomas' debe estar entre 0 y 10."

    return None


def predecir_estado_paciente(edad, presion, sintomas):
    """Simula una predicción del estado de salud de un paciente."""

    error = validar_entradas(edad, presion, sintomas)

    if error is not None:
        return {
            "estado": "ERROR",
            "mensaje": error
        }

    if edad >= 80 and sintomas >= 9 and presion >= 180:
        resultado = "ENFERMEDAD TERMINAL"

    elif edad >= 60 and sintomas >= 8 and presion >= 150:
        resultado = "ENFERMEDAD CRÓNICA"

    elif sintomas <= 1 and presion < 130:
        resultado = "NO ENFERMO"

    elif sintomas <= 4 and presion < 140:
        resultado = "ENFERMEDAD LEVE"

    else:
        resultado = "ENFERMEDAD AGUDA"

    return {
        "estado": "OK",
        "resultado": resultado,
        "entradas": {
            "edad": edad,
            "presion": presion,
            "sintomas": sintomas
        },
        "version_modelo": "v2.0-simulada"
    }
