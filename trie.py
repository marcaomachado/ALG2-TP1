import math
import struct

def determinaCaractereUnpack(numeroBytes):
    if (numeroBytes == 1):     
        return 'B'
    if (numeroBytes == 2): 
        return 'H'
    if (numeroBytes == 4):
        return 'I'
    if (numeroBytes == 8):
        return 'Q'


class No:
    def __init__(self, codigo = 0):
        self.caractere = None
        self.codigo = codigo
        self.codigoPai = 0
        self.filho = {}

class Trie:
    def __init__(self):
        self.raiz = No()
        self.dSeq = 0

    def insercaoParaContarBytesInteiros(self, nomeArquivoEntrada):
        arquivoEntrada = open(nomeArquivoEntrada, 'r', encoding="utf-8")
        arquivo = arquivoEntrada.read()
        noAtual = self.raiz

        for caractere in arquivo:
            if caractere not in noAtual.filho:
                self.dSeq += 1
                noAtual.filho[caractere] = No(codigo = self.dSeq)
                noAtual = self.raiz
            else:
                noAtual = noAtual.filho[caractere]

        numeroDeBits = self.dSeq.bit_length()
        numeroDeBytes = math.ceil(numeroDeBits / 8)

        if (numeroDeBytes > 2 and numeroDeBytes <= 4):
            return 4
        elif (numeroDeBytes > 4 and numeroDeBytes <= 8):
            return 8
        else:
            return numeroDeBytes

    def inserirComprimindo(self, nomeArquivoEntrada, nomeArquivoSaida, numeroDeBytes):
        arquivoEntrada = open(nomeArquivoEntrada, 'r', encoding="utf-8")
        arquivo = arquivoEntrada.read()
        self.raiz = No()
        self.dSeq = 0
        noAtual = self.raiz
        caractereUnpack = determinaCaractereUnpack(numeroDeBytes)

        with open(nomeArquivoSaida, 'wb') as arquivoSaida:
            # Insere no primeiro byte do arquivo a quantidade de Bytes que o arquivo precisará para para armazenar os códigos
            inteiroCompactado = struct.pack('B', numeroDeBytes)
            arquivoSaida.write(inteiroCompactado)

            cadeia = ''
            for caractere in arquivo:
                if caractere not in noAtual.filho:
                    cadeia = ''
                    inteiroEmBytes = struct.pack(caractereUnpack, noAtual.codigo)
                    arquivoSaida.write(inteiroEmBytes)
                    if (len(caractere.encode('utf-8')) == 2):
                        til = '~'
                        arquivoSaida.write(til.encode('utf-8'))
                    if (len(caractere.encode('utf-8')) == 3):
                        circunflexo = '^'
                        arquivoSaida.write(circunflexo.encode('utf-8'))
                    arquivoSaida.write(caractere.encode('utf-8'))
                    self.dSeq += 1
                    noAtual.filho[caractere] = No(codigo = self.dSeq)
                    noAtual = self.raiz
                else:
                    codigoPai = noAtual.codigo
                    noAtual = noAtual.filho[caractere]
                    noAtual.codigoPai = codigoPai
                    cadeia += caractere
            if (cadeia != ''):
                inteiroEmBytes = struct.pack(caractereUnpack, noAtual.codigoPai)
                arquivoSaida.write(inteiroEmBytes)
                if (len(caractere.encode('utf-8')) == 2):
                    til = '~'
                    arquivoSaida.write(til.encode('utf-8'))
                if (len(caractere.encode('utf-8')) == 3):
                    circunflexo = '^'
                    arquivoSaida.write(circunflexo.encode('utf-8'))
                arquivoSaida.write(caractere.encode('utf-8'))
