"""
    Faz a leitura de cada arquivo de entrada realizando a
    extração dos valores necessários, primeiro estabelecemos as pastas,
    separadas por metodos e o nome de cada arquivo.
"""


def extrair_informacoes(formulas, metodos, energias):
    """ 1 PASSO: MONTAR UMA LISTA DE TODOS OS ARQUIVOS """
    resultado, infos, valores, lista_arquivos = {}, {}, {}, []  # cria as variaveis vazias

    for formula in formulas:    # percorre formulas ['PH+', 'H2', 'PH3+'] e variando os métodos (3 x 4 itens)
        arquivos = {                                                    # 1ª EXECUCAO           # 2ª EXECUCAO       # 3ª
            0: str(f'./entrada/{formula}/{metodos[0]}/{formula}.out'),  # PH+/MP2/PH+.out       # H2/MP2/H2.out      ...
            1: str(f'./entrada/{formula}/{metodos[1]}/{formula}.out'),  # PH+/M062x/PH+.out     # H2/M062x/H2.out    ...
            2: str(f'./entrada/{formula}/{metodos[2]}/{formula}.out'),  # PH+/wb97x-d3/PH+.out  # H2/wb97x-d3/H2.out ...
            3: str(f'./entrada/{formula}/{metodos[3]}/{formula}.out')}  # PH+/wb97x/PH+.out     # H2/wb97x/H2.out    ...
        lista_arquivos.append(arquivos)
    print(f'lista_arquivos: {lista_arquivos}')



    """ 
        Percorremos cada uma das pastas e procuramos cada um dos arquivos
        extraindo o txto correspondente gravando as informações do dicionario
    """

    """ 2º PASSO: PERCORRER CADA UM DOS ARQUIVOS CONFORME A LISTA GERADA """
    for contador in range(0, len(lista_arquivos)):                # Percorre cada os pasta de formulas (3x)

        for indice, caminho in lista_arquivos[contador].items():  # percorrendo pasta de metodos (4x), indice=0, caminho='PH+/MP2/PH+.out'
            valores[metodos[indice]] = {}                         # valores['MP2'] = 0

            with open(caminho, 'r') as arquivo:                   # 'r'= read, o caminho 'PH+/MP2/PH+.out'

                for i in arquivo:
                    if "Electronic energy" in i:
                        valores[metodos[indice]][energias[0]] = float(i[36:52])  # valores['MP2']['ee'] ='-341.03214039'
                    if "Zero point energy" in i:
                        valores[metodos[indice]][energias[1]] = float(i[36:52])  # valores['MP2']['ze'] ='0.0056353'
                    if "Total free energy" in i:
                        valores[metodos[indice]][energias[2]] = float(i[37:52])  # valores['MP2']['te'] ='-341.0241445'
                        infos = valores.copy()
                resultado[formulas[contador]] = infos                     # armazena as informações em resultado['MP2']

    print(f'informacoes: {resultado}')
    return resultado
