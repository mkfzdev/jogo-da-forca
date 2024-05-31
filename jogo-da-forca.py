resposta = input("Digite alguma letra: ")
vida = 6
forca = 'amigao'
palavra = ['_'] * len(forca)

while vida > 0 and '_' in palavra:
    acertou = False
    for i, letter in enumerate(forca):
        if letter == resposta:
            palavra[i] = resposta
            acertou = True
    if acertou:
        print('\nAcertou, parabéns!')
    else:
        print('\nErrou')
        vida -= 1
        print(f"Vida restante: {vida}")

    print('Palavra:', ' '.join(palavra))
    if "_" not in palavra:
        print("\nVitória")
        break

    if vida == 0:
        print('\nA vida acabou')
        break


    resposta = input("\nDigite alguma letra: ")
