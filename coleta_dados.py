import requests
import json
import pandas as pd


def fazer_carga_em_batches(palavras_chave):
    dados_armazenados = []  # Lista de dados armazenados
    
    # Carregar os dados do arquivo (se existir)
    try:
        with open("/home/airelribeiro/Desktop/Tudo/ada_engenharia_de_dados/extracao/extracao_projeto/dados_armazenados.json", 'r') as file:
            dados_antigos = json.load(file)
            dados_armazenados.extend(dados_antigos)
    except FileNotFoundError:
        pass

    for palavra_chave in palavras_chave:         
        # Busca na API com cada palavra-chave
        url = f'https://newsapi.org/v2/everything?q={palavra_chave}'
        response = requests.get(url, headers={"X-Api-Key": "528d65099fb24bf6a49142f9af54ed02"})
        data = json.loads(response.text)
        articles = data['articles']

        # Cria um conjunto das URLs dos artigos atuais
        urls_atuais = set(article['url'] for article in dados_armazenados)

        # Adiciona artigo por artigo se for novo
        for article in articles:
            if article['url'] not in urls_atuais:
                article['palavras_chave'] = [palavra_chave]
                dados_armazenados.append(article)
            else:
                article_existente = next((x for x in dados_armazenados if x['url'] == article['url']), None)
                article_existente['palavras_chave'].append(palavra_chave)

    # Salva os dados atualizados
    with open("/home/airelribeiro/Desktop/Tudo/ada_engenharia_de_dados/extracao/extracao_projeto/dados_armazenados.json", 'w') as file:
        json.dump(dados_armazenados, file, indent=4)

if __name__ == "__main__":
    palavras_chave = ['dna', 'rna']
    fazer_carga_em_batches(palavras_chave)
