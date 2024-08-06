codigo1 = input("Digite o código do primeiro produto: ")
nome1 = input("Digite o nome do primeiro produto: ")
quantidade1 = int(input("Digite a quantidade do primeiro produto: "))
preco1 = float(input("Digite o preço do primeiro produto: "))


codigo2 = input("Digite o código do segundo produto: ")
nome2 = input("Digite o nome do segundo produto: ")
quantidade2 = int(input("Digite a quantidade do segundo produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))

valor_total = (quantidade1 * preco1) + (quantidade2 * preco2)

print("\nInformações dos produtos cadastrados:")
print(f"Produto 1 - Código: {codigo1}, Nome: {nome1}, Quantidade: {quantidade1}, Preço: {preco1:.2f}")
print(f"Produto 2 - Código: {codigo2}, Nome: {nome2}, Quantidade: {quantidade2}, Preço: {preco2:.2f}")
print(f"\nValor total das compras: R$ {valor_total:.2f}")
