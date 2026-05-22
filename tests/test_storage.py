from app.storage import limpiar_predicciones, obtener_estadisticas, registrar_prediccion


def test_estadisticas_iniciales_vacias(monkeypatch, tmp_path):
    archivo_temporal = tmp_path / "predicciones_test.jsonl"
    monkeypatch.setenv("PREDICTIONS_FILE", str(archivo_temporal))

    limpiar_predicciones()
    estadisticas = obtener_estadisticas()

    assert estadisticas["total_predicciones"] == 0
    assert estadisticas["fecha_ultima_prediccion"] is None
    assert estadisticas["ultimas_5_predicciones"] == []
    assert estadisticas["total_por_categoria"]["ENFERMEDAD TERMINAL"] == 0


def test_registro_y_estadisticas_de_predicciones(monkeypatch, tmp_path):
    archivo_temporal = tmp_path / "predicciones_test.jsonl"
    monkeypatch.setenv("PREDICTIONS_FILE", str(archivo_temporal))

    limpiar_predicciones()

    registrar_prediccion(
        edad=85,
        presion=190,
        sintomas=10,
        resultado="ENFERMEDAD TERMINAL",
        version_modelo="v2.0-simulada",
    )

    estadisticas = obtener_estadisticas()

    assert estadisticas["total_predicciones"] == 1
    assert estadisticas["total_por_categoria"]["ENFERMEDAD TERMINAL"] == 1
    assert estadisticas["fecha_ultima_prediccion"] is not None
    assert estadisticas["ultimas_5_predicciones"][-1]["resultado"] == "ENFERMEDAD TERMINAL"
