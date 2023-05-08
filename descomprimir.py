import struct
from trie import determinaCaractereUnpack


def descomprimirBytes(nomeArquivoLz78):
    with open(nomeArquivoLz78, 'rb') as arquivoBinario:
        numeroDeBytesPorInteiro = struct.unpack('B', arquivoBinario.read(1))[0]
        caractereUnpack = determinaCaractereUnpack(numeroDeBytesPorInteiro)
        lista = []
        lista.append((0, ''))

        while True:
            byte = arquivoBinario.read(numeroDeBytesPorInteiro)
            if not byte:
                break
            codigo = struct.unpack(caractereUnpack, byte)[0]
            # print(codigo)

            byte = arquivoBinario.read(1)
            if not byte:
                break
            caractere = byte.decode('utf-8')
            if (caractere == '~'):
                byte = arquivoBinario.read(2)
                if not byte:
                    break
                # caractere = struct.unpack('c', byte)[0].decode('utf-8')
                caractere = byte.decode('utf-8')
                # print(caractere)
            if (caractere == '^'):
                byte = arquivoBinario.read(3)
                if not byte:
                    break
                # caractere = struct.unpack('c', byte)[0].decode('utf-8')
                caractere = byte.decode('utf-8')

            # print(caractere)

            lista.append((codigo, caractere))
        # print(lista)
        return lista

def remontarTextoOriginal(lista):
    texto = ''
    cadeiaInvertida = ''
    for i in range(1, len(lista)):
        iAux = i

        while lista[iAux][0] != 0:
            cadeiaInvertida += lista[iAux][1]
            iAux = lista[iAux][0]

        cadeiaInvertida += lista[iAux][1]
        cadeia = cadeiaInvertida[::-1]
        # print(cadeia)
        texto += cadeia
        cadeiaInvertida = ''
    return texto

def escreverArquivoTxt(ArquivoSaida, texto):
    with open(ArquivoSaida, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)
