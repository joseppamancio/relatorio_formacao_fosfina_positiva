[English](README.md) | [Português](README.pt.md)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-013220?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Chemistry](https://img.shields.io/badge/Chemistry-B22222?style=for-the-badge&logo=publons&logoColor=white)](https://www.acs.org/content/acs/en.html)

# Reporte de Formación de Fosfina Positiva

## 📝 Descripción

Este proyecto fue desarrollado para proporcionar un informe de Cálculo de Formación de Fosfina Positiva para Química Computacional. El objetivo es simular la reacción de formación de fosfina positiva mediante la adición de hidrógeno al ion fosfinio positivo. La reacción se representa mediante la siguiente ecuación química:

PH<sup>+</sup> + H<sub>2</sub> → PH<sub>3</sub><sup>+</sup>

## 📊 Resultados

A través de datos de entrada, el programa calcula la energía de formación de la fosfina positiva y genera un gráfico de energía potencial en función de la distancia entre los átomos de fósforo e hidrógeno.

![resultados](saida/grafico.png)

## 📚 Teoría

La energía de formación de un compuesto es la energía necesaria para formar un mol de una sustancia a partir de sus elementos constituyentes en el estado estándar. La energía de formación de la fosfina positiva se da por la diferencia entre la energía del producto y la suma de las energías de los reactivos:

ΔH<sub>f</sub> = E(PH<sub>3</sub><sup>+</sup>) - E(PH<sup>+</sup>) - E(H<sub>2</sub>)

donde:
- ΔH<sub>f</sub> es la energía de formación de la fosfina positiva
- E(PH<sub>3</sub><sup>+</sup>) es la energía del producto (fosfina positiva)
- E(PH<sup>+</sup>) es la energía del reactivo (fosfinio positivo)
- E(H<sub>2</sub>) es la energía del reactivo (hidrógeno)

## 🔄 Proceso

El proyecto cuenta con scripts para realizar los cálculos y generar los gráficos.
* **parametros.py** - contiene los parámetros de entrada del programa.
* **calculos.py** - realiza los cálculos de la energía de formación de la fosfina positiva y genera el gráfico de energía potencial.
* **gerar_grafico.py** - genera el gráfico de energía potencial en función de la distancia entre los átomos de fósforo e hidrógeno.
* **gera_arquivo.py** - genera un archivo de salida con los resultados de los cálculos.
* **main.py** - es el script principal que llama a las funciones de los otros scripts.

## 📋 Requisitos

Para ejecutar el proyecto, es necesario instalar Python y la biblioteca Matplotlib.

## 📦 Instalación

Para instalar la biblioteca Matplotlib, ejecute el siguiente comando:

```bash
pip install matplotlib
```

## 🚀 Tecnologías
* [Python](https://www.python.org/)
* [Matplotlib](https://matplotlib.org/)