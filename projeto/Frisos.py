# coding: utf-8

#IMPORTS#

import numpy as np
import cv2 as cv

#FUNÇÕES#
#===========================================================#

def geraNome(string):
    nome = (string.split("/"))[-1]
    nome = (nome.split("."))[0]

    return str(nome)


def espelhaImagem(imagem, eixo):
    if eixo == "Horizontal":
        return cv.flip(cv.flip(imagem, -1), 1)

    if eixo == "Vertical":
        return cv.flip(imagem, 1)


def rotacionaImagem(imagem, angulo, escala):
    ponto = ((imagem.shape[1] - 1) / 2, (imagem.shape[0] - 1) / 2)

    rotacao = cv.getRotationMatrix2D(ponto, angulo, escala)

    return cv.warpAffine(imagem, rotacao, (imagem.shape[1], imagem.shape[0]))


def exibeImagem(msg, imagem):
    cv.imshow(msg, imagem)
    cv.waitKey(0)
    cv.destroyAllWindows()


"""
Translação
"""


def frizo1(imagem, repeticoes):
    altura = imagem.shape[0]
    largura = imagem.shape[1]

    frizo = (np.ones((altura, largura * repeticoes, 3)) * 255).astype(np.uint8)

    aux_l = 0

    for i in range(repeticoes):
        frizo[0:altura - 1, aux_l:aux_l + largura - 1] = imagem[0:altura - 1, 0:largura - 1]

        aux_l += largura

    return frizo


"""
Reflexao Vertical
"""


def frizo2(imagem, repeticoes):
    altura = imagem.shape[0]
    largura = imagem.shape[1]

    frizo = (np.ones((altura, largura * repeticoes, 3)) * 255).astype(np.uint8)

    aux_l = 0

    for i in range(repeticoes):
        frizo[0:altura - 1, aux_l:aux_l + largura - 1] = imagem[0:altura - 1, 0:largura - 1]

        imagem = espelhaImagem(imagem, "Vertical")

        aux_l += largura

    return frizo


"""
Reflexão Horizontal com translação
"""


def frizo3(imagem, repeticoes):
    altura = imagem.shape[0]
    largura = imagem.shape[1]

    frizo = (np.ones((altura * 2, largura * repeticoes, 3)) * 255).astype(np.uint8)

    espelhadaH = espelhaImagem(imagem, "Horizontal")

    aux_l = 0

    for i in range(repeticoes):
        frizo[0:altura - 1, aux_l:aux_l + largura - 1] = imagem[0:altura - 1, 0:largura - 1]

        frizo[altura:altura * 2 - 1, aux_l:aux_l + largura - 1] = espelhadaH[0:altura - 1, 0:largura - 1]

        aux_l += largura

    return frizo


"""
Reflexao Deslizante
"""


def frizo4_1(imagem, repeticoes):
    altura = imagem.shape[0]
    largura = imagem.shape[1]

    frizo = (np.ones((altura, largura * repeticoes, 3)) * 255).astype(np.uint8)

    aux_l = 0

    for i in range(repeticoes):
        frizo[0:altura - 1, aux_l:aux_l + largura - 1] = imagem[0:altura - 1, 0:largura - 1]

        imagem = espelhaImagem(imagem, "Horizontal")

        aux_l += largura

    return frizo


"""
Reflexao Deslizante
"""


def frizo4_2(imagem, repeticoes):
    altura = imagem.shape[0]
    largura = imagem.shape[1]

    frizo = (np.ones((altura * 2, largura * repeticoes, 3)) * 255).astype(np.uint8)

    espelhadaH = espelhaImagem(imagem, "Horizontal")

    aux_l = 0

    for i in range(repeticoes):
        if i % 2 == 0:
            frizo[0:altura - 1, aux_l:aux_l + largura - 1] = imagem[0:altura - 1, 0:largura - 1]

        else:
            frizo[altura:altura * 2 - 1, aux_l:aux_l + largura - 1] = espelhadaH[0:altura - 1, 0:largura - 1]

        aux_l += largura

    return frizo


"""
Reflexão deslizante e vertical
"""


def frizo5(imagem, repeticoes):
    altura = imagem.shape[0]
    largura = imagem.shape[1]

    frizo = (np.ones((altura * 2, largura * repeticoes, 3)) * 255).astype(np.uint8)

    espelhadaV = espelhaImagem(imagem, "Vertical")
    espelhadaH = espelhaImagem(imagem, "Horizontal")
    duplaEspelhada = rotacionaImagem(imagem, 180, 1.0)

    aux_l = 0

    for i in range(repeticoes):
        if i % 2 == 0:
            frizo[0:altura - 1, aux_l:aux_l + largura - 1] = imagem[0:altura - 1, 0:largura - 1]

            frizo[altura:altura * 2 - 1, aux_l:aux_l + largura - 1] = duplaEspelhada[0:altura - 1, 0:largura - 1]

        else:
            frizo[0:altura - 1, aux_l:aux_l + largura - 1] = espelhadaV[0:altura - 1, 0:largura - 1]

            frizo[altura:altura * 2 - 1, aux_l:aux_l + largura - 1] = espelhadaH[0:altura - 1, 0:largura - 1]

        aux_l += largura

    return frizo


"""
Reflexão vertical e horizontal
"""


