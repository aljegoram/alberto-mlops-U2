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
python app/main.py
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

