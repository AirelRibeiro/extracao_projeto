import json
import pandas as pd
from collections import defaultdict


class TransformadorDados:
    def __init__(self, palavras_chave):
        self.dados_armazenados = self.recupera_dados_armazenados()
        self.palavras_chave = palavras_chave

    def calcular_quantidade_por_data(self):
        df = pd.DataFrame(self.dados_armazenados)
        df['publishedAt'] = pd.to_datetime(df['publishedAt'])

        contagem = defaultdict(int)

        for index, row in df.iterrows():
            data = row['publishedAt']
            contagem[data.strftime('%d/%m/%Y')] += 1
            contagem[data.strftime('%m/%Y')] += 1
            contagem[data.strftime('%Y')] += 1

        contagem = dict(contagem)

        return contagem

    def calcular_quantidade_por_fonte_autor(self):
        df = pd.DataFrame(self.dados_armazenados)

        quantidade_por_fonte = df['source'].apply(lambda x: x['name']).value_counts().to_dict()
        quantidade_por_autor = df['author'].value_counts().to_dict()

        return {
            'source': quantidade_por_fonte,
            'author': quantidade_por_autor
        }

    def calcular_quantidade_palavras_chave_por_data(self):
        df = pd.DataFrame(self.dados_armazenados)
        df['publishedAt'] = pd.to_datetime(df['publishedAt'])

        contagem_por_palavra_chave = {}

        for palavra_chave in self.palavras_chave:
            df_filtrado = df[df['content'].str.contains(palavra_chave, case=False)]

            quantidade_por_ano = df_filtrado['publishedAt'].dt.strftime('%Y').value_counts().to_dict()
            quantidade_por_mes = df_filtrado['publishedAt'].dt.strftime('%m/%Y').value_counts().to_dict()
            quantidade_por_dia = df_filtrado['publishedAt'].dt.strftime('%d/%m/%Y').value_counts().to_dict()

            contagem_por_data = {
                'Quantidade por dia': quantidade_por_dia,
                'Quantidade por mês': quantidade_por_mes,
                'Quantidade por ano': quantidade_por_ano
            }

            contagem_por_palavra_chave[palavra_chave] = contagem_por_data

        return contagem_por_palavra_chave

    def salvar_resultados_json(self):
        contagem = self.calcular_quantidade_por_data()
        contagem_fonte_e_autor = self.calcular_quantidade_por_fonte_autor()
        contagem_por_palavra_chave = self.calcular_quantidade_palavras_chave_por_data()

        dados_transformados = {
            'quantidade_por_data': contagem,
            'quantidade_por_fonte_e_autor': contagem_fonte_e_autor,
            'quantidade_por_palavra_chave': contagem_por_palavra_chave
        }

        with open("/home/airelribeiro/Desktop/Tudo/ada_engenharia_de_dados/extracao/extracao_projeto/dados_transformados.json", 'w') as file:
            json.dump(dados_transformados, file, indent=4)

    def recupera_dados_armazenados():
      dados_armazenados = []
      with open("/home/airelribeiro/Desktop/Tudo/ada_engenharia_de_dados/extracao/extracao_projeto/dados_armazenados.json", 'r') as file:
        dados_armazenados = json.load(file)

      return dados_armazenados

if __name__ == "__main__":
    palavras_chave = ['dna', 'rna']
    transformador = TransformadorDados(palavras_chave)
    transformador.salvar_resultados_json()

    
