import os

def ler_matriz(file):
    """
    Lê uma matriz a partir de um arquivo.
    Argumentos:
        file (str): O caminho para o arquivo que contém a matriz.
    Retorna:
        list: Uma lista de listas de inteiros representando a matriz, ou
        imprime uma mensagem de erro se o arquivo não existir ou se ocorrer um erro ao ler o arquivo.
    """

    if not os.path.exists(file):
        print(f"Erro: O arquivo {file} não existe.")
        return None
    
    try:
        with open(file, 'r') as arq:
            matriz = []
            for linha in arq:
                matriz.append([int(x) for x in linha.split()])
        return matriz
    
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None
   
def caixeiroViajante(custo):
    """
    Resolve o problema do Caixeiro Viajante usando programação dinâmica.
    Este método calcula o custo mínimo para visitar todas as cidades exatamente uma vez e retornar à cidade de origem.
    Parâmetros:
        custo (matriz(lista de listas de int)): Uma matriz de custos onde custo[i][j] representa o custo de viajar da cidade i para a cidade j.
    Retorna:
        int: O custo mínimo para completar o percurso do Caixeiro Viajante.
    """
    
    n = len(custo)

    # Usar um dicionário para memoização
    memo = {}

    return custoTotal(1, 0, n, custo, memo)
 
def custoTotal(mascara, atual, n, custo, memo):
    """
    Calcula o custo total mínimo para visitar todas as cidades e retornar à cidade inicial.
    Parâmetros:
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

    ans = float('inf') # Inicializar ans com infinito para garantir que qualquer custo encontrado será menor
    
    for proximo in range(n):
        if mascara & (1 << proximo) == 0:
            novo_custo = custo[atual][proximo] + custoTotal(mascara | (1 << proximo), proximo, n, custo, memo)
            ans = min(ans, novo_custo)

    memo[(atual, mascara)] = ans
    return ans