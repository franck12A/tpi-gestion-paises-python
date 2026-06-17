# Gestión de Datos de Países en Python

## Trabajo Práctico Integrador – Programación I

### Instituto Universitario de Tecnología

**Tecnicatura Universitaria en Programación a Distancia**

---

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de una aplicación en Python para la gestión de información de países. El sistema permite almacenar, consultar, actualizar y analizar datos mediante el uso de listas, diccionarios, funciones, archivos CSV y técnicas de filtrado, ordenamiento y estadísticas básicas.

La aplicación fue desarrollada como Trabajo Práctico Integrador de la materia **Programación I**, con el objetivo de aplicar los conceptos fundamentales estudiados durante la cursada.

---

## Docente

**Franco González**

---

## Integrantes

* Franco Elian Enrici
* Franco Exequiel Herrera Schachinger

---

## Objetivos

* Aplicar estructuras de datos como listas y diccionarios.
* Utilizar funciones para modularizar el código.
* Implementar búsquedas, filtros y ordenamientos.
* Generar estadísticas básicas sobre conjuntos de datos.
* Trabajar con archivos CSV para la persistencia de información.
* Utilizar Git y GitHub para el control de versiones y trabajo colaborativo.

---

## Funcionalidades

### Gestión de Datos

* Agregar países.
* Actualizar población y superficie.
* Guardar cambios en el archivo CSV.

### Búsquedas

* Buscar países por nombre.
* Coincidencia exacta o parcial.
* Búsquedas sin distinguir mayúsculas y minúsculas.

### Filtros

* Filtrar por continente.
* Filtrar por rango de población.
* Filtrar por rango de superficie.

### Ordenamientos

* Ordenar por nombre.
* Ordenar por población.
* Ordenar por superficie.
* Orden ascendente o descendente.

### Estadísticas

* País con mayor población.
* País con menor población.
* Promedio de población.
* Promedio de superficie.
* Cantidad de países por continente.

---

## Estructura del Proyecto

```text
TPI_PROGRAMACION/
│
├── main.py
├── datos.py
├── busquedas.py
├── filtros.py
├── ordenamientos.py
├── estadisticas.py
├── validaciones.py
├── paises.csv
├── README.md
└── __pycache__/
```

### Descripción de los módulos

| Archivo          | Función                                           |
| ---------------- | ------------------------------------------------- |
| main.py          | Controla el flujo principal y el menú del sistema |
| datos.py         | Gestión y persistencia de datos CSV               |
| busquedas.py     | Funciones de búsqueda                             |
| filtros.py       | Funciones de filtrado                             |
| ordenamientos.py | Ordenamiento de registros                         |
| estadisticas.py  | Cálculos estadísticos                             |
| validaciones.py  | Validación de entradas                            |
| paises.csv       | Almacenamiento de datos                           |

---

## Requisitos

* Python 3.x

No requiere librerías externas.

---

## Instrucciones de Ejecución

1. Clonar el repositorio:

```bash
git clone https://github.com/franck12A/tpi-gestion-paises-python.git
```

2. Ingresar al directorio:

```bash
cd tpi-gestion-paises-python
```

3. Ejecutar el programa:

```bash
python main.py
```

---

## Menú Principal

```text
1. Agregar país
2. Actualizar país
3. Buscar país
4. Filtrar países
5. Ordenar países
6. Estadísticas
7. Guardar
8. Salir
```

---

## Dataset Utilizado

Ejemplo de estructura del archivo CSV:

```csv
nombre,poblacion,superficie,continente
Argentina,46000000,2800000,America
Brasil,213993437,8515767,America
Japon,125800000,377975,Asia
```

---

## Tecnologías Utilizadas

* Python 3
* CSV
* Git
* GitHub

---

## Documentación

La documentación técnica y académica del proyecto se encuentra incluida en formato PDF dentro del repositorio.

**PDF:** [Agregar enlace]

---

## Video Demostración

**Video:** [Agregar enlace]

---

## Repositorio GitHub

https://github.com/franck12A/tpi-gestion-paises-python

---

## Conclusión

Este proyecto permitió aplicar conocimientos fundamentales de programación relacionados con estructuras de datos, modularización, persistencia de información y análisis de datos. Además, fortaleció el trabajo colaborativo mediante el uso de Git y GitHub para el control de versiones y la integración de cambios.
