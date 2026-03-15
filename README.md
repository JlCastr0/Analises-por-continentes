# Analise Historica de Medalhas Olimpicas (1896–2024)

Este projeto realiza a consolidacao de medalhas olimpicas de todas as edicoes dos Jogos de Verao e Inverno, integrando dados historicos oficiais com os resultados mais recentes de Paris 2024.

## Estrutura do Projeto

- historico_olimpiadas/: Contem os arquivos CSV com dados de 1896 a 2022.
- paris_2024/: Contem os resultados oficiais dos Jogos Olimpicos de Paris 2024.
- resultados/: Pasta gerada automaticamente contendo:
  - grafico_verao.png: Comparativo visual do Top 50 em Jogos de Verao.
  - grafico_inverno.png: Comparativo visual do Top 50 em Jogos de Inverno.
  - grafico_total.png: Comparativo visual do Total Geral acumulado.
  - tabela_verao.png: Tabela detalhada (Ouro, Prata, Bronze) - Verao.
  - tabela_inverno.png: Tabela detalhada (Ouro, Prata, Bronze) - Inverno.
  - tabela_total.png: Tabela detalhada - Geral.
- gerar_analises.py: Script Python responsavel pelo processamento e geracao dos ativos.

## Criterios de Analise

1. Consolidacao: Os dados de Paris 2024 foram somados ao historico de cada pais (identificado pelo codigo NOC).
2. Exclusoes: Foram removidos os "Jogos Intercalados de 1906", seguindo o padrao oficial do Comite Olimpico Internacional (COI).
3. Ordenacao: O ranking segue o padrao oficial:
    1. Medalhas de Ouro
    2. Medalhas de Prata
    3. Medalhas de Bronze
4. Visualizacao: Os graficos de barras sao puramente comparativos (sem numeros), enquanto as tabelas fornecem os dados exatos.

## Como Executar

Certifique-se de ter as bibliotecas pandas e matplotlib instaladas:

```bash
pip install pandas matplotlib
```

Execute o script de analise:

```bash
python gerar_analises.py
```

## Fontes dos Dados
- Basedosdados.org - Historico das Olimpiadas (https://basedosdados.org/dataset/62f8cb83-ac37-48be-874b-b94dd92d3e2b)
- Kaggle - Paris 2024 Olympic Summer Games (https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games/data)
