estoque = [
    ["Arroz", 10, 20.0],
    ["Feijão", 3, 8.5],
    ["Macarrão", 15, 4.5],
    ["Óleo", 2, 6.0],
    ["Leite", 8, 4.8]]

valor_total = sum(qtd * preco for _, qtd, preco in estoque)


produto_maior_valor = max(estoque, key=lambda item: item[1] * item[2])

estoque_baixo = [nome for nome, qtd, _ in estoque if qtd < 5]

def buscar_produto(nome_busca):
    for nome, qtd, preco in estoque:
        if nome.lower() == nome_busca.lower():
            return [nome, qtd, preco]
    return None

print(f"1. Valor total em estoque: R$ {valor_total:.2f}")
print(f"2. Produto de maior valor em estoque: {produto_maior_valor[0]} (R$ {produto_maior_valor[1] * produto_maior_valor[2]:.2f})")
print(f"3. Produtos com estoque abaixo de 5 unidades: {estoque_baixo}")

nome_procurado = input("\nDigite o nome de um produto para buscar: ")
resultado = buscar_produto(nome_procurado)

if resultado:
    print(f"Produto encontrado: Nome={resultado[0]}, Quantidade={resultado[1]}, Preço=R$ {resultado[2]:.2f}")
else:
    print("Produto não encontrado.")
