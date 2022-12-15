"""
    Percorremos cada item do json e gravamos um arquivo txt com base
    no padrão estabelescido abaixo.
"""


def gera_arquivo(parametros):

    with open('./saida/arquivo_saida.txt', 'w', encoding='utf-8') as arquivo:  # w-write
        for formula, val_formulas in parametros.items():
            for metodo, energias in val_formulas.items():
                arquivo.write("====================================================== \n")
                arquivo.write(f"{metodo}\n")
                arquivo.write("ELETRONIC ENERGY:\n")
                arquivo.write(f"{parametros[formula][metodo]['electronic_energy']} Eh," "------->"
                              f"{parametros[formula][metodo]['electronic_energy'] * 627.5096}, kcal/mol\n\n")
                arquivo.write("-------------------------------------------------------- \n")

                arquivo.write("ZERO POINT ENERGY\n:")
                arquivo.write(f"{parametros[formula][metodo]['zero_point_energy']} Eh," "------->"
                              f"{parametros[formula][metodo]['zero_point_energy'] * 627.5096}, kcal/mol\n\n")
                arquivo.write("-------------------------------------------------------- \n")

                arquivo.write("TOTAL FREE ENERGY:\n")
                arquivo.write(f"{parametros[formula][metodo]['total_free_energy']} Eh," "------->"
                              f"{parametros[formula][metodo]['total_free_energy'] * 627.5096}, kcal/mol\n\n")
                arquivo.write("-------------------------------------------------------- \n")

                arquivo.write(f"ENTALPIA TOTAL: {formula} | método: {metodo} | base: {formula}\n")
                arquivo.write(f"{parametros[formula][metodo]['entalpia_total']} Eh," "----->"
                              f"{parametros[formula][metodo]['entalpia_total'] * 627.5096}, kcal/mol\n\n")
                arquivo.write("-------------------------------------------------------- \n")
                arquivo.write("A entalpia total foi calculada pela soma: ELETRONIC ENERGY + ZERO POINT ENERGY.\n\n\n\n")
