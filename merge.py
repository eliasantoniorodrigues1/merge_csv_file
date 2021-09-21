import pandas as pd
import os


CAMINHO = os.path.join(os.getcwd(), 'dados')


def consolida_csv():
    # Consolida arquivos CSV
    for dir, root, files in os.walk(CAMINHO):
        dados_consolidado = pd.concat(
            [pd.read_csv(os.path.join(CAMINHO, file), delimiter=';', encoding='latin-1') for file in files if '.csv' in file])
    return dados_consolidado


def remove_duplicados(dataframe, coluna, manter, nome):
    # Remove duplicados
    print(coluna, manter)
    df = dataframe.drop_duplicates(subset=coluna, keep=manter)

    # Salva dataset sem duplicidade:
    df.to_csv(f'{nome}.csv', sep=';')


if __name__ == '__main__':
    dados = consolida_csv()
    print('Dados consolidados:')
    print(dados)

    # Determina se mantém o first ou o last duplicado encontrado:
    df = remove_duplicados(dados, 'ID', 'last', 'willer_bonner')
