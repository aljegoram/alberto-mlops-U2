"""
API Flask del Taller 2.

Incluye:
- Endpoint de predicción.
- Registro de predicciones.
- Endpoint de estadísticas.
"""

from flask import Flask, request, jsonify

from app.model import predecir_estado_paciente
from app.storage import obtener_estadisticas, registrar_prediccion

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Ruta principal de verificación."""
    return jsonify({
        "mensaje": "API de predicción médica simulada funcionando correctamente.",
        "version": "v2.0"
    })


@app.route("/predecir", methods=["POST"])
def predecir():
    """Recibe datos del paciente, predice y registra el resultado."""

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

    registro = registrar_prediccion(
        edad=edad,
        presion=presion,
        sintomas=sintomas,
        resultado=resultado["resultado"],
        version_modelo=resultado["version_modelo"],
    )

    resultado["registro"] = registro

    return jsonify(resultado), 200


@app.route("/estadisticas", methods=["GET"])
def estadisticas():
    """Retorna estadísticas de las predicciones realizadas."""
    return jsonify(obtener_estadisticas()), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
