from func import ler_matriz, caixeiroViajante

def main():
    """
    Função principal que executa o algoritmo do Caixeiro Viajante.
    Esta função lê uma matriz de um arquivo especificado, imprime a matriz
    e, em seguida, calcula e imprime a solução do problema do Caixeiro Viajante
    usando a função `caixeiroViajante`.
    O arquivo de entrada deve estar localizado no diretório "matrizes" e deve
    ser especificado pelo caminho relativo "matrizes/".
    A função `ler_matriz` é utilizada para ler a matriz do arquivo e a função
    `caixeiroViajante` é utilizada para calcular a solução do problema.
    Returns:
        None
    """
    arquivo = "matrizes/tsp3_1194.txt" # Caminho relativo para o arquivo de entrada, altere conforme necessário.
    matriz = ler_matriz(arquivo)
    
    if matriz is not None:
        print(matriz)
        
    print(caixeiroViajante(matriz))
        
if __name__ == "__main__":
    main()