from funcs import tsp

class Subconjunto:
    def __init__(self, pai, rank):
        self.pai = pai
        self.rank = rank

def encontrar(subconjuntos, i):
    """
    Encontra o representante do conjunto ao qual o elemento i pertence.

    Este método utiliza a técnica de compressão de caminho para otimizar
    a busca do representante do conjunto. Se o pai do subconjunto i não
    for ele mesmo, a função é chamada recursivamente até encontrar o
    representante, e o pai do subconjunto i é atualizado para o representante
    encontrado.

    Parâmetros:
        subconjuntos (vetor): Lista de subconjuntos, onde cada subconjunto
        possui um atributo 'pai' que aponta para o pai do subconjunto.
        i (int): Índice do elemento cujo representante do conjunto será encontrado.

    Retorna:
        int: O índice do representante do conjunto ao qual o elemento i pertence.
    """
    if subconjuntos[i].pai != i:
        subconjuntos[i].pai = encontrar(subconjuntos, subconjuntos[i].pai)
    return subconjuntos[i].pai

def uniao(subconjuntos, x, y):
    """
    Realiza a união de dois subconjuntos em uma estrutura de dados de conjuntos disjuntos.
    
    Parâmetros:
        subconjuntos (list): Lista de subconjuntos, onde cada subconjunto é representado por um objeto que possui atributos 'pai' e 'rank'.
        x (int): Índice do primeiro elemento.
        y (int): Índice do segundo elemento.
        
    Retorna:
        None
    """
    raiz_x = encontrar(subconjuntos, x)
    raiz_y = encontrar(subconjuntos, y)

    if subconjuntos[raiz_x].rank < subconjuntos[raiz_y].rank:
        subconjuntos[raiz_x].pai = raiz_y
    elif subconjuntos[raiz_x].rank > subconjuntos[raiz_y].rank:
        subconjuntos[raiz_y].pai = raiz_x
    else:
        subconjuntos[raiz_y].pai = raiz_x
        subconjuntos[raiz_x].rank += 1

def kruskal(matriz):
    """
    Implementa o algoritmo de Kruskal para encontrar a Árvore Geradora Mínima (MST) de um grafo representado por uma matriz de adjacência.
    Argumentos:
        matriz (matriz): Matriz de adjacência representando o grafo, onde matriz[i][j] é o peso da aresta entre os vértices i e j. Um valor de 0 indica que não há aresta entre os vértices.
    Retorna:
        resultado (vetor de tuplas): Lista de arestas que compõem a MST. Cada aresta é representada por uma tupla (u, v, peso), onde u e v são os vértices conectados pela aresta e peso é o peso da aresta.
    """
    num_vertices = len(matriz)
    arestas = []

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if matriz[i][j] != 0:
                arestas.append((i, j, matriz[i][j]))

    arestas = sorted(arestas, key=lambda aresta: aresta[2])

    resultado = []
    subconjuntos = [Subconjunto(v, 0) for v in range(num_vertices)]

    e = 0
    i = 0
    while e < num_vertices - 1 and i < len(arestas):
        u, v, peso = arestas[i]
        i += 1
        x = encontrar(subconjuntos, u)
        y = encontrar(subconjuntos, v)

        if x != y:
            e += 1
            resultado.append((u, v, peso))
            uniao(subconjuntos, x, y)

    return resultado

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
        int: A soma das distâncias do caminho aproximado gerado.
    """
    matriz, num_vertices = tsp(arquivo)
    
    mst = kruskal(matriz)
    visitado = [False] * num_vertices
    caminho = []
    pre_ordem(mst, 0, visitado, caminho)
    caminho.append(caminho[0])  # Retornar ao ponto de partida
    
    soma_caminho = 0
    for i in range(len(caminho) - 1):
        soma_caminho += matriz[caminho[i]][caminho[i + 1]]

    return soma_caminho