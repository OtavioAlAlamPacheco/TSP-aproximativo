from funcs import tsp
   
def tsp_deterministico(arquivo):
    """
    Resolve o problema do Caixeiro Viajante usando programação dinâmica.
    
    Parâmetros:
        arquivo (str): O caminho para o arquivo que contém a matriz de custos.
    
    Retorna:
        int: O custo mínimo para completar o percurso do Caixeiro Viajante, ou
        None se ocorrer um erro ao ler o arquivo.
    """
    matriz, num_vertices = tsp(arquivo)

    # Usar um dicionário para memoização
    memo = {}

    return custoTotal(1, 0, num_vertices, matriz, memo)
 
def custoTotal(mascara, atual, num_vertices, custo, memo):
    """
    Calcula o custo total mínimo para visitar todas as cidades e retornar à cidade inicial.
    
    Parâmetros:
        mascara (int): Um inteiro que representa as cidades visitadas até o momento usando bits.
        atual (int): O índice da cidade atual.
        num_vertices (int): O número total de cidades.
        custo (matriz): Uma matriz 2D onde custo[i][j] representa o custo de viajar da cidade i para a cidade j.
        memo (dicionario): Um dicionário usado para memoização, onde memo[(atual, mascara)] armazena o custo mínimo calculado para um estado específico.
    
    Retorna:
        int: O custo total mínimo para visitar todas as cidades e retornar à cidade inicial.
    """
    if mascara == (1 << num_vertices) - 1:
        return custo[atual][0]

    if (atual, mascara) in memo:
        return memo[(atual, mascara)]

    ans = float('inf')  # Inicializar ans com infinito para garantir que qualquer custo encontrado será menor
    
    for proximo in range(num_vertices):
        if mascara & (1 << proximo) == 0:
            novo_custo = custo[atual][proximo] + custoTotal(mascara | (1 << proximo), proximo, num_vertices, custo, memo)
            ans = min(ans, novo_custo)

    memo[(atual, mascara)] = ans
    return ans