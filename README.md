## Projeto desenvolvido durante a disciplina de Extração de dados.
GRUPO: Airel Ribeiro; Jhonata Leôncio; Marcelo; Rafael Gomes; Pedro Teixeira

# Sistema de Monitoramento de Avanços no Campo da Genômica


Sistema desenvolvido para coleta, estruturação e apresentação periódica dos estudos publicados no campo da genômica.

## Termos de consulta

Por meio de pesquisas em bases de estudos genômicos, são recomendados para consulta os termos:

- Allele
- Chromosome
- DNA
- DNA Methylation
- DNA Mutation
- Dominant
- Epigenetics
- Gene
- Genomics
- Genotype
- Metabolites
- Phenotype
- Protein
- Recessive
- Single nucleotide polymorphism

## Funcionalidades

### O sistema possui as seguintes funcionalidades:

- Consumo de Dados com a News API:

  - Implementação de um mecanismo para consumir dados de notícias de fontes confiáveis e especializadas em genômica e medicina personalizada a partir da News API.

- Cargas em Batches:

  - Armazenamento das notícias relevantes em um formato estruturado e facilmente acessível para consultas e análises posteriores. A carga ocorre uma vez por hora, evitando duplicações de dados.

- Transformação de Dados para Consulta Estatística:

  - Conversão dos dados armazenados em um formato que pode ser consultado através de informações como a quantidade de notícias por ano, mês e dia de publicação, quantidade de notícias por fonte e autor, e a quantidade de aparições de três palavras-chave específicas por ano, mês e dia de publicação.

## Estrutura dos Dados

### Os dados provenientes da API são limpos e estruturados para a seguinte forma:

```
{
  "source": "string",
  "author": "string",
  "title": "string",
  "description": "string",
  "url": "string",
  "publishedAt": "date",
  "content": "string",
  "palavras-chave": "string"
}
```

## Scripts e Funcionalidades

### coleta_dados.py

Este script é responsável por coletar dados de notícias usando a News API, aplicando critérios de relevância, armazenando os dados de forma estruturada e evitando duplicações.

### transforma_dados.py

Este script transforma os dados coletados em estatísticas e informações úteis, como a quantidade de notícias por data, fonte, autor e palavras-chave, conforme especificado.

## Execução

Os scripts são agendados para execução periódica usando Crontab. O primeiro script, `coleta_dados.py`, é executado para coletar e armazenar os dados, enquanto o segundo script, `transforma_dados.py`, transforma esses dados para consulta do público final.

## Requisitos

Para executar os scripts, é necessário ter instalado:

- python3
- Pandas
- requests

## Como Utilizar

- Configure as palavras-chave de acordo com suas necessidades;
- Agende a execução dos scripts conforme desejado, garantindo que os caminhos dos arquivos estejam corretos;
- Execute `coleta_dados.py` para coletar os dados das notícias;
- Execute `transforma_dados.py` para transformar os dados coletados em estatísticas e informações úteis para consulta.
