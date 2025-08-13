# Buscador de Artículos por Similitud de Abstract

Este proyecto es una aplicación web que permite a los usuarios encontrar artículos académicos buscando por similitud semántica en sus abstracts. La herramienta utiliza embeddings de texto para representar el significado de los abstracts y una base de datos PostgreSQL con la extensión `pgvector` para realizar búsquedas de similitud de manera eficiente y escalable.

La interfaz de usuario está construida con Streamlit y ofrece una forma sencilla de introducir un texto y obtener una lista de los artículos más relevantes de la base de datos.

---

## 🚀 Características Principales

* **Búsqueda por Similitud Semántica**: En lugar de buscar por palabras clave, el motor encuentra artículos basándose en el significado contextual del abstract proporcionado.
* **Interfaz de Usuario Interactiva**: Una aplicación web simple creada con Streamlit que permite a los usuarios introducir texto y ver los resultados al instante.
* **Backend Potente y Escalable**: Utiliza PostgreSQL junto con la extensión `pgvector` para almacenar y consultar eficientemente millones de vectores de embeddings.
* **Indexación para Búsquedas Rápidas**: Implementa índices especializados como HNSW y IVFFlat para acelerar drásticamente las búsquedas por similitud en grandes volúmenes de datos.

---

## ⚙️ Metodología / Cómo Funciona

El flujo de trabajo del proyecto se divide en dos fases principales: la ingesta de datos y la búsqueda en tiempo real.

### Procesamiento de Datos e Ingesta (`main.py`)

1.  **Carga de Datos**: Se carga un conjunto de datos de artículos de **arXiv** desde un archivo (`.jsonl`). El dataset utilizado se puede encontrar en Kaggle: [Cornell-University/arxiv](https://www.kaggle.com/datasets/Cornell-University/arxiv).
2.  **Generación de Embeddings**: Para cada artículo, se genera un vector numérico (embedding) a partir de su abstract utilizando la función `generate_embeddings`. Este vector captura la esencia semántica del texto.
3.  **Almacenamiento**: Los datos de los artículos, junto con sus embeddings correspondientes, se insertan en una tabla de PostgreSQL.

### Búsqueda por Similitud (`streamlit_app.py`)

1.  **Entrada del Usuario**: El usuario introduce un abstract en la interfaz de Streamlit.
2.  **Generación de Embedding**: La aplicación genera un embedding para este texto de entrada usando la misma función `generate_embeddings`.
3.  **Consulta**: Se ejecuta una consulta en la base de datos para encontrar los vectores más cercanos al vector de entrada. La "cercanía" se mide utilizando la **distancia de coseno** (`<=>`), que es una métrica eficaz para determinar la similitud de orientación entre dos vectores.
4.  **Resultados**: La consulta devuelve los 10 artículos más similares, que se muestran al usuario.

---

## 🛠️ Stack Tecnológico

* **Lenguaje**: Python
* **Interfaz de Usuario**: Streamlit
* **Base de Datos**: PostgreSQL
* **Extensión de Vector**: `pgvector`
* **Librerías Principales**: `streamlit`, `psycopg2` (o similar), y una librería de generación de embeddings (ej. Sentence Transformers, Hugging Face, etc.).

---

## 📂 Estructura del Proyecto

```plaintext
/
├── .env                  # Archivo de configuración para la base de datos
├── main.py               # Script para procesar datos y poblar la BD
├── streamlit_app.py      # Aplicación web para la búsqueda de similitud
├── src/
│   ├── data_processing.py  # Procesamiento y limpieza de datos
│   ├── embedding.py        # Generación de embeddings
│   └── database.py         # Conexión y operaciones con la base de datos
└── data/
    └── casos-test.jsonl    # Dataset de ejemplo
```

---

## 🚀 Cómo Empezar

### 1. Clonar el repositorio:

```bash
git clone [https://github.com/tu_usuario/tu_repositorio.git](https://github.com/tu_usuario/tu_repositorio.git)
cd tu_repositorio
```
### 2. Configurar el entorno

* Crea un entorno virtual e instala las dependencias (se recomienda crear un archivo `requirements.txt`).
* Instala PostgreSQL y habilita la extensión `pgvector`.
* [cite_start]Crea una base de datos (`SSAbstracts`) y un usuario (`postgres`)[cite: 5].

### 3. Configurar variables de entorno

* [cite_start]Crea un archivo `.env` a partir de un ejemplo y añade tus credenciales de la base de datos[cite: 5].

### 4. Poblar la base de datos

* Asegúrate de tener tu archivo de datos (`.jsonl`) en la ubicación correcta.
* Ejecuta el script principal para procesar los datos y guardarlos en PostgreSQL:

    ```bash
    python main.py
    ```
* *Nota: La inserción de datos (`insert_data_to_postgres`) debe ejecutarse solo una vez*.

### 5. Lanzar la aplicación

```bash
streamlit run streamlit_app.py

