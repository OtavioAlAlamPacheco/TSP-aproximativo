
import time
from aprox import tsp_aproximativo
from determ import tsp_deterministico

def main():
    """
    Função principal que executa os algoritmos do Caixeiro Viajante.
    A função lê uma matriz de custos de um arquivo, executa o algoritmo
    determinístico e o aproximativo do problema do Caixeiro Viajante, 
    e imprime o custo e o caminho resultante de ambos os métodos.
    O arquivo de entrada deve estar localizado no diretório 'matrizes'.
    """
    print(f"\n - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - \n")

    print(f"Digite o nome do arquivo (com extensão): ")
    arquivo = str(input())
    arquivo = "matrizes/" + arquivo
    
    print(f"\n - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - \n")
    
    começo = time.time()
    custo, caminho = tsp_deterministico(arquivo)
    print("Resultado do TSP Determinístico:")
    print(f"\tCusto -> {custo}")
    print(f"\tCaminho -> {caminho}")
    fim = time.time()
    print(f"\tTempo de execução: {fim - começo} segundos")
    
    print(f"\n - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - _ - \n")

    comeco = time.time()
    custo, caminho = tsp_aproximativo(arquivo)
    print("Resultado do TSP Aproximativo: ")
    print(f"\tCusto -> {custo}")
    print(f"\tCaminho -> {caminho}")
    fim = time.time()
    print(f"\tTempo de execução: {fim - comeco} segundos \n")


if __name__ == "__main__":
    main()
    