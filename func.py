import os

# Crie uma função que leia uma matriz de um txt
def ler_matriz(file):
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

def main():
    arquivo = "matrizes/tsp1_253.txt"
    matriz = ler_matriz(arquivo)
    if matriz is not None:
        print(matriz)

if __name__ == "__main__":
    main()