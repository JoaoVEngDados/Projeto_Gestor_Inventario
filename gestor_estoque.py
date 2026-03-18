import numpy as np

# Configuração para reprodutibilidade

np.random.seed(7)

# 1.simulação de Dados : 500 produtos, vendas diárias durante 30 dias
# Criando uma matriz onde Linhas = Produtos e Colunas = dias vendas_diarias
vendas_diarias = np.random.randint(0,50,size=(500,30))


# 2. Estoque Atual: Quantas Unidades temos hoje no armazem (aleatorio entre 100 e 500 )
estoque_atual = np.random.randint(100,501,size=500)

def otimizar_estoque(vendas,estoque):
    
    # Calcula métricas de reabastecimento usando operações
    #Média de vendas por produto (eixo 1 = coluna/dias)
    media_vendas = np.mean(vendas,axis=1)

    # Volatilidade das vendas (Desvio Padrão)
    # Isso Mostra quais produtos tem vendas instaveis
    desvio_vendas = np.std(vendas,axis=1)

    #Cálculo do estoque de segurança (Formula: Desvio * Fator de Serviço(1.65))
    # O fator 1.65 garante que o estoque não acabe em 95 % das vezes
    estoque_seguranca = np.ceil(desvio_vendas * 1.65).astype(int)

    # Ponto de Pedido (solicitação de um pedido pelo cliente até a entrega do produto ou serviço de 3 dias + Estoque de Segurança)
    # Quando o estoque chega aqui, devemos comprar mais
    ponto_pedido = (media_vendas * 3) + estoque_seguranca

    # Indentificar produtos que precisam de reposição
    # Criando um filtro onde o estoque atual é menor ou igual ao ponto de pedido
    precisa_repor = estoque <= ponto_pedido

    return {
        "media" : media_vendas,
        "segurança" : estoque_seguranca,
        "ponto_pedido" : ponto_pedido,
        # Indice de produtos que falta
        "alerta_indices" : np.where(precisa_repor)[0]
    }

# Executar Análise
analise = otimizar_estoque(vendas_diarias,estoque_atual)

# Exibir Resultados para os primeiros 5 produtos
print(f"{'ID Produto':<12} | {'Média Vendas':<12} | {'Estoque.Segurança':<15}")
print("-" * 60)
for i in range(7):
    status = "⚠️ REPOR ITENS" if i in analise["alerta_indices"] else "✅ OK"
    print(f"{i:<12} | {analise['media'][i]:<12.2f} | {analise['segurança'][i]:<15} | {status}")

total_repor = len(analise["alerta_indices"])
print(f"\nTotal de produtos que precisam de reabastecimento: {total_repor} de 500.")