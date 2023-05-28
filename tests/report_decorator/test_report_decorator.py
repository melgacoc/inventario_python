from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

COLLOR_RESET = "\033[0m"
COLLOR_RED = "\033[31m"
COLLOR_BLUE = "\033[36m"
COLLOR_GREEN = "\033[32m"


def test_decorar_relatorio():
    company_with_more_products = "Coca-Cola Company"
    oldest_date = "2020-01-01"
    nearest_expiration_date = "2024-12-31"
    green_texts = [
        "Data de fabricação mais antiga:",
        "Data de validade mais próxima:",
        "Empresa com mais produtos:",
    ]
    blue_texts = [oldest_date, nearest_expiration_date]
    red_texts = [company_with_more_products]
    products_list = [
        {
            "id": 1,
            "nome_do_produto": "Coca-Cola",
            "nome_da_empresa": company_with_more_products,
            "data_de_fabricacao": oldest_date,
            "data_de_validade": nearest_expiration_date,
            "numero_de_serie": "123456789",
            "instrucoes_de_armazenamento": "Manter em local seco",
        }
    ]

    report = ColoredReport(SimpleReport).generate(products_list)

    for text in green_texts:
        assert f"{COLLOR_GREEN}{text}{COLLOR_RESET}" in report
    for text in blue_texts:
        assert f"{COLLOR_BLUE}{text}{COLLOR_RESET}" in report
    for text in red_texts:
        assert f"{COLLOR_RED}{text}{COLLOR_RESET}" in report