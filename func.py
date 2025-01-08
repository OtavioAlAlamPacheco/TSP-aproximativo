import os

def ler_matriz(arquivo):
    """
    Lê uma matriz a partir de um arquivo.
    
    Argumentos:
        arquivo (str): O caminho para o arquivo que contém a matriz.
    
    Retorna:
        list: Uma lista de listas de inteiros representando a matriz, ou
        None se o arquivo não existir ou se ocorrer um erro ao ler o arquivo.
    """
    if not os.path.exists(arquivo):
        print(f"Erro: O arquivo {arquivo} não existe.")
        return None    
    
    with open(arquivo, 'r') as arq:
        matriz = []
        for linha in arq:
            matriz.append([int(x) for x in linha.split()])
    return matriz
   
def caixeiroViajante(arquivo):
    """
    Resolve o problema do Caixeiro Viajante usando programação dinâmica.
    
    Argumentos:
        arquivo (str): O caminho para o arquivo que contém a matriz de custos.
    
    Retorna:
        int: O custo mínimo para completar o percurso do Caixeiro Viajante, ou
        None se ocorrer um erro ao ler o arquivo.
    """
    try:
        matriz = ler_matriz(arquivo)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None
    
    n = len(matriz)

    # Usar um dicionário para memoização
    memo = {}

    return custoTotal(1, 0, n, matriz, memo)
 
def custoTotal(mascara, atual, n, custo, memo):
    """
    Calcula o custo total mínimo para visitar todas as cidades e retornar à cidade inicial.
    
    Argumentos:
        mascara (int): Um inteiro que representa as cidades visitadas até o momento usando bits.
        atual (int): O índice da cidade atual.
        n (int): O número total de cidades.
        custo (list): Uma matriz 2D onde custo[i][j] representa o custo de viajar da cidade i para a cidade j.
        memo (dict): Um dicionário usado para memoização, onde memo[(atual, mascara)] armazena o custo mínimo calculado para um estado específico.
    
    Retorna:
        int: O custo total mínimo para visitar todas as cidades e retornar à cidade inicial.
    """
    if mascara == (1 << n) - 1:
        return custo[atual][0]

    if (atual, mascara) in memo:
        return memo[(atual, mascara)]

    ans = float('inf')  # Inicializar ans com infinito para garantir que qualquer custo encontrado será menor
    
    for proximo in range(n):
        if mascara & (1 << proximo) == 0:
            novo_custo = custo[atual][proximo] + custoTotal(mascara | (1 << proximo), proximo, n, custo, memo)
            ans = min(ans, novo_custo)

    memo[(atual, mascara)] = ans
    return ans