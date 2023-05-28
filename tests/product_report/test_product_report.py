from inventory_report.inventory.product import Product


def test_relatorio_produto():
    id = 1
    nome_do_produto = "Coca-Cola"
    nome_da_empresa = "Coca-Cola Company"
    data_de_fabricacao = "2020-01-01"
    data_de_validade = "2020-12-31"
    numero_de_serie = "123456789"
    instrucoes_de_armazenamento = "Manter em local seco e arejado"
    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert str(product).startswith(f"O produto {nome_do_produto} fabricado em")
    assert nome_do_produto in str(product)
    assert data_de_fabricacao in str(product)
    assert nome_da_empresa in str(product)
    assert data_de_validade in str(product)
    assert instrucoes_de_armazenamento in str(product)