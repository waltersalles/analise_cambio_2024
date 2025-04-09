
import matplotlib.pyplot as plt

# Dados de câmbio médio Jan-Mar 2024 (valores simulados)
exchange_rates = {
    "USD - Dólar Americano": 4.92,
    "EUR - Euro": 5.34,
    "GBP - Libra Esterlina": 6.23,
    "JPY - Iene Japonês": 0.033,
    "CNY - Yuan Chinês": 0.68,
    "ARS - Peso Argentino": 0.0057,
    "CHF - Franco Suíço": 5.56
}

# Preparando os dados
moedas = list(exchange_rates.keys())
valores = list(exchange_rates.values())

# Criando o gráfico
plt.figure(figsize=(12, 6))
bars = plt.bar(moedas, valores, color="mediumseagreen", edgecolor="black")
plt.title("Média Cambial Jan-Mar 2024 - 1 Unidade de Moeda em Reais (BRL)", fontsize=14)
plt.ylabel("R$ (Real)")
plt.xticks(rotation=45, ha='right')

# Adicionando os valores acima das barras
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f'R${yval:.2f}', ha='center', fontsize=9)

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.savefig("comparativo_cambio_real_2024.png")
plt.show()
