import os

def ler_matriz(arquivo):
    """
    Lê uma matriz a partir de um arquivo.
    
    Argumentos:
        arquivo (str): O caminho para o arquivo que contém a matriz.
    
    Retorna:
        matriz: Uma lista de listas de inteiros representando a matriz, ou
        None se o arquivo não existir.
    """
    if not os.path.exists(arquivo):
        print(f"Erro: O arquivo {arquivo} não existe.")
        exit()   
    
    with open(arquivo, 'r') as arq:
        matriz = []
        for linha in arq:
            matriz.append([int(x) for x in linha.split()])
    return matriz

def tsp(arquivo):
    """
    Resolve o problema do Caixeiro Viajante usando programação dinâmica.
    
    Argumentos:
        arquivo (str): O caminho para o arquivo que contém a matriz de custos.
    
    Retorna:
        matriz, n: Uma tupla da matriz lida e o numero de cidades, ou
        None se ocorrer um erro ao ler o arquivo.
    """
    try:
        matriz = ler_matriz(arquivo)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        exit()
    
    n = len(matriz)
    
    return matriz, n