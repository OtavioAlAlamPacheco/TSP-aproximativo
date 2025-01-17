
from funcs import ler_matriz
   
def tsp_deterministico(arquivo):
    """
    Resolve o problema do Caixeiro Viajante usando programação dinâmica.
    
    Parâmetros:
        arquivo (str): O caminho para o arquivo que contém a matriz de custos.
    
    Retorna:
        custo (int): O custo mínimo para completar o percurso do Caixeiro Viajante, ou None se ocorrer um erro ao ler o arquivo.
        caminhos(dict): O caminho percorrido, armazenando os nodos visitados na ordem.
    """
    matriz = ler_matriz(arquivo)
    num_vertices = len(matriz)
    memo = {}       # dicionário para memoização dos nodos visitados
    caminhos = {}   # dicionário para memoização dos caminhos

    custo, caminho = custoTotal(1, 0, num_vertices, matriz, memo, caminhos)
    caminho = [0] + caminho + [0]

    return custo, caminho
 

def custoTotal(mascara, atual, num_vertices, custo, memo, caminhos):
    """
    Calcula o custo total mínimo para visitar todas as cidades e retornar à cidade inicial, e armazena os nodos percorridos.
    
    Parâmetros:
        mascara (int): Um inteiro que representa as cidades visitadas até o momento usando bits.
        atual (int): O índice da cidade atual.
        num_vertices (int): O número total de cidades.
        custo (matriz): Uma matriz 2D onde custo[i][j] representa o custo de viajar da cidade i para a cidade j.
        memo (dict): Um dicionário usado para memoização, onde memo[(atual, mascara)] armazena o custo mínimo calculado para um estado específico.
        caminhos (dict): Um dicionário usado para memoização, onde caminhos[(atual, mascara)] representa um nodo percorrido.
        
    Retorna:
        custo (int): O custo total mínimo para visitar todas as cidades e retornar à cidade inicial.
        caminhos (dict): O caminho percorrido, armazenando os nodos visitados.
    """
    if mascara == (1 << num_vertices) - 1:
        return custo[atual][0], []
    
    if (atual, mascara) in memo:
        return memo[(atual, mascara)], caminhos[(atual, mascara)]
    
    custo_final = float('inf')      # infinito, para ser substituído por qualquer valor
    melhor_caminho = []
    
    for proximo in range(num_vertices):
        if mascara & (1 << proximo) == 0:   # "se a cidade já foi visitada"
            novo_custo, subcaminho = custoTotal(mascara | (1 << proximo), proximo, num_vertices, custo, memo, caminhos)
            novo_custo += custo[atual][proximo]

            if novo_custo < custo_final:  # "se encontramos um custo menor"
                custo_final = novo_custo
                melhor_caminho = [proximo] + subcaminho

    memo[(atual, mascara)] = custo_final
    caminhos[(atual, mascara)] = melhor_caminho

    return custo_final, melhor_caminho
