from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products: list[dict]) -> str:
        industry = Counter(
            product["nome_da_empresa"] for product in products
        )
        industry_products = "\n".join(
            f"- {company}: {quantity}"
            for company, quantity in industry.items()
        )

        return (
            f"{super().generate(products)}\n"
            "Produtos estocados por empresa:\n"
            f"{industry_products}\n"
        )
