import unicodedata

# configuraçoes de texto criptografado e chave

TEXTO = "SEGURANCA"
CHAVE = "REDE"

# normalizando o texto
def normalizar(texto):
    #converte tudo para maiusculo
    texto = texto.upper()

    #remove os acentos
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn" 
    )

    #mantem somente as letras de A a Z, removendo espaços e numeros
    texto = "".join(
        caractere
        for caractere in texto
        if "A" <= caractere <= "Z"
    )

    return texto


#Substituiçao | Formula: C = (P + K + i) mod 26
def substituir(texto, chave):
    resultado = ""

    for i in range(len(texto)):
        letra_texto = texto[i]

        #faz a chave se repetir no tamanho da mensagem que sera criptografada
        letra_chave = chave[i % len(chave)]

        #converte as letras para os valores de 0 a 25 (mod 26)
        valor_texto = ord(letra_texto) - ord("A")
        valor_chave = ord(letra_chave) - ord("A")

        #Aplicando a formula de substituiçao
        valor_cifrado = (valor_texto + valor_chave + i) % 26

        #converte o numero novamente para uma letra
        letra_cifrada = chr(valor_cifrado + ord("A"))

        resultado += letra_cifrada

    return resultado


#Transposiçao
#o tamanho de cada bloco é definido pelo tamanho da chave
#blocos impares serao invertidos, blocos pares mantidos
def transpor(texto, tamanho_bloco):
    resultado = ""
    numero_bloco = 1

    for inicio in range(0, len(texto), tamanho_bloco):
        bloco = texto[inicio:inicio + tamanho_bloco]

        #se o numero do bloco for impar, inverte
        if numero_bloco % 2 != 0:
            bloco = bloco[::-1]

        resultado += bloco

        numero_bloco += 1

    return resultado


#Encriptaçao 
def encriptar(texto, chave):
    texto = normalizar(texto)
    chave = normalizar(chave)

    #impedindo que seja usada uma chave vazia
    if not chave:
        raise ValueError("A chave precisa possuir pelo menos uma letra.")

    #Primeira etapa: substituiçao
    texto_substituido = substituir(texto, chave)

    #Segunda etapa: Transposicao
    texto_cifrado = transpor(texto_substituido, len(chave))

    return texto, texto_substituido, texto_cifrado


#Executando
texto_normalizado, texto_substituido, texto_cifrado = encriptar(
    TEXTO,
    CHAVE
)

print("=== ENCRIPTADOR ===\n")
print("Texto original: ", TEXTO)
print("Chave: ", CHAVE)
print("Texto normalizado: ", texto_normalizado)
print("Texto substituido: ", texto_substituido)
print("Texto cifrado: ", texto_cifrado)

