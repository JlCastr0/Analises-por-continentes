# Análise Histórica de Medalhas Olímpicas (1896–2024)

Este projeto realiza a consolidação de medalhas olímpicas de todas as edições dos Jogos de Verão e Inverno, integrando dados históricos oficiais com os resultados mais recentes de Paris 2024.

## 📂 Estrutura do Projeto

- `historico_olimpiadas/`: Contém os arquivos CSV com dados de 1896 a 2022.
- `paris_2024/`: Contém os resultados oficiais dos Jogos Olímpicos de Paris 2024.
- `resultados/`: Pasta gerada automaticamente contendo:
  - `grafico_verao.png`: Comparativo visual do Top 50 em Jogos de Verão.
  - `grafico_inverno.png`: Comparativo visual do Top 50 em Jogos de Inverno.
  - `grafico_total.png`: Comparativo visual do Total Geral acumulado.
  - `tabela_verao.png`: Tabela detalhada (Ouro, Prata, Bronze) - Verão.
  - `tabela_inverno.png`: Tabela detalhada (Ouro, Prata, Bronze) - Inverno.
  - `tabela_total.png`: Tabela detalhada - Geral.
- `gerar_analises.py`: Script Python responsável pelo processamento e geração dos ativos.

## 📊 Critérios de Análise

1.  **Consolidação:** Os dados de Paris 2024 foram somados ao histórico de cada país (identificado pelo código NOC).
2.  **Exclusões:** Foram removidos os "Jogos Intercalados de 1906", seguindo o padrão oficial do Comitê Olímpico Internacional (COI).
3.  **Ordenação:** O ranking segue o padrão oficial:
    1. Medalhas de Ouro
    2. Medalhas de Prata
    3. Medalhas de Bronze
4.  **Visualização:** Os gráficos de barras são puramente comparativos (sem números), enquanto as tabelas fornecem os dados exatos.

## 🚀 Como Executar

Certifique-se de ter as bibliotecas `pandas` e `matplotlib` instaladas:

```bash
pip install pandas matplotlib
```

Execute o script de análise:

```bash
python gerar_analises.py
```

## 🔗 Fontes dos Dados
- [Basedosdados.org - Histórico das Olimpíadas](https://basedosdados.org/dataset/62f8cb83-ac37-48be-874b-b94dd92d3e2b)
- [Kaggle - Paris 2024 Olympic Summer Games](https://www.kaggle.com/datasets/piterfm/paris-2024-olympic-summer-games/data)
