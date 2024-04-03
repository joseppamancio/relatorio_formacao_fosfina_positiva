[English](README.md) | [Español](README.es.md)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-013220?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Chemistry](https://img.shields.io/badge/Chemistry-B22222?style=for-the-badge&logo=publons&logoColor=white)](https://www.acs.org/content/acs/en.html)

# Reatório de Formação de Fosfina Positiva

## 📝 Descrição

Este projeto foi desenvolvido para fornecer relatório de Cálculo de Formação de Fosfina Positiva para Química Computacional.
O objetivo é simular a reação de formação de fosfina positiva pela adição de hidrogênio ao íon fosfínio positivo.
A reação é representada pela seguinte equação química:

PH<sup>+</sup> + H<sub>2</sub> → PH<sub>3</sub><sup>+</sup>

## 📊 Resultados
Através de dados de entrada, o programa calcula a energia de formação da fosfina positiva e gera um gráfico de energia potencial em função da distância entre os átomos de fósforo e hidrogênio.

![resultados](saida/grafico.png)

## 📚 Teoria
A energia de formação de um composto é a energia necessária para formar um mol de uma substância a partir de seus elementos constituintes no estado padrão.
A energia de formação da fosfina positiva é dada pela diferença entre a energia do produto e a soma das energias dos reagentes:

ΔH<sub>f</sub> = E(PH<sub>3</sub><sup>+</sup>) - E(PH<sup>+</sup>) - E(H<sub>2</sub>)

onde:
- ΔH<sub>f</sub> é a energia de formação da fosfina positiva
- E(PH<sub>3</sub><sup>+</sup>) é a energia do produto (fosfina positiva)
- E(PH<sup>+</sup>) é a energia do reagente (fosfínio positivo)
- E(H<sub>2</sub>) é a energia do reagente (hidrogênio)

## 🔄 Processo
O projeto possui scripts para realizar os cálculos e gerar os gráficos.
* **parametros.py** - contém os parâmetros de entrada do programa.
* **calculos.py** - realiza os cálculos da energia de formação da fosfina positiva e gera o gráfico de energia potencial.
* **gerar_grafico.py** - gera o gráfico de energia potencial em função da distância entre os átomos de fósforo e hidrogênio.
* **gera_arquivo.py** - gera um arquivo de saída com os resultados dos cálculos.
* **main.py** - é o script principal que chama as funções dos outros scripts.

## 📋 Requisitos
Para executar o projeto, é necessário instalar o Python e a biblioteca Matplotlib.

## 📦 Instalação
Para instalar a biblioteca Matplotlib, execute o seguinte comando:
```bash
pip install matplotlib
```

## 🚀 Tecnologias
* [Python](https://www.python.org/)
* [Matplotlib](https://matplotlib.org/)