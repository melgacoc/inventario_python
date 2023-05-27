from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products: list[dict]) -> str:
        products_by_company = Counter(
            product["nome_da_empresa"] for product in products
        )
        products_by_company_str = "\n".join(
            f"- {company}: {quantity}"
            for company, quantity in products_by_company.items()
        )

        return (
            f"{super().generate(products)}\n"
            "Produtos estocados por empresa:\n"
            f"{products_by_company_str}\n"
        )