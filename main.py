import sys
import numpy as np
from trie import Trie
from descomprimir import descomprimirBytes, remontarTextoOriginal, escreverArquivoTxt

def main():
    opcaoEntrada = sys.argv[1]
    arquivoDeEntrada = sys.argv[2]
    opcaoSaida = ''
    arquivoSaida =''
    
    # for arg in sys.argv:
    #     print(arg)
    # print(len(sys.argv))

    if (len(sys.argv) > 3):
        opcaoSaida = sys.argv[3]
        arquivoSaida = sys.argv[4]
    
    # Define o nome do arquivo de saída
    if not arquivoSaida:
        if opcaoEntrada == '-c':
            arquivoSaida = arquivoDeEntrada[:-3] + 'z78'
        elif opcaoEntrada == '-x':
            arquivoSaida = arquivoDeEntrada[:-3] + 'txt'

    if opcaoEntrada == '-c':
        # Realiza a compressão do arquivo de entrada
        trie = Trie()
        numeroBytesParaInteiros = trie.insercaoParaContarBytesInteiros(arquivoDeEntrada)
        trie.inserirComprimindo(arquivoDeEntrada, arquivoSaida, numeroBytesParaInteiros)
        print(f'Arquivo comprimido: {arquivoDeEntrada} -> {arquivoSaida}')
    else:
        # Realiza a descompressão do arquivo de entrada
        lista = descomprimirBytes(arquivoDeEntrada)
        texto = remontarTextoOriginal(lista)
        escreverArquivoTxt(arquivoSaida, texto)
        print(f'Arquivo descomprimido: {arquivoDeEntrada} -> {arquivoSaida}')

if __name__ == '__main__':
    main()

