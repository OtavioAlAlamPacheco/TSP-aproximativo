
import os


def ler_matriz(arquivo):
    """
    Lê uma matriz a partir de um arquivo.
    
    Argumentos:
        arquivo (str): O caminho para o arquivo que contém a matriz.
    
    Retorna:
        matriz (list): Uma lista de listas de inteiros representando a matriz de custos,
        ou None se o arquivo não existir.
    """
    if not os.path.exists(arquivo):
        print(f"Erro: O arquivo {arquivo} não existe.")
        exit()   
    
    with open(arquivo, 'r') as arq:
        matriz = []
        for linha in arq:
            matriz.append([int(x) for x in linha.split()])
    return matriz
