# 🔐 Encriptador e Decriptador em Python

Projeto desenvolvido em **Python** com o objetivo de implementar um algoritmo próprio de criptografia simétrica utilizando conceitos clássicos de **substituição** e **transposição**.

O algoritmo combina uma substituição com deslocamento variável, determinada por uma chave e pela posição de cada caractere, com uma etapa de transposição alternada por blocos.

> **Observação:** este projeto possui finalidade acadêmica e didática. O algoritmo desenvolvido não deve ser utilizado para proteção de informações reais ou sensíveis.

---

## 📚 Sobre o projeto

O projeto é composto por duas aplicações independentes:

* 🔒 **Encriptador:** recebe um texto claro e uma chave e gera o texto cifrado.
* 🔓 **Decriptador:** recebe o texto cifrado e a mesma chave e recupera o texto claro.

O algoritmo utiliza uma combinação de duas técnicas clássicas:

1. **Substituição**
2. **Transposição**

A estratégia foi modificada para criar um algoritmo próprio, em vez de implementar diretamente uma cifra clássica existente.

---

## ⚙️ Funcionamento

O processo de encriptação ocorre em duas etapas principais:

```text
Texto claro
    ↓
Normalização
    ↓
Substituição variável
    ↓
Transposição alternada por blocos
    ↓
Texto cifrado
```

A decriptação realiza o processo inverso:

```text
Texto cifrado
    ↓
Reversão da transposição
    ↓
Reversão da substituição
    ↓
Texto claro
```

---

## 🧹 Normalização

Antes da encriptação, o texto e a chave são normalizados.

As seguintes regras são aplicadas:

* conversão para letras maiúsculas;
* remoção de espaços;
* remoção de números;
* remoção de acentos;
* conversão de `Ç` para `C`;
* utilização apenas das letras de `A` até `Z`.

### Exemplo

Entrada:

```text
Segurança da Informação
```

Após a normalização:

```text
SEGURANCADAINFORMACAO
```

O algoritmo não diferencia letras maiúsculas de minúsculas.

---

## 🔑 Chave

O algoritmo utiliza uma chave textual compartilhada entre o encriptador e o decriptador.

Caso a chave seja menor que o texto, ela é repetida automaticamente até atingir o tamanho necessário.

### Exemplo

Texto:

```text
SEGURANCA
```

Chave:

```text
REDE
```

A chave utilizada durante o processamento será equivalente a:

```text
Texto: SEGURANCA
Chave: REDEREDER
```

A chave original continua sendo apenas `REDE`. A repetição é realizada internamente pelo algoritmo.

---

## 🔄 Substituição

Cada letra do alfabeto é representada por um número entre `0` e `25`:

```text
A = 0
B = 1
C = 2
...
Z = 25
```

Diferentemente de uma cifra de deslocamento fixo, o algoritmo utiliza um deslocamento variável.

Para cada caractere, são considerados:

* `P` — valor da letra do texto claro;
* `K` — valor da letra correspondente da chave;
* `i` — posição do caractere no texto;
* `C` — valor do caractere cifrado.

A fórmula utilizada na encriptação é:

```text
C = (P + K + i) mod 26
```

Dessa forma, o deslocamento não depende somente da chave, mas também da posição do caractere na mensagem.

Isso permite que ocorrências de uma mesma letra possam produzir caracteres cifrados diferentes.

---

## 🔀 Transposição

Após a substituição, o resultado é dividido em blocos.

O **tamanho de cada bloco é determinado pelo tamanho da chave**.

Com a chave:

```text
REDE
```

o tamanho dos blocos será:

```text
4
```

A transposição segue uma regra alternada:

* blocos **ímpares** permanecem na ordem original;
* blocos **pares** são invertidos.

### Exemplo

Após a substituição:

```text
JJLBMJWNZ
```

Divisão em blocos:

```text
JJLB | MJWN | Z
```

Aplicação da transposição:

```text
Bloco 1 → JJLB → JJLB
Bloco 2 → MJWN → NWJM
Bloco 3 → Z    → Z
```

Resultado:

```text
JJLB | NWJM | Z
```

Texto cifrado:

```text
JJLBNWJMZ
```

---

## 🔒 Exemplo completo de encriptação

Considere:

```text
Texto: SEGURANCA
Chave: REDE
```

A chave é repetida:

```text
Texto:  S E G U R A N C A
Chave:  R E D E R E D E R
Índice: 0 1 2 3 4 5 6 7 8
```

Aplicando:

```text
C = (P + K + i) mod 26
```

é obtido:

```text
JJLBMJWNZ
```

Em seguida, são criados os blocos:

```text
JJLB | MJWN | Z
```

Os blocos ímpares são mantidos e os blocos pares são invertidos:

```text
JJLB | NWJM | Z
```

Portanto:

```text
Texto claro:   SEGURANCA
Chave:         REDE
Texto cifrado: JJLBNWJMZ
```

---

## 🔓 Decriptação

O processo de decriptação utiliza a **mesma chave**.

Primeiramente, é desfeita a transposição.

Texto recebido:

```text
JJLBNWJMZ
```

Divisão em blocos:

```text
JJLB | NWJM | Z
```

Aplicando novamente a regra de transposição:

```text
JJLB → JJLB
NWJM → MJWN
Z    → Z
```

Resultado intermediário:

```text
JJLBMJWNZ
```

Depois é aplicada a fórmula inversa da substituição:

```text
P = (C - K - i) mod 26
```

Obtendo novamente:

