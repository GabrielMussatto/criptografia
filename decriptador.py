import unicodedata

# Configuracoes do texto cifrado e da chave
TEXTO_CIFRADO = "BLJJMJWNZ"
CHAVE = "REDE"

# normalizando o texto
def normalizar(texto):
    #convertendo tudo para maiusculo
    texto = texto.upper()

    #removendo os acentos
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    # mantendo as letras de A a Z
    texto = "".join(
        caractere
        for caractere in texto
        if "A" <= caractere <= "Z"
    )

    return texto

#Transposicao
# o tamanho de cada bloco é definido pelo tamanho da chave
#blocos impares serao invertidos, blocos pares mantidos
def transpor(texto, tamanho_bloco):
    resultado = ""
    numero_bloco = 1

    for inicio in range(0, len(texto), tamanho_bloco):
        bloco = texto[inicio:inicio + tamanho_bloco]

        #se o numero do bloco for impar, inverte
        if numero_bloco %2 != 0:
            bloco = bloco[::-1]

        resultado += bloco

        numero_bloco += 1

    return resultado

#Decriptacao da substituicao | Formula: P = (C - K - i) mod 26
def desfazer_substituicao(texto, chave):
    resultado = ""

    for i in range(len(texto)):
        letra_cifrada = texto[i]

        #faz a chave se repetir no tamanho da mensagem
        letra_chave = chave[i % len(chave)]

        #converte as letras para valores de 0 a 25 (mod 26)
        valor_cifrado = ord(letra_cifrada) - ord("A")
        valor_chave = ord(letra_chave) - ord("A")

        #aplica a formula inversa da substituicao
        valor_original = (valor_cifrado - valor_chave - i) % 26

        #converte o numero novamente para letra
        letra_original = chr(valor_original + ord("A"))

        resultado += letra_original

    return resultado

#Decriptacao
def decriptar(texto_cifrado, chave):
    texto_crifrado = normalizar(texto_cifrado)
    chave = normalizar(chave)

    #impede que uma chave vazia seja utilizada
    if not chave:
        raise ValueError("A chave precisa possuir pelo menos uma letra.")

    #Primeira etapa: desfazendo a transposicao
    texto_sem_transposicao = transpor(texto_cifrado, (len(chave)))

    #Segunda etapa: desfazendo a substituicao
    texto_original = desfazer_substituicao(texto_sem_transposicao, chave)

    return texto_cifrado, texto_sem_transposicao, texto_original

#Executando
texto_cifrado, texto_sem_transposicao, texto_original = decriptar(
    TEXTO_CIFRADO,
    CHAVE
)

print("=== DECRIPTADOR ===\n")
print("Texto cifrado: ", texto_cifrado)
print("Chave: ", CHAVE)
print("Após desfazer transposição: ", texto_sem_transposicao)
print("Texto decriptado: ", texto_original)