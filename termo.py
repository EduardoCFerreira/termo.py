numero_tentativas = 0
letras_acertadas = ''

while True:
    palavra = input('Digite uma palavra de 5 caracteres: ')

    tamanho_palavra = len(palavra)

    if tamanho_palavra == 5:
        print('Sua palvra foi aceita')
    else:
        print('Digite apenas palvras com 5 caracteres!')
        continue
    while True:
        letra = input('Digite apenas uma letra: ')
        numero_tentativas += 1

        tamanho_letra = len(letra)

        if tamanho_letra > 1:
            print('Digite apenas uma letra!')
            continue
        
        if letra in palavra:
            letras_acertadas += letra

        palavra_formada = ''
        for letra_secreta in palavra:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'
        print(palavra_formada)

        if palavra_formada == palavra:
            print('Você acertou!!')
            print(f'Suas tentativas foram: {numero_tentativas}x')
            letras_acertadas = ''
            numero_tentativas = 0