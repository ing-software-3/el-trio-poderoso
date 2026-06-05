# Inventario Digital de Materiales - Liceo Infantil "Expresiones Pedagógicas"

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Objetivos](#objetivos)
- [Stock Tecnológico](#stock-tecnológico)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Flujo de Datos (Gestión del Inventario Digital)](#flujo-de-datos-gestión-del-inventario-digital)
- [Estructura de Base de Datos](#estructura-de-Base-de-Datos)
- [Estado por Fases](#estado-por-fases)
- [Instalación](#instalación)
- [Uso](#uso)
- [Notas Importantes](#notas-importantes)
- [Autores](#autores)

## 📝 Descripción del Proyecto

Este proyecto introduce un sistema de gestión de inventario digital para el Liceo Infantil "Expresiones Pedagógicas". Por primera vez, se centralizará y organizará el control de todos los materiales didácticos, de juego, de aseo y de oficina de manera electrónica.

## 🎯 Objetivos

- **Digitalizar la Información:** Migrar los registros físicos a un formato digital centralizado.
- **Optimizar el Control de Stock:** Seguimiento automatizado de entradas y salidas.
- **Reducir Pérdidas:** Mejorar la visibilidad sobre el uso de materiales.
- **Automatizar la Reposición:** Alertas digitales para stock bajo.
- **Organización:** Mantener información clara y estructurada.
- **Control de inventario:** Registrar productos disponibles en el jardín.

## 🛠️ Stack Tecnológico

### Entorno de Desarrollo

PyCharm: IDE utilizado para desarrollar, organizar y ejecutar el proyecto

### Backend

Python 3.10+: Lenguaje principal
FastAPI: Creación de la API
MySQL: Base de datos relacional
PyCharm: Entorno de desarrollo

### Librerías

SQLAlchemy: Conexión a base de datos
Uvicorn: Servidor para FastAPI

## 📁 Estructura del Proyecto

```inventario-jardin/
│
├── app/
│   ├── main.py              # Punto de entrada FastAPI
│   ├── core/
│   │   └── database.py      # Conexión a MySQL
│   ├── models/
│   │   └── products.py
│   ├── schemas/
│   │   └── producto_schema.py
│   ├── routes/
│   │   └── producto_routes.py
│   └── crud/
│       └── producto_crud.py
│
├── docs/                    # Documentación
├── requirements.txt
└── README.md

```

## 🔄Flujo de Datos

Usuario (profesor/administrador) hace una petición
La API en FastAPI recibe la solicitud
Se procesa la lógica en el módulo CRUD
Se consulta o modifica la base de datos en MySQL
Se devuelve una respuesta en formato JSON

## 🗄️Estructura de la Base de Datos

```env
| Campo          | Tipo    | Descripción         |
|----------------|---------|---------------------|
| id             | INT     | Identificador único |
| nombre         | VARCHAR | Nombre del producto |
| categoria      | VARCHAR | Tipo de producto    |
| cantidad       | INT     | Cantidad disponible |
| precio         | FLOAT   | Precio              |
| fecha_registro | DATETIME| Fecha de ingreso    |

```

## 🚦Estado por Fases

### ✅Fase 1: Base del sistema

Creación de base de datos
Conexión con MySQL
Estructura del proyecto en Python

### 🔄 Fase 2: CRUD básico

Crear productos
Listar productos
Actualizar productos
Eliminar productos

### 🔮 Fase 3: Mejoras futuras

Control de alertas (stock bajo)
Reportes simples
Interfaz gráfica (opcional)

## 🔧 Instalación

Requisitos
Python 3.10+
MySQL
PyCharm

```#Crear entorno virtual
python -m venv venv

#Activar entorno
venv\Scripts\activate

#Instalar dependencias
pip install -r requirements.txt

```

## 🚀 Uso

```Ejecutar el servidor:

uvicorn app.main:app --reload

Abrir en navegador:
```

<http://127.0.0.1:8000/docs>

## 📝 Notas Importantes

Es un sistema básico, no necesita ser complejo
Enfocado en aprendizaje y presentación
Código organizado tipo proyecto real
Ideal para subir a GitHub como evidencia académica

## 👩‍💻 Autores

Sandra Bibiana Casas Morales

Karen Atehortúa

Laura Delgado


