"""
API Flask para exponer la función de predicción simulada.

Esta versión corresponde a la solución inicial del Taller 2,
basada en el Taller 1.
"""

from flask import Flask, request, jsonify
from app.model import predecir_estado_paciente


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Ruta principal de prueba."""
    return jsonify({
        "mensaje": "API de predicción médica simulada funcionando correctamente.",
        "version": "v1.0"
    })


@app.route("/predecir", methods=["POST"])
def predecir():
    """Recibe datos del paciente y retorna una predicción simulada."""

    datos = request.get_json()

    if datos is None:
        return jsonify({
            "estado": "ERROR",
            "mensaje": "Debe enviar un cuerpo JSON válido."
        }), 400

    edad = datos.get("edad")
    presion = datos.get("presion")
    sintomas = datos.get("sintomas")

    resultado = predecir_estado_paciente(
        edad=edad,
        presion=presion,
        sintomas=sintomas
    )

    if resultado.get("estado") == "ERROR":
        return jsonify(resultado), 400

    return jsonify(resultado), 200


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
