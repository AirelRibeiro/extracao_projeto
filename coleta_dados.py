import requests
import json
import os

class CargaDeDados:
    def __init__(self):
        self.dados_armazenados = []

    def carregar_dados_antigos(self, file_path):
        try:
            with open(file_path, 'r') as file:
                dados_antigos = json.load(file)
                self.dados_armazenados.extend(dados_antigos)
        except FileNotFoundError:
            pass

    def limpar_dados(self, article, palavra_chave):
        return {
            "source": article.get('source', {}).get('name', 'string'),
            "author": article.get('author', 'string'),
            "title": article.get('title', 'string'),
            "description": article.get('description', 'string'),
            "url": article.get('url', 'string'),
            "publishedAt": article.get('publishedAt', 'string'),
            "content": article.get('content', 'string'),
            "palavras_chave": palavra_chave
        }

    def fazer_carga_em_batches(self, palavras_chave):
        for palavra_chave in palavras_chave:
            # Busca na API com cada palavra-chave
            url = f'https://newsapi.org/v2/everything?q={palavra_chave}'
            response = requests.get(url, headers={"X-Api-Key": "528d65099fb24bf6a49142f9af54ed02"})
            data = json.loads(response.text)
            articles = data['articles']

            # Cria um conjunto das URLs dos artigos atuais
            urls_atuais = set(article['url'] for article in self.dados_armazenados)

            # Adiciona artigo por artigo se for novo
            for article in articles:
                if article['url'] not in urls_atuais:
                    article_cleaned = self.limpar_dados(article, palavra_chave)
                    self.dados_armazenados.append(article_cleaned)
                else:
                    article_existente = next((x for x in self.dados_armazenados if x['url'] == article['url']), None)
                    article_existente['palavras_chave'] += f', {palavra_chave}'

    # Salva os dados atualizados
    def salvar_dados(self, file_path):
        with open(file_path, 'w') as file:
            json.dump(self.dados_armazenados, file, indent=4)

if __name__ == "__main__":
    file_path = f"{os.getcwd()}/database/dados_armazenados.json"
    palavras_chave = ['dna', 'rna']

    carga_dados = CargaDeDados()
    carga_dados.carregar_dados_antigos(file_path)
    carga_dados.fazer_carga_em_batches(palavras_chave)
    carga_dados.salvar_dados(file_path)




