# Evaluación Final POA - Fase 5: Control de Inventario.

Solución desarrollada en **Python** para el **Problema #3** del banco de problemas de la Fase 5 - Evaluación Final POA del curso **FUNDAMENTOS DE PROGRMACIÓN** de la UNAD.



**DESCRIPCIÓN DEL PROBLEMA**

El Problema gestiona una matriz de inventario con al menos 5 artículos [Código del artículo, Nombre del artículo, Stock actual, Stock minimo, Stock mínimo requerido] 
y calcula la cantidad exacta a pedir para reabastecer cada artículo mediante una función:

- Si el **Stock actual** es menor que el **Stock minimo requerido**, la cantidad a pedir es `Stock mínimo requerido - Stock actual`.
- Si el **Stock actual** es mayor o igual al **Stock minimo requerido**, la cantidad a pedir es '0'

**ARCHIVO INCLUIDO**
- 'Problema-Python-Fase5.py': Código fuente en Python que define la matriz de inventario, implementa la función de cálculo
y muestra el listado de cada artículo con la cantidad a solicitar
