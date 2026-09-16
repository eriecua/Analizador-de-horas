# Convert_time.py — Conversor de Tiempo

Script de consola en Python para hacer conversiones rápidas entre **horas y minutos** (y viceversa). Ideal para calcular el tiempo trabajado en la semana y expresarlo en la unidad que necesites.

## 📋 Requisitos

- Python 3.x (no requiere librerías externas, solo la librería estándar).

## 🚀 Ejecución

Desde la terminal, navega a la carpeta del proyecto y ejecuta:

```bash
python Convert_time.py
```

O directamente:

```bash
python "c:\Users\MSI ERICK\Desktop\Proyectos varios\Analizador de horas\Convert_time.py"
```

## 🖥️ Uso

Al iniciar, el script muestra un menú con tres opciones:

```
------------------------------------------
Option (1): Hours Converted
Option (2): Minutes Converted
Option (3): Exit
------------------------------------------
```

### Opción 1 — Hours Converted (horas → minutos)

1. Elige la opción `1`.
2. Escribe la cantidad de **horas** (debe ser mayor que 0).
3. Escribe la cantidad de **minutos** (debe ser 0 o mayor).

El script calcula y muestra el total en minutos.

**Ejemplo:**

```
Chose your option: 1
Type hours: 2
Type minutes: 30
The total minutes is: 150 minutes
```

### Opción 2 — Minutes Converted (minutos → horas y minutos)

1. Elige la opción `2`.
2. Escribe una lista de valores en **minutos**, uno por uno.
3. Escribe `0` para terminar la entrada de datos.

El script suma todos los valores y muestra el total convertido a **horas y minutos**, además de cuántos números ingresaste.

**Ejemplo:**

```
Chose your option: 2
Type minutes: 45
Type minutes: 90
Type minutes: 0
------------------------------------------
Total Time: 2 hours and 15 minutes.
------------------------------------------
You type 2 numbers
```

### Opción 3 — Exit

Finaliza el programa con un mensaje de despedida.

## ⚠️ Validaciones y comportamiento

- **Opción 1:** si las horas no son mayores que 0 o los minutos son negativos, se muestra un mensaje de error y se vuelven a pedir los valores.
- **Opción 2:** el valor `0` actúa como señal de fin de entrada; los minutos se suman acumulativamente.
- **Cualquier otra opción:** se muestra `Invalid option. Please, try again` y el menú vuelve a pedir una opción.
- **Nota:** la entrada se lee con `int()`, por lo que si se ingresa texto no numérico el programa terminará con un `ValueError`.

## 📁 Estructura

| Archivo | Descripción |
|---|---|
| `Convert_time.py` | Script principal (menú interactivo de conversión de tiempo). |
| `README.md` | Descripción general del proyecto. |
| `README_Convert_time.md` | Este documento, específico del script. |