```text
SEGURANCA
```

Portanto:

```text
JJLBNWJMZ + REDE
        ↓
    SEGURANCA
```

---

## 🧮 Teste de mesa

| Posição | Texto |  P | Chave |  K | Operação               | Resultado |
| ------: | :---: | -: | :---: | -: | ---------------------- | :-------: |
|       0 |   S   | 18 |   R   | 17 | `(18 + 17 + 0) mod 26` |     J     |
|       1 |   E   |  4 |   E   |  4 | `(4 + 4 + 1) mod 26`   |     J     |
|       2 |   G   |  6 |   D   |  3 | `(6 + 3 + 2) mod 26`   |     L     |
|       3 |   U   | 20 |   E   |  4 | `(20 + 4 + 3) mod 26`  |     B     |
|       4 |   R   | 17 |   R   | 17 | `(17 + 17 + 4) mod 26` |     M     |
|       5 |   A   |  0 |   E   |  4 | `(0 + 4 + 5) mod 26`   |     J     |
|       6 |   N   | 13 |   D   |  3 | `(13 + 3 + 6) mod 26`  |     W     |
|       7 |   C   |  2 |   E   |  4 | `(2 + 4 + 7) mod 26`   |     N     |
|       8 |   A   |  0 |   R   | 17 | `(0 + 17 + 8) mod 26`  |     Z     |

Resultado da substituição:

```text
JJLBMJWNZ
```

Divisão em blocos:

```text
JJLB | MJWN | Z
```

Aplicação da transposição:

```text
Bloco 1 (ímpar) → mantém  → JJLB
Bloco 2 (par)   → inverte → NWJM
Bloco 3 (ímpar) → mantém  → Z
```

Após a transposição:

```text
JJLBNWJMZ
```

---

## 📁 Estrutura do projeto

```text
.
├── encriptador.py
├── decriptador.py
└── README.md
```

### `encriptador.py`

Responsável por:

* normalizar o texto;
* normalizar a chave;
* realizar a substituição;
* realizar a transposição;
* exibir o texto cifrado.

### `decriptador.py`

Responsável por:

* receber o texto cifrado;
* desfazer a transposição;
* aplicar a substituição inversa;
* recuperar o texto claro.

---

## ▶️ Como executar

É necessário possuir o **Python 3** instalado.

Clone o repositório e acesse a pasta do projeto.

Para executar o encriptador:

```bash
python encriptador.py
```

Para executar o decriptador:

```bash
python decriptador.py
```

---

## ✏️ Alterando texto e chave

No arquivo `encriptador.py`, altere:

```python
TEXTO = "SEGURANCA"
CHAVE = "REDE"
```

Por exemplo:

```python
TEXTO = "CRIPTOGRAFIA"
CHAVE = "SENHA"
```

Após executar o programa, copie o texto cifrado gerado.

No arquivo `decriptador.py`, informe o texto cifrado e utilize **a mesma chave**:

```python
TEXTO_CIFRADO = "..."
CHAVE = "SENHA"
```

Se a chave estiver correta, o texto original normalizado será recuperado.

---

## 🧠 Características do algoritmo

O algoritmo combina diferentes elementos:

* criptografia simétrica;
* chave textual;
* repetição automática da chave;
* substituição com deslocamento variável;
* influência da posição do caractere;
* aritmética modular;
* transposição por blocos;
* alternância entre blocos mantidos e invertidos;
* processo reversível de encriptação e decriptação.

A utilização da posição do caractere faz com que a substituição não utilize um único deslocamento constante durante toda a mensagem.

Além disso, a etapa de transposição modifica a posição dos caracteres após a substituição. Os blocos ímpares são mantidos em sua ordem original, enquanto os blocos pares são invertidos.

---

## 🔍 Criptoanálise

O projeto também permite estudar técnicas de **criptoanálise**.

Um atacante que possua apenas o texto cifrado pode tentar identificar:

* padrões de repetição;
* tamanho e comportamento da chave;
* periodicidade;
* frequência dos caracteres;
* padrão utilizado na transposição;
* relação entre posição e deslocamento.

Apesar de apresentar maior complexidade que uma cifra de deslocamento fixo simples, o algoritmo foi desenvolvido para **fins educacionais** e não possui as garantias de segurança oferecidas por algoritmos criptográficos modernos.

---

## 🛠️ Tecnologias utilizadas

* **Python 3**
* Biblioteca padrão `unicodedata`

Não são utilizadas bibliotecas externas de criptografia. As operações de substituição e transposição são implementadas diretamente no projeto.

---

## 🎓 Finalidade acadêmica

Este projeto foi desenvolvido como atividade prática para estudo de conceitos relacionados a:

* criptografia simétrica;
* substituição;
* transposição;
* chaves criptográficas;
* aritmética modular;
* encriptação e decriptação;
* criptoanálise;
* ataques por força bruta.

O objetivo é compreender o funcionamento de técnicas clássicas de criptografia por meio da implementação e modificação de estratégias estudadas em sala de aula.

---

## ⚠️ Aviso

Este algoritmo **não deve ser utilizado para proteger senhas, documentos, dados pessoais ou qualquer informação sensível**.

Ele foi desenvolvido exclusivamente para **estudo e demonstração de conceitos de criptografia**.

---

## 👥 Colaboradores

Este projeto foi desenvolvido por:

* [**Gabriel Mussatto**](https://github.com/GabrielMussatto)
* [**Erick Meneses**](https://github.com/MenesesErick)
