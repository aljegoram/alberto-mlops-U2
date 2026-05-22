#!/usr/bin/env bash

echo "Probando ruta principal..."
curl http://localhost:5000/

echo ""
echo "Caso 1 - NO ENFERMO"
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d "{\"edad\":25,\"presion\":120,\"sintomas\":0}"

echo ""
echo "Caso 2 - ENFERMEDAD LEVE"
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d "{\"edad\":30,\"presion\":125,\"sintomas\":3}"

echo ""
echo "Caso 3 - ENFERMEDAD AGUDA"
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d "{\"edad\":45,\"presion\":145,\"sintomas\":6}"

echo ""
echo "Caso 4 - ENFERMEDAD CRÓNICA"
curl -X POST http://localhost:5000/predecir \
  -H "Content-Type: application/json" \
  -d "{\"edad\":70,\"presion\":160,\"sintomas\":9}"

echo ""
