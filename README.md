# Projeto: Explorador de Arte do Rijksmuseum

Este projeto é uma aplicação de console desenvolvida em Python que permite aos usuários explorar a vasta coleção de pinturas do famoso Rijksmuseum em Amsterdã. A aplicação consome a API pública do museu para buscar obras por artista, exibir seus detalhes e visualizar as imagens das obras.

O principal objetivo deste projeto é demonstrar a aplicação prática dos conceitos fundamentais da Programação Orientada a Objetos (POO) em uma solução funcional e criativa.

## Funcionalidades

* Buscar pinturas pelo nome de um artista.
* Listar as obras encontradas de forma organizada no terminal.
* Visualizar informações detalhadas de uma obra específica.
* Exibir a imagem da obra de arte em uma **janela separada**, utilizando o visualizador de imagens padrão do sistema operacional.

## Tecnologias Utilizadas

* **Linguagem:** Python 3
* **API:** [Rijksmuseum API](https://data.rijksmuseum.nl/)
* **Bibliotecas de Terceiros (POO):**
    * `requests`: Para realizar requisições HTTP à API do Rijksmuseum.
    * `Pillow (PIL)`: Para processar e exibir as imagens das obras de arte.

## Como Executar e Utilizar (Ambiente Local)

Siga os passos abaixo para configurar e executar o projeto em um ambiente de desenvolvimento local como o Visual Studio Code.

### Pré-requisitos

1.  **Python 3:** É necessário ter o Python instalado. Certifique-se de que, durante a instalação, a opção "Add Python to PATH" foi marcada. [Baixar Python](https://www.python.org/downloads/).
2.  **Visual Studio Code:** Um editor de código. [Baixar VS Code](https://code.visualstudio.com/).
3.  **Chave de API (API Key):** É obrigatório ter uma chave da API do Rijksmuseum.
    * Crie uma conta gratuita no site do Rijksmuseum.
    * Após o login, acesse as configurações do seu perfil para encontrar e gerar sua chave de API.

### Passos para Execução

1.  **Clone ou baixe os arquivos** para uma pasta no seu computador.
2.  **Abra a pasta do projeto** no Visual Studio Code.
3.  **Abra o terminal integrado** no VS Code (atalho: `Ctrl+` \` ou menu `Exibir > Terminal`).
4.  **Crie um ambiente virtual** para isolar as dependências do projeto. No terminal, digite:
    ```bash
    python -m venv venv
    ```
5.  **Ative o ambiente virtual:**
    * No Windows:
        ```powershell
        .\venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
6.  **Instale as bibliotecas necessárias.** Com o ambiente ativo, execute:
    ```bash
    pip install requests Pillow
    ```
7.  **Execute o programa:**
    ```bash
    python main.py
    ```
8.  O programa solicitará sua **chave da API**. Cole-a e pressione Enter para iniciar.

## Exemplo de Uso no Terminal

Por favor, insira sua chave da API do Rijksmuseum: [usuário cola a chave aqui]

===== Explorador de Arte do Rijksmuseum =====

1. Buscar obras por artista
2. Sair
Escolha uma opção: 1

Digite o nome do artista: Johannes Vermeer

Buscando obras de 'Johannes Vermeer'...
Encontradas 5 pinturas para 'Johannes Vermeer'.

--- Obras encontradas para: Johannes Vermeer ---
1: "The Milkmaid" por Johannes Vermeer (c. 1660)
2: "View of Houses in Delft, Known as ‘The Little Street’" por Johannes Vermeer (c. 1658)
3: "The Love Letter" por Johannes Vermeer (c. 1669 - c. 1670)
...

Escolha uma obra para ver detalhes: 1

========================================
Título: The Milkmaid
Artista: Johannes Vermeer
Ano: c. 1660
ID do Objeto: SK-A-2344
========================================
Detalhes Específicos da Pintura:
  Técnica: Pintura (detalhes via API)
----------------------------------------
Abrindo a imagem em uma nova janela...

(Uma janela com a imagem da obra "A Leiteira" é aberta no computador.)

Pressione Enter para voltar à lista de obras...

## Demonstração dos Conceitos de POO

Este projeto foi estruturado para aplicar os seguintes conceitos de POO:

* **Classes e Objetos:**
    * `ObraDeArte`: Modela as características e comportamentos genéricos de uma obra.
    * `Pintura`: Modela um tipo específico de obra, a pintura.
    * `ApiRijksmuseum`: Modela o serviço de comunicação com a API, encapsulando a lógica de acesso a dados.

* **Herança:**
    * A classe `Pintura` herda da classe `ObraDeArte` (`class Pintura(ObraDeArte):`), reutilizando seus atributos e métodos e adicionando novos comportamentos específicos.

* **Sobreposição de Métodos (Override):**
    * O método `exibir_informacoes()` da classe `ObraDeArte` é sobreposto na classe filha `Pintura`. A nova versão chama a implementação da classe pai com `super()` e adiciona a exibição de informações extras, demonstrando polimorfismo na prática. A execução do código confirma este comportamento.

* **Sobrecarga de Métodos (Simulada):**
    * O construtor `__init__` da classe `ObraDeArte` utiliza parâmetros com valores padrão (ex: `url_imagem=None`). Isso permite que objetos sejam criados com diferentes conjuntos de argumentos, simulando a sobrecarga de construtores de forma idiomática em Python.

* **Encapsulamento:**
    * A classe `ApiRijksmuseum` encapsula toda a complexidade de interagir com a API (URL, parâmetros, tratamento de erros). O resto do programa não precisa saber *como* a API funciona, apenas como usar os métodos do objeto `ApiRijksmuseum`.