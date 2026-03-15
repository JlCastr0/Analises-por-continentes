import pandas as pd
import matplotlib.pyplot as plt
import os

PATH_HIST = 'historico_olimpiadas/world_olympedia_olympics_game_medal_tally.csv'
PATH_PARIS = 'paris_2024/medals_total.csv'
OUT_DIR = 'resultados/'

os.makedirs(OUT_DIR, exist_ok=True)

df_hist = pd.read_csv(PATH_HIST)
df_hist = df_hist[~df_hist['edition'].str.contains('Intercalated')]
df_hist['type'] = df_hist['edition'].apply(lambda x: 'Winter' if 'Winter' in x else 'Summer')
hist_grouped = df_hist.groupby(['country_noc', 'country', 'type'])[['gold', 'silver', 'bronze']].sum().reset_index()

df_paris = pd.read_csv(PATH_PARIS)
df_paris = df_paris.rename(columns={'country_code': 'country_noc', 'Gold Medal': 'gold', 'Silver Medal': 'silver', 'Bronze Medal': 'bronze'})
df_paris['type'] = 'Summer'
df_paris_subset = df_paris[['country_noc', 'country', 'type', 'gold', 'silver', 'bronze']]

df_combined = pd.concat([hist_grouped, df_paris_subset], ignore_index=True)
final_grouped = df_combined.groupby(['country_noc', 'type']).agg({'country': 'first', 'gold': 'sum', 'silver': 'sum', 'bronze': 'sum'}).reset_index()

summer = final_grouped[final_grouped['type'] == 'Summer'].copy()
winter = final_grouped[final_grouped['type'] == 'Winter'].copy()
total_geral = final_grouped.groupby(['country_noc']).agg({'country': 'first', 'gold': 'sum', 'silver': 'sum', 'bronze': 'sum'}).reset_index()

for df in [summer, winter, total_geral]:
    df['total'] = df['gold'] + df['silver'] + df['bronze']
    df.sort_values(by=['gold', 'silver', 'bronze'], ascending=False, inplace=True)

def plot_clean_stacked(df, title, filename):
    top_50 = df.head(50).copy()
    top_50 = top_50.iloc[::-1]
    
    fig, ax = plt.subplots(figsize=(14, 16))
    ax.barh(top_50['country'], top_50['gold'], color='#FFD700', edgecolor='black', linewidth=0.5, label='Ouro')
    ax.barh(top_50['country'], top_50['silver'], left=top_50['gold'], color='#C0C0C0', edgecolor='black', linewidth=0.5, label='Prata')
    ax.barh(top_50['country'], top_50['bronze'], left=top_50['gold'] + top_50['silver'], color='#CD7F32', edgecolor='black', linewidth=0.5, label='Bronze')
    
    ax.set_title(title, fontsize=20, pad=35, fontweight='bold')
    ax.legend(loc='lower right', fontsize=12)
    ax.grid(axis='x', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, filename), dpi=120)
    plt.close()

def save_table_img(df, title, filename):
    top_50 = df.head(50)[['country', 'gold', 'silver', 'bronze', 'total']].copy()
    top_50.columns = ['País', 'Ouro', 'Prata', 'Bronze', 'Total']
    
    fig, ax = plt.subplots(figsize=(12, 20))
    ax.axis('off')
    
    ax.set_title(title, fontsize=22, weight='bold', pad=50, loc='center')
    
    table = ax.table(cellText=top_50.values, colLabels=top_50.columns, loc='upper center', cellLoc='center')
    
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.2, 2.2)
    
    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#2c3e50')
        elif row > 0:
            if row % 2 == 0:
                cell.set_facecolor('#f2f2f2')
            
    plt.savefig(os.path.join(OUT_DIR, filename), bbox_inches='tight', dpi=150, pad_inches=0.5)
    plt.close()

plot_clean_stacked(summer, 'Top 50 - Medalhas Jogos de Verão (Histórico + Paris 2024)', 'grafico_verao.png')
plot_clean_stacked(winter, 'Top 50 - Medalhas Jogos de Inverno (Histórico)', 'grafico_inverno.png')
plot_clean_stacked(total_geral, 'Top 50 - Medalhas Total Geral', 'grafico_total.png')

save_table_img(summer, 'Tabela Detalhada - Jogos de Verão', 'tabela_verao.png')
save_table_img(winter, 'Tabela Detalhada - Jogos de Inverno', 'tabela_inverno.png')
save_table_img(total_geral, 'Tabela Detalhada - Total Geral', 'tabela_total.png')

print("Análises regeneradas. Títulos das tabelas agora estão devidamente isolados no topo.")
