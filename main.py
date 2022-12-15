from parametros import extrair_informacoes
from calculos import calculo_energia, calculo_delta
from gera_grafico import gera_grafico
from gera_arquivo import gera_arquivo

formulas = ['PH+', 'H2', 'PH3+']
metodos = ['MP2', 'M062x', 'wb97x-d3', 'wb97x']
energias = ['electronic_energy', 'zero_point_energy', 'total_free_energy']

# Realiza a extração das informações dos arquivos TXT
informacoes = extrair_informacoes(formulas, metodos, energias)

# Realiza o calculo das energias
parametros = calculo_energia(informacoes)

# Realiza o calculo do delta
deltas = calculo_delta(parametros, metodos)

# Gera o arquivo txt na pasta de saída
gera_arquivo(parametros)

# Gera o gráfico em png na pasta saída
gera_grafico(deltas['delta_convertido'])
