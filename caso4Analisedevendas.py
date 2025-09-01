vendas = [10, 15, 20, 5, 0, 8, 25, 30, 12, 18,
          22, 17, 5, 8, 10, 14, 19, 21, 9, 6,
          11, 16, 23, 7, 13, 20, 28, 4, 9, 15]

total = sum(vendas)

mais_vendas = max(vendas)
menos_vendas = min(vendas)
dia_mais = vendas.index(mais_vendas) + 1  
dia_menos = vendas.index(menos_vendas) + 1

media = total / len(vendas)

dias_acima_media = [i+1 for i, v in enumerate(vendas) if v > media]

print(f"1. Total de vendas no mês: {total}")
print(f"2. Dia com mais vendas: Dia {dia_mais} ({mais_vendas} vendas)")
print(f"   Dia com menos vendas: Dia {dia_menos} ({menos_vendas} vendas)")
print(f"3. Média de vendas por dia: {media:.2f}")
print(f"4. Dias com vendas acima da média: {dias_acima_media}")
