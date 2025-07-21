# 📦 Python con SQL server

Este proyecto tiene como objetivo automatizar la carga de datos tabulares (Excel) y geográficos (Shapefiles) en una base de datos SQL Server, además de permitir la ejecución de consultas SQL para análisis y validación.

## 🗂 Estructura del Proyecto

```
Python con SQL server/  
├── config/ # Configuraciones (conexiones, parámetros)  
│ └── config.py  
├── data/ # Archivos fuente: Excel y Shapefiles  
├── notebooks/ # Notebooks de ejecución y pruebas  
├── utils/ # Funciones de carga, conexión, consultas SQL  
└── README.md
```

## 🚀 Funcionalidades Principales

- 📥 Importación de archivos Excel a SQL Server.
- 🌍 Carga de archivos Shapefile a SQL Server (con geometría).
- 🔎 Ejecución de consultas SQL y visualización con Pandas.
- 🔧 Modularizado para facilitar el mantenimiento y la reutilización.

## 🧰 Tecnologías Usadas

- Python 3.8+
- Pandas, Geopandas
- SQLAlchemy o pyodbc
- OS, SYS, dotenv
- Jupyter Notebooks

## ⚙️ Configuración

Configura tu conexión a SQL Server en `config/config.py` o usando variables de entorno (`.env`):
    
    ```python
    SQL_CONFIG = {
        "driver": "ODBC Driver 17 for SQL Server",
        "server": "TU_SERVIDOR",
        "database": "TU_BBDD",
        "username": "usuario",
        "password": "contraseña"
    }
    ```
    
## 🧪 Ejemplo de Uso

```python
# Leer Excel
df = pd.read_excel("data/tabla_ejemplo.xlsx")

# Subir a SQL Server
importar_dataframe_a_sqlserver(df, nombre_tabla="tabla_destino")

# Ejecutar consulta
df_resultado = ejecutar_consulta_sql("SELECT * FROM tabla_destino")
```

## 📌 Notas

- Las rutas se manejan con `os.path` para asegurar compatibilidad cross-platform.
- Los notebooks ubicados en `notebooks/` muestran ejemplos prácticos y trazas de ejecución.
    