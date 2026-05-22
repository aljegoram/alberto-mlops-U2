# Taller 2 — Solución inicial del servicio médico simulado

## 1. Descripción general

Este repositorio contiene una solución de MLOps para un caso médico simulado.

La solución expone una API con Flask que recibe datos básicos de un paciente y retorna una clasificación simulada del estado del paciente.

Esta versión corresponde a la solución inicial basada en el Taller 1.

## 2. Categorías de predicción iniciales

La función simulada retorna una de las siguientes categorías:

- `NO ENFERMO`
- `ENFERMEDAD LEVE`
- `ENFERMEDAD AGUDA`
- `ENFERMEDAD CRÓNICA`
- `ENFERMEDAD TERMINAL`

## 3. Estructura del proyecto

```text
app/
├── __init__.py
├── main.py
└── model.py
scripts/
└── probar_api.sh
Dockerfile
requirements.txt
README.md
.dockerignore
.gitignore
```

## 4. Ejecución local

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno en Windows:

```bash
venv\Scripts\activate
```

Activar entorno en Linux/Mac:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar API:

```bash
python -m app.main
```

## 5. Construir imagen Docker

```bash
docker build -t medico-mlops .
```

## 6. Ejecutar contenedor Docker

```bash
docker run -p 5000:5000 medico-mlops
```

## 7. Probar la API

Ruta principal:

```bash
curl http://localhost:5000/
```

Predicción:

```bash
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d "{\"edad\":70,\"presion\":160,\"sintomas\":9}"
```


## Nueva categoría agregada

Se incorpora la categoría `ENFERMEDAD TERMINAL` como nuevo requerimiento funcional del Taller 2.

Ejemplo de entrada que retorna `ENFERMEDAD TERMINAL`:

```bash
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d "{\"edad\":85,\"presion\":190,\"sintomas\":10}"
```

Respuesta esperada:

```json
{
  "estado": "OK",
  "resultado": "ENFERMEDAD TERMINAL"
}
```
## Reporte de estadísticas

Se agregó el endpoint:

```text
GET /estadisticas
```

Este endpoint permite consultar:

- Número total de predicciones realizadas.
- Número total de predicciones por categoría.
- Últimas 5 predicciones realizadas.
- Fecha de la última predicción.

## Ejemplo de uso

Primero realiza algunas predicciones:

```bash
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d "{\"edad\":85,\"presion\":190,\"sintomas\":10}"
```

Luego consulta las estadísticas:

```bash
curl http://localhost:5000/estadisticas
```

Respuesta esperada de ejemplo:

```json
{
  "total_predicciones": 1,
  "total_por_categoria": {
    "NO ENFERMO": 0,
    "ENFERMEDAD LEVE": 0,
    "ENFERMEDAD AGUDA": 0,
    "ENFERMEDAD CRÓNICA": 0,
    "ENFERMEDAD TERMINAL": 1
  },
  "ultimas_5_predicciones": [
    {
      "fecha": "2026-05-22T10:30:00+00:00",
      "edad": 85,
      "presion": 190,
      "sintomas": 10,
      "resultado": "ENFERMEDAD TERMINAL",
      "version_modelo": "v2.0-simulada"
    }
  ],
  "fecha_ultima_prediccion": "2026-05-22T10:30:00+00:00"
}
```
## Pruebas unitarias

El proyecto incluye pruebas unitarias con `pytest`.

Las pruebas se encuentran en la carpeta:

```text
tests/
```

Incluyen validaciones sobre:

- Retorno de la categoría `ENFERMEDAD TERMINAL`.
- Retorno de las cinco categorías de predicción.
- Validación de campos faltantes.
- Estadísticas iniciales vacías.
- Registro de predicciones.
- Funcionamiento del endpoint `/predecir`.
- Funcionamiento del endpoint `/estadisticas`.

Para ejecutar las pruebas:

```bash
pytest -q
```

Resultado esperado:

```text
6 passed
```
## CI/CD con GitHub Actions

El proyecto incluye un workflow de CI/CD en:

```text
.github/workflows/ci-cd.yml
```

El workflow se ejecuta en dos eventos:

### Pull Request hacia `main`

Cuando se crea un Pull Request contra `main`, el workflow:

1. Comenta en el PR: `CI/CD en acción. Ejecutando tareas …`
2. Descarga el código.
3. Configura Python 3.11.
4. Instala dependencias.
5. Ejecuta pruebas unitarias con `python -m pytest -q`.
6. Si todo sale bien, comenta: `CI/CD terminado con éxito.`

### Push en `main`

Cuando hay un push en `main`, normalmente después de un merge, el workflow:

1. Descarga el código.
2. Configura Python 3.11.
3. Instala dependencias.
4. Ejecuta pruebas unitarias.
5. Construye una imagen Docker.
6. Publica la imagen en GitHub Container Registry / GitHub Packages.

## Imagen Docker publicada

La imagen se publica con formato:

```text
ghcr.io/<usuario>/<repositorio>:latest
```

Ejemplo:

```text
ghcr.io/aljegoram/alberto-mlops-U2:latest
```

