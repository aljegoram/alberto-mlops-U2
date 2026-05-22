"""
Almacenamiento simple de predicciones en JSONL.

JSONL significa un objeto JSON por línea.
Para producción real se recomendaría una base de datos, bucket o sistema de logs.
"""

import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from app.model import CATEGORIAS

DEFAULT_PREDICTIONS_FILE = "data/predicciones.jsonl"


def obtener_ruta_predicciones():
    """Obtiene la ruta del archivo de predicciones."""
    return Path(os.getenv("PREDICTIONS_FILE", DEFAULT_PREDICTIONS_FILE))


def asegurar_directorio_predicciones():
    """Crea el directorio de predicciones si no existe."""
    ruta = obtener_ruta_predicciones()
    ruta.parent.mkdir(parents=True, exist_ok=True)
    return ruta


def registrar_prediccion(edad, presion, sintomas, resultado, version_modelo):
    """Registra una predicción en formato JSONL."""
    ruta = asegurar_directorio_predicciones()

    registro = {
        "fecha": datetime.now(timezone.utc).isoformat(),
        "edad": edad,
        "presion": presion,
        "sintomas": sintomas,
        "resultado": resultado,
        "version_modelo": version_modelo,
    }

    with ruta.open("a", encoding="utf-8") as archivo:
        archivo.write(json.dumps(registro, ensure_ascii=False) + "\n")

    return registro


def leer_predicciones():
    """Lee todas las predicciones registradas."""
    ruta = obtener_ruta_predicciones()

    if not ruta.exists():
        return []

    predicciones = []

    with ruta.open("r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if linea:
                predicciones.append(json.loads(linea))

    return predicciones


def obtener_estadisticas():
    """
    Calcula:
    - total de predicciones;
    - total por categoría;
    - últimas 5 predicciones;
    - fecha de última predicción.
    """

    predicciones = leer_predicciones()
    conteo = Counter(p["resultado"] for p in predicciones)

    total_por_categoria = {
        categoria: conteo.get(categoria, 0)
        for categoria in CATEGORIAS
    }

    ultimas_5 = predicciones[-5:]
    fecha_ultima = predicciones[-1]["fecha"] if predicciones else None

    return {
        "total_predicciones": len(predicciones),
        "total_por_categoria": total_por_categoria,
        "ultimas_5_predicciones": ultimas_5,
        "fecha_ultima_prediccion": fecha_ultima,
    }


def limpiar_predicciones():
    """Elimina el archivo de predicciones. Útil para pruebas."""
    ruta = obtener_ruta_predicciones()
    if ruta.exists():
        ruta.unlink()
