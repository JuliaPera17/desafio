def obter_vendas_estoque(produto):
    while True:
        try:
            vendas = float(input(f"Digite as vendas semanais do {produto}: "))
            estoque = float(input(f"Digite o estoque disponível do {produto}: "))
            if vendas < 0 or estoque < 0:
                raise ValueError("As vendas e o estoque devem ser valores não negativos.")
            return vendas, estoque
        except ValueError as e:
            print(e)

def classificar_necessidade_reabastecimento(vendas, estoque):
    if vendas > 0:
        porcentagem_estoque = estoque / vendas
    else:
        porcentagem_estoque = 0
    
    if porcentagem_estoque < 0.2:
        return "Reabastecimento Imediato"
    elif 0.2 <= porcentagem_estoque <= 0.5:
        return "Monitorar Estoque"
    else:
        return "Estoque Suficiente"

def calcular_media_ponderada(prioridades):
    soma_ponderada = sum(peso * (1 if necessidade == "Reabastecimento Imediato" else (2 if necessidade == "Monitorar Estoque" else 3)) 
                         for peso, necessidade in prioridades)
    total_pesos = sum(peso for peso, _ in prioridades)
    return soma_ponderada / total_pesos if total_pesos > 0 else 0

def main():
    produtos = {
        "Produto A": 5,
        "Produto B": 3,
        "Produto C": 1
    }

    prioridades = []

    for produto, peso in produtos.items():
        vendas, estoque = obter_vendas_estoque(produto)
        necessidade = classificar_necessidade_reabastecimento(vendas, estoque)
        print(f"{produto}: {necessidade}")
        prioridades.append((peso, necessidade))

    media_ponderada = calcular_media_ponderada(prioridades)
    print(f"Média Ponderada de Prioridade de Reabastecimento: {media_ponderada:.2f}")

if __name__ == "__main__":
    main()