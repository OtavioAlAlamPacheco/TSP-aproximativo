import time
from func import caixeiroViajante

def main():
    """
    Função principal que executa o algoritmo do Caixeiro Viajante.
    Esta função lê uma matriz de um arquivo especificado, calcula e imprime
    a solução do problema do Caixeiro Viajante usando a função `caixeiroViajante`.
    O arquivo de entrada deve estar localizado no diretório "matrizes" e deve
    ser especificado pelo caminho relativo "matrizes/XXX.txt".
    """
    
    começo = time.time()
    arquivo = "matrizes/tsp4_7013.txt" # Caminho relativo para o arquivo de entrada, altere conforme necessário.
    
    print("Resultado do TSP: ", caixeiroViajante(arquivo))
        
    fim = time.time()
    print(f"Tempo de execução: {fim - começo} segundos")
    
    
if __name__ == "__main__":
    main()