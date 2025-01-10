import time
from aprox import tsp_aproximativo
from determ import tsp_deterministico

def main():
    """
    Função principal que executa o algoritmo do Caixeiro Viajante.
    Esta função lê uma matriz de um arquivo especificado, calcula e imprime
    a solução do problema do Caixeiro Viajante usando as funções 'tsp_deterministico'
    e 'tsp_aproximativo'. O arquivo de entrada deve estar localizado no diretório
    'matrizes' e deve ser especificado pelo caminho relativo 'matrizes/XXX.txt'.
    """
    arquivo = "matrizes/tsp1_2453.txt" # Caminho relativo para o arquivo de entrada, altere conforme necessário.
    
    começo = time.time()
    print("Resultado do TSP Determinístico:\t", tsp_deterministico(arquivo))
    fim = time.time()
    print(f"Tempo de execução:\t\t\t{fim - começo} segundos")
    
    começo = time.time()
    print("\nResultado do TSP Aproximativo:\t\t", tsp_aproximativo(arquivo))
    fim = time.time()
    print(f"Tempo de execução:\t\t\t{fim - começo} segundos")
    
    
if __name__ == "__main__":
    main()