def frizo6(imagem, repeticoes):
    altura = imagem.shape[0]
    largura = imagem.shape[1]

    frizo = (np.ones((altura * 2, largura * repeticoes, 3)) * 255).astype(np.uint8)

    espelhadaV = espelhaImagem(imagem, "Vertical")
    espelhadaH = espelhaImagem(imagem, "Horizontal")
    duplaEspelhada = rotacionaImagem(imagem, 180, 1.0)

    aux_l = 0

    for i in range(repeticoes):
        if i % 2 == 0:
            frizo[0:altura - 1, aux_l:aux_l + largura - 1] = imagem[0:altura - 1, 0:largura - 1]

            frizo[altura:altura * 2 - 1, aux_l:aux_l + largura - 1] = espelhadaH[0:altura - 1, 0:largura - 1]

        else:
            frizo[0:altura - 1, aux_l:aux_l + largura - 1] = espelhadaV[0:altura - 1, 0:largura - 1]

            frizo[altura:altura * 2 - 1, aux_l:aux_l + largura - 1] = duplaEspelhada[0:altura - 1, 0:largura - 1]

        aux_l += largura

    return frizo


"""
Simetria de rotação
"""


def frizo7(imagem, repeticoes, anguloRotacao=180):
    altura = imagem.shape[0]
    largura = imagem.shape[1]

    frizo = (np.ones((altura, largura * repeticoes, 3)) * 255).astype(np.uint8)

    aux_l = 0

    for i in range(repeticoes):
        frizo[0:altura - 1, aux_l:aux_l + largura - 1] = imagem[0:altura - 1, 0:largura - 1]

        imagem = rotacionaImagem(imagem, anguloRotacao, 1.0)

        aux_l += largura

    return frizo


'''
Main do programa
'''


def main():
    while True:
        entrada = input("Digite o diretório da imagem: ")

        img = cv.imread(entrada)

        if img is None:
            print("\nDiretório ou imagem inexistente.")

        else:
            break

    while True:
        try:
            qtd_vezes = int(input("Digite a quantidade de vezes que a imagem deve se repetir: "))

            if qtd_vezes < 2 or qtd_vezes > 30:
                raise ValueError('')

            break

        except ValueError:
            print("\nValor inválido.")

    while True:
        try:
            angulo = int(input("Digite um ângulo de rotação multiplo de 90 (em graus): "))

            if angulo % 90 != 0:
                raise ValueError('')

            break

        except ValueError:
            print("\nValor inválido.")

    frizo_1 = frizo1(img, qtd_vezes)
    frizo_2 = frizo2(img, qtd_vezes)
    frizo_3 = frizo3(img, qtd_vezes)
    frizo_4_1 = frizo4_1(img, qtd_vezes)
    frizo_4_2 = frizo4_2(img, qtd_vezes)
    frizo_5 = frizo5(img, qtd_vezes)
    frizo_6 = frizo6(img, qtd_vezes)
    frizo_7 = frizo7(img, qtd_vezes, angulo)

    print("\nO que você deseja fazer?")
    print(
        "1. Gerar arquivos dos frizos (1)  |  2. Exibir frizos sem gerar arquivos (2)  |  3. Exibir frizos e gerar arquivos (3)")

    opcao = str(input(""))

    while opcao != "1" and opcao != "2" and opcao != "3":
        print("\nValor inválido.")
        print("O que você deseja fazer?")
        print(
            "1. Gerar arquivos dos frizos  |  2. Exibir frizos sem gerar arquivos  |  3. Exibir frizos e gerar arquivos")
        opcao = str(input(""))

    if opcao == "1" or opcao == "3":
        print("\nQual formato de imagem você deseja salvar?")
        print("1. JPG  |  2. PNG")
        formato = str(input(""))

        while formato != "1" and formato != "2":
            print("\nValor inválido.")
            print("Qual formato de imagem você deseja salvar?")
            print("1. JPG  |  2. PNG")
            formato = str(input(""))

        if formato == "1":
            formato = ".jpg"

        if formato == "2":
            formato = ".png"

        cv.imwrite((geraNome(entrada) + "_FRIZO_TRANSLACAO" + formato), frizo_1)
        cv.imwrite((geraNome(entrada) + "_FRIZO_REFLEXAO_VERTICAL" + formato), frizo_2)
        cv.imwrite((geraNome(entrada) + "_FRIZO_REFLEXAO_HORIZONTAL_+_TRANSLACAO" + formato), frizo_3)
        cv.imwrite((geraNome(entrada) + "_FRIZO_REFLEXAO_DESLIZANTE_1" + formato), frizo_4_1)
        cv.imwrite((geraNome(entrada) + "_FRIZO_REFLEXAO_DESLIZANTE_2" + formato), frizo_4_2)
        cv.imwrite((geraNome(entrada) + "_FRIZO_REFLEXAO_DESLIZANTE_E_VERTICAL" + formato), frizo_5)
        cv.imwrite((geraNome(entrada) + "_FRIZO_REFLEXAO_VERTICAL_E_HORIZONTAL" + formato), frizo_6)
        cv.imwrite((geraNome(entrada) + "_FRIZO_TRANSLACAO_COM_ROTACAO" + formato), frizo_7)

    if opcao == "2" or opcao == "3":
        exibeImagem("Imagem", img)
        exibeImagem("Frizo1", frizo_1)
        exibeImagem("Frizo2", frizo_2)
        exibeImagem("Frizo3", frizo_3)
        exibeImagem("Frizo4_1", frizo_4_1)
        exibeImagem("Frizo4_2", frizo_4_2)
        exibeImagem("Frizo5", frizo_5)
        exibeImagem("Frizo6", frizo_6)
        exibeImagem("Frizo7", frizo_7)


main()
