"""
    Percorremos cada item do json buscamos as energias correspondentes de cada item,
    efetuando o cáclulo 'electronic_energy + zero_point_energy'.
"""


def calculo_energia(informacoes):
    for formulas, val_formulas in informacoes.items():  # percorre cada formula
        for metodos, energias in val_formulas.items():  # percorre cada metodos
            informacoes[formulas][metodos]['entalpia_total'] = energias['electronic_energy'] + energias['zero_point_energy']
    print(f'informacoes: {informacoes}')
    return informacoes


""" 
    Percorremos cada item do json buscamos as energias correspondentes de cada item,
    obtendo o cáclulo  da soma das energias 'electronic_energy + zero_point_energy'
    calculando o delta e já realizando a conversão.
    
"""


def calculo_delta(parametros, metodos):
    resultados = {'delta': {}, 'delta_convertido': {}}
    for metodo in metodos:
        delta = parametros['PH3+'][metodo]['entalpia_total'] - (parametros['PH+'][metodo]['entalpia_total'] + parametros['H2'][metodo]['entalpia_total'])
        resultados['delta'].update({metodo: delta})
        resultados['delta_convertido'].update({metodo: delta*627.5096})
    print(f'resultados: {resultados}')
    return resultados
