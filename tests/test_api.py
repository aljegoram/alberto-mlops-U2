from app.main import app
from app.storage import limpiar_predicciones


def test_api_predecir_y_estadisticas(monkeypatch, tmp_path):
    archivo_temporal = tmp_path / "predicciones_api_test.jsonl"
    monkeypatch.setenv("PREDICTIONS_FILE", str(archivo_temporal))

    limpiar_predicciones()

    cliente = app.test_client()

    respuesta = cliente.post(
        "/predecir",
        json={"edad": 85, "presion": 190, "sintomas": 10},
    )

    assert respuesta.status_code == 200

    data = respuesta.get_json()
    assert data["resultado"] == "ENFERMEDAD TERMINAL"

    respuesta_stats = cliente.get("/estadisticas")
    assert respuesta_stats.status_code == 200

    stats = respuesta_stats.get_json()
    assert stats["total_predicciones"] == 1
    assert stats["total_por_categoria"]["ENFERMEDAD TERMINAL"] == 1
