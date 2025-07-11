# main.py - Versão para VS Code e execução local

import requests
import os
from PIL import Image
from io import BytesIO

# Função para limpar o terminal
def limpar_tela():
    # 'cls' para Windows, 'clear' para macOS/Linux
    os.system('cls' if os.name == 'nt' else 'clear')

# --- DEFINIÇÃO DAS CLASSES ---

class ObraDeArte:
    """Representa uma obra de arte genérica."""
    def __init__(self, titulo, artista_principal, id_objeto, url_imagem=None, data_criacao=None):
        self.titulo = titulo
        self.artista_principal = artista_principal
        self.id_objeto = id_objeto
        self.url_imagem = url_imagem
        self.data_criacao = data_criacao

    def __str__(self):
        return f'"{self.titulo}" por {self.artista_principal} ({self.data_criacao})'

    def exibir_informacoes(self):
        print("\n" + "=" * 40)
        print(f"Título: {self.titulo}")
        print(f"Artista: {self.artista_principal}")
        if self.data_criacao:
            print(f"Ano: {self.data_criacao}")
        print(f"ID do Objeto: {self.id_objeto}")
        print("=" * 40)

    def mostrar_imagem(self):
        """Busca a imagem e a exibe no visualizador de imagens padrão do SO."""
        if self.url_imagem:
            try:
                response = requests.get(self.url_imagem)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content))
                
                print("Abrindo a imagem em uma nova janela...")
                # .show() abre o visualizador de imagens padrão do sistema operacional
                img.show()

            except requests.exceptions.RequestException as e:
                print(f"Erro ao buscar a imagem: {e}")
        else:
            print("Esta obra não possui uma imagem disponível.")

class Pintura(ObraDeArte):
    """Representa uma Pintura, um tipo específico de ObraDeArte."""
    def __init__(self, titulo, artista_principal, id_objeto, url_imagem=None, data_criacao=None, tecnica=None, dimensoes=None):
        super().__init__(titulo, artista_principal, id_objeto, url_imagem, data_criacao)
        self.tecnica = tecnica
        self.dimensoes = dimensoes

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Detalhes Específicos da Pintura:")
        if self.tecnica:
            print(f"  Técnica: {self.tecnica}")
        if self.dimensoes:
            print(f"  Dimensões: {self.dimensoes}")
        print("-" * 40)

class ApiRijksmuseum:
    """Classe responsável pela comunicação com a API do Rijksmuseum."""
    def __init__(self, chave_api):
        self.base_url = "https://www.rijksmuseum.nl/api/en/collection"
        self.api_key = chave_api

    def _fazer_requisicao(self, params={}):
        request_params = {'key': self.api_key, 'format': 'json', **params}
        try:
            response = requests.get(self.base_url, params=request_params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Ocorreu um erro na comunicação com a API: {e}")
            return None

    def buscar_obras_por_artista(self, nome_artista, max_resultados=5):
        print(f"\nBuscando obras de '{nome_artista}'...")
        params = {'involvedMaker': nome_artista, 'p': 1, 'ps': max_resultados, 'imgonly': 'True', 'type': 'painting'}
        dados = self._fazer_requisicao(params)
        obras_encontradas = []
        if dados and dados['artObjects']:
            print(f"Encontradas {len(dados['artObjects'])} pinturas para '{nome_artista}'.") # Feedback para o usuário
            for item in dados['artObjects']:
                
                # --- LÓGICA DE DECISÃO ADICIONADA ---
                # Como filtramos por 'painting' na API, podemos instanciar a classe Pintura diretamente.
                # Isso garante que a sobreposição de método será utilizada.
                
                obra = Pintura(
                    titulo=item['title'],
                    artista_principal=item['principalOrFirstMaker'],
                    id_objeto=item['objectNumber'],
                    data_criacao=item.get('longTitle', '').split(', ')[-1],
                    url_imagem=item.get('webImage', {}).get('url'),
                    tecnica="Pintura (detalhes via API)", # Adicionamos um placeholder
                    dimensoes=None # A API de busca não fornece dimensões
                )
                obras_encontradas.append(obra)
        
        return obras_encontradas

# --- FUNÇÃO PRINCIPAL DA APLICAÇÃO ---

def main():
    """Função principal que executa o programa."""
    limpar_tela()
    api_key = input("Por favor, insira sua chave da API do Rijksmuseum: ")
    if not api_key:
        print("Chave de API inválida. Encerrando.")
        return
    
    api = ApiRijksmuseum(api_key)
    
    while True:
        limpar_tela()
        print("===== Explorador de Arte do Rijksmuseum =====")
        print("\n1. Buscar obras por artista")
        print("2. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome_artista = input("Digite o nome do artista: ")
            obras = api.buscar_obras_por_artista(nome_artista)

            if not obras:
                print(f"Nenhuma obra encontrada para '{nome_artista}'. Pressione Enter para continuar.")
                input()
                continue
            
            while True:
                limpar_tela()
                print(f"--- Obras encontradas para: {nome_artista} ---")
                for i, obra in enumerate(obras):
                    print(f"{i + 1}: {obra}")
                print("\nDigite 'v' para voltar ao menu principal.")
                
                detalhe_escolha = input("Escolha uma obra para ver detalhes: ")
                if detalhe_escolha.lower() == 'v':
                    break

                try:
                    num_obra = int(detalhe_escolha) - 1
                    if 0 <= num_obra < len(obras):
                        obra_selecionada = obras[num_obra]
                        limpar_tela()
                        obra_selecionada.exibir_informacoes()
                        obra_selecionada.mostrar_imagem()
                        input("\nPressione Enter para voltar à lista de obras...")
                    else:
                        print("Número inválido. Pressione Enter para tentar novamente.")
                        input()
                except ValueError:
                    print("Entrada inválida. Pressione Enter para tentar novamente.")
                    input()
        
        elif escolha == '2':
            print("Obrigado por usar o Explorador de Arte!")
            break
        else:
            print("Opção inválida. Pressione Enter para tentar novamente.")
            input()

# --- PONTO DE ENTRADA DO SCRIPT ---

if __name__ == "__main__":
    main()