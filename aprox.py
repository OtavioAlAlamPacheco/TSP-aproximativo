
from funcs import ler_matriz
from kruskal import kruskal_algo

def pre_ordem(mst, v, visitado, caminho):
    """
    Realiza uma travessia em pré-ordem na árvore geradora mínima (MST) a partir de um vértice dado.

    Parâmetros:
        mst (vetor de tuplas tuples): Lista de arestas da árvore geradora mínima, onde cada aresta é representada por uma tupla (u, w, peso).
        v (int): Vértice inicial para a travessia.
        visitado (vetor de bool): Lista que mantém o controle dos vértices visitados.
        caminho (vetor de int): Lista que armazena a ordem dos vértices visitados durante a travessia.

    Retorna:
        None
    """
    visitado[v] = True
    caminho.append(v)
    for u, w, peso in mst:
        if u == v and not visitado[w]:
            pre_ordem(mst, w, visitado, caminho)
        elif w == v and not visitado[u]:
            pre_ordem(mst, u, visitado, caminho)


def tsp_aproximativo(arquivo):
    """
    Resolve o problema do caixeiro viajante (TSP) utilizando uma abordagem aproximativa.
    Esta função lê uma matriz de adjacência de um arquivo, constrói uma árvore geradora mínima (MST) 
    usando o algoritmo de Kruskal, realiza uma travessia em pré-ordem na MST para gerar um caminho 
    aproximado e calcula a soma das distâncias desse caminho.
    
    Parâmetros:
        arquivo (str): O caminho para o arquivo que contém a matriz de adjacência.
        
    Retorna:
        soma_caminho (int): A soma das distâncias do caminho aproximado gerado.
        caminho (vetor de int): Lista que armazena a ordem dos vértices visitados durante a travessia.
    """
    matriz = ler_matriz(arquivo)
    num_vertices = len(matriz)

    mst = kruskal_algo(matriz)
    visitado = [False] * num_vertices
    caminho = []

    pre_ordem(mst, 0, visitado, caminho)
    caminho.append(caminho[0])  # retornar ao ponto de partida
    soma_caminho = 0

    for i in range(len(caminho) - 1):
        soma_caminho += matriz[caminho[i]][caminho[i + 1]]
    
    return soma_caminho, caminho

  