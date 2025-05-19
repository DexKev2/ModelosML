# ModelosML - Mushroom Classification

### Desarrollado por: 
#### Kevin Saldarriaga Garcia
#### Julian Lopera

Este repositorio contiene un modelo de clasificación para determinar si un hongo es comestible o venenoso basado en sus características físicas.

## Estructura del Repositorio

### `/Dataset`
Contiene el conjunto de datos utilizado para entrenar y evaluar el modelo de clasificación de hongos. El dataset incluye diversas características que definen a los hongos y su clasificación como comestibles o venenosos.

### `/Notebook`
Incluye un archivo Jupyter/Colab con todo el proceso de:
- Preprocesamiento de datos
- Limpieza de datos (data cleaning)
- Entrenamiento de diversos modelos
- Evaluación de rendimiento
- Exportación del modelo seleccionado

### `/Orange`
Contiene archivos relacionados con el uso de Orange Data Mining para la evaluación visual y comparativa de modelos.

### `/app`
Contiene:
- El modelo ya entrenado y listo para su uso
- Una implementación FastAPI para exponer el modelo como un servicio web

## Selección del Modelo

Tras comparar varios algoritmos de aprendizaje automático (KNN, Naive Bayes, Tree, SVM), se seleccionó **KNN (K-Nearest Neighbors)** como el modelo final debido a su rendimiento superior:

- **Precisión (Precision)**: 0.976
- **Recall**: 0.988
- **F1 Score**: 0.982
- **AUC**: 0.983
- **MCC**: 0.976

KNN y SVM mostraron métricas casi idénticas, pero KNN fue elegido por su simplicidad y eficiencia en la clasificación para este conjunto de datos en particular.

## Cómo Usar el Repositorio

### Requisitos previos
```bash
pip install fastapi uvicorn scikit-learn pandas numpy
Ejecutar la API

Navega hasta la carpeta /app:

bashcd app

Inicia el servidor FastAPI:

bashuvicorn main:app --reload

La API estará disponible en: http://localhost:8000

Testear con Postman

Abre Postman
Crea una nueva petición POST a http://localhost:8000/predict
Configura el cuerpo de la petición como JSON con el siguiente formato:

json{
  "Capshape": 5,
  "Capsurf": 3,
  "Capcolor": 4,
  "Bruises": 1,
  "Odor": 6,
  "Gillatt": 0,
  "Gillspace": 1,
  "Gillsize": 1,
  "Gillcolor": 2,
  "Stalkshape": 0,
  "Stalkroot": 1,
  "Ssurfabove": 2,
  "Ssurfbelow": 2,
  "Scolorabove": 4,
  "Scolorbelow": 4,
  "Veiltype": 0,
  "Veilcolor": 2,
  "Ringnum": 1,
  "Ringtype": 4,
  "Spore": 6,
  "Pop": 3,
  "Habitat": 2
}

Envía la petición
La respuesta debería ser similar a:

json{
  "prediction": "poisonous",
  "probability": 0.98
}

