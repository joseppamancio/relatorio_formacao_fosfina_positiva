from matplotlib import pyplot as plt

""" 
    Realiza a geração do grafico conforme os valores obtidos nos calculos,
    recebe como entrada uma lista com os deltas já calculados e convetidos.
"""


def gera_grafico(deltas_convertidos):
    plt.title('Reação I - PH${^+}$ + H${_2}$ -> PH${_3^+}$', color='red')
    plt.xlabel('Reação')
    plt.ylabel('Entalpia (kcal/mol)')
    x = [1, 2]
    plt.plot(x, [0, list(deltas_convertidos.values())[0]], label='MP2', color='black')
    plt.plot(x, [0, list(deltas_convertidos.values())[1]], label='m06-2x', color='blue')
    plt.plot(x, [0, list(deltas_convertidos.values())[2]], label='wB97x-D3', color='green')
    plt.plot(x, [0, list(deltas_convertidos.values())[3]], label='wB97x', color='red')
    plt.legend()
    plt.savefig('./saida/grafico')
    plt.show()
